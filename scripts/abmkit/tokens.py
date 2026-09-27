"""Token control space: JSONL ledger (build + run), report (N1), static dashboard (N2), budgets.

Event schema: contract/token-event.schema.json (aligned with OpenTelemetry GenAI semantic conventions).
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from .common import Ctx, cfg, emit, est_tokens, load_yaml_file, now_iso, write_text

PHASES = ("build", "run")
SOURCES = ("telemetry", "provider-usage", "estimate")


def _manifest(ctx):
    p = ctx.root / "ads.yaml"
    return load_yaml_file(p) if p.exists() else {}


def ledger_path(ctx) -> Path:
    return ctx.root / ((_manifest(ctx).get("tokens") or {}).get("ledger") or "ops/tokens/ledger.jsonl")


def read_ledger(ctx):
    p = ledger_path(ctx)
    if not p.exists():
        return []
    out = []
    for i, ln in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if ln.strip():
            try:
                out.append(json.loads(ln))
            except json.JSONDecodeError:
                out.append({"_invalid_line": i})
    return out


def load_pricing(ctx):
    p = ctx.root / cfg(ctx.conf, "tokens.pricing", "integrations/observability/pricing.yaml")
    return (load_yaml_file(p) or {}).get("models", {}) if p.exists() else {}


def cost(ev, pricing):
    if ev.get("cost_usd") is not None:
        return float(ev["cost_usd"])
    pr = pricing.get(f"{ev.get('provider')}/{ev.get('model')}")
    if not pr or pr.get("input_per_mtok") is None:
        return None
    return round((ev.get("input_tokens", 0) * float(pr["input_per_mtok"]) + ev.get("output_tokens", 0) * float(pr.get("output_per_mtok", 0))) / 1e6, 6)


def validate_event(ev):
    errs = []
    if ev.get("phase") not in PHASES:
        errs.append("phase debe ser build|run")
    if ev.get("source") not in SOURCES:
        errs.append("source debe ser telemetry|provider-usage|estimate")
    for k in ("input_tokens", "output_tokens"):
        if not isinstance(ev.get(k, 0), int) or ev.get(k, 0) < 0:
            errs.append(f"{k} debe ser entero ≥ 0")
    if not ev.get("ts"):
        errs.append("ts obligatorio")
    return errs


def append(ctx, ev):
    errs = validate_event(ev)
    if errs:
        return None, errs
    p = ledger_path(ctx)
    if not ctx.dry_run:
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(ev, ensure_ascii=False, sort_keys=True) + "\n")
    return p, []


def cmd_record(ctx, args):
    ev = {"ts": now_iso(), "phase": args.phase, "source": args.source, "input_tokens": args.input, "output_tokens": args.output,
          "cache_read_tokens": args.cache_read, "provider": args.provider, "model": args.model, "tool": args.tool,
          "actor": args.actor, "unit": args.unit, "command": args.command_name, "feature": args.feature, "tenant": args.tenant,
          "cost_usd": args.cost, "note": args.note}
    ev = {k: v for k, v in ev.items() if v is not None}
    p, errs = append(ctx, ev)
    if errs:
        return emit(ctx, {"errors": errs}, [f"Evento inválido: {'; '.join(errs)}"], ok=False)
    return emit(ctx, {"recorded": ev, "ledger": str(p.relative_to(ctx.root))}, [f"Registrado en {p.relative_to(ctx.root)}: in={ev['input_tokens']} out={ev['output_tokens']} ({ev['source']})"])


def cmd_estimate(ctx, args):
    """Estimate output tokens from files produced (chars/4); marks source=estimate."""
    total = 0
    for f in args.files:
        p = ctx.root / f
        if p.is_file():
            total += est_tokens(p.read_text(encoding="utf-8", errors="ignore"))
        elif p.is_dir():
            for q in p.rglob("*"):
                if q.is_file() and q.suffix in (".md", ".py", ".yaml", ".yml", ".json", ".html", ".js", ".ts", ".toml", ".sh", ".cmd"):
                    total += est_tokens(q.read_text(encoding="utf-8", errors="ignore"))
    ev = {"ts": now_iso(), "phase": args.phase, "source": "estimate", "input_tokens": int(total * args.input_ratio),
          "output_tokens": total, "unit": args.unit, "tool": args.tool, "actor": args.actor, "note": "estimado: caracteres/4 de lo producido"}
    ev = {k: v for k, v in ev.items() if v is not None}
    p, errs = append(ctx, ev)
    return emit(ctx, {"recorded": ev}, [f"Estimado {args.unit}: out≈{total} in≈{ev['input_tokens']} tokens → {p.relative_to(ctx.root) if p else '-'}"], ok=not errs)


def aggregate(events, pricing, by):
    agg = defaultdict(lambda: {"events": 0, "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "cost_known": True, "estimated": 0})
    for ev in events:
        if "_invalid_line" in ev:
            continue
        key = str(ev.get(by) or "—")
        a = agg[key]
        a["events"] += 1
        a["input_tokens"] += int(ev.get("input_tokens", 0))
        a["output_tokens"] += int(ev.get("output_tokens", 0))
        c = cost(ev, pricing)
        if c is None:
            a["cost_known"] = False
        else:
            a["cost_usd"] += c
        a["estimated"] += 1 if ev.get("source") == "estimate" else 0
    return dict(agg)


def budgets_status(ctx, events):
    b = ((_manifest(ctx).get("tokens") or {}).get("budgets")) or {}
    status = []
    total = sum(int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0)) for e in events if "_invalid_line" not in e)
    if "total" in b:
        status.append(_budget_row("total", total, b["total"]))
    if "unit" in b:
        per = defaultdict(int)
        for e in events:
            per[e.get("unit") or "—"] += int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0))
        for u, t in per.items():
            status.append(_budget_row(f"unit:{u}", t, b["unit"]))
    if "feature" in b:
        per = defaultdict(int)
        for e in events:
            if e.get("phase") == "run":
                per[e.get("feature") or "—"] += int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0))
        for u, t in per.items():
            status.append(_budget_row(f"feature:{u}", t, b["feature"]))
    return status


def _budget_row(scope, used, lim):
    soft, hard = (lim.get("soft"), lim.get("hard")) if isinstance(lim, dict) else (lim, None)
    state = "ok"
    if hard and used > int(hard):
        state = "hard"
    elif soft and used > int(soft):
        state = "soft"
    return {"scope": scope, "used": used, "soft": soft, "hard": hard, "state": state}


def report_md(ctx, events, pricing):
    by_unit = aggregate(events, pricing, "unit")
    by_model = aggregate(events, pricing, "model")
    by_phase = aggregate(events, pricing, "phase")
    tin = sum(a["input_tokens"] for a in by_phase.values())
    tout = sum(a["output_tokens"] for a in by_phase.values())
    est = sum(a["estimated"] for a in by_phase.values())
    lines = ["---", "type: Token Report", "title: Reporte de tokens", "description: Consumo de tokens y costo del ADS (construcción y operación), generado desde el ledger.",
             "tags: [tokens, finops]", "status: stable", f"generated: {{ by: process:abm-tokens, at: {now_iso()} }}", "---", "",
             "# Reporte de tokens", "", "<!-- Generado por `abm tokens report`. No editar a mano. -->", "",
             f"- **Total:** {tin + tout:,} tokens (entrada {tin:,} · salida {tout:,}) en {sum(a['events'] for a in by_phase.values())} eventos.",
             f"- **Estimados** (caracteres/4, sin telemetría): {est} eventos.", ""]

    def table(title, agg):
        out = [f"## {title}", "", "| Clave | Eventos | Entrada | Salida | Costo USD |", "|---|---|---|---|---|"]
        for k, a in sorted(agg.items(), key=lambda kv: -(kv[1]["input_tokens"] + kv[1]["output_tokens"])):
            c = f"{a['cost_usd']:.4f}" if a["cost_known"] else (f"≥ {a['cost_usd']:.4f} (precio no registrado)" if a["cost_usd"] else "n/d")
            out.append(f"| {k} | {a['events']} | {a['input_tokens']:,} | {a['output_tokens']:,} | {c} |")
        return out + [""]

    lines += table("Por fase", by_phase) + table("Por unidad (FU/DU/WU)", by_unit) + table("Por modelo", by_model)
    st = budgets_status(ctx, events)
    if st:
        lines += ["## Presupuestos", "", "| Alcance | Usado | Blando | Duro | Estado |", "|---|---|---|---|---|"]
        lines += [f"| {s['scope']} | {s['used']:,} | {s['soft'] or '—'} | {s['hard'] or '—'} | {s['state']} |" for s in st]
    return "\n".join(lines).rstrip() + "\n"


def cmd_report(ctx, args):
    events = read_ledger(ctx)
    pricing = load_pricing(ctx)
    tok = _manifest(ctx).get("tokens") or {}
    target = ctx.root / (tok.get("report") or "TOKENS.md")
    state = write_text(ctx, target, report_md(ctx, events, pricing))
    agg = aggregate(events, pricing, args.by)
    lines = [f"{k}: in={a['input_tokens']:,} out={a['output_tokens']:,} costo={'%.4f' % a['cost_usd'] if a['cost_known'] else 'n/d'}" for k, a in agg.items()]
    lines.append(f"{target.relative_to(ctx.root)} {state} · {len(events)} eventos")
    return emit(ctx, {"by": args.by, "aggregate": agg, "report": str(target.relative_to(ctx.root)), "state": state}, lines)


def cmd_budget(ctx, args):
    st = budgets_status(ctx, read_ledger(ctx))
    hard = [s for s in st if s["state"] == "hard"]
    soft = [s for s in st if s["state"] == "soft"]
    lines = [f"{s['state'].upper()} {s['scope']}: {s['used']:,} tokens (blando {s['soft']}, duro {s['hard']})" for s in st if s["state"] != "ok"]
    lines.append(f"Presupuestos: {len(st)} alcances · {len(soft)} sobre umbral blando (→ cola) · {len(hard)} sobre tope duro (→ bloqueante)")
    return emit(ctx, {"budgets": st}, lines, ok=not hard)


def cmd_attest(ctx, args):
    """Deterministic attester (OKF §10): recomputes totals from the ledger and compares with the report."""
    import re as _re
    events = [e for e in read_ledger(ctx) if "_invalid_line" not in e]
    invalid = [e for e in read_ledger(ctx) if "_invalid_line" in e]
    bad = [i for i, e in enumerate(events) if validate_event(e)]
    tin = sum(int(e.get("input_tokens", 0)) for e in events)
    tout = sum(int(e.get("output_tokens", 0)) for e in events)
    tok = _manifest(ctx).get("tokens") or {}
    rp = ctx.root / (tok.get("report") or "TOKENS.md")
    claimed = None
    if rp.exists():
        m = _re.search(r"\*\*Total:\*\* ([\d,.]+) tokens \(entrada ([\d,.]+) · salida ([\d,.]+)\)", rp.read_text(encoding="utf-8"))
        if m:
            claimed = tuple(int(x.replace(",", "").replace(".", "")) for x in m.groups())
    receipt = {"events": len(events), "invalid_lines": len(invalid), "invalid_events": bad, "total": tin + tout, "input": tin, "output": tout,
               "claimed": claimed}
    ok = claimed == (tin + tout, tin, tout) and not invalid and not bad
    lines = [f"Ledger: {len(events)} eventos · total {tin + tout:,} (entrada {tin:,} · salida {tout:,})",
             f"Reporte {rp.name}: {claimed if claimed else 'sin cifras'}",
             f"Atestación: {'OK — las cifras del reporte salen del ledger' if ok else 'FALLA — regenera con `abm tokens report` o corrige el ledger'}"]
    return emit(ctx, {"verdict": "pass" if ok else "fail", "receipt": receipt}, lines, ok)


def register(sub):
    p = sub.add_parser("tokens", help="Espacio de control de tokens (ledger, reporte, dashboard, presupuestos)")
    s = p.add_subparsers(dest="tokens_cmd", required=True)
    r = s.add_parser("record", help="Registra un evento de consumo")
    r.add_argument("--phase", choices=PHASES, default="build")
    r.add_argument("--source", choices=SOURCES, default="estimate")
    r.add_argument("--input", type=int, default=0)
    r.add_argument("--output", type=int, default=0)
    r.add_argument("--cache-read", type=int, default=None)
    for k in ("provider", "model", "tool", "actor", "unit", "feature", "tenant", "note"):
        r.add_argument(f"--{k}")
    r.add_argument("--command", dest="command_name")
    r.add_argument("--cost", type=float)
    r.set_defaults(func=cmd_record)
    e = s.add_parser("estimate", help="Estima tokens de lo producido (caracteres/4)")
    e.add_argument("--unit", required=True)
    e.add_argument("--phase", choices=PHASES, default="build")
    e.add_argument("--tool")
    e.add_argument("--actor")
    e.add_argument("--input-ratio", type=float, default=3.0, help="tokens de entrada por token producido (estimación)")
    e.add_argument("files", nargs="+")
    e.set_defaults(func=cmd_estimate)
    rp = s.add_parser("report", help="Genera el reporte N1 (TOKENS.md)")
    rp.add_argument("--by", default="unit", choices=["unit", "model", "phase", "feature", "tool", "provider", "tenant"])
    rp.set_defaults(func=cmd_report)
    at = s.add_parser("attest", help="Atesta que las cifras de TOKENS.md salen del ledger (OKF Attested Computation)")
    at.set_defaults(func=cmd_attest)
    b = s.add_parser("budget", help="Verifica presupuestos (falla si se supera un tope duro)")
    b.set_defaults(func=cmd_budget)
    try:
        from . import dashboard
        dashboard.register(s)
    except ImportError:
        pass
