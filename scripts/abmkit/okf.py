"""OKF (Open Knowledge Format, Google Cloud, v0.2) validator + ABM profile + index generator.

Levels: 'spec' checks conformance (§11 of the spec) and the shape of optional families;
'abm' (default) adds the stricter ABM producer profile declared in abm.yaml → okf.
"""
from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

from .common import Ctx, cfg, emit, matches, now_iso, parse_iso, read_md, walk_files, write_text

STATUS = {"draft", "stable", "deprecated"}
ACTOR = re.compile(r"^(human:[^\s]+|process:[^\s]+|[^\s:/]+/[^\s]+)$")
FOOTREF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FOOTDEF = re.compile(r"^\[\^([^\]\s]+)\]:", re.M)
DATE_H = re.compile(r"^## (.+)$", re.M)
CODE = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]*`", re.S)


def _f(file, level, code, msg):
    return {"file": file, "level": level, "code": code, "msg": msg}


def _check_actor_event(rel, name, ev, out):
    if not isinstance(ev, dict):
        out.append(_f(rel, "error", "okf.trust.shape", f"`{name}` debe ser un mapa {{by, at}}"))
        return
    by = ev.get("by")
    if not by:
        out.append(_f(rel, "error", "okf.trust.by", f"`{name}.by` es obligatorio"))
    elif not ACTOR.match(str(by)):
        out.append(_f(rel, "error", "okf.actor", f"`{name}.by` no sigue la convención de actores: {by!r}"))
    at = ev.get("at")
    if at is not None and not parse_iso(at):
        out.append(_f(rel, "error", "okf.datetime", f"`{name}.at` no es ISO 8601 con zona: {at!r}"))
    elif at is not None and parse_iso(at) > _dt.datetime.now(_dt.timezone.utc) + _dt.timedelta(days=1):
        out.append(_f(rel, "warn", "okf.future", f"`{name}.at` está en el futuro: {at}"))


def check_concept(rel: str, fm: dict, body: str, profile: str, conf: dict, out: list):
    """Spec §11: only a parseable frontmatter with a non-empty `type` is a hard requirement; the
    families of §5–§10 are SHOULD for producers → warnings in spec mode, errors in the ABM profile."""
    start = len(out)
    _check_concept(rel, fm, body, profile, conf, out)
    if profile != "abm":
        for f in out[start:]:
            if f["code"] != "okf.type":
                f["level"] = "warn"


def _check_concept(rel: str, fm: dict, body: str, profile: str, conf: dict, out: list):
    typ = fm.get("type")
    if not isinstance(typ, str) or not typ.strip():
        out.append(_f(rel, "error", "okf.type", "falta `type` (obligatorio)"))
    if "generated" in fm:
        _check_actor_event(rel, "generated", fm["generated"], out)
    if "verified" in fm:
        v = fm["verified"]
        for ev in (v if isinstance(v, list) else [v]):
            _check_actor_event(rel, "verified", ev, out)
    if "status" in fm and fm["status"] not in STATUS:
        out.append(_f(rel, "error", "okf.status", f"`status` debe ser draft|stable|deprecated (es {fm['status']!r})"))
    if "stale_after" in fm and not parse_iso(fm["stale_after"]):
        out.append(_f(rel, "error", "okf.datetime", f"`stale_after` no es ISO 8601 con zona: {fm['stale_after']!r}"))
    ids = set()
    if "sources" in fm:
        if not isinstance(fm["sources"], list):
            out.append(_f(rel, "error", "okf.sources", "`sources` debe ser una lista"))
        else:
            for i, s in enumerate(fm["sources"]):
                if not isinstance(s, dict) or not s.get("resource"):
                    out.append(_f(rel, "error", "okf.sources", f"`sources[{i}].resource` es obligatorio"))
                    continue
                if s.get("id"):
                    ids.add(str(s["id"]))
                if s.get("last_modified") and not parse_iso(s["last_modified"]):
                    out.append(_f(rel, "warn", "okf.datetime", f"`sources[{i}].last_modified` no es ISO 8601 con zona"))
    if typ == "Attested Computation":
        for k in ("runtime", "executor", "attester"):
            if not fm.get(k):
                out.append(_f(rel, "error", "okf.attested", f"Attested Computation exige `{k}` (spec §10)"))
    if profile != "abm":
        return
    # ---- ABM producer profile (stricter than the spec, never contradicting it)
    for key in cfg(conf, "okf.require_fields", ["type", "title", "description", "status", "generated"]):
        if key not in fm or fm.get(key) in (None, ""):
            out.append(_f(rel, "error", "abm.required", f"falta `{key}` (perfil ABM)"))
    if "timestamp" in fm:
        out.append(_f(rel, "error", "abm.legacy", "`timestamp` es v0.1: usa `generated.at`"))
    if typ in (cfg(conf, "okf.stale_required_types", []) or []) and "stale_after" not in fm:
        out.append(_f(rel, "error", "abm.stale_after", f"el tipo {typ!r} exige `stale_after`"))
    text = CODE.sub("", body)
    refs = set(FOOTREF.findall(text))
    defs = set(FOOTDEF.findall(text))
    for r in sorted(refs - defs):
        out.append(_f(rel, "error", "abm.footnote", f"nota al pie [^{r}] sin definición"))
    if ids:
        for r in sorted(refs - ids):
            out.append(_f(rel, "warn", "abm.footnote", f"nota al pie [^{r}] no coincide con ningún `sources[].id`"))
    sa = parse_iso(fm.get("stale_after", "")) if fm.get("stale_after") else None
    if sa and _dt.datetime.now(_dt.timezone.utc) >= sa:
        level = "error" if typ in (cfg(conf, "okf.critical_stale_types", []) or []) else "warn"
        out.append(_f(rel, level, "abm.stale", f"contenido caducado desde {fm['stale_after']}"))


def check_index(rel, text, is_root, out):
    fm, body, err = read_md_text(text)
    if err:
        out.append(_f(rel, "error", "okf.index", err))
    if fm is not None:
        extra = set(fm) - {"okf_version"}
        if not is_root or extra:
            out.append(_f(rel, "error", "okf.index", "index.md no admite frontmatter (salvo `okf_version` en la raíz)"))


def check_log(rel, text, out):
    fm, body, _ = read_md_text(text)
    if fm is not None:
        out.append(_f(rel, "warn", "okf.log", "log.md no debería llevar frontmatter"))
    for h in DATE_H.findall(CODE.sub("", body)):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", h.strip()):
            out.append(_f(rel, "error", "okf.log", f"los encabezados de log.md deben ser YYYY-MM-DD (hallado {h!r})"))


def read_md_text(text):
    from .common import FM_RE, yamlmini
    m = FM_RE.match(text)
    if not m:
        return None, text, None
    try:
        return (yamlmini.loads(m.group(1)) or {}), text[m.end():], None
    except Exception as e:  # noqa: BLE001
        return None, text[m.end():], f"frontmatter YAML inválido: {e}"


def validate(ctx: Ctx, paths=None, profile="abm"):
    conf, root = ctx.conf, ctx.root
    exclude = cfg(conf, "okf.exclude", []) or []
    out, n = [], 0
    if paths:
        files = []
        for p in paths:
            rp = (root / p) if not Path(p).is_absolute() else Path(p)
            if rp.is_dir():
                base = rp.relative_to(root).as_posix().rstrip("/") + "/"
                files += [(q, base + r) for q, r in walk_files(rp, (".md",), [e[len(base):] if e.startswith(base) else e for e in exclude])
                          if not matches(base + r, exclude)]
            else:
                files.append((rp, rp.relative_to(root).as_posix() if rp.is_absolute() else p))
    else:
        files = walk_files(root, (".md",), exclude)
    for path, rel in files:
        if not path.exists():
            continue
        n += 1
        text = path.read_text(encoding="utf-8")
        name = path.name
        if name == "index.md":
            from .common import bundle_root
            check_index(rel, text, path.parent.resolve() == bundle_root(root, path), out)
            continue
        if name == "log.md":
            check_log(rel, text, out)
            continue
        fm, body, err = read_md(path)
        if err:
            out.append(_f(rel, "error", "okf.frontmatter", err))
            continue
        if fm is None:
            out.append(_f(rel, "error", "okf.frontmatter", "sin frontmatter YAML (obligatorio en todo concepto)"))
            continue
        check_concept(rel, fm, body, profile, conf, out)
    if profile == "abm" and not paths:
        idx = root / "index.md"
        if not idx.exists():
            out.append(_f("index.md", "error", "abm.index", "falta index.md en la raíz del bundle"))
        else:
            fm, _, _ = read_md(idx)
            if not fm or str(fm.get("okf_version", "")) != str(cfg(conf, "okf.version", "0.2")):
                out.append(_f("index.md", "error", "abm.okf_version", "index.md raíz debe declarar okf_version"))
        if not (root / "log.md").exists():
            out.append(_f("log.md", "error", "abm.log", "falta log.md en la raíz del bundle"))
    return n, out


def build_index(ctx: Ctx) -> str:
    conf, root = ctx.conf, ctx.root
    exclude = (cfg(conf, "okf.exclude", []) or []) + (cfg(conf, "okf.index_exclude", []) or [])
    groups: dict[str, list] = {}
    for path, rel in walk_files(root, (".md",), exclude):
        if path.name in ("index.md", "log.md"):
            continue
        fm, _, err = read_md(path)
        if err or not fm:
            continue
        top = rel.split("/")[0] if "/" in rel else "(raíz)"
        title = fm.get("title") or path.stem
        desc = fm.get("description") or ""
        groups.setdefault(top, []).append((rel, str(title), str(desc)))
    order = cfg(conf, "okf.index_order", []) or []
    keys = sorted(groups, key=lambda k: (order.index(k) if k in order else len(order), k))
    lines = ["---", f'okf_version: "{cfg(conf, "okf.version", "0.2")}"', "---", "",
             "<!-- Generado por `abm okf index`. No editar a mano. -->", ""]
    for k in keys:
        lines.append(f"# {k}")
        lines.append("")
        for rel, title, desc in sorted(groups[k]):
            lines.append(f"* [{title}](/{rel})" + (f" - {desc}" if desc else ""))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


LLMS_SECTIONS = [
    ("Empieza aquí", ["AGENTS.md", "README.md", "QUICKSTART.md", "docs/glossary.md", "docs/manual/"]),
    ("Comandos", ["commands/"]),
    ("Metodología y plantillas", ["methodology/", "templates/"]),
    ("Estándares", ["standards/"]),
    ("Contrato ADS y OKF", ["contract/", "okf/", "profiles/"]),
    ("Stacks", ["stacks/"]),
    ("Integraciones", ["integrations/"]),
    ("Optional", ["docs/adr/", "docs/analysis/", "docs/compat-matrix.md", "agents/"]),
]


def build_llms(ctx: Ctx) -> str:
    conf, root = ctx.conf, ctx.root
    exclude = cfg(conf, "okf.exclude", []) or []
    docs = []
    for path, rel in walk_files(root, (".md",), exclude):
        if path.name in ("index.md", "log.md"):
            continue
        fm, _, err = read_md(path)
        if not err and fm:
            docs.append((rel, str(fm.get("title") or path.stem), str(fm.get("description") or "")))
    m = {}
    if (root / "ads.yaml").exists():
        from .common import load_yaml_file
        m = load_yaml_file(root / "ads.yaml")
    ep = m.get("endpoints") or {}
    mcp = (ep.get("mcp") or {}).get("command") or (ep.get("mcp") or {}).get("url")
    cli = (ep.get("cli") or {}).get("command")
    parts = ["Gobernanza para agentes: `AGENTS.md`."]
    if ep.get("skill"):
        parts.append(f"Skill de operación: `{ep['skill']}`.")
    if mcp:
        parts.append(f"Servidor MCP: `{mcp}`.")
    if cli:
        parts.append(f"CLI: `{cli}` (salida JSON).")
    if (m.get("tokens") or {}).get("report"):
        parts.append(f"Consumo de tokens: `{m['tokens']['report']}`.")
    parts.append("Mapa completo: `index.md`.")
    lines = [f"# {m.get('name') or root.name}", "", f"> {m.get('description') or 'ADS producido con ABM.'}", "", " ".join(parts), ""]
    used = set()
    for title, prefixes in LLMS_SECTIONS:
        items = [(r, t, d) for r, t, d in docs if r not in used and any(r == p or r.startswith(p) for p in prefixes)]
        if not items:
            continue
        lines += [f"## {title}", ""]
        for r, t, d in sorted(items, key=lambda x: (prefixes.index(next(p for p in prefixes if x[0] == p or x[0].startswith(p))), x[0])):
            used.add(r)
            lines.append(f"- [{t}](/{r})" + (f": {d}" if d else ""))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def cmd_validate(ctx: Ctx, args) -> int:
    n, out = validate(ctx, args.paths or None, "spec" if args.spec_only else "abm")
    errors = [f for f in out if f["level"] == "error"]
    warns = [f for f in out if f["level"] == "warn"]
    lines = [f"{f['level'].upper()} {f['file']}: {f['msg']} [{f['code']}]" for f in out]
    lines.append(f"OKF {'spec' if args.spec_only else 'perfil ABM'}: {n} archivos · {len(errors)} errores · {len(warns)} avisos → {'OK' if not errors else 'FALLA'}")
    return emit(ctx, {"files": n, "errors": len(errors), "warnings": len(warns), "findings": out}, lines, ok=not errors)


def cmd_index(ctx: Ctx, args) -> int:
    targets = {"index.md": build_index(ctx), "llms.txt": build_llms(ctx)}
    if args.check:
        stale = [n for n, c in targets.items() if not (ctx.root / n).exists() or (ctx.root / n).read_text(encoding="utf-8") != c]
        ok = not stale
        return emit(ctx, {"up_to_date": ok, "stale": stale}, ["index.md y llms.txt al día" if ok else f"desactualizado: {', '.join(stale)} → ejecuta `abm okf index`"], ok)
    states = {n: write_text(ctx, ctx.root / n, c) for n, c in targets.items()}
    return emit(ctx, {"written": states}, [f"{n} {s}" for n, s in states.items()])


def register(sub):
    p = sub.add_parser("okf", help="Validar OKF y generar index.md")
    s = p.add_subparsers(dest="okf_cmd", required=True)
    v = s.add_parser("validate", help="Valida conformidad OKF v0.2 + perfil ABM")
    v.add_argument("paths", nargs="*")
    v.add_argument("--spec-only", action="store_true", help="solo la conformidad de la spec")
    v.set_defaults(func=cmd_validate)
    i = s.add_parser("index", help="Genera index.md (mapa de contexto) y llms.txt")
    i.add_argument("--check", action="store_true")
    i.set_defaults(func=cmd_index)
