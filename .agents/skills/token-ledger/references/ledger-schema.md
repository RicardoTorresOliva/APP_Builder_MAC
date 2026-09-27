---
type: Reference
title: Esquema del evento de tokens y reglas del ledger
description: Campos del evento (contract/token-event.schema.json), ruta por defecto del ledger, niveles N1/N2/N3 y la regla de costo "n/d".
tags: [referencia, tokens, finops]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Esquema del evento de tokens

Definido en `contract/token-event.schema.json` (ADR 0013); mapea 1:1 a atributos `gen_ai.*` de
OpenTelemetry (estado "Development": ninguno es aún "Stable").

## Campos del evento

| Campo | Tipo | Notas |
|---|---|---|
| `ts` | ISO 8601 UTC | Momento del evento. |
| `phase` | `build` \| `run` | Construcción del ADS vs operación ya entregado. |
| `source` | `telemetry` \| `provider-usage` \| `estimate` | Nunca inventado; `estimate` es válido. |
| tokens de entrada/salida/caché | entero | Desglose cuando la fuente lo permite. |
| `provider`, `model` | string | Categoría/identificador, no marketing. |
| `tool`, `actor`, `unit`, `command`, `feature`, `tenant` | string | Trazabilidad completa. |
| `cost` | número o `"n/d"` | Solo si hay precio en `pricing.yaml` con fuente y fecha. |

## Ruta del ledger

`ads.yaml → tokens.ledger`, por defecto `ops/tokens/ledger.jsonl`. Un evento por línea (JSONL),
nunca se reescribe una línea existente — un evento incorrecto se corrige con uno nuevo que lo anote.

## Niveles de reporte

- **N1** — `TOKENS.md`, generado por `abm tokens report`: tabla agregada legible, para todo ADS.
- **N2** — dashboard HTML estático (`abm tokens dashboard`), con presupuestos visibles; para
  ceremonia `producto` y `enterprise-regulado`.
- **N3** — guía de pipeline OTel hacia la pila de observabilidad que el humano ya use; ABM no la
  ejecuta, solo documenta cómo conectarla.

## Regla de costo "n/d"

```text
Si integrations/observability/pricing.yaml no tiene una fila para (provider, model)
con fuente y fecha  →  cost: "n/d"
Nunca: estimar un precio de memoria o por analogía con otro modelo.
```

Esto es deliberado (ADR 0013): un "n/d" visible es preferible a un costo inventado que alguien
podría tomar como cifra real.

## Presupuestos y bloqueante

`ads.yaml → tokens.budgets` declara umbral blando y tope duro por sesión, unidad o funcionalidad.
`abm tokens budget` falla (exit ≠ 0) si algún tope duro está superado; ese fallo es el bloqueante
(f) de `AGENTS.md`, no una sugerencia.
