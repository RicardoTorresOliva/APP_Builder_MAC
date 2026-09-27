"""Minimal, dependency-free YAML subset parser used by ABM (frontmatter, abm.yaml, ads.yaml).

Supported subset (documented in okf/PROFILE.md):
- block mappings and block sequences by indentation (spaces only);
- scalars: plain, 'single' and "double" quoted, int, float, true/false, null/~;
- flow sequences  [a, "b c", 3]  and flow mappings  { k: v, k2: [x, y] } (nesting allowed);
- sequence items that open a mapping on the dash line ("- id: x" + indented keys);
- literal/folded block scalars ( | and > ) with indentation;
- comments (# ...) outside quotes.
Dates and timestamps are returned as strings (never converted), so results are identical everywhere.
"""
from __future__ import annotations

import re

__all__ = ["loads", "YAMLError"]


class YAMLError(ValueError):
    pass


_INT = re.compile(r"^[-+]?\d+$")
_FLOAT = re.compile(r"^[-+]?(\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?$")


def _strip_comment(line: str) -> str:
    out, q = [], None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "'\"":
            q = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _scalar(tok: str):
    t = tok.strip()
    if t == "":
        return None
    if (t[0] == t[-1] == '"') and len(t) >= 2:
        return bytes(t[1:-1], "utf-8").decode("unicode_escape") if "\\" in t else t[1:-1]
    if (t[0] == t[-1] == "'") and len(t) >= 2:
        return t[1:-1].replace("''", "'")
    low = t.lower()
    if low in ("null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    if _INT.match(t):
        return int(t)
    if _FLOAT.match(t) and not re.match(r"^\d+\.\d+\.\d+", t):
        try:
            return float(t)
        except ValueError:
            return t
    return t


class _Flow:
    def __init__(self, s: str):
        self.s, self.i = s, 0

    def ws(self):
        while self.i < len(self.s) and self.s[self.i] in " \t":
            self.i += 1

    def parse(self):
        self.ws()
        c = self.s[self.i] if self.i < len(self.s) else ""
        if c == "[":
            return self.seq()
        if c == "{":
            return self.map()
        return self.atom(",]}")

    def atom(self, stops):
        self.ws()
        if self.i < len(self.s) and self.s[self.i] in "'\"":
            q = self.s[self.i]
            j = self.i + 1
            while j < len(self.s):
                if self.s[j] == q:
                    if q == "'" and j + 1 < len(self.s) and self.s[j + 1] == "'":
                        j += 2
                        continue
                    break
                j += 1
            tok = self.s[self.i : j + 1]
            self.i = j + 1
            return _scalar(tok)
        j = self.i
        depth = 0
        while j < len(self.s):
            ch = self.s[j]
            if ch in "[{":
                depth += 1
            elif ch in "]}" and depth:
                depth -= 1
            elif depth == 0 and ch in stops:
                break
            j += 1
        tok = self.s[self.i : j]
        self.i = j
        return _scalar(tok)

    def seq(self):
        self.i += 1
        out = []
        while True:
            self.ws()
            if self.i >= len(self.s):
                raise YAMLError("unterminated flow sequence")
            if self.s[self.i] == "]":
                self.i += 1
                return out
            out.append(self.parse())
            self.ws()
            if self.i < len(self.s) and self.s[self.i] == ",":
                self.i += 1

    def map(self):
        self.i += 1
        out = {}
        while True:
            self.ws()
            if self.i >= len(self.s):
                raise YAMLError("unterminated flow mapping")
            if self.s[self.i] == "}":
                self.i += 1
                return out
            key = self.atom(":,}")
            self.ws()
            if self.i < len(self.s) and self.s[self.i] == ":":
                self.i += 1
                out[str(key)] = self.parse()
            else:
                out[str(key)] = None
            self.ws()
            if self.i < len(self.s) and self.s[self.i] == ",":
                self.i += 1


def _value(tok: str):
    t = tok.strip()
    if t.startswith("[") or t.startswith("{"):
        f = _Flow(t)
        v = f.parse()
        f.ws()
        if f.i != len(t):
            raise YAMLError(f"trailing characters in flow value: {t!r}")
        return v
    return _scalar(t)


_KEY = re.compile(r"""^(?P<key>"[^"]*"|'[^']*'|[^:#'"][^:#]*?)\s*:(?:\s+(?P<rest>.*)|\s*)$""")


def loads(text: str):
    raw = text.replace("\t", "    ").splitlines()
    lines = []  # (indent, content, rawline)
    for r in raw:
        c = _strip_comment(r)
        if c.strip() == "" or c.strip() in ("---", "..."):
            lines.append((None, "", r))
            continue
        lines.append((len(c) - len(c.lstrip(" ")), c.strip(), r))
    pos = [0]

    def skip():
        while pos[0] < len(lines) and lines[pos[0]][0] is None:
            pos[0] += 1

    def block_scalar(style, parent_indent):
        buf, ind = [], None
        while pos[0] < len(raw):
            r = raw[pos[0]]
            if r.strip() == "":
                buf.append("")
                pos[0] += 1
                continue
            cur = len(r) - len(r.lstrip(" "))
            if cur <= parent_indent:
                break
            ind = cur if ind is None else ind
            buf.append(r[ind:])
            pos[0] += 1
        while buf and buf[-1] == "":
            buf.pop()
        return ("\n".join(buf) + "\n") if style == "|" else " ".join(x.strip() for x in buf) + "\n"

    def parse_block(indent):
        skip()
        if pos[0] >= len(lines):
            return None
        ind, content, _ = lines[pos[0]]
        if content.startswith("- ") or content == "-":
            return parse_seq(ind)
        return parse_map(ind)

    def parse_map(indent, first=None):
        out = {}
        if first is not None:
            k, v = first
            out.update({k: v})
        while True:
            skip()
            if pos[0] >= len(lines):
                return out
            ind, content, _ = lines[pos[0]]
            if ind < indent:
                return out
            if ind > indent:
                raise YAMLError(f"bad indentation at line {pos[0]+1}: {content!r}")
            if content.startswith("- "):
                return out
            m = _KEY.match(content)
            if not m:
                raise YAMLError(f"expected 'key: value' at line {pos[0]+1}: {content!r}")
            key = str(_scalar(m.group("key")))
            rest = m.group("rest")
            pos[0] += 1
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                out[key] = block_scalar(rest[0], ind)
            elif rest is None or rest == "":
                skip()
                if pos[0] < len(lines) and lines[pos[0]][0] is not None and (
                    lines[pos[0]][0] > ind or (lines[pos[0]][0] == ind and lines[pos[0]][1].startswith("- "))
                ):
                    out[key] = parse_block(lines[pos[0]][0])
                else:
                    out[key] = None
            else:
                out[key] = _value(rest)

    def parse_seq(indent):
        out = []
        while True:
            skip()
            if pos[0] >= len(lines):
                return out
            ind, content, _ = lines[pos[0]]
            if ind < indent or not (content.startswith("- ") or content == "-"):
                return out
            if ind > indent:
                raise YAMLError(f"bad indentation at line {pos[0]+1}")
            item = content[1:].strip()
            pos[0] += 1
            if item == "":
                out.append(parse_block(indent + 1))
                continue
            m = _KEY.match(item) if not item.startswith(("[", "{", '"', "'")) else None
            if m:
                key = str(_scalar(m.group("key")))
                rest = m.group("rest")
                child_indent = ind + 2
                if rest is None or rest == "":
                    skip()
                    val = parse_block(lines[pos[0]][0]) if pos[0] < len(lines) and lines[pos[0]][0] is not None and lines[pos[0]][0] > child_indent else None
                else:
                    val = _value(rest)
                out.append(parse_map(child_indent, (key, val)))
            else:
                out.append(_value(item))

    skip()
    if pos[0] >= len(lines):
        return None
    result = parse_block(lines[pos[0]][0])
    skip()
    if pos[0] < len(lines):
        raise YAMLError(f"unexpected content at line {pos[0]+1}: {lines[pos[0]][1]!r}")
    return result
