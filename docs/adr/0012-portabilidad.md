---
type: ADR
title: "ADR 0012 — Portabilidad corporativa"
description: Gateway LLM, matriz multinube y estrategia legacy.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0012 — Portabilidad corporativa

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Los ADS deben adaptarse a stacks corporativos existentes, soportar varios proveedores LLM y nubes, y escalar.

## Decisión
- **Gateway LLM (categoría):** la interfaz de chat compatible (el formato de facto que exponen la mayoría de gateways y proveedores) como lingua franca; proveedor y modelo por configuración (`.env`), sin tocar código. Matriz de capacidades con fecha en `stacks/llm-providers.md`.
- **Multinube:** matriz de equivalencias por bloque en `stacks/clouds.md`; IaC como categoría; contenedores y 12-factor; todo servicio propietario lleva abstracción o plan de salida (`portability.exit_plan`).
- **Legacy:** comando `assess` inventaría el stack existente en OKF; catálogo de patrones (strangler fig, anti-corruption layer, fachada API, CDC/eventos, batch/SFTP/EDI; RPA solo como último recurso) en `stacks/legacy.md`.
- **Escalabilidad:** checklist en `standards/backend/` y `standards/database/` (sin estado, caché, colas, réplicas, multi-tenant, pruebas de carga, SLO y costo por unidad).

## Consecuencias
- El encargo (f) de la Fase 4 debe resolverse solo con estos artefactos.

## Alternativas descartadas
- Elegir un proveedor o nube por defecto: viola la regla 7 y el HITL de stack.
