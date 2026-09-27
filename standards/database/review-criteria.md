---
type: Reference
title: Criterios de revisión — database
description: Qué mira el revisor independiente de datos y con qué severidad.
tags: [database, revision, severidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Criterios de revisión — database

El revisor usa un contexto limpio (nunca quien construyó, AGENTS.md §Unidades de trabajo).

## Bloqueante

- Migración sin camino de reversión y sin justificación documentada.
- Tabla multi-tenant sin RLS ni control de acceso equivalente: fuga de datos entre tenants.
- Dato personal sin clasificar, o sin política de retención, en una tabla nueva.
- Backup no probado en un ADS que ya está en operación.

## Mayor

- Falta índice en una columna usada por una consulta frecuente y el plan de ejecución lo muestra.
- Seed no idempotente: correrlo dos veces duplica filas o rompe.
- Cambio sobre dato sensible sin quedar auditado.
- Tipos de aplicación mantenidos a mano en paralelo al esquema (riesgo de drift).

## Menor

- ERD desactualizado respecto al esquema real, sin afectar la operación.
- Nombre de tabla/columna inconsistente con la convención del ADS.
- Desnormalización sin comentario que explique el motivo.

## Evidencia esperada

Diff de la migración con su reversión ejecutada, plan de ejecución (`EXPLAIN` o equivalente) de la
consulta crítica, y resultado de los tests de migraciones y de datos.
