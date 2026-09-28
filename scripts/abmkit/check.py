"""`abm check`: runs every validator (the CI entry point)."""
from __future__ import annotations

import argparse
import contextlib
import io
import json

from .common import Ctx, emit

CHECKS = [
    ("okf", ["okf", "validate"]),
    ("okf-index", ["okf", "index", "--check"]),
    ("links", ["links"]),
    ("token-budget", ["token-budget"]),
    ("secrets", ["secrets"]),
    ("sync", ["sync", "--check"]),
    ("ads-check", ["ads-check"]),
    ("lint-core", ["lint", "core"]),
    ("lint-playbooks", ["lint", "playbooks"]),
    ("lint-manual", ["lint", "manual"]),
    ("lint-skills", ["lint", "skills"]),
    ("units", ["units"]),
    ("tokens-attest", ["tokens", "attest"]),
    ("tokens-budget", ["tokens", "budget"]),
    ("agent-conformance", ["agent-conformance"]),
]


def cmd_check(ctx: Ctx, args) -> int:
    from .cli import build_parser
    ap = build_parser()
    results, lines = [], []
    only = set(args.only.split(",")) if args.only else None
    for name, argv in CHECKS:
        if only and name not in only:
            continue
        try:
            a = ap.parse_args(argv)
        except SystemExit:
            results.append({"check": name, "ok": None, "note": "no disponible"})
            lines.append(f"–  {name}: no disponible")
            continue
        a.json, a.dry_run = True, False
        sub = Ctx(ctx.root, True, False)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                code = a.func(sub, a)
            except Exception as e:  # noqa: BLE001 — un validador roto no tumba a los demás
                print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
                code = 1
        try:
            data = json.loads(buf.getvalue() or "{}")
        except json.JSONDecodeError:
            data = {"raw": buf.getvalue()[-2000:]}
        ok = code == 0
        results.append({"check": name, "ok": ok, "data": data})
        lines.append(f"{'✔' if ok else '✖'} {name}")
    failed = [r["check"] for r in results if r["ok"] is False]
    lines.append(f"abm check: {len(results)} checks · {len(failed)} fallan" + (f" ({', '.join(failed)})" if failed else "") + f" → {'OK' if not failed else 'FALLA'}")
    if ctx.json:
        return emit(ctx, {"results": results, "failed": failed}, ok=not failed)
    if failed and args.verbose:
        for r in results:
            if r["ok"] is False:
                lines.append(json.dumps(r["data"], ensure_ascii=False)[:1500])
    return emit(ctx, {}, lines, ok=not failed)


def register(sub):
    p = sub.add_parser("check", help="Ejecuta todos los validadores (entrada de CI)")
    p.add_argument("--only", help="lista separada por comas")
    p.add_argument("--verbose", "-v", action="store_true")
    p.set_defaults(func=cmd_check)
