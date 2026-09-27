"""`abm sync`: generates per-tool adapters from neutral sources (ADR 0002).

Sources: AGENTS.md, commands/*.md, skills/<name>/, agents/<role>.md, adapters/tools.yaml.
Outputs follow docs/compat-matrix.md. Every generated file is recorded in adapters/.generated.json
(path → sha256) so `--check` detects drift, hand edits and orphans. Turbo permission templates are
written to adapters/turbo/ and only installed into active tool paths with `--apply-turbo`.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from .common import Ctx, emit, load_yaml_file, read_md

REGISTRY = "adapters/.generated.json"
MARK = "GENERADO por abm sync"


def _h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _yaml_str(s: str) -> str:
    s = str(s or "").replace("\n", " ").strip()
    return json.dumps(s, ensure_ascii=False)


def _toml_str(s: str) -> str:
    return json.dumps(str(s or ""), ensure_ascii=False)


# ---------------------------------------------------------------- sources
def load_sources(root: Path) -> dict:
    cmds = []
    for p in sorted((root / "commands").glob("*.md")):
        fm, body, _ = read_md(p)
        fm = fm or {}
        cmds.append({"name": p.stem, "desc": str(fm.get("description") or p.stem), "args": str(fm.get("args") or ""),
                     "title": str(fm.get("title") or p.stem)})
    roles = []
    for p in sorted((root / "agents").glob("*.md")):
        if p.name == "README.md":
            continue
        fm, body, _ = read_md(p)
        fm = fm or {}
        roles.append({"name": p.stem, "desc": str(fm.get("description") or p.stem), "tier": str(fm.get("model_tier") or "strong"),
                      "body": body.strip()})
    skills = sorted(d for d in (root / "skills").iterdir() if d.is_dir() and (d / "SKILL.md").exists()) if (root / "skills").exists() else []
    tools = load_yaml_file(root / "adapters/tools.yaml") if (root / "adapters/tools.yaml").exists() else {}
    return {"commands": cmds, "roles": roles, "skills": skills, "tools": tools}


# ---------------------------------------------------------------- builders
def pointer_md(extra: str = "") -> str:
    return (f"<!-- {MARK}. No editar: la gobernanza vive en AGENTS.md. -->\n"
            "# ABM — puntero de gobernanza\n\n"
            "Lee y sigue `AGENTS.md` (raíz del repo) antes de actuar: es la única fuente de gobernanza. "
            "Comandos: `commands/<nombre>.md`. Mapa del repo: `index.md`." + (f"\n\n{extra}" if extra else "") + "\n")


def playbook_body(c, argvar: str) -> str:
    arg = f" Argumentos: {argvar}" if argvar else ""
    return f"<!-- {MARK} desde commands/{c['name']}.md. No editar. -->\nLee y ejecuta el playbook `commands/{c['name']}.md` siguiendo `AGENTS.md`.{arg}\n"


def playbooks_skill(cmds) -> str:
    rows = "\n".join(f"| `{c['name']}` | {c['desc']} |" for c in cmds)
    return f"""---
