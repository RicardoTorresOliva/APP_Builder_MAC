"""Capa de datos del panel de ventas: migraciones versionadas y reversibles, seeds y reglas de negocio.

Solo biblioteca estándar (sqlite3, hashlib, secrets). Toda consulta es parametrizada. La usan por igual
la web (server.py), la CLI (cli.py) y el servidor MCP (ops/mcp_server.py): una sola fuente de reglas.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import random
import re
import secrets
import sqlite3
import time
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "panel.db"
PBKDF2_ITER = 600_000          # PBKDF2-HMAC-SHA256 (recomendación OWASP vigente para este algoritmo)
SESSION_TTL = 8 * 3600
ROLES = ("admin", "vendedor")
MONEDA = os.environ.get("PANEL_VENTAS_MONEDA", "USD")
MAX_MONTO = 100_000_000        # centavos (1 000 000,00)
PROBLEM = "urn:panel-ventas:problem:"

# ------------------------------------------------------------------ migraciones (up/down)
MIGRATIONS = [
    (1, "esquema inicial", (
        """CREATE TABLE usuarios (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE CHECK (length(username) BETWEEN 3 AND 40),
             nombre TEXT NOT NULL CHECK (length(nombre) BETWEEN 1 AND 80),
             rol TEXT NOT NULL CHECK (rol IN ('admin', 'vendedor')),
             pw_hash TEXT NOT NULL, pw_salt TEXT NOT NULL, pw_iter INTEGER NOT NULL CHECK (pw_iter >= 1000),
             creado_en TEXT NOT NULL)""",
        """CREATE TABLE ventas (
             id INTEGER PRIMARY KEY,
             vendedor_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE RESTRICT,
             fecha TEXT NOT NULL CHECK (fecha GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'),
             cliente TEXT NOT NULL CHECK (length(cliente) BETWEEN 1 AND 120),
             producto TEXT NOT NULL CHECK (length(producto) BETWEEN 1 AND 80),
             monto_centavos INTEGER NOT NULL CHECK (monto_centavos > 0),
             idem_key TEXT UNIQUE,
             creado_en TEXT NOT NULL)""",
        """CREATE TABLE sesiones (
             token_hash TEXT PRIMARY KEY,
             usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
             csrf TEXT NOT NULL,
             expira_en INTEGER NOT NULL)""",
    ), ("DROP TABLE sesiones", "DROP TABLE ventas", "DROP TABLE usuarios")),
    (2, "indices y auditoria", (
        "CREATE INDEX ix_ventas_fecha ON ventas(fecha)",
        "CREATE INDEX ix_ventas_vendedor_fecha ON ventas(vendedor_id, fecha)",
        "CREATE INDEX ix_sesiones_expira ON sesiones(expira_en)",
        """CREATE TABLE auditoria (
             id INTEGER PRIMARY KEY, ts TEXT NOT NULL, actor TEXT NOT NULL,
             accion TEXT NOT NULL CHECK (accion IN ('crear', 'borrar')),
             entidad TEXT NOT NULL, entidad_id INTEGER, antes TEXT, despues TEXT)""",
    ), ("DROP TABLE auditoria", "DROP INDEX ix_sesiones_expira", "DROP INDEX ix_ventas_vendedor_fecha",
        "DROP INDEX ix_ventas_fecha")),
]
LATEST = MIGRATIONS[-1][0]


class DomainError(Exception):
    status, slug, title = 400, "solicitud", "Solicitud inválida"

    def __init__(self, detail="", errors=None):
        super().__init__(detail)
        self.detail, self.errors = detail, errors or []

    def problem(self):
        p = {"type": PROBLEM + self.slug, "title": self.title, "status": self.status, "detail": self.detail}
        if self.errors:
            p["errors"] = self.errors
        return p


class ValidationError(DomainError):
    status, slug, title = 422, "validacion", "Datos inválidos"


class Forbidden(DomainError):
    status, slug, title = 403, "prohibido", "Acción no permitida para tu rol"


class NotFound(DomainError):
    status, slug, title = 404, "no-encontrado", "Recurso no encontrado"


class NotInitialized(DomainError):
    status, slug, title = 503, "sin-inicializar", "Base de datos sin inicializar"


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def db_path():
    return Path(os.environ.get("PANEL_VENTAS_DB") or DEFAULT_DB)


def connect(path=None, readonly=False):
    """Conexión con claves foráneas activas. `readonly` abre en modo ro (mínimo privilegio para lecturas)."""
    p = Path(path) if path else db_path()
    if readonly:
        if not p.exists():
            raise NotInitialized(f"no existe {p.name}: ejecuta `python3 app/cli.py seed`")
        conn = sqlite3.connect(p.resolve().as_uri() + "?mode=ro", uri=True, timeout=5)
    else:
        p.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(p), timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def current_version(conn):
    try:
        return conn.execute("SELECT COALESCE(MAX(version), 0) FROM schema_migrations").fetchone()[0]
    except sqlite3.OperationalError:
        return 0


def migrate(conn, target=None, dry_run=False):
    """Lleva el esquema a `target` (por defecto, la última). Cada paso es una transacción atómica."""
    cur = current_version(conn)
    target = LATEST if target is None else int(target)
    if not 0 <= target <= LATEST:
        raise ValidationError(f"versión fuera de rango (0..{LATEST})")
    if target >= cur:
        steps = [("up", m) for m in MIGRATIONS if cur < m[0] <= target]
    else:
        steps = [("down", m) for m in reversed(MIGRATIONS) if target < m[0] <= cur]
    plan = [{"direccion": d, "version": m[0], "nombre": m[1]} for d, m in steps]
    if dry_run:
        return {"desde": cur, "hasta": target, "pasos": plan, "dry_run": True}
    conn.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY, "
                 "nombre TEXT NOT NULL, aplicada_en TEXT NOT NULL)")
    conn.commit()
    for direction, (ver, name, up, down) in steps:
        try:
            conn.execute("BEGIN")
            for stmt in (up if direction == "up" else down):
                conn.execute(stmt)
            if direction == "up":
                conn.execute("INSERT INTO schema_migrations (version, nombre, aplicada_en) VALUES (?, ?, ?)",
                             (ver, name, now_iso()))
            else:
                conn.execute("DELETE FROM schema_migrations WHERE version = ?", (ver,))
            conn.commit()
        except Exception:
            conn.rollback()
            raise
    return {"desde": cur, "hasta": target, "pasos": plan, "dry_run": False}


# ------------------------------------------------------------------ identidad
def hash_password(password, salt=None, iterations=PBKDF2_ITER):
    salt = salt or secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return dk.hex(), salt.hex(), iterations


def verify_password(password, pw_hash, pw_salt, pw_iter):
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(pw_salt), int(pw_iter))
    return hmac.compare_digest(dk.hex(), pw_hash)


def create_user(conn, username, nombre, rol, password, iterations=PBKDF2_ITER):
    if rol not in ROLES:
        raise ValidationError("rol inválido", [{"pointer": "#/rol", "detail": "admin o vendedor"}])
    h, s, it = hash_password(password, iterations=iterations)
    cur = conn.execute("INSERT INTO usuarios (username, nombre, rol, pw_hash, pw_salt, pw_iter, creado_en) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?)", (username, nombre, rol, h, s, it, now_iso()))
    conn.commit()
    return cur.lastrowid


def authenticate(conn, username, password):
    """Devuelve el usuario o None. Mismo costo si el usuario no existe (no revela cuáles existen)."""
    if not username or not password or len(password) > 1024:
        return None
    row = conn.execute("SELECT id, username, nombre, rol, pw_hash, pw_salt, pw_iter FROM usuarios "
                       "WHERE username = ?", (username,)).fetchone()
    if row is None:
        hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), b"\0" * 16, PBKDF2_ITER)
        return None
    if not verify_password(password, row["pw_hash"], row["pw_salt"], row["pw_iter"]):
        return None
    return {"id": row["id"], "username": row["username"], "nombre": row["nombre"], "rol": row["rol"]}


def _token_hash(token):
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_session(conn, user_id, ttl=SESSION_TTL):
    """Crea una sesión; en la base solo queda el hash del token. Devuelve (token, csrf)."""
    token, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
    now = int(time.time())
    conn.execute("DELETE FROM sesiones WHERE expira_en <= ?", (now,))
    conn.execute("INSERT INTO sesiones (token_hash, usuario_id, csrf, expira_en) VALUES (?, ?, ?, ?)",
                 (_token_hash(token), user_id, csrf, now + ttl))
    conn.commit()
    return token, csrf


def get_session(conn, token):
    if not token or len(token) > 200:
        return None
    row = conn.execute("SELECT u.id, u.username, u.nombre, u.rol, s.csrf FROM sesiones s "
                       "JOIN usuarios u ON u.id = s.usuario_id WHERE s.token_hash = ? AND s.expira_en > ?",
                       (_token_hash(token), int(time.time()))).fetchone()
    return dict(row) if row else None


def delete_session(conn, token):
    conn.execute("DELETE FROM sesiones WHERE token_hash = ?", (_token_hash(token or ""),))
    conn.commit()


# ------------------------------------------------------------------ ventas
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _parse_date(value, field):
    if not isinstance(value, str) or not DATE_RE.match(value):
        raise ValidationError("fecha inválida", [{"pointer": f"#/{field}", "detail": "usa el formato AAAA-MM-DD"}])
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValidationError("fecha inválida", [{"pointer": f"#/{field}", "detail": "la fecha no existe"}]) from None


def parse_monto(value):
    """Monto en unidades ('1234.50', '1234,50' o número) → centavos enteros. Nunca float para dinero."""
    d = None
    if isinstance(value, (int, float, str, Decimal)) and not isinstance(value, bool) and str(value).strip():
        try:
            d = Decimal(str(value).strip().replace(",", "."))
        except InvalidOperation:
            d = None
    if d is None or not d.is_finite() or d.as_tuple().exponent < -2:
        raise ValueError("usa un número con hasta 2 decimales")
    cents = int(d * 100)
    if not 0 < cents <= MAX_MONTO:
        raise ValueError("debe ser mayor que 0 y menor o igual a 1.000.000")
    return cents


def validate_filters(desde=None, hasta=None):
    d = _parse_date(desde, "desde") if desde else None
    h = _parse_date(hasta, "hasta") if hasta else None
    if d and h and d > h:
        raise ValidationError("rango inválido", [{"pointer": "#/desde", "detail": "desde debe ser anterior a hasta"}])
    return (d.isoformat() if d else None), (h.isoformat() if h else None)


def _resolve_vendedor(conn, data):
    ref = data.get("vendedor_id", data.get("vendedor"))
    if ref in (None, ""):
        return None
    if isinstance(ref, int) and not isinstance(ref, bool):
        row = conn.execute("SELECT id FROM usuarios WHERE id = ?", (ref,)).fetchone()
    else:
        row = conn.execute("SELECT id FROM usuarios WHERE username = ?", (str(ref),)).fetchone()
    if not row:
        raise ValidationError("vendedor inexistente", [{"pointer": "#/vendedor", "detail": "no existe"}])
    return row["id"]


def validate_venta(conn, data, today=None):
    if not isinstance(data, dict):
        raise ValidationError("el cuerpo debe ser un objeto JSON")
    errors, clean = [], {}
    try:
        f = _parse_date(data.get("fecha"), "fecha")
        if f > (today or date.today()) or f.year < 2000:
            errors.append({"pointer": "#/fecha", "detail": "no puede ser futura ni anterior a 2000"})
        clean["fecha"] = f.isoformat()
    except ValidationError as e:
        errors += e.errors
    for field, maxlen in (("cliente", 120), ("producto", 80)):
        v = data.get(field)
        v = v.strip() if isinstance(v, str) else ""
        if not 1 <= len(v) <= maxlen:
            errors.append({"pointer": f"#/{field}", "detail": f"obligatorio, hasta {maxlen} caracteres"})
        clean[field] = v
    try:
        clean["monto_centavos"] = parse_monto(data.get("monto"))
    except ValueError as e:
        errors.append({"pointer": "#/monto", "detail": str(e)})
    try:
        clean["vendedor_id"] = _resolve_vendedor(conn, data)
    except ValidationError as e:
        errors += e.errors
    if errors:
        raise ValidationError("revisa los campos marcados", errors)
    return clean


def _venta(conn, venta_id):
    row = conn.execute("SELECT v.id, v.fecha, v.cliente, v.producto, v.monto_centavos, v.vendedor_id, "
                       "u.nombre AS vendedor FROM ventas v JOIN usuarios u ON u.id = v.vendedor_id "
                       "WHERE v.id = ?", (venta_id,)).fetchone()
    return dict(row) if row else None


def _audit(conn, actor, accion, venta_id, antes, despues):
    conn.execute("INSERT INTO auditoria (ts, actor, accion, entidad, entidad_id, antes, despues) "
                 "VALUES (?, ?, ?, 'venta', ?, ?, ?)",
                 (now_iso(), actor["username"], accion, venta_id,
                  json.dumps(antes, ensure_ascii=False) if antes else None,
                  json.dumps(despues, ensure_ascii=False) if despues else None))


def create_venta(conn, actor, data, idem_key=None, dry_run=False):
    """Crea una venta. Vendedor: solo a su nombre. Idempotente por `idem_key`. Devuelve (venta, creada)."""
    clean = validate_venta(conn, data)
    if actor["rol"] != "admin":
        if clean["vendedor_id"] not in (None, actor["id"]):
            raise Forbidden("un vendedor solo registra ventas a su nombre")
        clean["vendedor_id"] = actor["id"]
    elif clean["vendedor_id"] is None:
        if actor.get("id") is None:
            raise ValidationError("falta el vendedor", [{"pointer": "#/vendedor", "detail": "obligatorio"}])
        clean["vendedor_id"] = actor["id"]
    key = f"{actor['username']}:{idem_key}" if idem_key else None
    if key:
        row = conn.execute("SELECT id FROM ventas WHERE idem_key = ?", (key,)).fetchone()
        if row:
            return _venta(conn, row["id"]), False
    if dry_run:
        return {"would_create": clean}, False
    cur = conn.execute("INSERT INTO ventas (vendedor_id, fecha, cliente, producto, monto_centavos, idem_key, creado_en) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?)", (clean["vendedor_id"], clean["fecha"], clean["cliente"],
                                                        clean["producto"], clean["monto_centavos"], key, now_iso()))
    _audit(conn, actor, "crear", cur.lastrowid, None, clean)
    conn.commit()
    return _venta(conn, cur.lastrowid), True


def delete_venta(conn, actor, venta_id, dry_run=False):
    """Borra una venta (solo admin). Queda auditada con su estado anterior."""
    if actor["rol"] != "admin":
        raise Forbidden("solo un admin puede borrar ventas")
    antes = _venta(conn, int(venta_id))
    if not antes:
        raise NotFound(f"no existe la venta {venta_id}")
    if dry_run:
        return {"would_delete": antes}
    conn.execute("DELETE FROM ventas WHERE id = ?", (antes["id"],))
    _audit(conn, actor, "borrar", antes["id"], antes, None)
    conn.commit()
    return {"deleted": antes}


def _scope(actor, desde, hasta, vendedor_id=None):
    where, params = [], []
    if actor["rol"] != "admin":
        where.append("v.vendedor_id = ?")
        params.append(actor["id"])
    elif vendedor_id:
        where.append("v.vendedor_id = ?")
        params.append(vendedor_id)
    if desde:
        where.append("v.fecha >= ?")
        params.append(desde)
    if hasta:
        where.append("v.fecha <= ?")
        params.append(hasta)
    return (" WHERE " + " AND ".join(where)) if where else "", params


def list_ventas(conn, actor, desde=None, hasta=None, vendedor_id=None, limit=50, offset=0):
    desde, hasta = validate_filters(desde, hasta)
    try:
        limit, offset = max(1, min(int(limit), 500)), max(0, int(offset))
        vendedor_id = int(vendedor_id) if vendedor_id not in (None, "") else None
    except (TypeError, ValueError):
        raise ValidationError("parámetros inválidos", [{"pointer": "#/limit", "detail": "limit, offset y vendedor_id son enteros"}]) from None
    where, params = _scope(actor, desde, hasta, vendedor_id)
    total = conn.execute(f"SELECT COUNT(*) FROM ventas v{where}", params).fetchone()[0]
    rows = conn.execute("SELECT v.id, v.fecha, v.cliente, v.producto, v.monto_centavos, v.vendedor_id, "
                        f"u.nombre AS vendedor FROM ventas v JOIN usuarios u ON u.id = v.vendedor_id{where} "
                        "ORDER BY v.fecha DESC, v.id DESC LIMIT ? OFFSET ?", params + [limit, offset]).fetchall()
    return {"items": [dict(r) for r in rows], "total": total, "limit": limit, "offset": offset}


def _months(first, last):
    y, m = int(first[:4]), int(first[5:7])
    out = []
    while (y, m) <= (int(last[:4]), int(last[5:7])):
        out.append(f"{y:04d}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def resumen(conn, actor, desde=None, hasta=None):
    """Totales, ticket promedio y series por mes (sin huecos) y por vendedor del rango."""
    desde, hasta = validate_filters(desde, hasta)
    where, params = _scope(actor, desde, hasta)
    tot = conn.execute(f"SELECT COUNT(*) AS n, COALESCE(SUM(monto_centavos), 0) AS total, MIN(fecha) AS f0, "
                       f"MAX(fecha) AS f1 FROM ventas v{where}", params).fetchone()
    by_month = {r["mes"]: r for r in conn.execute(
        f"SELECT substr(v.fecha, 1, 7) AS mes, SUM(v.monto_centavos) AS total, COUNT(*) AS n FROM ventas v{where} "
        "GROUP BY mes ORDER BY mes", params)}
    por_mes = []
    if tot["n"]:
        for mes in _months((desde or tot["f0"])[:7], (hasta or tot["f1"])[:7])[-36:]:
            r = by_month.get(mes)
            por_mes.append({"mes": mes, "total_centavos": r["total"] if r else 0, "n": r["n"] if r else 0})
    por_vendedor = [dict(r) for r in conn.execute(
        "SELECT u.id AS vendedor_id, u.nombre AS vendedor, SUM(v.monto_centavos) AS total_centavos, COUNT(*) AS n "
        f"FROM ventas v JOIN usuarios u ON u.id = v.vendedor_id{where} GROUP BY u.id ORDER BY total_centavos DESC",
        params)]
    return {"moneda": MONEDA, "rango": {"desde": desde, "hasta": hasta}, "n_ventas": tot["n"],
            "total_centavos": tot["total"], "ticket_promedio_centavos": tot["total"] // tot["n"] if tot["n"] else 0,
            "por_mes": por_mes, "por_vendedor": por_vendedor}


def status(conn):
    ver = current_version(conn)
    out = {"id": "panel-ventas", "schema_version": ver, "schema_latest": LATEST, "estado": "ok" if ver == LATEST else "migrar"}
    if ver >= 1:
        out["usuarios"] = conn.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0]
        out["ventas"] = conn.execute("SELECT COUNT(*) FROM ventas").fetchone()[0]
        out["ultima_venta"] = conn.execute("SELECT MAX(fecha) FROM ventas").fetchone()[0]
    return out


# ------------------------------------------------------------------ seeds (idempotentes)
USUARIOS_DEMO = [("ana", "Ana Rojas", "admin"), ("bruno", "Bruno Díaz", "vendedor"),
                 ("carla", "Carla Méndez", "vendedor"), ("diego", "Diego Paredes", "vendedor")]
CLIENTES = ["Ferretería El Roble", "Café Aroma", "Clínica Dental Sonrisa", "Librería Andina",
            "Taller Mecánico Ruta 5", "Panadería La Espiga", "Estudio Contable Vega", "Óptica Visión Clara",
            "Gimnasio Fuerza Total", "Hostal Los Aromos", "Farmacia San Martín", "Constructora Alto Valle"]
PRODUCTOS = [("Plan Básico (anual)", 49_000), ("Plan Pro (anual)", 129_000), ("Implementación", 45_000),
             ("Soporte premium", 8_900), ("Capacitación de equipo", 22_000)]


def seed(conn, password=None, iterations=PBKDF2_ITER, today=None, dry_run=False):
    """Crea usuarios demo y ~12 meses de ventas si faltan. Correrlo dos veces no duplica nada.

    Contraseña: argumento > PANEL_VENTAS_DEMO_PASSWORD > aleatoria por usuario (se devuelve una sola vez).
    """
    faltan = [u for u in USUARIOS_DEMO if not conn.execute(
        "SELECT 1 FROM usuarios WHERE username = ?", (u[0],)).fetchone()]
    n_ventas = conn.execute("SELECT COUNT(*) FROM ventas").fetchone()[0]
    if dry_run:
        return {"usuarios_a_crear": [u[0] for u in faltan], "ventas_a_crear": 0 if n_ventas else "~180", "dry_run": True}
    creds = []
    for username, nombre, rol in faltan:
        pw = password or os.environ.get("PANEL_VENTAS_DEMO_PASSWORD") or secrets.token_urlsafe(12)
        create_user(conn, username, nombre, rol, pw, iterations)
        creds.append({"username": username, "rol": rol, "password": pw})
    creadas = 0
    if not n_ventas:
        rng, today = random.Random(42), today or date.today()
        ids = {r["username"]: r["id"] for r in conn.execute("SELECT id, username FROM usuarios")}
        pesos = [("bruno", 0.40), ("carla", 0.35), ("diego", 0.25)]
        for back in range(364, -1, -1):
            dia = today - timedelta(days=back)
            if dia.weekday() >= 5 or rng.random() > 0.55 + 0.25 * (364 - back) / 364:
                continue
            vend = rng.choices([p[0] for p in pesos], [p[1] for p in pesos])[0]
            prod, precio = rng.choice(PRODUCTOS)
            monto = precio * rng.choice((1, 1, 1, 2, 3))
            conn.execute("INSERT INTO ventas (vendedor_id, fecha, cliente, producto, monto_centavos, creado_en) "
                         "VALUES (?, ?, ?, ?, ?, ?)", (ids[vend], dia.isoformat(), rng.choice(CLIENTES), prod,
                                                       monto, now_iso()))
            creadas += 1
        conn.commit()
    return {"usuarios_creados": creds, "ventas_creadas": creadas, "dry_run": False}
