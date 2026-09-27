"""ADS contract checker (`abm ads-check`): static verification of ads.yaml against contract/ levels."""
from __future__ import annotations

import re
from pathlib import Path

from .common import Ctx, cfg, emit, load_yaml_file

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LEVELS = ("minimo", "extendido")
TOKEN_LEVELS = ("N1", "N2", "N3")

# requirement → (level where it becomes mandatory, check function name)
MIN_FILES = [("endpoints.agents_md", "AGENTS.md del ADS"), ("endpoints.skill", "skill de operación (SKILL.md)"),
             ("endpoints.llms_txt", "llms.txt"), ("docs.okf_index", "índice OKF")]
EXT_FILES = [("endpoints.mcp.command", None), ("endpoints.cli.command", None)]


def _get(d, dotted):
    cur = d
    for p in dotted.split("."):
        if not isinstance(cur, dict) or p not in cur:
            return None
        cur = cur[p]
    return cur


def _exists(root: Path, rel) -> bool:
    return bool(rel) and (root / str(rel)).exists()


def profile_level(root: Path, profile: str) -> str | None:
    p = root / "profiles" / profile / "profile.md"
    if not p.exists():
        return None
    m = re.search(r"^ads_contract_level:\s*(\w+)", p.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def check_manifest(root: Path, manifest: Path):
    f = []

    def err(code, msg):
        f.append({"level": "error", "code": code, "msg": msg})

    def warn(code, msg):
        f.append({"level": "warn", "code": code, "msg": msg})

    if not manifest.exists():
        err("ads.manifest", f"falta el manifiesto {manifest.name}")
        return None, f
    m = load_yaml_file(manifest)
    for k in ("id", "name", "version", "profile", "owner", "description", "capabilities", "endpoints", "tokens", "portability", "security"):
        if m.get(k) in (None, "", [], {}):
            err("ads.required", f"falta `{k}`")
    if m.get("id") and not KEBAB.match(str(m["id"])):
        err("ads.id", "`id` debe ser kebab-case")
    if m.get("version") and not SEMVER.match(str(m["version"])):
        err("ads.version", "`version` debe ser semver (MAJOR.MINOR.PATCH)")
    level = m.get("contract_level") or profile_level(root, str(m.get("profile", ""))) or "minimo"
    if level not in LEVELS:
        err("ads.level", f"`contract_level` debe ser {'|'.join(LEVELS)}")
        level = "minimo"
    plevel = profile_level(root, str(m.get("profile", "")))
    if plevel == "extendido" and level == "minimo":
        err("ads.level", "el perfil exige nivel `extendido`")
    # --- mínimo (todo ADS)
    for key, label in MIN_FILES:
        val = _get(m, key)
        if not _exists(root, val):
            err("ads.min." + key.split(".")[-1], f"{label}: `{key}` falta o no existe ({val})")
    for i, c in enumerate(m.get("capabilities") or []):
        if not isinstance(c, dict) or not c.get("id") or not c.get("description"):
            err("ads.capability", f"capabilities[{i}] requiere id y description")
        elif c.get("mode") not in ("read", "write", "destructive"):
            err("ads.capability", f"capabilities[{i}].mode debe ser read|write|destructive")
    tok = m.get("tokens") or {}
    if tok.get("level") not in TOKEN_LEVELS:
        err("ads.tokens.level", "`tokens.level` debe ser N1|N2|N3")
    if not tok.get("ledger"):
        err("ads.tokens.ledger", "`tokens.ledger` es obligatorio")
    if not _exists(root, tok.get("report")):
        err("ads.tokens.report", f"falta el reporte de tokens ({tok.get('report')})")
    port = m.get("portability") or {}
    for k in ("languages", "llm_providers"):
        if port.get(k) in (None, [], ""):
            err("ads.portability", f"`portability.{k}` es obligatorio (usa [] explícito si no aplica… o 'none')")
    sec = m.get("security") or {}
    if sec.get("secrets") not in ("env", "secret-manager"):
        err("ads.security.secrets", "`security.secrets` debe ser env|secret-manager")
    # --- extendido
    if level == "extendido":
        if not _get(m, "endpoints.mcp.command") and not _get(m, "endpoints.mcp.url"):
            err("ads.ext.mcp", "nivel extendido: falta `endpoints.mcp` (command o url)")
        if not _get(m, "endpoints.cli.command") and not _get(m, "endpoints.api.openapi"):
            err("ads.ext.interface", "nivel extendido: falta CLI (`endpoints.cli`) o API (`endpoints.api.openapi`)")
        if _get(m, "endpoints.api.openapi") and not str(_get(m, "endpoints.api.openapi")).startswith("http") and not _exists(root, _get(m, "endpoints.api.openapi")):
            err("ads.ext.openapi", "el OpenAPI declarado no existe")
        if tok.get("level") == "N1":
            err("ads.ext.tokens", "nivel extendido exige dashboard de tokens N2 o N3")
        if tok.get("level") in ("N2", "N3") and not _exists(root, tok.get("dashboard")):
            warn("ads.ext.dashboard", f"dashboard no generado aún ({tok.get('dashboard')}); ejecuta `abm tokens dashboard`")
        if not tok.get("budgets"):
            err("ads.ext.budgets", "nivel extendido exige `tokens.budgets`")
        if not sec.get("agent_audit_log"):
            err("ads.ext.audit", "nivel extendido exige `security.agent_audit_log`")
        if not port.get("exit_plan"):
            warn("ads.ext.exit_plan", "nivel extendido: documenta `portability.exit_plan`")
    import json as _json
    if re.search(r"<[^<>\n]{2,60}>", _json.dumps(m, ensure_ascii=False)):
        warn("ads.placeholder", "quedan valores de plantilla <...> en ads.yaml: complétalos en init-project")
    destructive = [c.get("id") for c in m.get("capabilities") or [] if isinstance(c, dict) and c.get("mode") == "destructive"]
    hitl = set(sec.get("hitl_actions") or [])
    for d in destructive:
        if d not in hitl:
            err("ads.hitl", f"la capacidad destructiva `{d}` debe figurar en `security.hitl_actions`")
    return m, f


def cmd_ads_check(ctx: Ctx, args) -> int:
    root = Path(args.path).resolve() if args.path else ctx.root
    manifest = root / "ads.yaml"
    m, findings = check_manifest(root, manifest)
    errors = [x for x in findings if x["level"] == "error"]
    level = (m or {}).get("contract_level") or profile_level(root, str((m or {}).get("profile", ""))) or "minimo"
    lines = [f"{x['level'].upper()} {x['msg']} [{x['code']}]" for x in findings]
    lines.append(f"Contrato ADS ({(m or {}).get('id', '?')}, nivel {level}): {len(errors)} errores → {'OK' if not errors else 'FALLA'}")
    return emit(ctx, {"ads": (m or {}).get("id"), "level": level, "findings": findings}, lines, ok=not errors)


def register(sub):
    p = sub.add_parser("ads-check", help="Verifica el Contrato ADS (ads.yaml)")
    p.add_argument("path", nargs="?", help="raíz del ADS (por defecto, este repo)")
    p.set_defaults(func=cmd_ads_check)
