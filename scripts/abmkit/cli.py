"""ABM command-line entry point. Every command supports --json (machine output) and --dry-run where it writes."""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
from pathlib import Path

from . import __version__
from .common import Ctx, find_root

MODULES = [
    "okf", "links", "budget", "units", "lint", "doctor", "sync", "ads", "tokens", "pending",
    "methodology", "decide", "conformance", "mcp_server", "newads", "secrets", "check",
]


def build_parser():
    ap = argparse.ArgumentParser(prog="abm", description="APP_Builder_MAC — CLI de la fábrica de ADS")
    ap.add_argument("--version", action="version", version=f"abm {__version__}")
    ap.add_argument("--json", action="store_true", help="salida JSON para agentes")
    ap.add_argument("--dry-run", action="store_true", help="no escribe nada; informa qué haría")
    ap.add_argument("--root", default=None, help="raíz del repo (por defecto: se detecta)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in MODULES:
        try:
            mod = importlib.import_module(f"abmkit.{name}")
        except ModuleNotFoundError as e:
            if e.name and e.name.startswith("abmkit"):
                continue
            raise
        mod.register(sub)
    return ap


def _utf8_streams():
    """Windows consoles/pipes may default to cp1252: force UTF-8 so ✔/→/tildes never crash."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv=None) -> int:
    _utf8_streams()
    argv = list(sys.argv[1:] if argv is None else argv)
    flags = {f: (f in argv) for f in ("--json", "--dry-run")}
    argv = [a for a in argv if a not in flags]
    ap = build_parser()
    args = ap.parse_args(argv)
    args.json = args.json or flags["--json"]
    args.dry_run = args.dry_run or flags["--dry-run"]
    ctx = Ctx(find_root(args.root), args.json, args.dry_run)
    try:
        return int(args.func(ctx, args) or 0)
    except (ValueError, FileNotFoundError, PermissionError, KeyError, OSError) as e:
        if os.environ.get("ABM_DEBUG"):
            raise
        msg = f"{type(e).__name__}: {e}"
        if ctx.json:
            print(json.dumps({"error": msg}, ensure_ascii=False))
        else:
            print(f"ERROR {msg}  (detalle: ABM_DEBUG=1)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