name: abm-playbooks
description: Catálogo de los playbooks de ABM (comandos) para herramientas sin slash commands. Úsala al empezar o retomar un proyecto ABM, o cuando necesites planificar, construir, revisar, medir tokens o iterar un ADS.
license: MIT
metadata: {{ okf_type: Skill, abm_version: "5.0.0", generated: "abm sync" }}
---
<!-- {MARK} desde commands/*.md. No editar. -->
# Playbooks de ABM

La gobernanza está en `AGENTS.md`. Cada fila es un playbook neutral en `commands/<nombre>.md`: léelo solo cuando toque (no los precargues).

Flujo: `session-start` siempre primero → sin plan publicado, `init-project` → `start-execution` por unidad → `review` por milestone → `closeout` → `iterate`.

| Playbook | Para qué |
|---|---|
{rows}

CLI para agentes: `./abm <orden> --json` (Windows: `abm.cmd`). Servidor MCP: `python3 scripts/abm.py mcp`.
"""


def role_md_claude(r) -> str:
    model = "haiku" if r["tier"] == "fast" else "inherit"
    return f"---\nname: {r['name']}\ndescription: {_yaml_str(r['desc'])}\nmodel: {model}\n---\n<!-- {MARK} desde agents/{r['name']}.md. No editar. -->\n{r['body']}\n"


def role_md_generic(r, suffix_fm: str = "") -> str:
    return f"---\nname: {r['name']}\ndescription: {_yaml_str(r['desc'])}\n{suffix_fm}---\n<!-- {MARK} desde agents/{r['name']}.md. No editar. -->\n{r['body']}\n"


def mcp_json(tools, key="mcpServers", extra=None) -> str:
    s = tools.get("mcp_server") or {"name": "abm", "command": "python3", "args": ["scripts/abm.py", "mcp"]}
    entry = {"command": s["command"], "args": s["args"]}
    if extra:
        entry = {**extra, **entry}
    return json.dumps({key: {s["name"]: entry}}, ensure_ascii=False, indent=2) + "\n"


def ignore_txt(tools) -> str:
    pats = tools.get("ignore_patterns") or []
    return f"# {MARK}. Archivos que el agente no debe leer ni indexar.\n" + "\n".join(pats) + "\n"


# ---------------------------------------------------------------- per tool
def emit_all(root: Path, src: dict) -> dict:
    out: dict[str, str | Path] = {}
    tools = src["tools"]
    enabled = {k for k, v in (tools.get("tools") or {}).items() if (v or {}).get("enabled", True)}
    cmds, roles = src["commands"], src["roles"]
    skill_dirs = list(src["skills"])
    generated_skill = playbooks_skill(cmds)
    out["skills/abm-playbooks/SKILL.md"] = generated_skill

    def skills_to(base: str):
        for d in skill_dirs:
            if d.name == "abm-playbooks":
                continue
            for f in sorted(d.rglob("*")):
                if f.is_file():
                    out[f"{base}/{d.name}/{f.relative_to(d).as_posix()}"] = f
        out[f"{base}/abm-playbooks/SKILL.md"] = generated_skill

    if "claude-code" in enabled:
        out["CLAUDE.md"] = f"<!-- {MARK}. No editar: la gobernanza vive en AGENTS.md (se importa abajo). -->\n@AGENTS.md\n"
        for c in cmds:
            fm = f"---\ndescription: {_yaml_str(c['desc'])}\n" + (f"argument-hint: {_yaml_str(c['args'])}\n" if c["args"] else "") + "---\n"
            out[f".claude/commands/{c['name']}.md"] = fm + playbook_body(c, "$ARGUMENTS")
        skills_to(".claude/skills")
        for r in roles:
            out[f".claude/agents/{r['name']}.md"] = role_md_claude(r)
        out[".mcp.json"] = mcp_json(tools)
    if "codex" in enabled:
        skills_to(".codex/skills")
        s = tools.get("mcp_server") or {}
        out[".codex/config.toml"] = (f"# {MARK}. No editar. Codex lee AGENTS.md de forma nativa.\n"
                                     f"[mcp_servers.{s.get('name', 'abm')}]\ncommand = {_toml_str(s.get('command', 'python3'))}\n"
                                     f"args = [{', '.join(_toml_str(a) for a in s.get('args', []))}]\n")
    if {"antigravity", "gemini-cli", "hermes", "cursor"} & enabled:
        skills_to(".agents/skills")
    if "antigravity" in enabled:
        for c in cmds:
            out[f".agents/workflows/{c['name']}.md"] = f"---\ndescription: {_yaml_str(c['desc'])}\n---\n" + playbook_body(c, "")
        out[".agents/mcp_config.json"] = mcp_json(tools)
    if "copilot" in enabled:
        out[".github/copilot-instructions.md"] = pointer_md()
        for c in cmds:
            out[f".github/prompts/{c['name']}.prompt.md"] = (f"---\ndescription: {_yaml_str(c['desc'])}\nagent: agent\n---\n"
                                                             + playbook_body(c, "${input:args}"))
        for r in roles:
            out[f".github/agents/{r['name']}.agent.md"] = role_md_generic(r)
        out[".vscode/mcp.json"] = mcp_json(tools, key="servers", extra={"type": "stdio"})
    if "cursor" in enabled:
        out[".cursor/mcp.json"] = mcp_json(tools)
        out[".cursorignore"] = ignore_txt(tools)
    if "gemini-cli" in enabled:
        s = tools.get("mcp_server") or {}
        settings = {"context": {"fileName": ["AGENTS.md"]},
                    "mcpServers": {s.get("name", "abm"): {"command": s.get("command", "python3"), "args": s.get("args", [])}}}
        out[".gemini/settings.json"] = json.dumps(settings, ensure_ascii=False, indent=2) + "\n"
        for c in cmds:
            out[f".gemini/commands/{c['name']}.toml"] = (f"# {MARK} desde commands/{c['name']}.md. No editar.\n"
                                                        f"description = {_toml_str(c['desc'])}\n"
                                                        f"prompt = {_toml_str(playbook_body(c, '{{args}}').split(chr(10), 1)[1].strip())}\n")
        for r in roles:
            out[f".gemini/agents/{r['name']}.md"] = role_md_generic(r)
        out[".geminiignore"] = ignore_txt(tools)
    if "windsurf" in enabled:
        rule = "---\ntrigger: always_on\n---\n" + pointer_md()
        out[".devin/rules/abm.md"] = rule
        out[".windsurf/rules/abm.md"] = rule
        for c in cmds:
            out[f".devin/workflows/{c['name']}.md"] = f"---\ndescription: {_yaml_str(c['desc'])}\n---\n" + playbook_body(c, "")
        out[".devinignore"] = ignore_txt(tools)
    if "kiro" in enabled:
        out[".kiro/steering/abm.md"] = "---\ninclusion: always\n---\n" + pointer_md()
        out[".kiro/steering/abm-playbooks.md"] = "---\ninclusion: manual\n---\n" + generated_skill.split("---\n", 2)[2]
        out[".kiro/settings/mcp.json"] = mcp_json(tools)
        out[".kiroignore"] = ignore_txt(tools)
    if "hermes" in enabled:
        s = tools.get("mcp_server") or {}
        out["adapters/hermes/config.example.yaml"] = (
            f"# {MARK}. Fragmento para ~/.hermes/config.yaml (Hermes solo admite MCP a nivel usuario).\n"
            "# Hermes carga AGENTS.md y .agents/skills/ del proyecto de forma nativa.\n"
            "mcp_servers:\n"
            f"  {s.get('name', 'abm')}:\n"
            f"    command: {s.get('command', 'python3')}\n"
            f"    args: [{', '.join(s.get('args', []))}]\n"
            "    tools:\n"
            "      include: [abm_doctor, abm_check, abm_okf_validate, abm_ads_check, abm_methodology_classify, abm_decide, abm_pending_list, abm_tokens_summary]\n"
            "      resources: true\n"
            "      prompts: false\n")
    turbo_templates(out, tools, enabled)
    return out


def turbo_templates(out, tools, enabled):
    t = tools.get("turbo") or {}
    allow = t.get("allow_commands", [])
    ask = t.get("ask_commands", [])
    deny_read = t.get("deny_read", [])
    deny_cmd = t.get("deny_commands", [])
    if "claude-code" in enabled:
        claude = {"permissions": {"defaultMode": "acceptEdits",
                                  "allow": [f"Bash({c}:*)" for c in allow],
                                  "ask": [f"Bash({c}:*)" for c in ask],
                                  "deny": [f"Read(./{p})" for p in deny_read] + [f"Bash({c}:*)" for c in deny_cmd]}}
        out["adapters/turbo/claude-code/settings.json"] = json.dumps(claude, ensure_ascii=False, indent=2) + "\n"
    if "codex" in enabled:
        out["adapters/turbo/codex/config.toml"] = (f"# {MARK}. Plantilla turbo; se añade a .codex/config.toml con `abm sync --apply-turbo`.\n"
                                                   'approval_policy = "on-request"\nsandbox_mode = "workspace-write"\n')
    if "gemini-cli" in enabled:
        out["adapters/turbo/gemini-cli/settings.json"] = json.dumps({"general": {"defaultApprovalMode": "auto_edit"}}, indent=2) + "\n"
    if "copilot" in enabled:
        vs = {"chat.tools.terminal.autoApprove": {**{c: True for c in allow}, **{c: False for c in ask + deny_cmd}}}
        out["adapters/turbo/vscode/settings.json"] = json.dumps(vs, ensure_ascii=False, indent=2) + "\n"
    if "hermes" in enabled:
        out["adapters/turbo/hermes/config.example.yaml"] = (f"# {MARK}. Fragmento turbo para ~/.hermes/config.yaml.\n"
                                                            "approvals:\n  mode: smart\nsecurity:\n  redact_secrets: true\n  tirith_enabled: true\n")
    if "kiro" in enabled:
        rules = "\n".join(f"  - {{ capability: shell, match: \"{c}*\", effect: allow }}" for c in allow)
        rules += "\n" + "\n".join(f"  - {{ capability: shell, match: \"{c}*\", effect: ask }}" for c in ask)
        rules += "\n" + "\n".join(f"  - {{ capability: fs_read, match: \"{p}\", effect: deny }}" for p in deny_read)
        out["adapters/turbo/kiro/permissions.example.yaml"] = (f"# {MARK}. Kiro guarda permisos a nivel usuario (~/.kiro/settings/permissions.yaml); cópialo tú.\n"
                                                              f"rules:\n{rules}\n")


APPLY = {
    "adapters/turbo/claude-code/settings.json": (".claude/settings.json", "json"),
    "adapters/turbo/codex/config.toml": (".codex/config.toml", "toml-append"),
    "adapters/turbo/gemini-cli/settings.json": (".gemini/settings.json", "json"),
    "adapters/turbo/vscode/settings.json": (".vscode/settings.json", "json"),
}


def _merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        r = dict(a)
        for k, v in b.items():
            r[k] = _merge(a.get(k), v) if k in a else v
        return r
    return b


def apply_turbo(out: dict):
    for tpl, (target, kind) in APPLY.items():
        if tpl not in out:
            continue
        tv = out[tpl]
        if kind == "json":
            base = json.loads(out[target]) if target in out else {}
            out[target] = json.dumps(_merge(base, json.loads(tv)), ensure_ascii=False, indent=2) + "\n"
        else:
            base = out.get(target, "")
            body = "\n".join(l for l in tv.splitlines() if not l.startswith("#"))
            out[target] = body.strip() + "\n\n" + base if base else body.strip() + "\n"


# ---------------------------------------------------------------- run
def _content(v) -> bytes:
    return v.read_bytes() if isinstance(v, Path) else v.encode("utf-8")


def plan(ctx: Ctx, with_turbo: bool):
    root = ctx.root
    src = load_sources(root)
    out = emit_all(root, src)
    reg_path = root / REGISTRY
    reg = json.loads(reg_path.read_text(encoding="utf-8")) if reg_path.exists() else {"files": {}, "turbo_applied": False}
    turbo = with_turbo or reg.get("turbo_applied", False)
    if turbo:
        apply_turbo(out)
    desired = {p: _content(v) for p, v in out.items()}
    changes = []
    for p, data in sorted(desired.items()):
        f = root / p
        cur = f.read_bytes() if f.exists() else None
        if cur != data:
            changes.append({"path": p, "action": "update" if cur is not None else "create"})
    orphans = [p for p in reg.get("files", {}) if p not in desired]
    edited = [p for p, h in reg.get("files", {}).items() if p in desired and (root / p).exists()
              and hashlib.sha256((root / p).read_bytes()).hexdigest() != h and hashlib.sha256(desired[p]).hexdigest() == h]
    return desired, changes, orphans, edited, turbo


def cmd_sync(ctx: Ctx, args) -> int:
    root = ctx.root
    desired, changes, orphans, edited, turbo = plan(ctx, args.apply_turbo)
    if args.check:
        ok = not changes and not orphans
        lines = [f"DESFASE {c['path']} ({c['action']})" for c in changes[:40]] + [f"HUÉRFANO {p}" for p in orphans]
        lines.append(f"sync --check: {len(desired)} salidas · {len(changes)} desfasadas · {len(orphans)} huérfanas → {'OK' if ok else 'FALLA (ejecuta ./abm sync)'}")
        return emit(ctx, {"outputs": len(desired), "changes": changes, "orphans": orphans, "hand_edited": edited}, lines, ok)
    if not ctx.dry_run:
        for p, data in desired.items():
            f = root / p
            f.parent.mkdir(parents=True, exist_ok=True)
            if not f.exists() or f.read_bytes() != data:
                f.write_bytes(data)
        for p in orphans:
            f = root / p
            if f.exists():
                f.unlink()
                parent = f.parent
                while parent != root and parent.exists() and not any(parent.iterdir()):
                    parent.rmdir()
                    parent = parent.parent
        reg = {"note": "Registro de archivos generados por abm sync (ruta → sha256). No editar.",
               "turbo_applied": turbo,
               "files": {p: hashlib.sha256(d).hexdigest() for p, d in sorted(desired.items())}}
        (root / REGISTRY).write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    verb = "haría" if ctx.dry_run else "hecho"
    lines = [f"sync {verb}: {len(desired)} salidas · {len(changes)} escritas · {len(orphans)} huérfanas eliminadas" + (" · turbo instalado" if turbo else "")]
    if edited:
        lines.append(f"AVISO: {len(edited)} archivos generados estaban editados a mano y se sobrescribieron")
    return emit(ctx, {"outputs": len(desired), "changes": changes, "orphans_removed": orphans, "turbo_applied": turbo}, lines)


def register(sub):
    p = sub.add_parser("sync", help="Genera los adaptadores por herramienta desde las fuentes neutrales")
    p.add_argument("--check", action="store_true", help="falla si alguna salida está desfasada")
    p.add_argument("--apply-turbo", action="store_true", help="instala las plantillas turbo en las rutas activas")
    p.set_defaults(func=cmd_sync)
