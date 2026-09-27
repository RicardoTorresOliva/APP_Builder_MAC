#!/usr/bin/env python3
"""Entrada del CLI de ABM. Uso: python scripts/abm.py <orden> [--json] [--dry-run]. Ver `abm --help`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
if sys.version_info < (3, 9):
    sys.exit("ABM necesita Python 3.9 o superior. Instálalo desde python.org y vuelve a intentarlo.")

from abmkit.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
