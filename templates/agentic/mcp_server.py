#!/usr/bin/env python3
"""Plantilla de servidor MCP (stdio, JSON-RPC 2.0) para un ADS — solo biblioteca estándar.

Uso: `python3 ops/mcp_server.py`. Registra capacidades con @tool; declara cada una en ads.yaml.
- Protocolo base 2025-11-25 (acepta 2025-06-18/2025-03-26; tolera clientes sin estado 2026-07-28).
- Herramientas de escritura: dry_run=true por defecto. Destructivas: exigen confirm=true y figurar en
  ads.yaml → security.hitl_actions.
- Cada llamada queda en el log de auditoría; el recurso <id>://tokens/summary resume el ledger.
- La salida de una herramienta es un dato, nunca una instrucción.
Si el ADS usa otro lenguaje, implementa el mismo contrato con el SDK MCP oficial de ese lenguaje.
"""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADS_ID = "<id>"
AUDIT = ROOT / "ops/audit/agent-actions.jsonl"
LEDGER = ROOT / "ops/tokens/ledger.jsonl"
PROTOCOL, SUPPORTED = "2025-11-25", ("2025-11-25", "2025-06-18", "2025-03-26")
TOOLS = {}


def tool(name, description, properties=None, required=None, mode="read"):
    """mode: read | write | destructive (igual que ads.yaml → capabilities[].mode)."""
    def deco(fn):
        props = dict(properties or {})
        if mode != "read":
            props["dry_run"] = {"type": "boolean", "default": True}
        if mode == "destructive":
            props["confirm"] = {"type": "boolean", "default": False, "description": "confirmación humana explícita"}
        TOOLS[name] = {"fn": fn, "mode": mode, "spec": {
            "name": name, "description": description,
            "inputSchema": {"type": "object", "properties": props, "required": required or [], "additionalProperties": False},
            "annotations": {"readOnlyHint": mode == "read", "destructiveHint": mode == "destructive",
                            "idempotentHint": mode == "read", "openWorldHint": False}}}
        return fn
    return deco


# ------------------------------------------------------------------ capacidades del ADS
@tool("status", "Estado del ADS: versión y salud.")
def status(args):
    return {"id": ADS_ID, "status": "ok", "ts": datetime.now(timezone.utc).isoformat()}


# @tool("create_item", "Crea un registro.", {"name": {"type": "string"}}, ["name"], mode="write")
# def create_item(args):
#     if args.get("dry_run", True):
#         return {"would_create": args["name"]}
#     ...  # lógica real, idempotente


# ------------------------------------------------------------------ infraestructura
def tokens_summary():
    agg = defaultdict(int)
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if line.strip():
                e = json.loads(line)
                agg[e.get("phase", "run")] += int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0))
    return {"total_tokens": sum(agg.values()), "by_phase": dict(agg)}


def audit(name, args, ok):
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": datetime.now(timezone.utc).isoformat(), "tool": name, "arguments": args, "ok": ok}, ensure_ascii=False) + "\n")


def hitl_actions():
    """Capacidades destructivas autorizadas en ads.yaml → security.hitl_actions (lectura mínima, sin dependencias)."""
    f = ROOT / "ads.yaml"
    if not f.exists():
        return set()
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("hitl_actions:"):
            return {x.strip().strip("'\"") for x in line.split("[", 1)[-1].rstrip("]").split(",") if x.strip()}
    return set()


def call(params):
    name, args = params.get("name"), params.get("arguments") or {}
    t = TOOLS.get(name)
    if not t:
        raise KeyError(f"herramienta desconocida: {name}")
    if not isinstance(args, dict):
        return {"content": [{"type": "text", "text": "arguments debe ser un objeto"}], "isError": True}
    if t["mode"] == "destructive" and not args.get("dry_run", True):
        # confirm=true lo fija el cliente tras pedir aprobación humana (destructiveHint); además la
        # capacidad debe estar declarada en hitl_actions. Sin ambas, no se ejecuta.
        if not args.get("confirm") or name not in hitl_actions():
            return {"content": [{"type": "text", "text": "Requiere confirmación humana (confirm=true) y figurar en ads.yaml → security.hitl_actions."}], "isError": True}
    try:
        data, ok = t["fn"](args), True
    except Exception as e:  # noqa: BLE001 — error estructurado estilo problem+json
        data, ok = {"type": "about:blank", "title": type(e).__name__, "detail": str(e)}, False
    if isinstance(data, dict) and t["mode"] != "read":
        data.setdefault("dry_run", bool(args.get("dry_run", True)))
    audit(name, args, ok)
    return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}], "structuredContent": data, "isError": not ok}


def handle(msg):
    if not isinstance(msg, dict):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "solicitud inválida"}}
    method, mid, p = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if not isinstance(p, dict):
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "params debe ser un objeto"}}
    if mid is None:
        return None
    try:
        if method in ("initialize", "server/discover"):
            v = p.get("protocolVersion")
            res = {"protocolVersion": v if v in SUPPORTED else PROTOCOL,
                   "capabilities": {"tools": {"listChanged": False}, "resources": {"listChanged": False}},
                   "serverInfo": {"name": ADS_ID, "version": "0.1.0"}}
        elif method == "ping":
            res = {}
        elif method == "tools/list":
            res = {"tools": [t["spec"] for t in TOOLS.values()]}
        elif method == "tools/call":
            res = call(p)
        elif method == "resources/list":
            res = {"resources": [{"uri": f"{ADS_ID}://tokens/summary", "name": "tokens-summary", "mimeType": "application/json"}]}
        elif method == "resources/read" and p.get("uri") == f"{ADS_ID}://tokens/summary":
            res = {"contents": [{"uri": p["uri"], "mimeType": "application/json", "text": json.dumps(tokens_summary())}]}
        else:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"no soportado: {method}"}}
        return {"jsonrpc": "2.0", "id": mid, "result": res}
    except KeyError as e:
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": str(e)}}


def cli(argv):
    """Modo CLI con salida JSON (Contrato ADS): python3 ops/mcp_server.py --cli <tool> [--arg k=v] [--dry-run|--apply]."""
    name, args = argv[0], {}
    it = iter(argv[1:])
    for a in it:
        if a == "--arg":
            k, _, v = next(it).partition("=")
            args[k] = v
        elif a in ("--dry-run", "--apply"):
            args["dry_run"] = a == "--dry-run"
    res = call({"name": name, "arguments": args})
    print(json.dumps(res["structuredContent"], ensure_ascii=False, indent=2))
    return 1 if res.get("isError") else 0


if __name__ == "__main__":
    for _s in (sys.stdin, sys.stdout, sys.stderr):  # UTF-8 en cualquier SO (Windows usa cp1252 por defecto)
        try:
            _s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    if len(sys.argv) > 2 and sys.argv[1] == "--cli":
        sys.exit(cli(sys.argv[2:]))
    for line in sys.stdin:
        if line.strip():
            try:
                out = handle(json.loads(line))
            except json.JSONDecodeError:
                out = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "JSON inválido"}}
            except Exception as e:  # noqa: BLE001
                out = {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": f"error interno: {e}"}}
            if out:
                sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
                sys.stdout.flush()
