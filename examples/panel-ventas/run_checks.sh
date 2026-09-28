#!/usr/bin/env sh
# "Build" y verificación del panel de ventas (golden path de ABM). Uso: ./run_checks.sh
set -eu
cd "$(dirname "$0")"
ABM="python3 scripts/abm.py"   # = python3 ../../scripts/abm.py --root .
step() { printf '\n== %s\n' "$1"; }
step "compileall";          python3 -m compileall -q app ops tests
step "tests";               python3 -m unittest discover -s tests
step "e2e (servidor real)"; python3 ops/smoke_e2e.py
step "ads-check";           $ABM ads-check
step "agent-conformance";   $ABM agent-conformance
step "okf index";           $ABM okf index
step "okf validate";        $ABM okf validate
step "tokens budget";       $ABM tokens budget
step "secrets";             $ABM secrets
printf '\nTODO OK\n'
