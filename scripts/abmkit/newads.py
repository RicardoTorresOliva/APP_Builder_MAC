"""`abm new-ads <dir>`: scaffolds a lean ADS repository from ABM (kit only, no ABM's own history).

Copies governance, CLI, playbooks, skills, roles, methodology, standards, templates, catalogs and
the chosen profile(s); writes ads.yaml, the operate-<id> skill, abm.yaml (profile + ceremony) and
fresh workspace stubs; then runs `sync` and `okf index` inside the new ADS.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

from .common import Ctx, emit, load_yaml_file, now_iso

KIT = ["AGENTS.md", "abm", "abm.cmd", ".gitattributes", ".markdownlint-cli2.jsonc", ".env.example", ".github/workflows/abm-ci.yml", "scripts", "okf", "contract", "commands", "skills", "agents", "methodology",
       "standards", "templates", "stacks", "integrations", "adapters/tools.yaml", "docs/glossary.md", "docs/manual",
       "docs/compat-matrix.md", "planning", "implementation", "design_docs", "deliverables", "knowledge",
       "docs/decision_log.md", "docs/project_memory.md", "docs/work_log.md", "docs/tooling", ".gitignore", "START_PROJECT.md"]
SKIP = {"__pycache__"}
LEVELS = {"minimo": 0, "extendido": 1}


def _copy(src: Path, dst: Path):
    if src.is_dir():
        for f in src.rglob("*"):
            if f.is_file() and not (SKIP & set(f.parts)):
                t = dst / f.relative_to(src)
                t.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, t)
    elif src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def _profile_chain(root: Path, name: str, seen=None):
    seen = seen or []
    p = root / "profiles" / name / "profile.md"
    if not p.exists() or name in seen:
        return seen
    seen.append(name)
    m = re.search(r"^composes:\s*\[(.*?)\]", p.read_text(encoding="utf-8"), re.M)
    for dep in (m.group(1).split(",") if m else []):
        _profile_chain(root, dep.strip(), seen)
    return seen


def _level(root: Path, profiles):
    lv = "minimo"
    for n in profiles:
        m = re.search(r"^ads_contract_level:\s*(\w+)", (root / "profiles" / n / "profile.md").read_text(encoding="utf-8"), re.M)
        if m and LEVELS.get(m.group(1), 0) > LEVELS[lv]:
            lv = m.group(1)
    return lv


def cmd_new_ads(ctx: Ctx, args) -> int:
    root = ctx.root
    dst = Path(args.dir).resolve()
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", args.id):
        return emit(ctx, {"error": "id inválido"}, ["`--id` debe ser kebab-case"], ok=False)
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", args.profile) or not (root / "profiles" / args.profile / "profile.md").exists():
        return emit(ctx, {"error": "perfil inexistente"}, [f"No existe el perfil {args.profile} (ver profiles/)"], ok=False)
    if dst.exists() and any(dst.iterdir()):
        return emit(ctx, {"error": "destino no vacío"}, [f"{dst} no está vacío: elige otra carpeta (bloqueante a: no se sobrescribe)"], ok=False)
    chain = _profile_chain(root, args.profile)
    level = args.level or _level(root, chain)
    if LEVELS.get(level, 0) < LEVELS[_level(root, chain)]:
        return emit(ctx, {"error": "nivel menor al del perfil"}, ["El nivel no puede ser menor que el del perfil"], ok=False)
    plan = [k for k in KIT if (root / k).exists()]
    if ctx.dry_run:
        return emit(ctx, {"dir": str(dst), "copy": plan, "profiles": chain, "level": level},
                    [f"Crearía {dst} con {len(plan)} piezas del kit · perfiles {chain} · nivel {level}"])
    dst.mkdir(parents=True, exist_ok=True)
    for k in plan:
        if k == "profiles":
            continue
        _copy(root / k, dst / k)
    _copy(root / "profiles/_contract.md", dst / "profiles/_contract.md")
    for n in chain:
        _copy(root / "profiles" / n, dst / "profiles" / n)
    # abm.yaml con perfil y ceremonia
    conf = (root / "abm.yaml").read_text(encoding="utf-8")
    conf = re.sub(r"^active_profile:.*$", f"active_profile: {args.profile}", conf, flags=re.M)
    conf = re.sub(r"^ceremony:.*$", f"ceremony: {args.ceremony}", conf, flags=re.M)
    (dst / "abm.yaml").write_text(conf, encoding="utf-8")
    # ads.yaml desde la plantilla
    t = (root / "templates/agentic/ads.yaml").read_text(encoding="utf-8")
    import json as _json
    q = lambda v: _json.dumps(str(v), ensure_ascii=False)  # noqa: E731 — valores seguros en YAML
    for key, val in (("name", args.name), ("owner", args.owner), ("description", args.description)):
        t = re.sub(rf"^{key}: <[^>\n]*>.*$", f"{key}: {q(val)}", t, count=1, flags=re.M)
    rep = {"<id-kebab-case>": args.id, "<id>": args.id,
           "<software-app | api-service | data-product | research-report | intelligence-product | automation-integration>": args.profile,
           "<minimo | extendido>": level,
           "<N1 | N2 | N3>": "N2" if level == "extendido" else "N1"}
    for a, b in rep.items():
        t = t.replace(a, b)
    (dst / "ads.yaml").write_text(t, encoding="utf-8")
    sk = (root / "templates/agentic/operate-skill/SKILL.md").read_text(encoding="utf-8").replace("<id>", args.id).replace("<Nombre>", args.name)
    (dst / f"skills/operate-{args.id}").mkdir(parents=True, exist_ok=True)
    (dst / f"skills/operate-{args.id}/SKILL.md").write_text(sk, encoding="utf-8")
    shutil.rmtree(dst / "skills/operate-abm", ignore_errors=True)
    (dst / "ops").mkdir(parents=True, exist_ok=True)
    (dst / "ops/mcp_server.py").write_text((root / "templates/agentic/mcp_server.py").read_text(encoding="utf-8").replace('ADS_ID = "<id>"', f'ADS_ID = "{args.id}"'), encoding="utf-8")
    llms = (root / "templates/agentic/llms.txt").read_text(encoding="utf-8").replace("<id>", args.id).replace("<Nombre del ADS>", args.name)
    (dst / "llms.txt").write_text(llms, encoding="utf-8")
    # espacio de trabajo limpio
    now = now_iso()
    (dst / "docs/_work").mkdir(parents=True, exist_ok=True)
    (dst / "log.md").write_text(f"# Registro del bundle {args.name}\n\n## {now[:10]}\n* **Creation**: ADS creado con `abm new-ads` (perfil {args.profile}, nivel {level}).\n", encoding="utf-8")
    (dst / "ops/tokens").mkdir(parents=True, exist_ok=True)
    (dst / "ops/tokens/ledger.jsonl").write_text("", encoding="utf-8")
    steps = []
    for argv in (["sync"], ["tokens", "report"], ["okf", "index"], ["pending", "list"]):
        r = subprocess.run([sys.executable, str(dst / "scripts/abm.py"), "--root", str(dst), *argv], capture_output=True, text=True)
        steps.append({"cmd": " ".join(argv), "ok": r.returncode == 0, "out": (r.stdout or r.stderr).strip().splitlines()[-1:]})
    lines = [f"ADS creado en {dst} · perfil {args.profile} ({', '.join(chain)}) · nivel {level} · ceremonia {args.ceremony}"]
    lines += [f"{'✔' if s['ok'] else '✖'} abm {s['cmd']}" for s in steps]
    lines.append("Siguiente: cd a la carpeta, `git init`, describe el encargo en START_PROJECT.md y ejecuta `init-project`.")
    ok = all(s["ok"] for s in steps)
    return emit(ctx, {"dir": str(dst), "profiles": chain, "level": level, "steps": steps}, lines, ok)


def register(sub):
    p = sub.add_parser("new-ads", help="Crea el esqueleto de un ADS nuevo desde ABM")
    p.add_argument("dir")
    p.add_argument("--id", required=True, help="kebab-case")
    p.add_argument("--name", required=True)
    p.add_argument("--profile", required=True)
    p.add_argument("--ceremony", default="mvp", choices=["prototipo", "mvp", "producto", "enterprise-regulado"])
    p.add_argument("--level", choices=["minimo", "extendido"])
    p.add_argument("--owner", default="por definir")
    p.add_argument("--description", default="por definir")
    p.set_defaults(func=cmd_new_ads)
