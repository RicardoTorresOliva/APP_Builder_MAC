---
type: Template
title: closeout.md — cierre de unidad
description: Qué se hizo, sincronía intención/spec/contrato/código, tokens de la unidad y pendientes.
tags: [template, closeout, drift]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Cierre: `<FU/DU-id> — <nombre>`

Modo: `<VIBE|IDD|SDD|SPDD|AIDD>` · Fecha: `<ISO 8601>`

## Qué se hizo

`<resumen de acciones, con archivo o commit por línea>`

## Sincronía (drift)

Ejecutado `/drift` (`/methodology/drift.md`) contra:

| Artefacto | Estado | Acción tomada |
|---|---|---|
| `intent.md \| requirements.md/design.md/tasks.md \| prompt-contract.md` | `sincronizado \| actualizado \| desviación corregida` | `<qué se ajustó, o "ninguna">` |
| Contrato ADS (`ads.yaml`) | `sin cambios \| actualizado` | `<...>` |

## Quality gate

`<perfil activo>` — `<pasa \| hallazgos y su resolución>`

## Tokens de la unidad

| Fuente | Tokens | Costo |
|---|---|---|
| `telemetry \| provider-usage \| estimate` | `<n>` | `<n o "n/d">` |

Registrado con: `abm tokens record` o `abm tokens estimate`.

## Pendientes

`<+n nuevos a docs/_work/PENDIENTES.md; total n>` — `<uno por línea, o "ninguno">`

## No verificado

`<ítem → motivo, o "ninguno">`

## Siguiente

`<acción concreta que sigue>`
