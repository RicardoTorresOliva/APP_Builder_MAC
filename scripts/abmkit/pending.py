"""Pending queue (`docs/_work/PENDIENTES.md`): list, add and resolve non-blocking decisions in batch."""
from __future__ import annotations

import re

from .common import Ctx, cfg, emit, now_iso, write_text

COLS = ["ID", "Tipo", "Contexto", "Default aplicado", "Alternativa", "Impacto si no se responde", "Estado"]
TYPES = ("decisión", "aprobación", "credencial", "revisión", "propuesta de alcance")


def _path(ctx):
    return ctx.root / (cfg(ctx.conf, "pending.path", "docs/_work/PENDIENTES.md"))


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse(text):
    rows = []
    for ln in text.splitlines():
        if ln.startswith("| P-"):
            c = _cells(ln)
            if len(c) >= len(COLS):
                rows.append(dict(zip(COLS, c[: len(COLS)])))
    return rows


def _row(r):
    return "| " + " | ".join(str(r.get(k, "")).replace("|", "/") for k in COLS) + " |"


def _render(text, rows):
    out, done = [], False
    for ln in text.splitlines():
        if ln.startswith("| P-"):
            if not done:
                out.extend(_row(r) for r in rows)
                done = True
            continue
        out.append(ln)
    if not done:
        if not any(l.startswith("| ID ") for l in out):
            out += ["", "| " + " | ".join(COLS) + " |", "|" + "---|" * len(COLS)]
        out.extend(_row(r) for r in rows)
    return "\n".join(out).rstrip() + "\n"


TEMPLATE = """---
type: Pending Queue
title: Cola de pendientes
description: Decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado.
tags: [turbo, pendientes]
status: draft
generated: {{ by: process:abm-pending, at: {now} }}
---

# Cola de pendientes

Cada ítem ya tiene su default aplicado. Responde solo si quieres cambiarlo (`abm pending resolve P-00N --answer "..."`).

| {cols} |
|{sep}
"""


def load(ctx):
    p = _path(ctx)
    text = p.read_text(encoding="utf-8") if p.exists() else TEMPLATE.format(now=now_iso(), cols=" | ".join(COLS), sep="---|" * len(COLS))
    return p, text, parse(text)


def cmd_list(ctx, args):
    _, _, rows = load(ctx)
    if not args.all:
        rows = [r for r in rows if r["Estado"].startswith("abierto")]
    lines = [f"{r['ID']} [{r['Tipo']}] {r['Contexto']} → default: {r['Default aplicado']}" for r in rows]
    lines.append(f"Pendientes {'(todos)' if args.all else 'abiertos'}: {len(rows)}")
    return emit(ctx, {"pending": rows}, lines)


def cmd_add(ctx, args):
    p, text, rows = load(ctx)
    if args.type not in TYPES:
        return emit(ctx, {"error": "tipo inválido"}, [f"Tipo inválido. Usa: {', '.join(TYPES)}"], ok=False)
    nums = [int(re.sub(r"\D", "", r["ID"]) or 0) for r in rows]
    new = {"ID": f"P-{(max(nums) + 1 if nums else 1):03d}", "Tipo": args.type, "Contexto": args.context,
           "Default aplicado": args.default, "Alternativa": args.alternative or "—",
           "Impacto si no se responde": args.impact or "—", "Estado": "abierto"}
    rows.append(new)
    state = write_text(ctx, p, _render(text, rows))
    return emit(ctx, {"added": new, "file": state}, [f"{new['ID']} añadido ({state})"])


def cmd_resolve(ctx, args):
    p, text, rows = load(ctx)
    ids = set(args.ids)
    hit = [r for r in rows if r["ID"] in ids]
    for r in hit:
        r["Estado"] = f"resuelto: {args.answer or 'default aceptado'}"
    state = write_text(ctx, p, _render(text, rows))
    missing = ids - {r["ID"] for r in hit}
    lines = [f"{r['ID']} → {r['Estado']}" for r in hit] + [f"No existe: {m}" for m in sorted(missing)]
    return emit(ctx, {"resolved": [r["ID"] for r in hit], "missing": sorted(missing), "file": state}, lines, ok=not missing)


def register(sub):
    p = sub.add_parser("pending", help="Cola de pendientes (turbo)")
    s = p.add_subparsers(dest="pending_cmd", required=True)
    l = s.add_parser("list"); l.add_argument("--all", action="store_true"); l.set_defaults(func=cmd_list)
    a = s.add_parser("add")
    a.add_argument("--type", required=True, help="|".join(TYPES))
    a.add_argument("--context", required=True)
    a.add_argument("--default", required=True)
    a.add_argument("--alternative")
    a.add_argument("--impact")
    a.set_defaults(func=cmd_add)
    r = s.add_parser("resolve"); r.add_argument("ids", nargs="+"); r.add_argument("--answer")
    r.set_defaults(func=cmd_resolve)
