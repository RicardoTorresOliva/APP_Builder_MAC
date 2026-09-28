"""`abm agent-conformance`: dynamic check (executes the MCP command declared by the ADS: use it on trusted repos only) that an external agent can operate an ADS (ADR 0010).

Generic MCP stdio client (standard library): initialize → tools/list → read tool → write tool in
dry-run → resources (tokens). Level `minimo` ADS without MCP get the static checks only.
Optional `--hermes`: smoke test with the Hermes CLI if installed (one-shot mode).
"""
from __future__ import annotations

import json
import queue
import re
import shlex
import shutil
import subprocess
import sys
import threading
from pathlib import Path

from .common import Ctx, emit, load_yaml_file, read_md

NAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
SKILL_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


class Client:
    def __init__(self, cmd, cwd, timeout=60):
        import os
        argv = shlex.split(cmd, posix=(os.name != "nt"))
        if argv and argv[0] in ("python3", "python"):
            argv[0] = sys.executable
        env = {**__import__("os").environ, "ABM_NO_AUDIT": "1", "PYTHONUTF8": "1"}
        self.p = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                  text=True, encoding="utf-8", bufsize=1, env=env)
        self.q: queue.Queue = queue.Queue()
        self.timeout, self.nid = timeout, 0
        threading.Thread(target=self._reader, daemon=True).start()

    def _reader(self):
        for line in self.p.stdout:
            line = line.strip()
            if line:
                try:
                    self.q.put(json.loads(line))
                except json.JSONDecodeError:
                    self.q.put({"_invalid": line})

    def request(self, method, params=None):
        self.nid += 1
        mid = self.nid
        self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": mid, "method": method, "params": params or {}}) + "\n")
        self.p.stdin.flush()
        while True:
            msg = self.q.get(timeout=self.timeout)
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result")

    def notify(self, method, params=None):
        self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": method, "params": params or {}}) + "\n")
        self.p.stdin.flush()

    def close(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=10)
        except Exception:  # noqa: BLE001
            self.p.kill()


def minimal_args(schema: dict) -> dict:
    """Smallest valid arguments for the required properties of an inputSchema (for a real dry-run)."""
    out = {}
    props = schema.get("properties") or {}
    for k in schema.get("required") or []:
        sp = props.get(k) or {}
        if "enum" in sp:
            out[k] = sp["enum"][0]
        else:
            out[k] = {"string": "conformance", "integer": 1, "number": 1, "boolean": False, "array": [], "object": {}}.get(sp.get("type"), "conformance")
    return out


def static_checks(root: Path, m: dict):
    steps = []
    ep = m.get("endpoints") or {}
    for key in ("agents_md", "llms_txt"):
        ok = bool(ep.get(key)) and (root / ep[key]).exists()
        steps.append({"step": f"descubrir:{key}", "ok": ok, "detail": ep.get(key)})
    sk = ep.get("skill")
    ok, detail = False, sk
    if sk and (root / sk).exists():
        fm, _, err = read_md(root / sk)
        extra = set(fm or {}) - SKILL_KEYS
        name_ok = (fm or {}).get("name") == Path(sk).parent.name
        ok = bool(fm) and not err and not extra and name_ok and bool((fm or {}).get("description"))
        detail = f"{sk} (claves extra: {sorted(extra)})" if extra else sk
    steps.append({"step": "descubrir:skill", "ok": ok, "detail": detail})
    llms = root / (ep.get("llms_txt") or "llms.txt")
    if llms.exists():
        steps.append({"step": "descubrir:llms.txt-h1", "ok": llms.read_text(encoding="utf-8").lstrip("﻿").startswith("# "), "detail": "H1 obligatorio"})
    return steps


