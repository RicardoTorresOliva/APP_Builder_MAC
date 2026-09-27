---
name: operate-abm
description: Cómo cualquier agente externo (CLI de agentes, IDE con agente, orquestador) opera ABM directamente — CLI `./abm` con --json, servidor MCP `abm mcp` y sus tools abm_*, cola de pendientes y tokens. Actívala cuando el agente vaya a ejecutar una orden de ABM, verificar antes de terminar una unidad, o cuando otro agente pregunte cómo trabajar con este repo. Es la skill operate-abm que el Contrato ADS exige para el propio ABM.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# operate-abm

ABM es un CLI de Python sin dependencias: `./abm <orden>` (Windows: `abm.cmd`). Toda orden admite
`--json` (salida máquina) y, si escribe, `--dry-run` (informa qué haría sin tocar disco).

## Al empezar una sesión
1. `./abm session-start` (o lee `docs/project_memory.md` + `implementation/task_tracker.md`) para
   saber dónde retomar.
2. `./abm doctor` si algo del entorno falla.
3. `./abm pending list` para ver la cola antes de decidir un default por tu cuenta.

## Órdenes que usarás seguido
- `okf validate [rutas]` / `okf index` — conformidad OKF y mapa del repo.
- `check` — auditoría agregada (usar antes de cerrar una unidad).
- `lint core|playbooks|manual` — regla 7 (sin productos), estructura de playbooks, paridad manual.
- `token-budget [-v]` — presupuesto de tokens por archivo.
- `links` — enlaces internos rotos.
- `methodology classify` — clasifica encargo/módulo para el `methodology-map.md`.
- `decide` — capa System One (choice/score/boolean con confianza y fallback).
- `tokens record|estimate|report|dashboard|budget|attest` — espacio de tokens.
- `pending list|add|resolve` — cola de pendientes en modo turbo.
- `ads-check` / `agent-conformance` — Contrato ADS, estático y dinámico.
- `sync [--check] [--apply-turbo]` — genera adaptadores por herramienta.
- `secrets` — barrido de secretos antes de commitear o entregar.

Cada orden imprime líneas terse por defecto; con `--json` devuelve un objeto `{ ...datos, findings
o rows }`. Confía en su salida — no la repitas a mano ni la reinterpretes en prosa larga.

## Servidor MCP
`./abm mcp` levanta un servidor stdio con una tool por orden, nombrada `abm_<orden>` con guiones
bajos (`abm_okf_validate`, `abm_ads_check`, `abm_tokens_report`, `abm_pending_list`,
`abm_methodology_classify`, `abm_decide`, `abm_agent_conformance`…). Las tools de escritura traen
`dry_run=true` por defecto — pásalo en `false` explícito solo cuando de verdad quieras escribir.
Recurso de solo lectura: `abm://tokens/summary`. Prefiere el servidor MCP sobre invocar el CLI por
shell cuando tu cliente ya habla MCP: evita parsear texto y respeta mejor el mínimo privilegio.

## Antes de terminar cualquier unidad
Corre `./abm check`; si tocaste `.md` del núcleo, además `okf validate`, `lint core`,
`token-budget -v` y `links` sobre tus rutas. Corrige hasta que todo pase. Registra el consumo con
`tokens record` (o `estimate` si no hay medición) antes de cerrar el reporte de la unidad.

## Detalle extra
`references/mcp-server.md`: inventario completo de tools `abm_*`, sus hints y un flujo de ejemplo.
