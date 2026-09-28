#!/usr/bin/env python3
"""CLI del panel de ventas para personas y agentes (Contrato ADS): `--json` en toda orden, `--dry-run` en las que escriben.

  python3 app/cli.py status --json
  python3 app/cli.py ventas-resumen [--desde AAAA-MM-DD] [--hasta AAAA-MM-DD] --json
  python3 app/cli.py crear-venta --fecha F --cliente C --producto P --monto 120.50 --vendedor bruno [--idempotency-key K] [--dry-run] --json
  python3 app/cli.py borrar-venta --id N (--dry-run | --confirm) --json      # destructiva: confirmación humana
  python3 app/cli.py migrate [--to N] [--dry-run] --json
  python3 app/cli.py seed [--dry-run] --json                                 # contraseñas demo solo en consola

Errores: objeto application/problem+json en stdout y código de salida 1 (datos) o 2 (uso/confirmación).
"""
from __future__ import annotations

import argparse
import json
import sys
from contextlib import closing
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

ACTOR = {"id": None, "username": "agente:cli", "rol": "admin"}


def parser():
    ap = argparse.ArgumentParser(prog="panel-ventas", description="Opera el panel de ventas (salida JSON con --json)")
    ap.add_argument("--db", help="ruta de la base (por defecto PANEL_VENTAS_DB o data/panel.db)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="estado del ADS (lectura)")
    r = sub.add_parser("ventas-resumen", help="totales y series por mes y vendedor (lectura)")
    r.add_argument("--desde")
    r.add_argument("--hasta")
    c = sub.add_parser("crear-venta", help="registra una venta (escritura)")
    for k in ("fecha", "cliente", "producto", "monto", "vendedor"):
        c.add_argument(f"--{k}", required=True)
    c.add_argument("--idempotency-key")
    c.add_argument("--dry-run", action="store_true")
    b = sub.add_parser("borrar-venta", help="borra una venta (destructiva; exige --confirm)")
    b.add_argument("--id", type=int, required=True)
    b.add_argument("--confirm", action="store_true", help="confirmación humana explícita")
    b.add_argument("--dry-run", action="store_true")
    m = sub.add_parser("migrate", help="aplica o revierte migraciones")
    m.add_argument("--to", type=int)
    m.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("seed", help="migra y siembra datos demo (idempotente)")
    s.add_argument("--dry-run", action="store_true")
    return ap


def run(a):
    path = a.db or db.db_path()
    if a.cmd in ("status", "ventas-resumen"):
        if a.cmd == "status" and not Path(path).exists():
            return {"id": "panel-ventas", "estado": "sin-inicializar", "schema_version": 0, "schema_latest": db.LATEST}
        with closing(db.connect(path, readonly=True)) as conn:
            return db.status(conn) if a.cmd == "status" else db.resumen(conn, ACTOR, a.desde, a.hasta)
    if a.cmd == "borrar-venta" and not (a.dry_run or a.confirm):
        raise UsageProblem("Requiere confirmación humana", "borrar-venta es destructiva: usa --dry-run o --confirm")
    with closing(db.connect(path)) as conn:
        if a.cmd == "migrate":
            return db.migrate(conn, a.to, a.dry_run)
        if a.cmd == "seed":
            mig = db.migrate(conn, dry_run=a.dry_run)
            return {"migracion": mig, **db.seed(conn, dry_run=a.dry_run)} if not a.dry_run else \
                {"migracion": mig, "dry_run": True}
        if db.current_version(conn) < db.LATEST:
            raise db.NotInitialized("ejecuta `python3 app/cli.py seed`")
        if a.cmd == "crear-venta":
            data = {k: getattr(a, k) for k in ("fecha", "cliente", "producto", "monto", "vendedor")}
            venta, created = db.create_venta(conn, ACTOR, data, a.idempotency_key, a.dry_run)
            return {**venta, "created": created, "dry_run": a.dry_run}
        return {**db.delete_venta(conn, ACTOR, a.id, a.dry_run), "dry_run": a.dry_run}


class UsageProblem(db.DomainError):
    status, slug, title = 428, "confirmacion", "Requiere confirmación humana"

    def __init__(self, title, detail):
        super().__init__(detail)
        self.title = title


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in argv
    argv = [x for x in argv if x != "--json"]
    a = parser().parse_args(argv)
    try:
        out, code = run(a), 0
    except UsageProblem as e:
        out, code = e.problem(), 2
    except db.DomainError as e:
        out, code = e.problem(), 1
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for k, v in out.items():
            print(f"{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v}")
    return code


if __name__ == "__main__":
    sys.exit(main())
