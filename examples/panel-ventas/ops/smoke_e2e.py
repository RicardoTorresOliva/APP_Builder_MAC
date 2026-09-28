#!/usr/bin/env python3
"""Prueba de humo de punta a punta: arranca el servidor real, inicia sesión como admin y consulta /api/resumen.

Usa una base temporal y una contraseña demo aleatoria (no queda en ningún archivo). Uso: python3 ops/smoke_e2e.py [--port N]
"""
import argparse
import http.cookiejar
import json
import os
import re
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=0)
    port = ap.parse_args().port or free_port()
    pw = secrets.token_urlsafe(12)
    with tempfile.TemporaryDirectory() as tmp:
        env = {**os.environ, "PANEL_VENTAS_DEMO_PASSWORD": pw}
        srv = subprocess.Popen([sys.executable, str(ROOT / "app/server.py"), "--port", str(port), "--quiet",
                                "--db", os.path.join(tmp, "smoke.db")], env=env, stdout=subprocess.DEVNULL)
        base = f"http://127.0.0.1:{port}"
        try:
            for _ in range(100):
                try:
                    urllib.request.urlopen(base + "/healthz", timeout=1)
                    break
                except OSError:
                    time.sleep(0.1)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
            form = opener.open(base + "/login").read().decode()
            csrf = re.search(r'name="csrf" value="([^"]+)"', form).group(1)
            data = urllib.parse.urlencode({"csrf": csrf, "username": "ana", "password": pw}).encode()
            dash = opener.open(urllib.request.Request(base + "/login", data=data, headers={"Origin": base}))
            assert dash.geturl().endswith("/dashboard"), dash.geturl()
            res = json.load(opener.open(base + "/api/resumen"))
            out = {"login": "ok", "dashboard": dash.status, "n_ventas": res["n_ventas"],
                   "total": res["total_centavos"] / 100, "meses": len(res["por_mes"]),
                   "vendedores": [v["vendedor"] for v in res["por_vendedor"]]}
            print(json.dumps(out, ensure_ascii=False))
            return 0 if res["n_ventas"] > 0 else 1
        finally:
            srv.terminate()
            srv.wait(timeout=10)


if __name__ == "__main__":
    sys.exit(main())
