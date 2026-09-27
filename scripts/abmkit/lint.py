"""Lints: core without product names (rule 7), playbook structure + output template (§4.17), manual parity."""
from __future__ import annotations

import re

from .common import Ctx, cfg, emit, walk_files

PLAYBOOK_SECTIONS = ["Propósito", "Cuándo usarlo", "Entradas", "Pasos", "Salidas", "Gates", "Fallback", "Reporte", "Invocación por agentes"]
TAG = re.compile(r"\[(verde|amarillo|rojo)\]")
CODE = re.compile(r"```.*?```", re.S)


def _sections(text):
    return {m.group(1).strip(): m.start() for m in re.finditer(r"^## (.+)$", text, re.M)}


def _section_body(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def lint_core(ctx: Ctx):
    products = cfg(ctx.conf, "lint.products", []) or []
    paths = cfg(ctx.conf, "lint.core_paths", []) or []
    allow = cfg(ctx.conf, "lint.core_allow", []) or []
    rx = re.compile(r"(?<![\w./-])(" + "|".join(re.escape(p) for p in products) + r")(?![\w-])") if products else None
    hits = []
    if not rx:
        return hits
    from .common import matches
    for path, rel in walk_files(ctx.root, (".md", ".yaml", ".yml"), cfg(ctx.conf, "okf.exclude", []) or []):
        if not matches(rel, paths) or matches(rel, allow):
            continue
        text = path.read_text(encoding="utf-8")
        for m in rx.finditer(text):
            hits.append({"file": rel, "line": text.count("\n", 0, m.start()) + 1, "product": m.group(1)})
    return hits


def lint_playbooks(ctx: Ctx):
    out = []
    max_lines = int(cfg(ctx.conf, "lint.report_max_lines", 12))
    for path, rel in walk_files(ctx.root / "commands", (".md",)):
        text = path.read_text(encoding="utf-8")
        rel = "commands/" + rel
        secs = _sections(text)
        for s in PLAYBOOK_SECTIONS:
            if s not in secs:
                out.append({"file": rel, "msg": f"falta la sección `## {s}`"})
        steps = _section_body(text, "Pasos")
        step_lines = [l for l in steps.splitlines() if re.match(r"^\s*\d+\.\s", l)]
        if not step_lines:
            out.append({"file": rel, "msg": "`## Pasos` sin pasos numerados"})
        for l in step_lines:
            if not TAG.search(l):
                out.append({"file": rel, "msg": f"paso sin semáforo [verde|amarillo|rojo]: {l.strip()[:60]}"})
        rep = _section_body(text, "Reporte")
        m = re.search(r"```[a-z]*\n(.*?)```", rep, re.S)
        if not m:
            out.append({"file": rel, "msg": "`## Reporte` sin plantilla en bloque de código"})
        elif len(m.group(1).rstrip("\n").splitlines()) > max_lines:
            out.append({"file": rel, "msg": f"plantilla de reporte > {max_lines} líneas"})
    return out


def lint_manual(ctx: Ctx):
    out = []
    cmds = {p.stem for p in (ctx.root / "commands").glob("*.md")}
    mdir = ctx.root / cfg(ctx.conf, "manual.commands_dir", "docs/manual/comandos")
    pages = {p.stem for p in mdir.glob("*.md")} if mdir.exists() else set()
    for c in sorted(cmds - pages):
        out.append({"file": f"commands/{c}.md", "msg": f"sin página de manual ({mdir.relative_to(ctx.root)}/{c}.md)"})
    for p in sorted(pages - cmds - {"index"}):
        out.append({"file": f"{mdir.relative_to(ctx.root)}/{p}.md", "msg": "página de manual sin comando"})
    sheet = ctx.root / cfg(ctx.conf, "manual.cheatsheet", "docs/manual/cheatsheet.md")
    if sheet.exists():
        text = sheet.read_text(encoding="utf-8")
        for c in sorted(cmds):
            if not re.search(rf"`{re.escape(c)}`", text):
                out.append({"file": str(sheet.relative_to(ctx.root)), "msg": f"cheatsheet no menciona `{c}`"})
    else:
        out.append({"file": "docs/manual", "msg": "falta cheatsheet"})
    return out


SKILL_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def lint_skills(ctx: Ctx):
    from .common import read_md
    out = []
    base = ctx.root / "skills"
    for d in sorted(p for p in base.iterdir() if p.is_dir()) if base.exists() else []:
        f = d / "SKILL.md"
        rel = f"skills/{d.name}/SKILL.md"
        if not f.exists():
            out.append({"file": f"skills/{d.name}", "msg": "carpeta sin SKILL.md"})
            continue
        fm, body, err = read_md(f)
        if err or fm is None:
            out.append({"file": rel, "msg": err or "sin frontmatter"})
            continue
        extra = set(fm) - SKILL_KEYS
        if extra:
            out.append({"file": rel, "msg": f"claves no estándar de Agent Skills: {sorted(extra)} (usa metadata)"})
        name = str(fm.get("name", ""))
        if name != d.name or not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
            out.append({"file": rel, "msg": f"`name` debe ser kebab-case ≤ 64 e igual a la carpeta ({d.name})"})
        desc = str(fm.get("description", ""))
        if not desc or len(desc) > 1024:
            out.append({"file": rel, "msg": "`description` obligatoria y ≤ 1024 caracteres"})
        md = fm.get("metadata")
        if md is not None and (not isinstance(md, dict) or any(not isinstance(v, str) for v in md.values())):
            out.append({"file": rel, "msg": "`metadata` debe ser un mapa texto → texto"})
    return out


def cmd_lint(ctx: Ctx, args) -> int:
    kind = args.kind
    if kind == "core":
        hits = lint_core(ctx)
        lines = [f"PRODUCTO EN NÚCLEO {h['file']}:{h['line']} → {h['product']}" for h in hits]
        lines.append(f"Núcleo sin productos (regla 7): {len(hits)} hallazgos → {'OK' if not hits else 'FALLA'}")
        return emit(ctx, {"findings": hits}, lines, ok=not hits)
    res = {"playbooks": lint_playbooks, "manual": lint_manual, "skills": lint_skills}[kind](ctx)
    lines = [f"{r['file']}: {r['msg']}" for r in res]
    lines.append(f"Lint {kind}: {len(res)} hallazgos → {'OK' if not res else 'FALLA'}")
    return emit(ctx, {"findings": res}, lines, ok=not res)


def register(sub):
    p = sub.add_parser("lint", help="Lints de núcleo, playbooks y manual")
    p.add_argument("kind", choices=["core", "playbooks", "manual", "skills"])
    p.set_defaults(func=cmd_lint)
