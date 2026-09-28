#!/usr/bin/env python3
"""Servidor web del panel de ventas (http.server + sqlite3, solo biblioteca estándar).

Uso: python3 app/server.py [--host 127.0.0.1] [--port 8765] [--db data/panel.db] [--secure-cookies]
Si la base está vacía, migra y siembra datos demo; las contraseñas generadas se muestran solo en consola.
Seguridad: PBKDF2 con sal por usuario, sesión en cookie HttpOnly + SameSite=Strict, CSRF por sesión,
roles admin/vendedor, consultas parametrizadas, CSP estricta y errores application/problem+json.
"""
from __future__ import annotations

import argparse
import hmac
import html
import json
import secrets
import sys
import threading
import time
import traceback
from contextlib import closing, contextmanager
from http.cookies import CookieError, SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

STATIC = Path(__file__).resolve().parent / "static"
STATIC_FILES = {"/static/app.js": "text/javascript; charset=utf-8", "/static/app.css": "text/css; charset=utf-8"}
MAX_BODY = 16 * 1024
SESSION_COOKIE, LOGIN_COOKIE = "pv_session", "pv_login"
CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; "
       "form-action 'self'; frame-ancestors 'none'; base-uri 'none'")
SEC_HEADERS = {"Content-Security-Policy": CSP, "X-Content-Type-Options": "nosniff", "Referrer-Policy": "same-origin",
               "X-Frame-Options": "DENY", "Cross-Origin-Opener-Policy": "same-origin"}


class HttpProblem(Exception):
    def __init__(self, status, title, detail="", slug=None, headers=None):
        super().__init__(detail)
        self.status, self.title, self.detail, self.headers = status, title, detail, headers or {}
        self.type = db.PROBLEM + slug if slug else "about:blank"


class LoginLimiter:
    """Máximo `max_fails` intentos fallidos por (IP, usuario) en `window` segundos."""

    def __init__(self, max_fails=5, window=900):
        self.max_fails, self.window, self.fails, self.lock = max_fails, window, {}, threading.Lock()

    def _recent(self, key, now):
        return [t for t in self.fails.get(key, []) if now - t < self.window]

    def blocked(self, key):
        with self.lock:
            return len(self._recent(key, time.time())) >= self.max_fails

    def fail(self, key):
        with self.lock:
            now = time.time()
            self.fails[key] = self._recent(key, now) + [now]

    def reset(self, key):
        with self.lock:
            self.fails.pop(key, None)


def page(title, body, extra_head=""):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title>'
            f'<meta name="description" content="Panel de ventas del equipo: registro y gráficos por mes y vendedor.">'
            f'<link rel="stylesheet" href="/static/app.css">{extra_head}</head><body>{body}</body></html>')


def login_page(csrf, username="", error=""):
    err = f'<p class="alert" role="alert">{html.escape(error)}</p>' if error else ""
    return page("Ingresar · Panel de ventas", f"""
<main class="login"><h1>Panel de ventas</h1>{err}
<form method="post" action="/login" class="card stack">
  <input type="hidden" name="csrf" value="{html.escape(csrf)}">
  <label for="username">Usuario</label>
  <input id="username" name="username" autocomplete="username" required maxlength="40" value="{html.escape(username)}">
  <label for="password">Contraseña</label>
  <input id="password" name="password" type="password" autocomplete="current-password" required maxlength="1024">
  <button type="submit" class="primary">Ingresar</button>
</form></main>""")


