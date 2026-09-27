---
type: Methodology
title: Metodologías de ABM — índice
description: Qué modo metodológico usar, cuándo, cómo se mezclan y dónde está cada pieza del motor.
tags: [metodologia, router, idd, sdd, spdd, aidd, vibe]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Metodologías de ABM

No existe una metodología óptima para todo encargo. ABM elige y **mezcla** el modo por **módulo**,
según seis dimensiones del encargo, y lo fija en `methodology-map.md`. Decisión: `/docs/adr/0006-router-metodologico.md`.

## Los cinco modos

| Modo | Qué es | Úsalo cuando | Detalle |
|---|---|---|---|
| **VIBE** | Exploración rápida, desechable, en rama sandbox | Prototipo o experimento de riesgo bajo | `/methodology/vibe.md` |
| **IDD** | Minimum Viable Spec: intención + restricciones; el agente decide el cómo | Incertidumbre media/alta, riesgo bajo/medio, MVP | `/methodology/idd.md` |
| **SDD** | Requirements (EARS) → design → tasks, trazables | Riesgo alto, equipo grande, sistema de largo plazo | `/methodology/sdd.md` |
| **SPDD** | Contrato de prompt versionado, sincronizado con el código | Módulos vivos con mucha autonomía del agente | `/methodology/spdd.md` |
| **AIDD** | Híbrido: explorar (VIBE) → consolidar (IDD/SDD) → construir con revisión humana | Incertidumbre alta + necesidad de llegar a producción | `/methodology/aidd.md` |

## Cómo se decide y se mezcla

- **`/methodology/router.md`** — las seis dimensiones, las reglas de decisión en orden, los disparadores
  de escalamiento/desescalamiento. **`/methodology/router.yaml`** es la versión máquina-legible que
  consume `abm methodology classify`.
- **`/methodology/mixing.md`** — cómo un mismo ADS mezcla modos por módulo, con un ejemplo completo.
- **`/methodology/ceremony.md`** — los cuatro niveles de ceremonia (Prototipo/MVP/Producto/Enterprise-Regulado)
  que fijan el modo por defecto, los gates y el nivel del Contrato ADS y del dashboard de tokens.
- **`/methodology/drift.md`** — cómo se detecta y corrige la deriva entre intención, spec, contratos y código.
- **`/methodology/governance-regulated.md`** — capa opcional de trazabilidad para el perfil Enterprise-Regulado.

## Plantillas

Cada modo produce artefactos definidos en `/templates/README.md`: `intent.md` (IDD), `spec/` (SDD),
`prompt-contract.md` (SPDD), `explore-log.md` (VIBE), más `methodology-map.md`, `adr.md`, `closeout.md`,
`handoff.md`, `state.md`, `plan.md` y `assessment.md`, comunes a todos.

## Uso

- Al clasificar un encargo o módulo: `abm methodology classify` (entrada estructurada o texto libre).
- Al construir: el agente sigue el flujo del modo asignado en `methodology-map.md`.
- Al cerrar una unidad: el `closeout.md` sincroniza intención/spec/contrato/código (`/methodology/drift.md`).
