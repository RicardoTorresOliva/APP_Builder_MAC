---
type: Reference
title: Estándares de ABM — índice
description: Mapa de standards/ — qué contiene, cuándo se carga cada archivo y quién lo usa.
tags: [estandares, calidad, indice]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Estándares — índice

`standards/` es la fuente de verdad de calidad técnica de todo ADS. Se carga por ruta o por tarea,
nunca completo: cada skill o comando indica qué archivo abrir. Sigue AGENTS.md regla 9 (OKF) y
regla 7 (sin lock-in): categorías, nunca productos.

## Paridad Frontend / Backend / Database
Misma forma en `standards/frontend/`, `standards/backend/`, `standards/database/`:

| Archivo | Contenido | Lo usa |
|---|---|---|
| `README.md` | índice y alcance de la capa | quien entra por primera vez |
| `standard.md` | el estándar (qué se construye y cómo) | skill builder de la capa |
| `checklist-dod.md` | Definition of Done, casillas verificables | quien cierra la FU/DU |
| `review-criteria.md` | qué mira el revisor, severidades | `review`, revisor independiente |
| `testing.md` | qué tests, qué cubren, cuándo corren | `test-strategy`, CI |

## Transversales
| Ruta | Cuándo se carga |
|---|---|
| `standards/security/` | toda superficie web/API (`web-api.md`), toda superficie con LLM o agentes (`llm-agentic.md`), toda dependencia externa (`supply-chain.md`) |
| `standards/testing/README.md` | al definir la pirámide de tests y el gate de CI de una unidad |
| `standards/observability/README.md` | al instrumentar logs, trazas y métricas |
| `standards/a11y/README.md` | en cualquier interfaz con usuario humano |
| `standards/agentic/README.md` | al diseñar la superficie que opera un agente externo (CLI, API, MCP) |
| `standards/finops/README.md` | al medir costo y tokens de construcción u operación |
| `standards/communication.md` | protocolo de salida de cualquier agente que construya u opere un ADS |
| `standards/cross-cutting.md` | entornos, CI/CD, feature flags, costo |

## Cómo se carga (contexto mínimo)
1. Identifica la tarea (frontend, backend, database, seguridad, tests…).
2. Abre solo el archivo de esa tarea; usa grep antes de leer completo.
3. El nivel del Contrato ADS activo puede exigir un subconjunto adicional de `checklist-dod.md`.
4. Presupuesto: cada archivo de `standards/**/*.md` ≤ 3200 tokens (`abm token-budget`).

## Verificación
`./abm okf validate standards`, `./abm lint core`, `./abm token-budget -v`, `./abm links`.
