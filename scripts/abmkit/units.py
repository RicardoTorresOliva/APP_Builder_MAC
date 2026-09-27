"""Project-level unit checks ported from v4.1 bash scripts: completeness, work_log, doc-sync, preflight."""
from __future__ import annotations

import re

from .common import Ctx, cfg, emit

ROW = re.compile(r"^\|\s*((?:FU|DU)-?[\w.-]*)\s*\|(.*)$", re.I | re.M)


def _tracker_rows(ctx):
    p = ctx.root / "implementation/task_tracker.md"
    if not p.exists():
        return None
    rows = []
    for m in ROW.finditer(p.read_text(encoding="utf-8")):
        uid, rest = m.group(1).strip(), m.group(2)
        cells = [c.strip().lower() for c in rest.split("|")]
        typ = "DU" if uid.upper().startswith("DU") or "du" in cells[:1] else "FU"
        rows.append({"id": uid, "type": typ, "completed": any(c in ("completed", "completado", "hecho", "done") for c in cells)})
    return rows


def check_units(ctx):
    out = []
    rows = _tracker_rows(ctx)
    if rows is None:
        return [{"level": "error", "msg": "falta implementation/task_tracker.md"}]
    wl = ctx.root / "docs/work_log.md"
    wtext = wl.read_text(encoding="utf-8") if wl.exists() else ""
    done = [r for r in rows if r["completed"]]
    for r in done:
        if r["type"] == "DU" and r["id"] not in wtext:
            out.append({"level": "error", "msg": f"{r['id']} está 'completed' sin entrada en docs/work_log.md (completitud)"})
    if done and done[-1]["id"] not in wtext:
        out.append({"level": "error", "msg": f"última unidad completada ({done[-1]['id']}) sin entrada en work_log (regla 6)"})
    idx = ctx.root / "knowledge/index.md"
    if idx.exists():
        itext = idx.read_text(encoding="utf-8")
        for d in (ctx.root / "design_docs").glob("*.md"):
            if d.name != "README.md" and d.name not in itext:
                out.append({"level": "warn", "msg": f"design_docs/{d.name} no está enlazado desde knowledge/index.md (doc-sync)"})
    return out


def cmd_units(ctx: Ctx, args) -> int:
    f = check_units(ctx)
    errors = [x for x in f if x["level"] == "error"]
    lines = [f"{x['level'].upper()} {x['msg']}" for x in f] + [f"Unidades: {len(errors)} errores → {'OK' if not errors else 'FALLA'}"]
    return emit(ctx, {"findings": f}, lines, ok=not errors)


def cmd_preflight(ctx: Ctx, args) -> int:
    req = ["implementation/user_units.md", "implementation/task_tracker.md", "knowledge/index.md", "docs/project_memory.md"]
    out = []
    for r in req:
        p = ctx.root / r
        if not p.exists():
            out.append({"level": "error", "msg": f"falta {r}"})
        elif sum(1 for l in p.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith(("---", "type:", "title:", "description:", "tags:", "status:", "generated:"))) < 5:
            out.append({"level": "error", "msg": f"{r} está vacío o es plantilla (menos de 5 líneas con contenido)"})
    if not cfg(ctx.conf, "active_profile"):
        out.append({"level": "error", "msg": "abm.yaml → active_profile vacío: elige el perfil en init-project"})
    if not (ctx.root / "ads.yaml").exists():
        out.append({"level": "error", "msg": "falta ads.yaml (Contrato ADS)"})
    errors = [x for x in out if x["level"] == "error"]
    lines = [f"{x['level'].upper()} {x['msg']}" for x in out] + [f"Preflight: {'listo para construir' if not errors else 'completa el plan antes de construir'} → {'OK' if not errors else 'FALLA'}"]
    return emit(ctx, {"findings": out}, lines, ok=not errors)


def register(sub):
    p = sub.add_parser("units", help="Completitud de DU, work_log y doc-sync (proyecto)")
    p.set_defaults(func=cmd_units)
    q = sub.add_parser("preflight", help="Verifica que el plan esté completo antes de start-execution")
    q.set_defaults(func=cmd_preflight)
