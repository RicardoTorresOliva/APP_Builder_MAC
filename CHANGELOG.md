---
type: Changelog
title: Changelog de ABM
description: Cambios por versión de APP_Builder_MAC según versionado semántico.
tags: [changelog, versiones]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:53Z }
---

# Changelog

Formato: versionado semántico (MAJOR.MINOR.PATCH). Detalle de migración: `MIGRATION.md`.

## [5.0.0] — 2026-09-27

### Añadido

- **ADS y Contrato ADS**: `ads.yaml`, niveles mínimo/extendido, `abm ads-check` y `abm agent-conformance` (ADR 0001, 0009).
- **Superficie agéntica**: servidor MCP de ABM (stdio, protocolo 2025-11-25), skill `operate-abm`, `llms.txt`, plantillas agénticas para ADS y `abm new-ads` (ADR 0010).
- **CLI `abm`** multiplataforma en Python sin dependencias, con `--json` y `--dry-run` (ADR 0003).
- **Generador de adaptadores** `abm sync` para 9 herramientas + fallback `AGENTS.md`, con `--check` en CI (ADR 0002).
- **Motor metodológico** VIBE/IDD/SDD/SPDD/AIDD con router, mezcla por módulo y niveles de ceremonia (ADR 0006).
- **Capa System One** (`abm decide`): Jev de TypeSafe AI → LLM → reglas, con routing por confianza (ADR 0011).
- **Espacio de tokens**: ledger JSONL, reporte N1, dashboard N2, guía N3 OpenTelemetry, presupuestos y atestación (ADR 0013).
- **Modo turbo** y cola de pendientes (`abm pending`) (ADR 0014); **protocolo de salida** verificado por lint (ADR 0015).
- 36 comandos, 13 roles, 18 skills, estándares FE/BE/DB con paridad, catálogo de 14 stacks + nubes, LLMs y legacy, guías de integraciones, manual para no programadores.
- Perfiles `api-service` y `automation-integration`.
- CI multiplataforma y tests del CLI.

### Cambiado

- **OKF v0.2** (Google Cloud) en todo documento con el perfil ABM (ADR 0004).
- `AGENTS.md` reescrito en español (ADR 0008): turbo, bloqueantes, protocolo de salida, regla de salida de tools como dato.
- Perfiles traducidos y con `ads_contract_level`.

### Eliminado

- Copias manuales de adaptadores (`adapters/claude-code`, `adapters/cursor`, `adapters/antigravity`) y el puntero `.cursor/rules/app-builder.md` (Cursor ignora `.md` en esa ruta y ya lee `AGENTS.md`).

## [4.1.0]

- Gobernanza neutral en `AGENTS.md`, perfiles de activo componibles, FU/DU, 6 playbooks, scripts bash.
