"""Token budget: estimated tokens (chars/4) per file vs budgets declared in abm.yaml → budgets."""
from __future__ import annotations

from .common import Ctx, cfg, emit, est_tokens, matches, walk_files


def measure(ctx: Ctx):
    conf, root = ctx.conf, ctx.root
    rules = cfg(conf, "budgets.files", {}) or {}
    exclude = cfg(conf, "okf.exclude", []) or []
    rows, over = [], []
    for path, rel in walk_files(root, (".md",), [e for e in exclude if not e.startswith(".claude")]):
        for pat, limit in rules.items():
            if matches(rel, [pat]):
                t = est_tokens(path.read_text(encoding="utf-8"))
                row = {"file": rel, "tokens": t, "budget": int(limit), "rule": pat}
                rows.append(row)
                if t > int(limit):
                    over.append(row)
                break
    always = cfg(conf, "budgets.always_loaded", []) or []
    total = sum(est_tokens((root / f).read_text(encoding="utf-8")) for f in always if (root / f).exists())
    cap = int(cfg(conf, "budgets.always_loaded_max_tokens", 0) or 0)
    return rows, over, always, total, cap


def cmd_budget(ctx: Ctx, args) -> int:
    rows, over, always, total, cap = measure(ctx)
    ok = not over and (not cap or total <= cap)
    lines = [f"EXCEDE {r['file']}: {r['tokens']} > {r['budget']} tokens ({r['rule']})" for r in over]
    if args.verbose:
        lines += [f"{r['tokens']:>6} / {r['budget']:<6} {r['file']}" for r in sorted(rows, key=lambda r: -r["tokens"])]
    lines.append(f"Siempre cargado ({', '.join(always)}): {total} tokens" + (f" / tope {cap}" if cap else ""))
    lines.append(f"Presupuesto de tokens: {len(rows)} archivos medidos · {len(over)} exceden → {'OK' if ok else 'FALLA'}")
    return emit(ctx, {"always_loaded_tokens": total, "always_loaded_cap": cap, "files": rows, "over": over}, lines, ok)


def register(sub):
    p = sub.add_parser("token-budget", help="Mide tokens por archivo contra el presupuesto")
    p.add_argument("--verbose", "-v", action="store_true")
    p.set_defaults(func=cmd_budget)
