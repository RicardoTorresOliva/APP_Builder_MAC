"""Shared helpers: repo root, config, frontmatter, output protocol, globbing."""
from __future__ import annotations

import datetime as _dt
import fnmatch
import json
import math
import os
import re
import sys
from pathlib import Path

from . import yamlmini

FM_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)

DEFAULT_EXCLUDE = [
    ".git/**", "node_modules/**", "**/node_modules/**", ".venv/**", "**/.venv/**", "**/__pycache__/**",
]


def find_root(start: str | None = None) -> Path:
    if start:  # --root explícito: se respeta tal cual
        return Path(start).resolve()
    p = Path(os.getcwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "abm.yaml").exists() or (cand / "AGENTS.md").exists() and (cand / ".git").exists():
            return cand
    return p


def load_yaml_file(path: Path):
    return yamlmini.loads(path.read_text(encoding="utf-8")) or {}


def load_config(root: Path) -> dict:
    f = root / "abm.yaml"
    return load_yaml_file(f) if f.exists() else {}


def cfg(conf: dict, dotted: str, default=None):
    cur = conf
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur


def read_md(path: Path):
    """Return (frontmatter|None, body, error|None)."""
    try:
        text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    except (UnicodeDecodeError, OSError) as e:
        return None, "", f"no se puede leer como UTF-8: {e}"
    m = FM_RE.match(text)
    if not m:
        return None, text, None
    try:
        fm = yamlmini.loads(m.group(1))
    except (yamlmini.YAMLError, ValueError, RecursionError) as e:
        return None, text[m.end():], f"frontmatter YAML inválido: {e}"
    if fm is not None and not isinstance(fm, dict):
        return None, text[m.end():], "el frontmatter no es un mapa YAML"
    return fm or {}, text[m.end():], None


def est_tokens(text: str) -> int:
    return math.ceil(len(text) / 4)


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


ISO_DT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:\d{2})$")


def parse_iso(s: str):
    s = str(s)
    if not ISO_DT.match(s):
        return None
    try:
        return _dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _glob_to_re(pat: str) -> re.Pattern:
    i, out = 0, ""
    while i < len(pat):
        if pat.startswith("**/", i):
            out += "(?:.*/)?"
            i += 3
        elif pat.startswith("**", i):
            out += ".*"
            i += 2
        elif pat[i] == "*":
            out += "[^/]*"
            i += 1
        elif pat[i] == "?":
            out += "[^/]"
            i += 1
        else:
            out += re.escape(pat[i])
            i += 1
    return re.compile("^" + out + "$")


def matches(rel: str, patterns) -> bool:
    rel = rel.replace(os.sep, "/")
    for p in patterns or []:
        if _glob_to_re(p).match(rel) or fnmatch.fnmatch(rel, p):
            return True
    return False


def walk_files(root: Path, suffixes=(".md",), exclude=None):
    exclude = list(DEFAULT_EXCLUDE) + list(exclude or [])
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root).replace(os.sep, "/")
        rel_dir = "" if rel_dir == "." else rel_dir + "/"
        dirnames[:] = sorted(d for d in dirnames if not matches(rel_dir + d + "/", exclude) and not matches(rel_dir + d + "/x", exclude) and d != ".git")
        for fn in sorted(filenames):
            rel = rel_dir + fn
            if suffixes and not fn.endswith(tuple(suffixes)):
                continue
            if matches(rel, exclude):
                continue
            yield root / rel, rel


def bundle_root(root: Path, file: Path) -> Path:
    """Nearest ancestor (inside `root`) that is itself an ADS bundle (has abm.yaml or ads.yaml); else `root`."""
    r = root.resolve()
    cur = file.resolve().parent
    while cur != r and r in cur.parents:
        if (cur / "abm.yaml").exists() or (cur / "ads.yaml").exists():
            return cur
        cur = cur.parent
    return r


class Ctx:
    def __init__(self, root: Path, as_json: bool = False, dry_run: bool = False):
        self.root, self.json, self.dry_run = root, as_json, dry_run
        self.conf = load_config(root)


def emit(ctx: Ctx, data: dict, lines=None, ok: bool = True) -> int:
    """Output protocol: --json → machine JSON; otherwise terse lines. Returns exit code."""
    if ctx.json:
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
    else:
        for ln in lines or []:
            print(ln)
    return 0 if ok else 1


def write_text(ctx: Ctx, path: Path, content: str) -> str:
    """Write unless --dry-run. Returns 'created' | 'updated' | 'unchanged' | 'would-*'."""
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return "unchanged"
    state = "updated" if old is not None else "created"
    if ctx.dry_run:
        return "would-" + state
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:  # Python 3.9: write_text() no admite newline
        f.write(content)
    return state


def safe_path(root: Path, rel, what: str = "ruta") -> Path:
    """Resolve a user/agent-supplied path and refuse anything outside the repo root."""
    p = (root / str(rel)).resolve() if not Path(str(rel)).is_absolute() else Path(str(rel)).resolve()
    r = root.resolve()
    if p != r and r not in p.parents:
        raise ValueError(f"{what} fuera del repositorio: {rel}")
    return p


def die(msg: str, code: int = 2):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)
