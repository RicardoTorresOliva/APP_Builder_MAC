"""Identidad: PBKDF2 con sal por usuario, autenticación sin enumeración, sesiones y límite de intentos."""
import sqlite3
import tempfile
import time
import unittest

import support
from support import db

import server  # noqa: E402  (app/ ya está en sys.path vía support)


class PasswordTest(unittest.TestCase):
    def test_hash_uses_unique_salt_and_verifies(self):
        h1, s1, it = db.hash_password("clave-correcta", iterations=support.FAST_ITER)
        h2, s2, _ = db.hash_password("clave-correcta", iterations=support.FAST_ITER)
        self.assertNotEqual(s1, s2)
        self.assertNotEqual(h1, h2)
        self.assertEqual(len(bytes.fromhex(s1)), 16)
        self.assertTrue(db.verify_password("clave-correcta", h1, s1, it))
        self.assertFalse(db.verify_password("clave-incorrecta", h1, s1, it))

    def test_default_iterations_are_strong(self):
        self.assertGreaterEqual(db.PBKDF2_ITER, 600_000)


class AuthDbTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.conn = db.connect(support.fresh_db(self.tmp.name))

    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()

    def test_password_never_stored_in_clear(self):
        rows = self.conn.execute("SELECT pw_hash, pw_salt FROM usuarios").fetchall()
        self.assertEqual(len(rows), 4)
        for r in rows:
            self.assertNotIn(support.DEMO_PW, (r["pw_hash"], r["pw_salt"]))
        self.assertEqual(len({r["pw_salt"] for r in rows}), 4)

    def test_authenticate(self):
        self.assertEqual(db.authenticate(self.conn, "bruno", support.DEMO_PW)["rol"], "vendedor")
        self.assertIsNone(db.authenticate(self.conn, "bruno", "otra"))
        self.assertIsNone(db.authenticate(self.conn, "no-existe", support.DEMO_PW))
        self.assertIsNone(db.authenticate(self.conn, "bruno", "x" * 2000))

    def test_session_token_hashed_and_expires(self):
        u = db.authenticate(self.conn, "ana", support.DEMO_PW)
        token, csrf = db.create_session(self.conn, u["id"])
        stored = self.conn.execute("SELECT token_hash FROM sesiones").fetchone()[0]
        self.assertNotEqual(stored, token)
        s = db.get_session(self.conn, token)
        self.assertEqual((s["username"], s["csrf"]), ("ana", csrf))
        self.assertIsNone(db.get_session(self.conn, token + "x"))
        self.conn.execute("UPDATE sesiones SET expira_en = ?", (int(time.time()) - 1,))
        self.assertIsNone(db.get_session(self.conn, token))

    def test_logout_deletes_session(self):
        token, _ = db.create_session(self.conn, 1)
        db.delete_session(self.conn, token)
        self.assertIsNone(db.get_session(self.conn, token))

    def test_roles_constrained(self):
        with self.assertRaises(db.ValidationError):
            db.create_user(self.conn, "eva", "Eva", "superuser", "x" * 12, support.FAST_ITER)
        with self.assertRaises(sqlite3.IntegrityError):
            self.conn.execute("INSERT INTO usuarios (username, nombre, rol, pw_hash, pw_salt, pw_iter, creado_en) "
                              "VALUES ('eva', 'Eva', 'root', 'h', 's', 1000, 'x')")


class LimiterTest(unittest.TestCase):
    def test_blocks_after_max_fails_per_key(self):
        lim = server.LoginLimiter(max_fails=3, window=60)
        key = ("127.0.0.1", "bruno")
        for _ in range(3):
            self.assertFalse(lim.blocked(key))
            lim.fail(key)
        self.assertTrue(lim.blocked(key))
        self.assertFalse(lim.blocked(("127.0.0.1", "carla")))
        lim.reset(key)
        self.assertFalse(lim.blocked(key))


if __name__ == "__main__":
    unittest.main()
