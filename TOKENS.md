---
type: Token Report
title: Reporte de tokens
description: Consumo de tokens y costo del ADS (construcción y operación), generado desde el ledger.
tags: [tokens, finops]
status: stable
generated: { by: process:abm-tokens, at: 2026-09-27T23:49:54Z }
---

# Reporte de tokens

<!-- Generado por `abm tokens report`. No editar a mano. -->

- **Total:** 2,539,900 tokens (entrada 2,539,900 · salida 0) en 10 eventos.
- **Estimados** (caracteres/4, sin telemetría): 0 eventos.

## Por fase

| Clave | Eventos | Entrada | Salida | Costo USD |
|---|---|---|---|---|
| build | 10 | 2,539,900 | 0 | 5.0798 |

## Por unidad (FU/DU/WU)

| Clave | Eventos | Entrada | Salida | Costo USD |
|---|---|---|---|---|
| Fase-1 | 3 | 936,221 | 0 | 1.8724 |
| WU5 | 2 | 417,466 | 0 | 0.8349 |
| WU9-WU10 | 1 | 328,960 | 0 | 0.6579 |
| WU11 | 1 | 276,509 | 0 | 0.5530 |
| WU10 | 1 | 201,999 | 0 | 0.4040 |
| WU4 | 1 | 191,990 | 0 | 0.3840 |
| WU6 | 1 | 186,755 | 0 | 0.3735 |

## Por modelo

| Clave | Eventos | Entrada | Salida | Costo USD |
|---|---|---|---|---|
| claude-sonnet-5 | 10 | 2,539,900 | 0 | 5.0798 |

## Presupuestos

| Alcance | Usado | Blando | Duro | Estado |
|---|---|---|---|---|
| total | 2,539,900 | 8000000 | 14000000 | ok |
| unit:Fase-1 | 936,221 | 400000 | 1500000 | soft |
| unit:WU4 | 191,990 | 400000 | 1500000 | ok |
| unit:WU5 | 417,466 | 400000 | 1500000 | soft |
| unit:WU6 | 186,755 | 400000 | 1500000 | ok |
| unit:WU10 | 201,999 | 400000 | 1500000 | ok |
| unit:WU9-WU10 | 328,960 | 400000 | 1500000 | ok |
| unit:WU11 | 276,509 | 400000 | 1500000 | ok |
