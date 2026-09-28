---
type: Reference
title: Plantillas de ABM — índice
description: Qué plantilla usar según el modo metodológico y el momento del ciclo de vida.
tags: [template, indice, metodologia]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Plantillas

Cada plantilla trae frontmatter OKF con placeholders (`generated.by: human:tu-id`, `status: draft`);
al usarla, reemplaza el frontmatter con los valores reales del documento que produces.

## Por modo metodológico

| Modo | Plantilla(s) |
|---|---|
| VIBE | `/templates/explore-log.md` |
| IDD | `/templates/intent.md` |
| SDD | `/templates/spec/requirements.md`, `/templates/spec/design.md`, `/templates/spec/tasks.md` |
| SPDD | `/templates/prompt-contract.md` |
| AIDD | `explore-log.md` → `intent.md` o el trío de `spec/` |

Detalle de cada modo: `/methodology/README.md`.

## Comunes a todo ADS

| Plantilla | Cuándo se usa |
|---|---|
| `/templates/plan.md` | Al planificar, antes del Planning Gate |
| `/templates/methodology-map.md` | Salida de `abm methodology classify`, mezcla por módulo |
| `/templates/adr.md` | Decisión de diseño no trivial dentro de una unidad |
| `/templates/closeout.md` | Al cerrar una FU/DU |
| `/templates/handoff.md` | Traspaso entre agentes o sesiones |
| `/templates/state.md` | Memoria compacta del proyecto, al cerrar sesión |
| `/templates/assessment.md` | Inventario brownfield, comando `assess` |

## Otras plantillas del núcleo (no en este directorio)

`templates/agentic/` y `templates/command-playbook.md` cubren superficie agéntica y la estructura de un
playbook de `commands/`; existen o existirán como parte de otras unidades de trabajo del núcleo.
