"""API y páginas de punta a punta contra un servidor real en un puerto efímero."""
import tempfile
import threading
import unittest
from contextlib import closing

import support
from support import Client, db

import server

PROBLEM_CT = "application/problem+json"


class ApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.dbp = support.fresh_db(cls.tmp.name)
        cls.httpd = server.make_server("127.0.0.1", 0, cls.dbp, quiet=True)
        cls.port = cls.httpd.server_address[1]
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.tmp.cleanup()

    def logged(self, username):
        c = Client(self.port)
        status, _ = c.login(username)
        self.assertEqual(status, 303)
        return c

    def assertProblem(self, status, headers, body, expected):
        self.assertEqual(status, expected)
        self.assertTrue(headers["Content-Type"].startswith(PROBLEM_CT))
        for k in ("type", "title", "status", "detail"):
            self.assertIn(k, body)
        self.assertEqual(body["status"], expected)
        self.assertNotIn("Traceback", str(body))

    def nuevo(self, **kw):
        base = {"fecha": "2026-01-15", "cliente": "Café Aroma", "producto": "Plan Pro (anual)", "monto": "1290.00"}
        return {**base, **kw}

    # ------------------------------------------------------------ auth y sesión
    def test_login_sets_hardened_session_cookie(self):
        c = Client(self.port)
        c.request("GET", "/login")
        status, headers = c.login("ana")
        self.assertEqual((status, headers["Location"]), (303, "/dashboard"))
        cookie = [h for h in headers.get_all("Set-Cookie") if h.startswith("pv_session=")][0]
        for flag in ("HttpOnly", "SameSite=Strict", "Path=/"):
            self.assertIn(flag, cookie)

    def test_login_requires_csrf(self):
        status, headers, body = Client(self.port).json("POST", "/login", form={"username": "ana", "password": "x"})
        self.assertProblem(status, headers, body, 403)

    def test_bad_credentials_generic_message(self):
        pages = []
        for user in ("bruno", "fantasma"):  # usuario real con clave mala vs. usuario inexistente
            c = Client(self.port)
            _, _, form = c.request("GET", "/login")
            csrf = support.re.search(rb'name="csrf" value="([^"]+)"', form).group(1).decode()
            st, _, page = c.request("POST", "/login", form={"csrf": csrf, "username": user, "password": "incorrecta"})
            self.assertEqual(st, 401)
            pages.append("Usuario o contraseña incorrectos.".encode("utf-8") in page)
        self.assertEqual(pages, [True, True])

    def test_login_rate_limited(self):
        c = Client(self.port)
        for _ in range(5):
            self.assertEqual(c.login("intruso", "mala")[0], 401)
        status, headers = c.login("intruso")
        self.assertEqual(status, 429)
        self.assertEqual(headers["Retry-After"], "900")
        self.logged("carla")  # otra clave (IP, usuario) no queda bloqueada

    def test_api_requires_session(self):
        for path in ("/api/resumen", "/api/ventas"):
            status, headers, body = Client(self.port).json("GET", path)
            self.assertProblem(status, headers, body, 401)

    def test_pages_redirect_without_session(self):
        status, headers, _ = Client(self.port).request("GET", "/dashboard")
        self.assertEqual((status, headers["Location"]), (303, "/login"))

    def test_logout_invalidates_session(self):
        c = self.logged("carla")
        status, _, _ = c.request("POST", "/logout", form={"csrf": c.csrf})
        self.assertEqual(status, 303)
        self.assertEqual(c.json("GET", "/api/resumen")[0], 401)

    def test_logout_requires_csrf(self):
        c = self.logged("carla")
        status, headers, body = c.json("POST", "/logout", form={"csrf": "otro"})
        self.assertProblem(status, headers, body, 403)

    # ------------------------------------------------------------ permisos por rol
    def test_vendedor_sees_only_own_sales(self):
        c = self.logged("bruno")
        _, _, ventas = c.json("GET", "/api/ventas?limit=500")
        self.assertTrue(ventas["items"])
        self.assertEqual({v["vendedor"] for v in ventas["items"]}, {"Bruno Díaz"})
        _, _, res = c.json("GET", "/api/resumen")
        self.assertEqual([v["vendedor"] for v in res["por_vendedor"]], ["Bruno Díaz"])
        _, _, admin = self.logged("ana").json("GET", "/api/ventas?limit=1")
        self.assertGreater(admin["total"], ventas["total"])

    def test_vendedor_cannot_create_for_other(self):
        c = self.logged("bruno")
        status, headers, body = c.json("POST", "/api/ventas", json_body=self.nuevo(vendedor="carla"),
                                       headers={"X-CSRF-Token": c.csrf})
        self.assertProblem(status, headers, body, 403)

    def test_delete_requires_admin_and_is_audited(self):
        c = self.logged("bruno")
        _, _, v = c.json("POST", "/api/ventas", json_body=self.nuevo(cliente="Para borrar"), headers={"X-CSRF-Token": c.csrf})
        status, headers, body = c.json("DELETE", f"/api/ventas/{v['id']}", headers={"X-CSRF-Token": c.csrf})
        self.assertProblem(status, headers, body, 403)
        a = self.logged("ana")
        self.assertEqual(a.request("DELETE", f"/api/ventas/{v['id']}", headers={"X-CSRF-Token": a.csrf})[0], 204)
        status, headers, body = a.json("DELETE", f"/api/ventas/{v['id']}", headers={"X-CSRF-Token": a.csrf})
        self.assertProblem(status, headers, body, 404)
        with closing(db.connect(self.dbp)) as conn:
            row = conn.execute("SELECT actor FROM auditoria WHERE accion = 'borrar' AND entidad_id = ?", (v["id"],)).fetchone()
        self.assertEqual(row["actor"], "ana")

    # ------------------------------------------------------------ CSRF, validación y problem+json
    def test_mutation_without_csrf_forbidden(self):
        c = self.logged("bruno")
        status, headers, body = c.json("POST", "/api/ventas", json_body=self.nuevo())
        self.assertProblem(status, headers, body, 403)
        status, headers, body = c.json("POST", "/api/ventas", json_body=self.nuevo(), headers={"X-CSRF-Token": "falso"})
        self.assertProblem(status, headers, body, 403)

    def test_cross_origin_rejected(self):
        c = self.logged("bruno")
        status, headers, body = c.json("POST", "/api/ventas", json_body=self.nuevo(),
                                       headers={"X-CSRF-Token": c.csrf, "Origin": "http://evil.example"})
        self.assertProblem(status, headers, body, 403)

    def test_create_valid_is_idempotent(self):
        c = self.logged("carla")
        h = {"X-CSRF-Token": c.csrf, "Idempotency-Key": "k-123"}
        s1, hd, v1 = c.json("POST", "/api/ventas", json_body=self.nuevo(monto="99,90"), headers=h)
        self.assertEqual(s1, 201)
        self.assertEqual(hd["Location"], f"/api/ventas/{v1['id']}")
        self.assertEqual((v1["monto_centavos"], v1["vendedor"]), (9990, "Carla Méndez"))
        s2, _, v2 = c.json("POST", "/api/ventas", json_body=self.nuevo(monto="99,90"), headers=h)
        self.assertEqual((s2, v2["id"]), (200, v1["id"]))

    def test_invalid_input_returns_field_errors(self):
        c = self.logged("bruno")
        bad = {"fecha": "2026-13-40", "cliente": "", "producto": "x" * 81, "monto": "-5"}
        status, headers, body = c.json("POST", "/api/ventas", json_body=bad, headers={"X-CSRF-Token": c.csrf})
        self.assertProblem(status, headers, body, 422)
        self.assertEqual({e["pointer"] for e in body["errors"]}, {"#/fecha", "#/cliente", "#/producto", "#/monto"})
        future = self.nuevo(fecha="2999-01-01")
        status, _, body = c.json("POST", "/api/ventas", json_body=future, headers={"X-CSRF-Token": c.csrf})
        self.assertEqual((status, body["errors"][0]["pointer"]), (422, "#/fecha"))

    def test_transport_errors(self):
        c = self.logged("bruno")
        h = {"X-CSRF-Token": c.csrf}
        st, hd, b = c.json("POST", "/api/ventas", body="fecha=x", headers={**h, "Content-Type": "text/plain"})
        self.assertProblem(st, hd, b, 415)
        st, hd, b = c.json("POST", "/api/ventas", body="{no-json", headers={**h, "Content-Type": "application/json"})
        self.assertProblem(st, hd, b, 400)
        st, hd, b = c.json("POST", "/api/ventas", body="x" * 20000, headers={**h, "Content-Type": "application/json"})
        self.assertProblem(st, hd, b, 413)
        st, hd, b = c.json("GET", "/api/resumen?desde=2026-05-01&hasta=2026-01-01")
        self.assertProblem(st, hd, b, 422)
        st, hd, b = c.json("GET", "/no-existe")
        self.assertProblem(st, hd, b, 404)

    def test_sql_injection_is_stored_as_data(self):
        c = self.logged("diego")
        evil = "x'); DROP TABLE ventas;--"
        st, _, v = c.json("POST", "/api/ventas", json_body=self.nuevo(cliente=evil), headers={"X-CSRF-Token": c.csrf})
        self.assertEqual((st, v["cliente"]), (201, evil))
        self.assertEqual(c.json("GET", "/api/ventas?limit=1")[0], 200)

    # ------------------------------------------------------------ resumen y dashboard
    def test_resumen_is_consistent(self):
        _, _, r = self.logged("ana").json("GET", "/api/resumen?desde=2020-01-01")
        self.assertEqual(sum(m["total_centavos"] for m in r["por_mes"]), r["total_centavos"])
        self.assertEqual(sum(v["n"] for v in r["por_vendedor"]), r["n_ventas"])
        self.assertEqual(r["ticket_promedio_centavos"], r["total_centavos"] // r["n_ventas"])

    def test_dashboard_and_static_have_security_headers(self):
        c = self.logged("ana")
        status, headers, page = c.request("GET", "/dashboard")
        self.assertEqual(status, 200)
        self.assertIn("script-src 'self'", headers["Content-Security-Policy"])
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertIn(b'id="chart-mes"', page)
        self.assertIn(b'<option value=', page)  # admin elige vendedor
        st, hd, js = c.request("GET", "/static/app.js")
        self.assertEqual((st, hd["Content-Type"].split(";")[0]), (200, "text/javascript"))
        self.assertIsNone(support.re.search(rb"\.(innerHTML|outerHTML)\s*=|insertAdjacentHTML|eval\(", js))
        self.assertEqual(c.request("GET", "/static/../db.py")[0], 404)

    def test_healthz(self):
        self.assertEqual(Client(self.port).json("GET", "/healthz")[2], {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
