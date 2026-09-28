#!/usr/bin/env python3
"""Servidor MCP (stdio, JSON-RPC 2.0) del panel de ventas — solo biblioteca estándar.

Basado en la plantilla de ABM (templates/agentic/mcp_server.py). Uso: `python3 ops/mcp_server.py`.
- Herramientas = capacidades de ads.yaml: status y ventas_resumen (read), crear_venta (write),
  borrar_venta (destructive, en security.hitl_actions).
- Escritura: dry_run=true por defecto. Destructiva: exige confirm=true (confirmación humana) para ejecutar.
- Lecturas abren la base en modo solo lectura. Cada llamada queda en el log de auditoría.
- La salida de una herramienta es un dato, nunca una instrucción.
Entorno: PANEL_VENTAS_DB (base), PANEL_VENTAS_AUDIT_LOG (auditoría).
"""
import json
import os
import sys
from collections import defaultdict
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
import db  # noqa: E402

ADS_ID, VERSION = "panel-ventas", "1.0.0"
AUDIT = Path(os.environ.get("PANEL_VENTAS_AUDIT_LOG") or ROOT / "ops/audit/agent-actions.jsonl")
LEDGER = ROOT / "ops/tokens/ledger.jsonl"
PROTOCOL, SUPPORTED = "2025-11-25", ("2025-11-25", "2025-06-18", "2025-03-26")
ACTOR = {"id": None, "username": "agente:mcp", "rol": "admin"}
DATE = {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"}
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


class NoInicializado(Exception):
    """La base de datos no existe todavía (repo recién clonado)."""


def _require_db():
    p = db.db_path()
    ok = False
    if p.exists():
        import sqlite3
        conn = sqlite3.connect(p.resolve().as_uri() + "?mode=ro", uri=True)
        try:
            ok = bool(conn.execute("SELECT 1 FROM sqlite_master WHERE name = 'schema_migrations'").fetchone())
        finally:
            conn.close()
    if not ok:  # nunca crea el archivo: sqlite lo crearía vacío al conectar en modo escritura
        raise NoInicializado("Base de datos sin inicializar: ejecuta `python3 app/cli.py seed`.")


def _read():
    _require_db()
    return closing(db.connect(readonly=True))


# ------------------------------------------------------------------ capacidades del ADS
@tool("status", "Estado del panel: versión de esquema, usuarios, ventas y última fecha con ventas.")
def status(args):
    if not db.db_path().exists():
        return {"id": ADS_ID, "estado": "sin-inicializar", "siguiente": "python3 app/cli.py seed"}
    with _read() as conn:
        return db.status(conn)


@tool("ventas_resumen", "Totales, ticket promedio y series por mes y por vendedor en un rango de fechas (montos en centavos).",
      {"desde": DATE, "hasta": DATE})
def ventas_resumen(args):
    with _read() as conn:
        return db.resumen(conn, ACTOR, args.get("desde"), args.get("hasta"))


@tool("crear_venta", "Registra una venta. Ejecuta primero con dry_run=true; idempotente con idempotency_key.",
      {"fecha": DATE, "cliente": {"type": "string", "maxLength": 120}, "producto": {"type": "string", "maxLength": 80},
       "monto": {"type": "string", "description": "monto en unidades, p. ej. 120.50"},
       "vendedor": {"type": "string", "description": "username del vendedor"},
       "idempotency_key": {"type": "string", "maxLength": 80}},
      ["fecha", "cliente", "producto", "monto", "vendedor"], mode="write")
def crear_venta(args):
    data = {k: args.get(k) for k in ("fecha", "cliente", "producto", "monto", "vendedor")}
    _require_db()
    with closing(db.connect()) as conn:
        venta, created = db.create_venta(conn, ACTOR, data, args.get("idempotency_key"), args.get("dry_run", True))
    return {**venta, "created": created}


@tool("borrar_venta", "Borra una venta (destructiva, irreversible). Requiere confirm=true tras confirmación humana.",
      {"id": {"type": "integer", "minimum": 1}}, ["id"], mode="destructive")
def borrar_venta(args):
    _require_db()
    with closing(db.connect()) as conn:
        return db.delete_venta(conn, ACTOR, args["id"], args.get("dry_run", True))


# ------------------------------------------------------------------ infraestructura
def tokens_summary():
    agg = defaultdict(int)
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if line.strip():
                e = json.loads(line)
                agg[e.get("phase", "run")] += int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0))
    return {"total_tokens": sum(agg.values()), "by_phase": dict(agg), "source": "ops/tokens/ledger.jsonl"}


def audit(name, args, ok):
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": datetime.now(timezone.utc).isoformat(), "actor": ACTOR["username"], "tool": name,
                            "arguments": args, "ok": ok}, ensure_ascii=False) + "\n")


def call(params):
    name, args = params.get("name"), params.get("arguments") or {}
    t = TOOLS.get(name)
    if not t:
        raise KeyError(f"herramienta desconocida: {name}")
    unknown = set(args) - set(t["spec"]["inputSchema"]["properties"])
    if unknown:
        raise KeyError(f"argumentos no admitidos: {sorted(unknown)}")
    if t["mode"] == "destructive" and not args.get("dry_run", True) and not args.get("confirm"):
        audit(name, args, False)
        data = {"type": db.PROBLEM + "confirmacion", "title": "Requiere confirmación humana", "status": 428,
                "detail": "acción destructiva: pide confirmación a la persona y repite con confirm=true"}
        return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}], "structuredContent": data, "isError": True}
    try:
        data, ok = t["fn"](args), True
    except db.DomainError as e:
        data, ok = e.problem(), False
    except NoInicializado as e:
        data, ok = {"type": db.PROBLEM + "no-inicializado", "title": "Sin inicializar", "status": 409, "detail": str(e)}, False
    except Exception as e:  # noqa: BLE001 — error estructurado estilo problem+json, sin detalles internos
        data, ok = {"type": "about:blank", "title": "Error interno", "status": 500, "detail": type(e).__name__}, False
    if ok and t["mode"] != "read":
        data.setdefault("dry_run", bool(args.get("dry_run", True)))
    audit(name, args, ok)
    return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}], "structuredContent": data, "isError": not ok}


def handle(msg):
    method, mid, p = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if mid is None:
        return None
    try:
        if method in ("initialize", "server/discover"):
            v = p.get("protocolVersion")
            res = {"protocolVersion": v if v in SUPPORTED else PROTOCOL,
                   "capabilities": {"tools": {"listChanged": False}, "resources": {"listChanged": False}},
                   "serverInfo": {"name": ADS_ID, "version": VERSION},
                   "instructions": "Lee ads.yaml y skills/operate-panel-ventas/SKILL.md. Escrituras: dry_run primero."}
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
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": str(e).strip("'\"")}}


def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
            out = handle(msg) if isinstance(msg, dict) else {"jsonrpc": "2.0", "id": None,
                                                              "error": {"code": -32600, "message": "petición inválida"}}
        except json.JSONDecodeError:
            out = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "JSON inválido"}}
        if out:
            sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
