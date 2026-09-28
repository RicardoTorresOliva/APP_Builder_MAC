#!/usr/bin/env python3
"""Shim: ejecuta la CLI de ABM del repo que contiene este ejemplo, con este ADS como raíz.

Un ADS creado con `abm new-ads` trae su propia copia de `scripts/`; este ejemplo vive dentro de ABM y la reutiliza.
Uso: python3 scripts/abm.py <orden> [--json] [--dry-run]   (equivale a python3 ../../scripts/abm.py --root . <orden>)
"""
import sys
from pathlib import Path

ADS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ADS_ROOT.parents[1] / "scripts"))
from abmkit.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(["--root", str(ADS_ROOT), *sys.argv[1:]]))
