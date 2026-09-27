---
type: Attested Computation
title: Totales de tokens del ADS
description: Cálculo sancionado de los totales de tokens y costo a partir del ledger; verificable con un atestador determinista.
tags: [tokens, finops, atestacion]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:43:42Z }
runtime: python
parameters: []
computation: scripts/abmkit/tokens.py
executor:
  resource: scripts/abmkit/tokens.py
  receipt: [events, input, output, total]
attester:
  resource: scripts/abmkit/tokens.py
---

# Totales de tokens del ADS

Las cifras de `TOKENS.md` y del dashboard **solo** se obtienen ejecutando `./abm tokens report` sobre el ledger (`ads.yaml → tokens.ledger`). Ningún agente escribe cifras de consumo a mano.

## Computation
- Total = Σ `input_tokens` + Σ `output_tokens` de los eventos válidos del ledger (`/contract/token-event.schema.json`).
- Costo = Σ por evento: `cost_usd` si existe; si no, tokens × precio de `integrations/observability/pricing.yaml` (clave `<provider>/<model>`); sin precio → "n/d".

## Atestación
`./abm tokens attest` recalcula los totales desde el ledger y los compara con los de `TOKENS.md`. Falla si difieren o si hay eventos inválidos. Corre en `./abm check` cuando existe el reporte.