def dashboard_page(user, vendedores):
    e = html.escape
    opts = "".join(f'<option value="{v["id"]}">{e(v["nombre"])}</option>' for v in vendedores)
    vend_field = (f'<div class="field"><label for="f-vendedor">Vendedor</label><select id="f-vendedor" name="vendedor_id" '
                  f'aria-describedby="err-vendedor">{opts}</select><p class="field-error" id="err-vendedor"></p></div>'
                  if user["rol"] == "admin" else "")
    head = (f'<meta name="csrf-token" content="{e(user["csrf"])}"><meta name="rol" content="{e(user["rol"])}">'
            f'<meta name="moneda" content="{e(db.MONEDA)}"><script src="/static/app.js" defer></script>')
    field = ('<div class="field"><label for="f-{n}">{l}</label><input id="f-{n}" name="{n}" {a} '
             'aria-describedby="err-{n}"><p class="field-error" id="err-{n}"></p></div>')
    return page("Panel de ventas", f"""
<header class="topbar"><h1>Panel de ventas</h1>
  <div class="who"><span>{e(user["nombre"])} · {e(user["rol"])}</span>
    <button type="button" id="theme-toggle" class="ghost" aria-pressed="false">Modo oscuro</button>
    <form method="post" action="/logout"><input type="hidden" name="csrf" value="{e(user["csrf"])}">
    <button type="submit" class="ghost">Salir</button></form></div></header>
<main class="wrap">
  <section class="filters" aria-label="Rango de fechas">
    <div class="presets" role="group" aria-label="Rangos rápidos">
      <button type="button" data-preset="12m" aria-pressed="true">Últimos 12 meses</button>
      <button type="button" data-preset="ytd" aria-pressed="false">Este año</button>
      <button type="button" data-preset="90d" aria-pressed="false">Últimos 90 días</button>
      <button type="button" data-preset="all" aria-pressed="false">Todo</button></div>
    <form id="form-rango" class="range"><label for="desde">Desde</label><input type="date" id="desde" name="desde">
      <label for="hasta">Hasta</label><input type="date" id="hasta" name="hasta">
      <button type="submit">Aplicar</button></form>
  </section>
  <div id="status" class="status" role="status" aria-live="polite"></div>
  <div id="content">
  <section class="kpis" aria-label="Indicadores">
    <div class="kpi hero"><p class="kpi-label">Total vendido</p><p class="kpi-value" id="kpi-total">—</p></div>
    <div class="kpi"><p class="kpi-label">Ventas</p><p class="kpi-value" id="kpi-n">—</p></div>
    <div class="kpi"><p class="kpi-label">Ticket promedio</p><p class="kpi-value" id="kpi-ticket">—</p></div>
    <div class="kpi"><p class="kpi-label">Mejor mes</p><p class="kpi-value" id="kpi-mejor">—</p></div>
  </section>
  <section class="charts">
    <figure class="card"><figcaption><h2>Ventas por mes</h2><p class="sub">Monto total vendido cada mes</p></figcaption>
      <div class="chart" id="chart-mes"></div></figure>
    <figure class="card"><figcaption><h2>Ventas por vendedor</h2><p class="sub">Monto total del rango</p></figcaption>
      <div class="chart" id="chart-vendedor"></div></figure>
  </section>
  <section class="card"><h2>Registrar venta</h2>
    <form id="form-venta" class="grid-form" novalidate>
      {field.format(n="fecha", l="Fecha", a='type="date" required')}
      {field.format(n="cliente", l="Cliente", a='required maxlength="120" autocomplete="off"')}
      {field.format(n="producto", l="Producto", a='required maxlength="80" autocomplete="off"')}
      {field.format(n="monto", l=f"Monto ({e(db.MONEDA)})", a='inputmode="decimal" required placeholder="0.00"')}
      {vend_field}
      <div class="field actions"><button type="submit" class="primary">Guardar venta</button></div>
    </form></section>
  <section class="card"><h2>Detalle de ventas</h2><p class="sub" id="tabla-info"></p>
    <div class="table-wrap"><table id="tabla"><thead><tr><th scope="col">Fecha</th><th scope="col">Vendedor</th>
      <th scope="col">Cliente</th><th scope="col">Producto</th><th scope="col" class="num">Monto</th>
      <th scope="col"><span class="sr-only">Acciones</span></th></tr></thead><tbody></tbody></table></div></section>
  </div>
</main><div id="tooltip" class="tooltip" role="tooltip" hidden></div>""", head)


class App:
    def __init__(self, db_path, secure_cookies=False, quiet=False):
        self.db_path, self.secure, self.quiet, self.limiter = db_path, secure_cookies, quiet, LoginLimiter()

    @contextmanager
    def conn(self):
        c = db.connect(self.db_path)
        try:
            yield c
        finally:
            c.close()