def mcp_checks(root: Path, m: dict, cmd: str):
    steps = []
    caps = {c.get("mcp_tool") for c in (m.get("capabilities") or []) if isinstance(c, dict) and c.get("mcp_tool")}
    c = Client(cmd, root)
    try:
        init = c.request("initialize", {"protocolVersion": "2025-11-25", "capabilities": {},
                                        "clientInfo": {"name": "abm-conformance", "version": "5.0.0"}})
        steps.append({"step": "initialize", "ok": bool(init.get("protocolVersion")) and bool(init.get("serverInfo")),
                      "detail": f"{init.get('serverInfo', {}).get('name')} · {init.get('protocolVersion')}"})
        c.notify("notifications/initialized")
        tools = c.request("tools/list").get("tools", [])
        bad = [t.get("name") for t in tools if not NAME_RE.match(t.get("name", "")) or not t.get("description") or "inputSchema" not in t]
        long_desc = [t["name"] for t in tools if len(t.get("description", "")) > 300]
        steps.append({"step": "tools/list", "ok": bool(tools) and not bad, "detail": f"{len(tools)} tools; inválidas: {bad}"})
        steps.append({"step": "tools:descripciones-cortas", "ok": not long_desc, "detail": f"> 300 caracteres: {long_desc}"})
        names = {t["name"] for t in tools}
        missing = sorted(caps - names)
        steps.append({"step": "ads.yaml↔tools", "ok": not missing, "detail": f"capacidades sin tool: {missing}"})
        no_ann = [t["name"] for t in tools if "readOnlyHint" not in (t.get("annotations") or {})]
        steps.append({"step": "tools:anotaciones", "ok": not no_ann, "detail": f"sin readOnlyHint: {no_ann}"})
        ro = next((t for t in tools if (t.get("annotations") or {}).get("readOnlyHint") and not (t.get("inputSchema") or {}).get("required")), None)
        if ro:
            r = c.request("tools/call", {"name": ro["name"], "arguments": {}})
            steps.append({"step": f"leer:{ro['name']}", "ok": not r.get("isError") and bool(r.get("content")), "detail": "lectura"})
        else:
            steps.append({"step": "leer", "ok": False, "detail": "no hay tool de lectura sin argumentos obligatorios"})
        wr = [t for t in tools if not (t.get("annotations") or {}).get("readOnlyHint") and "dry_run" in ((t.get("inputSchema") or {}).get("properties") or {})]
        wr.sort(key=lambda t: (bool((t.get("annotations") or {}).get("destructiveHint")), len((t.get("inputSchema") or {}).get("required") or [])))
        fixture = (m.get("conformance") or {}).get("dry_run") or {}
        if fixture.get("tool"):
            wr = [t for t in tools if t["name"] == fixture["tool"]] or wr
        if wr:
            args = dict(fixture.get("arguments") or {}) if fixture.get("tool") == wr[0]["name"] else minimal_args(wr[0].get("inputSchema") or {})
            r = c.request("tools/call", {"name": wr[0]["name"], "arguments": {**args, "dry_run": True}})
            sc = r.get("structuredContent") or {}
            status = sc.get("status") if isinstance(sc.get("status"), int) else None
            if not r.get("isError") and sc.get("dry_run") is True:
                steps.append({"step": f"dry-run:{wr[0]['name']}", "ok": True, "detail": "escritura simulada"})
            elif r.get("isError") and status and 400 <= status < 500:
                steps.append({"step": f"dry-run:{wr[0]['name']}", "ok": True, "detail": f"rechazo controlado {status} ({sc.get('title')}); declara `conformance.dry_run` en ads.yaml para un caso válido"})
            else:
                steps.append({"step": f"dry-run:{wr[0]['name']}", "ok": False, "detail": f"error no controlado: {str(sc)[:160]}"})
        else:
            steps.append({"step": "dry-run", "ok": True, "detail": "sin tools de escritura con dry_run (no aplica)"})
        res = c.request("resources/list").get("resources", [])
        tok = next((r for r in res if "token" in r.get("uri", "")), None)
        if tok:
            rd = c.request("resources/read", {"uri": tok["uri"]})
            txt = (rd.get("contents") or [{}])[0].get("text", "")
            try:
                json.loads(txt)
                ok = True
            except json.JSONDecodeError:
                ok = False
            steps.append({"step": f"tokens:{tok['uri']}", "ok": ok, "detail": "resumen de consumo legible"})
        else:
            steps.append({"step": "tokens", "ok": False, "detail": "no hay recurso de tokens (p. ej. <id>://tokens/summary)"})
    except Exception as e:  # noqa: BLE001
        steps.append({"step": "mcp", "ok": False, "detail": f"{type(e).__name__}: {e}"})
    finally:
        c.close()
    return steps


def hermes_smoke(root: Path):
    exe = shutil.which("hermes")
    if not exe:
        return [{"step": "hermes", "ok": None, "detail": "Hermes no instalado: prueba omitida (no-verificado)"}]
    try:
        r = subprocess.run([exe, "-z", "Lee AGENTS.md y responde solo con el valor de `id` en ads.yaml."], cwd=root,
                           capture_output=True, text=True, timeout=300)
        m = load_yaml_file(root / "ads.yaml")
        return [{"step": "hermes:one-shot", "ok": r.returncode == 0 and str(m.get("id")) in r.stdout, "detail": r.stdout.strip()[-200:]}]
    except Exception as e:  # noqa: BLE001
        return [{"step": "hermes:one-shot", "ok": False, "detail": str(e)}]


def cmd_conformance(ctx: Ctx, args) -> int:
    root = Path(args.path).resolve() if args.path else ctx.root
    mf = root / "ads.yaml"
    if not mf.exists():
        return emit(ctx, {"error": "sin ads.yaml"}, ["FALLA: no hay ads.yaml (Contrato ADS)"], ok=False)
    m = load_yaml_file(mf)
    steps = static_checks(root, m)
    cmd = args.server or ((m.get("endpoints") or {}).get("mcp") or {}).get("command")
    level = m.get("contract_level", "minimo")
    if cmd:
        steps += mcp_checks(root, m, cmd)
    elif level == "extendido":
        steps.append({"step": "mcp", "ok": False, "detail": "nivel extendido sin endpoints.mcp.command"})
    if args.hermes:
        steps += hermes_smoke(root)
    failed = [s for s in steps if s["ok"] is False]
    lines = [f"{'✔' if s['ok'] else ('–' if s['ok'] is None else '✖')} {s['step']}: {s['detail']}" for s in steps]
    lines.append(f"Conformidad agéntica ({m.get('id')}): {len(steps)} pasos · {len(failed)} fallan → {'OK' if not failed else 'FALLA'}")
    return emit(ctx, {"ads": m.get("id"), "steps": steps}, lines, ok=not failed)


def register(sub):
    p = sub.add_parser("agent-conformance", help="Prueba que un agente externo puede operar el ADS (MCP)")
    p.add_argument("path", nargs="?", help="raíz del ADS (por defecto, este repo)")
    p.add_argument("--server", help="comando del servidor MCP (por defecto, ads.yaml → endpoints.mcp.command)")
    p.add_argument("--hermes", action="store_true", help="además, prueba one-shot con Hermes si está instalado")
    p.set_defaults(func=cmd_conformance)
