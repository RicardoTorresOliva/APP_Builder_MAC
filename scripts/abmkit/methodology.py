"""`abm methodology classify` (ADR 0006): deterministic router over methodology/router.yaml.

Dimensions come from explicit answers or are inferred from free text with the System One layer
(`decide`; offline fallback = keywords). Escalation/de-escalation triggers apply per module.
Low-confidence dimensions become pending questions (turbo) with their default applied.
"""
from __future__ import annotations

import json
import re

from .common import Ctx, cfg, emit, load_yaml_file, now_iso, write_text
from .common import safe_path
from .decide import decide, kw_match, norm

DEFAULTS = {"uncertainty": 1, "criticality": 0, "horizon": 1, "team": 0, "brownfield": 0, "autonomy": 1}


def load_router(ctx):
    p = ctx.root / "methodology/router.yaml"
    if not p.exists():
        raise FileNotFoundError("falta methodology/router.yaml")
    return load_yaml_file(p)


def infer_dimensions(ctx, router, text, provider=None):
    qs = {}
    for dim, spec in router["dimensions"].items():
        levels = spec.get("levels") or {}
        kw = spec.get("keywords") or {}
        qs[dim] = {"type": "score", "instructions": spec.get("question", dim),
                   "levels": [str(levels.get(str(i), levels.get(i, i))) for i in range(3)],
                   "keywords": {str(k): v for k, v in kw.items()}, "default": DEFAULTS.get(dim, 1)}
    res = decide(ctx, text, qs, provider=provider, use="abm-methodology")
    out = {}
    for dim, a in res["answers"].items():
        v = a.get("value")
        try:
            v = int(v)
        except (TypeError, ValueError):
            v = DEFAULTS.get(dim, 1)
        out[dim] = {"value": v, "confidence": a.get("confidence"), "route": a.get("route"), "source": res["provider"]}
    return out, res


def match_rule(rules, dims):
    for r in rules:
        cond = r.get("if") or {}
        if all(dims.get(k) in [int(x) for x in v] for k, v in cond.items()):
            return r
    return None


def triggers_for(text, router):
    t = norm(text)
    esc = [e for e in (router.get("triggers") or {}).get("escalate", []) if any(kw_match(k, t) for k in e.get("keywords", []))]
    de = [e for e in (router.get("triggers") or {}).get("deescalate", []) if any(kw_match(k, t) for k in e.get("keywords", []))]
    return esc, de


def split_modules(text, explicit):
    if explicit:
        mods = []
        for m in explicit:
            name, _, desc = m.partition("=")
            mods.append((name.strip(), (desc or name).strip()))
        return mods
    mods, grab = [], False
    for line in text.splitlines():
        if re.match(r"^\s*#+\s*.*(m[oó]dulo|key elements|elementos|funcionalidades|features)", line, re.I) or re.match(r"^\s*\*\*(key elements|m[oó]dulos|elementos)", line, re.I):
            grab = True
            continue
        if grab and re.match(r"^\s*#+\s", line):
            grab = False
        m = re.match(r"^\s*[-*]\s+(.+)$", line)
        if grab and m and "[" not in m.group(1)[:1]:
            item = m.group(1).strip()
            name = re.split(r"[:—–-]\s", item, maxsplit=1)[0].strip("* ")[:60]
            mods.append((name, item))
    return mods or [("general", text)]


def classify(ctx, text, answers=None, modules=None, provider=None):
    router = load_router(ctx)
    if answers:
        dims = {k: {"value": int(v), "confidence": 1.0, "route": "act", "source": "respuestas"} for k, v in answers.items()}
        for k, d in DEFAULTS.items():
            dims.setdefault(k, {"value": d, "confidence": 0.0, "route": "human", "source": "default"})
        dres = None
    else:
        dims, dres = infer_dimensions(ctx, router, text, provider)
    vals = {k: v["value"] for k, v in dims.items()}
    base_vals = dict(vals)
    esc_all, _ = triggers_for(text, router)
    if esc_all and vals.get("criticality", 0) < 2:
        vals["criticality"] = 2
        dims["criticality"] = {**dims["criticality"], "value": 2, "note": f"escalado por disparador: {', '.join(e['id'] for e in esc_all)}"}
    ceremony = cfg(ctx.conf, "ceremony") or "producto"
    cer = (router.get("ceremony") or {}).get(ceremony) or {}
    fallback = cer.get("default_mode") or router.get("default_mode", "IDD")
    rule = match_rule(router.get("rules") or [], vals)
    project_mode = rule["mode"] if rule else fallback
    why = rule["why"] if rule else f"sin regla aplicable: modo por defecto de la ceremonia {ceremony}"
    brule = match_rule(router.get("rules") or [], base_vals)
    base_mode = brule["mode"] if brule else fallback
    base_why = brule["why"] if brule else f"modo por defecto de la ceremonia {ceremony}"
    mods = []
    for name, desc in split_modules(text, modules):
        esc, de = triggers_for(desc, router)
        if esc:
            mods.append({"module": name, "mode": esc[0].get("mode", "SDD"), "review": esc[0].get("review", "human"),
                         "why": f"escalamiento: {', '.join(e['id'] for e in esc)}", "triggers": [e["id"] for e in esc]})
        elif de:
            mods.append({"module": name, "mode": de[0].get("mode", "IDD"), "review": "por milestone",
                         "why": f"desescalamiento: {', '.join(e['id'] for e in de)}", "triggers": [e["id"] for e in de]})
        else:
            mode, mwhy = base_mode, base_why
            if modules and not answers:
                # El riesgo es del módulo, no del encargo completo: criticidad inferida solo con su descripción.
                mdims, _ = infer_dimensions(ctx, router, desc, provider)
                mvals = {**base_vals, "criticality": mdims["criticality"]["value"]}
                mrule = match_rule(router.get("rules") or [], mvals)
                mode, mwhy = (mrule["mode"], mrule["why"]) if mrule else (fallback, base_why)
            if esc_all and mode == "VIBE":
                mode = "IDD"
            mods.append({"module": name, "mode": mode, "review": "humana" if mode == "SDD" else "por milestone",
                         "why": mwhy, "triggers": []})
    pending = [{"dimension": k, "default": v["value"], "confidence": v["confidence"],
                "question": router["dimensions"][k].get("question", k)} for k, v in dims.items() if v.get("route") != "act"]
    return {"ceremony": ceremony, "ceremony_rules": cer, "dimensions": dims, "project_mode": project_mode, "why": why,
            "modules": mods, "pending": pending, "provider": (dres or {}).get("provider", "respuestas")}


