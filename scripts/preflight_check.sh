#!/usr/bin/env sh
# Shim de compatibilidad (v4.1 → v5). Usa: ./abm preflight  (ver MIGRATION.md)
DIR="$(cd "$(dirname "$0")/.." && pwd)"; exec "$DIR/abm" preflight
