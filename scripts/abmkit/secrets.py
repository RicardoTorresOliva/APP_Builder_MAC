"""Offline secret scan (defense in depth; CI also runs a dedicated scanner)."""
from __future__ import annotations

import re

from .common import Ctx, cfg, emit, walk_files

PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    "slack-token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "llm-api-key": re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{24,}\b"),
    "google-api-key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "generic-assignment": re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][A-Za-z0-9/+_\-]{16,}['\"]"),
}
TEXT_EXT = (".md", ".py", ".js", ".ts", ".tsx", ".json", ".yaml", ".yml", ".toml", ".env", ".sh", ".cmd", ".ps1", ".html", ".txt", ".sql", ".ini", ".cfg")


def cmd_secrets(ctx: Ctx, args) -> int:
    allow = cfg(ctx.conf, "secrets.allow", []) or []
    exclude = (cfg(ctx.conf, "secrets.exclude", []) or []) + [".git/**"]
    hits, n = [], 0
    for path, rel in walk_files(ctx.root, TEXT_EXT, exclude):
        if path.name.endswith(".example") or path.name == ".env.example":
            continue
        n += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for name, rx in PATTERNS.items():
            for m in rx.finditer(text):
                if any(a in m.group(0) for a in allow):
                    continue
                line = text.count("\n", 0, m.start()) + 1
                hits.append({"file": rel, "line": line, "rule": name})
    lines = [f"POSIBLE SECRETO {h['file']}:{h['line']} ({h['rule']})" for h in hits]
    lines.append(f"Secret scan: {n} archivos · {len(hits)} hallazgos → {'OK' if not hits else 'FALLA'}")
    return emit(ctx, {"files": n, "findings": hits}, lines, ok=not hits)


def register(sub):
    p = sub.add_parser("secrets", help="Escaneo de secretos offline")
    p.set_defaults(func=cmd_secrets)
