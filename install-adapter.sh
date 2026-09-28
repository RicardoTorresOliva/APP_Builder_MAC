#!/usr/bin/env sh
# Shim de compatibilidad (v4.1 → v5): los adaptadores ahora se generan con `./abm sync`.
# Uso: sh install-adapter.sh   → regenera los adaptadores de todas las herramientas habilitadas en adapters/tools.yaml
DIR="$(cd "$(dirname "$0")" && pwd)"; exec "$DIR/abm" sync
