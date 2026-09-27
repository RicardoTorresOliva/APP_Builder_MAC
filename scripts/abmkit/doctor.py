"""`abm doctor`: detects tool, OS and dependencies and explains in plain language what is missing."""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys

from .common import Ctx, emit

TOOL_SIGNALS = [
    ("claude-code", ["CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "CLAUDE_CODE"]),
    ("codex", ["CODEX_HOME", "CODEX_SANDBOX", "CODEX_MANAGED_BY_NPM", "CODEX_CI"]),
    ("gemini-cli", ["GEMINI_CLI", "GEMINI_CLI_IDE_SERVER_PORT"]),
    ("cursor", ["CURSOR_TRACE_ID", "CURSOR_AGENT", "CURSOR"]),
    ("windsurf", ["WINDSURF", "CODEIUM_API_KEY"]),
    ("kiro", ["KIRO", "KIRO_PID"]),
    ("antigravity", ["ANTIGRAVITY", "ANTIGRAVITY_AGENT"]),
    ("copilot", ["COPILOT_AGENT", "GITHUB_COPILOT_AGENT"]),
    ("hermes", ["HERMES_HOME", "HERMES_SESSION_ID"]),
]


def detect_tool():
    env = os.environ
    for name, keys in TOOL_SIGNALS:
        if any(k in env for k in keys):
            return name
    term = env.get("TERM_PROGRAM", "").lower()
    if "vscode" in term:
        return "vscode"
    return "unknown"


def _ver(cmd):
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip().splitlines()[0]
    except Exception:  # noqa: BLE001
        return "?"


def cmd_doctor(ctx: Ctx, args) -> int:
    py_ok = sys.version_info >= (3, 9)
    deps = {
        "python": {"ok": py_ok, "version": platform.python_version(), "required": True,
                    "fix": "Instala Python 3.9 o superior desde python.org y vuelve a abrir la terminal."},
        "git": {"ok": bool(shutil.which("git")), "version": _ver(["git", "--version"]), "required": True,
                 "fix": "Instala Git (git-scm.com). Sirve para guardar puntos de control y deshacer."},
        "node": {"ok": bool(shutil.which("node")), "version": _ver(["node", "--version"]), "required": False,
                  "fix": "Opcional: solo lo necesitan algunos stacks o linters (markdownlint)."},
    }
    tool = detect_tool()
    issues = []
    for n, d in deps.items():
        if not d["ok"]:
            issues.append({"dep": n, "required": d["required"], "fix": d["fix"]})
    root = ctx.root
    files = {f: (root / f).exists() for f in ("AGENTS.md", "abm.yaml", "ads.yaml")}
    for f, ok in files.items():
        if not ok and f != "ads.yaml":
            issues.append({"dep": f, "required": True, "fix": f"Falta {f}: estás fuera de un repo ABM o se borró. Ejecuta los comandos desde la carpeta del proyecto."})
    lines = [f"Herramienta: {tool} · SO: {platform.system()} {platform.release()} · Python {platform.python_version()}"]
    for n, d in deps.items():
        lines.append(f"{'✔' if d['ok'] else ('✖' if d['required'] else '–')} {n}: {d['version'] or 'no instalado'}")
    for i in issues:
        lines.append(f"{'BLOQUEA' if i['required'] else 'OPCIONAL'} {i['dep']}: {i['fix']}")
    blocking = [i for i in issues if i["required"]]
    lines.append("Listo." if not blocking else f"Faltan {len(blocking)} requisitos obligatorios.")
    return emit(ctx, {"tool": tool, "os": platform.system(), "deps": deps, "files": files, "issues": issues}, lines, ok=not blocking)


def register(sub):
    p = sub.add_parser("doctor", help="Diagnóstico del entorno en lenguaje simple")
    p.set_defaults(func=cmd_doctor)
