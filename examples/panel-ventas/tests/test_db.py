"""Datos: migraciones up/down, integridad declarada en el esquema, seeds idempotentes y reglas de negocio."""
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

import support
from support import db

ADMIN = {"id": None, "username": "agente:test", "rol": "admin"}


def tables(conn):
    return {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'index') "
                                       "AND name NOT LIKE 'sqlite_%'")}


class MigrationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.conn = db.connect(Path(self.tmp.name) / "m.db")

    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()

    def test_up_down_up(self):
        plan = db.migrate(self.conn, dry_run=True)
        self.assertEqual([p["version"] for p in plan["pasos"]], [1, 2])
        self.assertEqual(db.current_version(self.conn), 0)  # dry-run no escribe
        db.migrate(self.conn)
        self.assertEqual(db.current_version(self.conn), db.LATEST)
        self.assertTrue({"usuarios", "ventas", "sesiones", "auditoria", "ix_ventas_fecha"} <= tables(self.conn))
        db.migrate(self.conn, 1)
        self.assertNotIn("auditoria", tables(self.conn))
        self.assertIn("ventas", tables(self.conn))
        db.migrate(self.conn, 0)
        self.assertEqual(tables(self.conn), {"schema_migrations"})
        db.migrate(self.conn)
        self.assertEqual(db.current_version(self.conn), db.LATEST)
        versions = [r[0] for r in self.conn.execute("SELECT version FROM schema_migrations ORDER BY version")]
        self.assertEqual(versions, [1, 2])

    def test_out_of_range_target(self):
        with self.assertRaises(db.ValidationError):
            db.migrate(self.conn, 99)

    def test_down_with_data_keeps_integrity(self):
        db.migrate(self.conn)
        db.seed(self.conn, password=support.DEMO_PW, iterations=support.FAST_ITER)
        db.migrate(self.conn, 1)
        self.assertGreater(self.conn.execute("SELECT COUNT(*) FROM ventas").fetchone()[0], 100)
        self.assertEqual(self.conn.execute("PRAGMA foreign_key_check").fetchall(), [])


class IntegrityTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.conn = db.connect(support.fresh_db(self.tmp.name))

    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()

    def insert(self, **kw):
        row = {"vendedor_id": 2, "fecha": "2026-01-10", "cliente": "C", "producto": "P", "monto_centavos": 100, **kw}
        self.conn.execute("INSERT INTO ventas (vendedor_id, fecha, cliente, producto, monto_centavos, creado_en) "
                          "VALUES (:vendedor_id, :fecha, :cliente, :producto, :monto_centavos, 'x')", row)

    def test_check_constraints(self):
        for bad in ({"monto_centavos": 0}, {"monto_centavos": -1}, {"fecha": "10/01/2026"}, {"cliente": ""}):
            with self.subTest(bad=bad), self.assertRaises(sqlite3.IntegrityError):
                self.insert(**bad)

    def test_foreign_keys_enforced(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.insert(vendedor_id=999)
        with self.assertRaises(sqlite3.IntegrityError):
            self.conn.execute("DELETE FROM usuarios WHERE username = 'bruno'")  # tiene ventas: RESTRICT

    def test_username_unique(self):
        with self.assertRaises(sqlite3.IntegrityError):
            db.create_user(self.conn, "bruno", "Otro", "vendedor", "x" * 12, support.FAST_ITER)

    def test_seed_is_idempotent(self):
        before = db.status(self.conn)
        again = db.seed(self.conn, password=support.DEMO_PW, iterations=support.FAST_ITER)
        self.assertEqual((again["usuarios_creados"], again["ventas_creadas"]), ([], 0))
        self.assertEqual(db.status(self.conn), before)
        self.assertGreater(before["ventas"], 100)

    def test_money_is_integer_cents(self):
        self.assertEqual(db.parse_monto("1290,5"), 129050)
        for bad in ("0", "-1", "1.001", "abc", None, True, "NaN", "2000000"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                db.parse_monto(bad)

    def test_resumen_fills_month_gaps(self):
        r = db.resumen(self.conn, ADMIN, "2020-01-01", "2020-03-31")
        self.assertEqual((r["n_ventas"], r["por_mes"]), (0, []))
        v, _ = db.create_venta(self.conn, ADMIN, {"fecha": "2020-01-05", "cliente": "A", "producto": "B",
                                                  "monto": "10", "vendedor": "bruno"})
        r = db.resumen(self.conn, ADMIN, "2020-01-01", "2020-03-31")
        self.assertEqual([m["mes"] for m in r["por_mes"]], ["2020-01", "2020-02", "2020-03"])
        self.assertEqual([m["n"] for m in r["por_mes"]], [1, 0, 0])

    def test_create_and_delete_are_audited(self):
        v, created = db.create_venta(self.conn, ADMIN, {"fecha": "2026-02-01", "cliente": "A", "producto": "B",
                                                        "monto": "10", "vendedor": "carla"})
        self.assertTrue(created)
        preview = db.delete_venta(self.conn, ADMIN, v["id"], dry_run=True)
        self.assertEqual(preview["would_delete"]["id"], v["id"])
        db.delete_venta(self.conn, ADMIN, v["id"])
        acciones = [r[0] for r in self.conn.execute("SELECT accion FROM auditoria WHERE entidad_id = ? ORDER BY id", (v["id"],))]
        self.assertEqual(acciones, ["crear", "borrar"])

    def test_readonly_connection_rejects_writes(self):
        with closing(db.connect(Path(self.tmp.name) / "panel.db", readonly=True)) as ro:
            with self.assertRaises(sqlite3.OperationalError):
                ro.execute("DELETE FROM ventas")


if __name__ == "__main__":
    unittest.main()
