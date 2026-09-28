---
type: Reference
title: APP_Builder_MAC (ABM) v5
description: Fábrica agent-native de Activos Digitales SLG (ADS), neutral de herramienta y de modelo; punto de entrada del repo.
tags: [abm, readme]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:13Z }
---

# APP_Builder_MAC (ABM) v5

ABM es una **fábrica**: guía a agentes de IA (Claude Code, Codex, Antigravity, Copilot, Cursor, Gemini CLI, Windsurf, Kiro, Hermes y cualquier lector de `AGENTS.md`) para producir **ADS — Activos Digitales SLG**: apps web y móviles, APIs, dashboards, ERPs, automatizaciones, apps con IA, informes y productos de datos.

Todo ADS nace **agent-native** (operable por otros agentes vía MCP, CLI `--json`, skill y `llms.txt`), con **espacio de tokens** (ledger, reporte y dashboard), **portable** (stacks corporativos y legacy, varios proveedores LLM y nubes) y construido en **modo turbo** con comunicación concreta.

## Empieza aquí

1. **Primeros 15 minutos:** `docs/manual/primeros-15-minutos.md`.
2. Comprueba el entorno: `./abm doctor` (Windows: `abm.cmd doctor`). Requisitos: Python 3.9+ y git.
3. Describe tu encargo en `START_PROJECT.md` y ejecuta `init-project` en tu herramienta.
4. O crea un ADS limpio: `./abm new-ads ../mi-ads --id mi-ads --name "Mi ADS" --profile software-app`.

## Qué hay dentro

| Pieza | Dónde |
|---|---|
| Gobernanza única (turbo, bloqueantes, protocolo de salida) | `AGENTS.md` |
| 36 comandos (playbooks) y su manual | `commands/`, `docs/manual/` |
| Skills (Agent Skills) y 13 roles | `skills/`, `agents/` |
| Motor metodológico (VIBE, IDD, SDD, SPDD, AIDD) | `methodology/`, `templates/` |
| Estándares FE/BE/DB, seguridad, tests, agentes, finops | `standards/` |
| Catálogo de stacks, nubes, LLMs y legacy | `stacks/` |
| MCP, APIs, Hermes, A2A, capa System One (Jev), observabilidad | `integrations/` |
| Contrato ADS y OKF v0.2 | `contract/`, `okf/`, `ads.yaml` |
| CLI `abm` (Python, sin dependencias) y servidor MCP | `scripts/`, `./abm`, `abm.cmd` |
| Adaptadores generados por herramienta | `./abm sync` → ver `adapters/README.md` |
| Decisiones y análisis | `docs/adr/`, `docs/analysis/` |
| Mapa completo del repo | `index.md` (generado) |

## Órdenes clave del CLI

`./abm check` (todos los validadores) · `./abm sync` · `./abm ads-check` · `./abm agent-conformance` · `./abm methodology classify` · `./abm decide` · `./abm tokens report|dashboard|budget` · `./abm pending list` · `./abm mcp`. Todas con `--json`; las que escriben, con `--dry-run`.

## Documentos del proyecto

`CHANGELOG.md` · `MIGRATION.md` (de v4.1 a v5) · `CONTRIBUTING.md` · `SECURITY.md` · `LICENSE`.
