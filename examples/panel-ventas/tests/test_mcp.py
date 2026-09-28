"""Superficie agéntica: servidor MCP por stdio (JSON-RPC) y CLI --json/--dry-run, como los usaría un agente."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

import support

SERVER = [sys.executable, str(support.ROOT / "ops" / "mcp_server.py")]
CLI = [sys.executable, str(support.ROOT / "app" / "cli.py")]


class McpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.env = {**os.environ, "PANEL_VENTAS_DB": str(support.fresh_db(cls.tmp.name)),
                   "PANEL_VENTAS_AUDIT_LOG": os.path.join(cls.tmp.name, "audit.jsonl")}
        cls.proc = subprocess.Popen(SERVER, cwd=support.ROOT, env=cls.env, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, text=True, encoding="utf-8")
        cls.nid = 0

    @classmethod
    def tearDownClass(cls):
        cls.proc.stdin.close()
        cls.proc.wait(timeout=10)
        cls.proc.stdout.close()
        cls.tmp.cleanup()

    def rpc(self, method, params=None):
        McpTest.nid += 1
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.nid, "method": method, "params": params or {}}) + "\n")
        self.proc.stdin.flush()
        msg = json.loads(self.proc.stdout.readline())
        self.assertEqual(msg["id"], self.nid)
        return msg

    def call(self, name, **arguments):
        return self.rpc("tools/call", {"name": name, "arguments": arguments})["result"]

    def n_ventas(self):
        return self.call("status")["structuredContent"]["ventas"]

    def test_1_initialize_and_list(self):
        init = self.rpc("initialize", {"protocolVersion": "2025-11-25", "capabilities": {}})["result"]
        self.assertEqual((init["serverInfo"]["name"], init["protocolVersion"]), ("panel-ventas", "2025-11-25"))
        tools = {t["name"]: t for t in self.rpc("tools/list")["result"]["tools"]}
        self.assertEqual(set(tools), {"status", "ventas_resumen", "crear_venta", "borrar_venta"})
        self.assertTrue(tools["status"]["annotations"]["readOnlyHint"])
        self.assertTrue(tools["borrar_venta"]["annotations"]["destructiveHint"])
        self.assertIn("confirm", tools["borrar_venta"]["inputSchema"]["properties"])
        self.assertTrue(tools["crear_venta"]["inputSchema"]["properties"]["dry_run"]["default"])

    def test_2_read_tools(self):
        st = self.call("status")
        self.assertFalse(st["isError"])
        self.assertEqual(st["structuredContent"]["estado"], "ok")
        res = self.call("ventas_resumen", desde="2020-01-01")["structuredContent"]
        self.assertEqual(sum(m["total_centavos"] for m in res["por_mes"]), res["total_centavos"])
        bad = self.call("ventas_resumen", desde="ayer")
        self.assertTrue(bad["isError"])
        self.assertEqual(bad["structuredContent"]["status"], 422)

    def test_3_write_defaults_to_dry_run(self):
        before = self.n_ventas()
        args = {"fecha": "2026-03-10", "cliente": "Librería Andina", "producto": "Capacitación de equipo",
                "monto": "220", "vendedor": "diego"}
        r = self.call("crear_venta", **args)
        self.assertFalse(r["isError"])
        self.assertTrue(r["structuredContent"]["dry_run"])
        self.assertIn("would_create", r["structuredContent"])
        self.assertEqual(self.n_ventas(), before)
        r = self.call("crear_venta", dry_run=False, idempotency_key="mcp-1", **args)
        self.assertEqual((r["structuredContent"]["created"], self.n_ventas()), (True, before + 1))
        again = self.call("crear_venta", dry_run=False, idempotency_key="mcp-1", **args)
        self.assertEqual((again["structuredContent"]["created"], self.n_ventas()), (False, before + 1))

    def test_4_destructive_requires_confirm(self):
        before = self.n_ventas()
        preview = self.call("borrar_venta", id=1)
        self.assertFalse(preview["isError"])
        self.assertIn("would_delete", preview["structuredContent"])
        denied = self.call("borrar_venta", id=1, dry_run=False)
        self.assertTrue(denied["isError"])
        self.assertEqual(denied["structuredContent"]["status"], 428)
        self.assertEqual(self.n_ventas(), before)
        ok = self.call("borrar_venta", id=1, dry_run=False, confirm=True)
        self.assertFalse(ok["isError"])
        self.assertEqual(self.n_ventas(), before - 1)
        with open(self.env["PANEL_VENTAS_AUDIT_LOG"], encoding="utf-8") as f:
            audit = [json.loads(line) for line in f]
        self.assertIn({"tool": "borrar_venta", "ok": False}, [{"tool": a["tool"], "ok": a["ok"]} for a in audit])

    def test_5_protocol_errors_and_tokens(self):
        self.assertEqual(self.rpc("tools/call", {"name": "no_existe"})["error"]["code"], -32602)
        self.assertEqual(self.rpc("metodo/raro")["error"]["code"], -32601)
        res = self.rpc("resources/list")["result"]["resources"]
        uri = res[0]["uri"]
        self.assertEqual(uri, "panel-ventas://tokens/summary")
        summary = json.loads(self.rpc("resources/read", {"uri": uri})["result"]["contents"][0]["text"])
        self.assertIn("total_tokens", summary)


class CliTest(unittest.TestCase):
    def run_cli(self, *args, env=None):
        p = subprocess.run(CLI + list(args) + ["--json"], env=env, capture_output=True, text=True, encoding="utf-8")
        return p.returncode, json.loads(p.stdout)

    def test_cli_json_and_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {**os.environ, "PANEL_VENTAS_DB": str(support.fresh_db(tmp))}
            code, st = self.run_cli("status", env=env)
            self.assertEqual((code, st["estado"]), (0, "ok"))
            code, dry = self.run_cli("crear-venta", "--fecha", "2026-04-02", "--cliente", "Café Aroma", "--producto",
                                     "Soporte premium", "--monto", "89", "--vendedor", "bruno", "--dry-run", env=env)
            self.assertEqual((code, dry["dry_run"], dry["created"]), (0, True, False))
            code, err = self.run_cli("borrar-venta", "--id", "1", env=env)
            self.assertEqual((code, err["status"]), (2, 428))
            code, err = self.run_cli("crear-venta", "--fecha", "x", "--cliente", "A", "--producto", "B",
                                     "--monto", "0", "--vendedor", "bruno", env=env)
            self.assertEqual((code, err["status"]), (1, 422))


if __name__ == "__main__":
    unittest.main()