class Handler(BaseHTTPRequestHandler):
    server_version, sys_version = "panel-ventas", ""
    timeout = 15  # segundos por conexión (evita conexiones colgadas)
    app: App = None

    # ---------------------------------------------------------------- infraestructura
    def log_message(self, fmt, *args):
        if not self.app.quiet:
            sys.stderr.write(json.dumps({"ts": db.now_iso(), "rid": getattr(self, "rid", "-"),
                                         "msg": fmt % args}, ensure_ascii=False) + "\n")

    def send(self, status, body=b"", ctype="application/json", headers=None, cookies=()):
        self.send_response(status)
        for k, v in {**SEC_HEADERS, "Cache-Control": "no-store", "X-Request-Id": self.rid, **(headers or {})}.items():
            self.send_header(k, v)
        for c in cookies:
            self.send_header("Set-Cookie", c)
        if status != 204:
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body and self.command != "HEAD":
            self.wfile.write(body)

    def json(self, status, data, headers=None):
        self.send(status, json.dumps(data, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8", headers)

    def problem(self, status, title, detail="", ptype="about:blank", errors=None, headers=None):
        p = {"type": ptype, "title": title, "status": status, "detail": detail, "instance": f"urn:request:{self.rid}"}
        if errors:
            p["errors"] = errors
        self.send(status, json.dumps(p, ensure_ascii=False).encode("utf-8"), "application/problem+json; charset=utf-8", headers)

    def html(self, status, text, cookies=()):
        self.send(status, text.encode("utf-8"), "text/html; charset=utf-8", cookies=cookies)

    def redirect(self, location, cookies=()):
        self.send(303, headers={"Location": location}, cookies=cookies)

    def cookie(self, name):
        try:
            c = SimpleCookie(self.headers.get("Cookie", ""))
        except CookieError:
            return None
        return c[name].value if name in c else None

    def set_cookie(self, name, value, max_age):
        return (f"{name}={value}; Path=/; HttpOnly; SameSite=Strict; Max-Age={max_age}"
                + ("; Secure" if self.app.secure else ""))

    def body(self, kind):
        ctype = self.headers.get("Content-Type", "").split(";")[0].strip().lower()
        if ctype != kind:
            raise HttpProblem(415, "Tipo de contenido no soportado", f"usa {kind}", "tipo-contenido")
        try:
            n = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            raise HttpProblem(400, "Content-Length inválido") from None
        if n < 0:
            raise HttpProblem(400, "Content-Length inválido")
        if n > MAX_BODY:
            raise HttpProblem(413, "Cuerpo demasiado grande", f"máximo {MAX_BODY // 1024} KiB", "demasiado-grande")
        raw = self.rfile.read(n).decode("utf-8", errors="replace")
        if kind == "application/json":
            try:
                return json.loads(raw or "null")
            except json.JSONDecodeError:
                raise HttpProblem(400, "JSON mal formado", "el cuerpo no es JSON válido", "json") from None
        return {k: v[0] for k, v in parse_qs(raw, max_num_fields=20).items()}

    def check_origin(self):
        origin = self.headers.get("Origin")
        if origin and urlsplit(origin).netloc != self.headers.get("Host"):
            raise HttpProblem(403, "Origen no permitido", "petición de otro origen", "origen")

    def user(self, conn, api=True):
        u = db.get_session(conn, self.cookie(SESSION_COOKIE))
        if not u and api:
            raise HttpProblem(401, "No autenticado", "inicia sesión en /login", "no-autenticado")
        return u

    def require_csrf(self, user, token):
        if not token or not hmac.compare_digest(str(token), user["csrf"]):
            raise HttpProblem(403, "Token CSRF inválido o ausente", "recarga la página", "csrf")

    # ---------------------------------------------------------------- despacho
    def do_GET(self):
        self.dispatch("GET")

    def do_HEAD(self):
        self.dispatch("GET")

    def do_POST(self):
        self.dispatch("POST")

    def do_DELETE(self):
        self.dispatch("DELETE")

    def dispatch(self, method):
        self.rid = secrets.token_hex(8)
        url = urlsplit(self.path)
        self.query = {k: v[0] for k, v in parse_qs(url.query, max_num_fields=20).items()}
        path = url.path
        try:
            if method != "GET":
                self.check_origin()
            if path in STATIC_FILES and method == "GET":
                return self.send(200, (STATIC / Path(path).name).read_bytes(), STATIC_FILES[path],
                                 {"Cache-Control": "no-cache"})
            if path.startswith("/api/ventas/") and method == "DELETE":
                return self.api_delete(path.rsplit("/", 1)[1])
            route = ROUTES.get((method, path))
            if not route:
                if any(p == path for _, p in ROUTES):
                    raise HttpProblem(405, "Método no permitido")
                raise HttpProblem(404, "No encontrado", f"no existe {path}")
            return route(self)
        except HttpProblem as p:
            self.problem(p.status, p.title, p.detail, p.type, headers=p.headers)
        except db.DomainError as e:
            pr = e.problem()
            self.problem(pr["status"], pr["title"], pr["detail"], pr["type"], pr.get("errors"))
        except Exception:  # noqa: BLE001 — nunca se filtran detalles internos al cliente
            sys.stderr.write(json.dumps({"ts": db.now_iso(), "rid": self.rid, "error": traceback.format_exc()}) + "\n")
            self.problem(500, "Error interno", "reintenta; si persiste, reporta el id de la petición")

    # ---------------------------------------------------------------- páginas
    def index(self):
        with self.app.conn() as conn:
            self.redirect("/dashboard" if self.user(conn, api=False) else "/login")

    def healthz(self):
        self.json(200, {"status": "ok"})

    def login_form(self, username="", error="", status=200):
        token = secrets.token_urlsafe(24)
        self.html(status, login_page(token, username, error), [self.set_cookie(LOGIN_COOKIE, token, 600)])

    def login(self):
        form = self.body("application/x-www-form-urlencoded")
        expected = self.cookie(LOGIN_COOKIE)
        if not expected or not hmac.compare_digest(form.get("csrf", ""), expected):
            raise HttpProblem(403, "Token CSRF inválido o ausente", "recarga el formulario de ingreso", "csrf")
        username = form.get("username", "").strip()[:40]
        key = (self.client_address[0], username.lower())
        if self.app.limiter.blocked(key):
            raise HttpProblem(429, "Demasiados intentos", "espera 15 minutos", "limite", {"Retry-After": "900"})
        with self.app.conn() as conn:
            u = db.authenticate(conn, username, form.get("password", ""))
            if not u:
                self.app.limiter.fail(key)
                return self.login_form(username, "Usuario o contraseña incorrectos.", 401)
            self.app.limiter.reset(key)
            token, _ = db.create_session(conn, u["id"])
        self.redirect("/dashboard", [self.set_cookie(SESSION_COOKIE, token, db.SESSION_TTL),
                                     self.set_cookie(LOGIN_COOKIE, "", 0)])

    def logout(self):
        form = self.body("application/x-www-form-urlencoded")
        with self.app.conn() as conn:
            u = self.user(conn)
            self.require_csrf(u, form.get("csrf"))
            db.delete_session(conn, self.cookie(SESSION_COOKIE))
        self.redirect("/login", [self.set_cookie(SESSION_COOKIE, "", 0)])

    def dashboard(self):
        with self.app.conn() as conn:
            u = self.user(conn, api=False)
            if not u:
                return self.redirect("/login")
            vend = [dict(r) for r in conn.execute("SELECT id, nombre FROM usuarios WHERE rol = 'vendedor' ORDER BY nombre")]
        self.html(200, dashboard_page(u, vend))

    # ---------------------------------------------------------------- API JSON
    def api_ventas(self):
        q = self.query
        with self.app.conn() as conn:
            u = self.user(conn)
            self.json(200, db.list_ventas(conn, u, q.get("desde"), q.get("hasta"), q.get("vendedor_id"),
                                          q.get("limit", 50), q.get("offset", 0)))

    def api_crear(self):
        with self.app.conn() as conn:
            u = self.user(conn)
            self.require_csrf(u, self.headers.get("X-CSRF-Token"))
            data = self.body("application/json")
            venta, created = db.create_venta(conn, u, data, self.headers.get("Idempotency-Key"))
        self.json(201 if created else 200, venta, {"Location": f"/api/ventas/{venta['id']}"})

    def api_delete(self, raw_id):
        if not raw_id.isdigit():
            raise HttpProblem(404, "No encontrado")
        with self.app.conn() as conn:
            u = self.user(conn)
            self.require_csrf(u, self.headers.get("X-CSRF-Token"))
            db.delete_venta(conn, u, int(raw_id))
        self.send(204)

    def api_resumen(self):
        with self.app.conn() as conn:
            u = self.user(conn)
            self.json(200, db.resumen(conn, u, self.query.get("desde"), self.query.get("hasta")))


ROUTES = {("GET", "/"): Handler.index, ("GET", "/healthz"): Handler.healthz, ("GET", "/login"): Handler.login_form,
          ("POST", "/login"): Handler.login, ("POST", "/logout"): Handler.logout,
          ("GET", "/dashboard"): Handler.dashboard, ("GET", "/api/ventas"): Handler.api_ventas,
          ("POST", "/api/ventas"): Handler.api_crear, ("GET", "/api/resumen"): Handler.api_resumen}


def prepare(db_path, quiet=False):
    """Migra y, si no hay usuarios, siembra datos demo. Devuelve las credenciales creadas (solo consola)."""
    with closing(db.connect(db_path)) as conn:
        db.migrate(conn)
        return db.seed(conn)["usuarios_creados"]


def make_server(host, port, db_path, secure_cookies=False, quiet=False):
    handler = type("BoundHandler", (Handler,), {"app": App(db_path, secure_cookies, quiet)})
    return ThreadingHTTPServer((host, port), handler)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Servidor del panel de ventas")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--db", default=str(db.db_path()))
    ap.add_argument("--secure-cookies", action="store_true", help="marca las cookies Secure (detrás de TLS)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    for c in prepare(a.db):
        print(f"Usuario demo creado: {c['username']} ({c['rol']}) · contraseña: {c['password']}  [solo se muestra ahora]")
    httpd = make_server(a.host, a.port, a.db, a.secure_cookies, a.quiet)
    print(f"Panel de ventas en http://{a.host}:{httpd.server_address[1]}  (Ctrl+C para detener)", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
