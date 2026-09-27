---
type: ADR
title: "ADR 0010 — Superficie agéntica"
description: Protocolos por los que un agente externo descubre y opera un ADS.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0010 — Superficie agéntica

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Hermes (y el resto) carga `AGENTS.md`, usa skills del estándar y consume MCP (ver 03-investigacion-agentica). MCP estable más desplegado: `2025-11-25`; existe `2026-07-28` (sin estado).

## Decisión
- **Todo ADS:** `ads.yaml`, `AGENTS.md`, skill `operate-<id>` (copiada por `sync` a `.agents/skills/` y equivalentes), `llms.txt`, índice OKF.
- **Extendido:** servidor MCP (stdio siempre; Streamable HTTP para servicios desplegados), protocolo base **2025-11-25** y tolerancia a clientes que pidan `2026-07-28`; tools con `readOnlyHint`/`destructiveHint` correctos y descripciones cortas; CLI `--json`/`--dry-run`; OpenAPI para APIs HTTP; errores `application/problem+json` (RFC 9457); webhooks firmados; log de auditoría.
- **A2A** (`/.well-known/agent-card.json`, v1.0) solo si el ADS es o expone un agente.
- **ABM expone su propio servidor MCP** (stdio, biblioteca estándar) sobre el CLI: tools de lectura y `dry-run`, recurso `abm://tokens/summary`. Coste bajo y permite que Hermes conduzca ABM sin parsear texto.
- **`abm agent-conformance`**: cliente MCP propio (stdlib) que ejecuta el guion descubrir → listar → leer → `dry-run` → tokens; si Hermes está instalado, además una prueba `hermes -z`.
- Plantillas en `templates/agentic/` y configuración para Hermes en `integrations/agents/hermes.md`.

## Consecuencias
- Operar cualquier ADS no requiere integración a medida.

## Alternativas descartadas
- Solo `2026-07-28`: demasiado nuevo; rompe servidores existentes.
