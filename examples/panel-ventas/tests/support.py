"""Utilidades compartidas por los tests: base temporal sembrada y cliente HTTP con cookies."""
import http.client
import json
import re
import secrets
import sys
from contextlib import closing
from http.cookies import SimpleCookie
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
import db  # noqa: E402

DEMO_PW = "t-" + secrets.token_urlsafe(10)  # generada en cada corrida; nunca se guarda
FAST_ITER = 1000                             # iteraciones bajas solo en tests (producción: db.PBKDF2_ITER)


def fresh_db(directory, name="panel.db"):
    path = Path(directory) / name
    with closing(db.connect(path)) as conn:
        db.migrate(conn)
        db.seed(conn, password=DEMO_PW, iterations=FAST_ITER)
    return path


class Client:
    """Cliente HTTP mínimo que guarda cookies y no sigue redirecciones."""

    def __init__(self, port):
        self.port, self.cookies = port, {}

    def request(self, method, path, body=None, headers=None, form=None, json_body=None):
        h = dict(headers or {})
        if form is not None:
            body, h["Content-Type"] = urlencode(form), "application/x-www-form-urlencoded"
        if json_body is not None:
            h.setdefault("Content-Type", "application/json")
            body = json.dumps(json_body)
        if self.cookies:
            h["Cookie"] = "; ".join(f"{k}={v}" for k, v in self.cookies.items())
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        conn.request(method, path, body=body, headers=h)
        r = conn.getresponse()
        data = r.read()
        for raw in r.headers.get_all("Set-Cookie") or []:
            c = SimpleCookie(raw)
            for k, m in c.items():
                if m["max-age"] == "0":
                    self.cookies.pop(k, None)
                else:
                    self.cookies[k] = m.value
        conn.close()
        return r.status, r.headers, data

    def json(self, method, path, **kw):
        status, headers, data = self.request(method, path, **kw)
        return status, headers, (json.loads(data) if data else None)

    def login(self, username, password=None):
        _, _, page = self.request("GET", "/login")
        csrf = re.search(rb'name="csrf" value="([^"]+)"', page).group(1).decode()
        status, headers, _ = self.request("POST", "/login", form={"csrf": csrf, "username": username,
                                                                   "password": password or DEMO_PW})
        if status == 303:
            _, _, dash = self.request("GET", "/dashboard")
            self.csrf = re.search(rb'name="csrf-token" content="([^"]+)"', dash).group(1).decode()
        return status, headers
