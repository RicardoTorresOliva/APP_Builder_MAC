"""Internal link checker for markdown (offline, deterministic)."""
from __future__ import annotations

import re
from urllib.parse import unquote

from .common import Ctx, cfg, emit, walk_files

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]*`", re.S)


def check(ctx: Ctx):
    root = ctx.root
    exclude = (cfg(ctx.conf, "okf.exclude", []) or []) + (cfg(ctx.conf, "links.exclude", []) or [])
    broken, n = [], 0
    for path, rel in walk_files(root, (".md",), exclude):
        text = CODE.sub("", path.read_text(encoding="utf-8"))
        for m in LINK.finditer(text):
            target = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#") or target.startswith("<"):
                continue
            n += 1
            t = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not t:
                continue
            dest = (root / t.lstrip("/")) if t.startswith("/") else (path.parent / t)
            if not dest.exists():
                broken.append({"file": rel, "link": target})
    return n, broken


def cmd_links(ctx: Ctx, args) -> int:
    n, broken = check(ctx)
    lines = [f"ROTO {b['file']}: {b['link']}" for b in broken]
    lines.append(f"Enlaces internos: {n} revisados · {len(broken)} rotos → {'OK' if not broken else 'FALLA'}")
    return emit(ctx, {"checked": n, "broken": broken}, lines, ok=not broken)


def register(sub):
    p = sub.add_parser("links", help="Verifica enlaces internos de markdown")
    p.set_defaults(func=cmd_links)
