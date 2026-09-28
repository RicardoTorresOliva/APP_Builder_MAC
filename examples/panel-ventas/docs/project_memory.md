---
type: Project Memory
title: Memoria del proyecto — panel de ventas
description: Estado vigente del ADS panel-ventas para retomar el trabajo en una sesión nueva (session-start).
tags: [memoria, estado, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:10:24Z }
---

# Memoria del proyecto

| Campo | Valor |
|---|---|
| active_profile | `software-app` (contrato `extendido`) |
| Ceremonia / modo | `producto` / turbo |
| Metodología | SDD en `auth`, `ventas` y `dashboard` ([mapa](../planning/methodology-map.md)) |
| Stack | Python 3.9+ solo biblioteca estándar + SQLite + HTML/CSS/SVG ([D-001](decision_log.md)) |
| Estado | M1 y M2 completados ([tracker](../implementation/task_tracker.md)) |
| Pendientes abiertos | 5 (`./abm pending list`): dimensiones metodológicas, confirmar stack, revisión humana de auth, review independiente, aprobar plan |
| Riesgos residuales | ver [work log](work_log.md) |

## Retomar

1. `./abm pending list` y resuelve lo que la persona responda (`./abm pending resolve P-00N --answer "..."`).
2. `./run_checks.sh` debe seguir en verde antes de tocar nada.
3. Próximo paso sugerido: review independiente de M1/M2 (P-004) y revisión humana de auth (P-003).
