---
type: Task Tracker
title: Task tracker — panel de ventas
description: Estado de las FU y DU del panel de ventas por milestone (start-execution).
tags: [tracker, unidades, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:42Z }
---

# Task tracker

Orden de ejecución: FU primero, luego DU por milestone ([unidades](user_units.md)).

## M1 — Base (FU)

| Unidad | Tipo | Estado | Evidencia |
|---|---|---|---|
| FU-01 | FU | completed | `test_db`: 11 tests OK; `compileall` OK |
| FU-02 | FU | completed | `test_auth`: 8 tests OK; auth en `test_api` OK |
| FU-03 | FU | completed | `ads-check` sin errores (nivel extendido) |

## M2 — Entregables (DU)

| Unidad | Tipo | Estado | Evidencia |
|---|---|---|---|
| DU-01 | DU | completed | `test_api`: permisos por rol, CSRF, 422, idempotencia, borrado auditado |
| DU-02 | DU | completed | navegador sin errores de consola; claro, oscuro, vacío y móvil verificados |
| DU-03 | DU | completed | `test_mcp` (6 tests) y `agent-conformance` OK |

Review independiente por milestone: pendiente (P-004), ver [work log](../docs/work_log.md).