def render_map(res, title):
    rows = "\n".join(f"| {m['module']} | {m['mode']} | {m['why']} | {m['review']} | {', '.join(m['triggers']) or '—'} |" for m in res["modules"])
    dims = "\n".join(f"| {k} | {v['value']} | {v['confidence']} | {v['source']} |" for k, v in res["dimensions"].items())
    return f"""---
type: Methodology Map
title: Mapa metodológico — {title}
description: Modo metodológico por módulo del ADS, con justificación, revisión y disparadores.
tags: [metodologia, plan]
status: draft
generated: {{ by: process:abm-methodology, at: {now_iso()} }}
---

# Mapa metodológico — {title}

Ceremonia: **{res['ceremony']}** · modo del proyecto: **{res['project_mode']}** · clasificación: {res['provider']}.

| Módulo | Modo | Justificación | Revisión | Disparadores |
|---|---|---|---|---|
{rows}

## Dimensiones
| Dimensión | Nivel (0–2) | Confianza | Fuente |
|---|---|---|---|
{dims}
"""


def cmd_classify(ctx: Ctx, args) -> int:
    text = args.text or ""
    if args.file:
        text += "\n" + safe_path(ctx.root, args.file, "--file").read_text(encoding="utf-8")
    if not text.strip() and not args.answers:
        return emit(ctx, {"error": "sin entrada"}, ["Falta la descripción: --text, --file o --answers"], ok=False)
    answers = json.loads(args.answers) if args.answers else None
    try:
        res = classify(ctx, text, answers, args.module, args.provider)
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        return emit(ctx, {"error": str(e)}, [f"ERROR {e}"], ok=False)
    written = None
    if args.write:
        written = write_text(ctx, safe_path(ctx.root, args.write, "--write"), render_map(res, args.title or "ADS"))
    if args.queue and not ctx.dry_run:
        from .pending import load, _render
        p, t, rows = load(ctx)
        nums = [int(re.sub(r"\D", "", r["ID"]) or 0) for r in rows]
        n = max(nums) if nums else 0
        for q in res["pending"]:
            n += 1
            rows.append({"ID": f"P-{n:03d}", "Tipo": "decisión", "Contexto": f"Metodología: {q['question']}",
                         "Default aplicado": f"nivel {q['default']}", "Alternativa": "otro nivel 0–2",
                         "Impacto si no se responde": "puede cambiar el modo de algún módulo", "Estado": "abierto"})
        write_text(ctx, p, _render(t, rows))
    lines = [f"Proyecto: {res['project_mode']} ({res['why']})"]
    lines += [f"- {m['module']}: {m['mode']} · revisión {m['review']} · {m['why']}" for m in res["modules"]]
    lines += [f"Pendiente (confianza baja): {q['dimension']} = {q['default']} por defecto" for q in res["pending"]]
    if written:
        lines.append(f"{args.write} {written}")
    return emit(ctx, {**res, "written": written}, lines)


def register(sub):
    p = sub.add_parser("methodology", help="Router metodológico")
    s = p.add_subparsers(dest="methodology_cmd", required=True)
    c = s.add_parser("classify", help="Clasifica el encargo y propone modo por módulo")
    c.add_argument("--text")
    c.add_argument("--file", help="p. ej. START_PROJECT.md")
    c.add_argument("--answers", help='JSON {"uncertainty":0-2,...}')
    c.add_argument("--module", action="append", help="nombre=descripción (repetible)")
    c.add_argument("--provider", help="fuerza proveedor de decide")
    c.add_argument("--write", help="ruta donde escribir el methodology-map (OKF)")
    c.add_argument("--title")
    c.add_argument("--queue", action="store_true", help="encola las dimensiones de baja confianza")
    c.set_defaults(func=cmd_classify)
