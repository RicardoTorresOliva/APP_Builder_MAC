---
type: Template
title: prompt-contract.md — contrato de prompt versionado (SPDD)
description: Versión, intención, entradas/salidas, invariantes, tests de aceptación y archivos vinculados.
tags: [template, spdd, prompt-contract]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Contrato de prompt: `<módulo>`

Modo: SPDD (`/methodology/spdd.md`). Sincronizado en ambos sentidos con el código: un cambio en
entradas/salidas/invariantes sube la versión; un desacuerdo con el código bloquea el `closeout`.

## Versión
`v1` · Última sincronía: `<fecha ISO>` · Estado: `<sincronizado | desincronizado>`

## Intención
`<qué hace este módulo agéntico, en una o dos frases>`

## Entradas
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `<campo>` | `<tipo>` | `sí/no` | `<qué representa>` |

## Salidas
| Campo | Tipo | Descripción |
|---|---|---|
| `<campo>` | `<tipo>` | `<qué representa>` |

## Invariantes
Reglas que nunca deben romperse, sin importar la entrada:
- `<invariante>`

## Tests de aceptación
| ID | Entrada de ejemplo | Salida esperada |
|---|---|---|
| ACC-01 | `<...>` | `<...>` |

## Archivos vinculados
- `<ruta del código que implementa este contrato>`

## Historial de versiones
| Versión | Cambio | Motivo |
|---|---|---|
| v1 | Creación | `<...>` |
