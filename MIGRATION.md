---
type: Migration Guide
title: Migración de ABM v4.1 a v5
description: Equivalencias de todo lo renombrado, movido o eliminado, con alias de compatibilidad.
tags: [migracion, compatibilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:53Z }
---

# Migración de ABM v4.1 a v5

Los proyectos v4.1 siguen funcionando: los scripts antiguos existen como shims y los 6 comandos conservan su nombre.

| v4.1 | v5 | Compatibilidad |
|---|---|---|
| `scripts/check_completeness.sh`, `check_worklog.sh`, `check_doc_sync.sh` | `./abm units` | shims que llaman a `abm units` |
| `scripts/preflight_check.sh` | `./abm preflight` | shim |
| `scripts/detect_platform.sh` | `./abm doctor` | shim (`--json`) |
| `install-adapter.sh <plataforma>` | `./abm sync` | shim (regenera todas las habilitadas) |
| `adapters/claude-code/`, `adapters/cursor/`, `adapters/antigravity/` | salidas generadas por `abm sync` según `adapters/tools.yaml` | se regeneran |
| `.cursor/rules/app-builder.md` | eliminado: Cursor lee `AGENTS.md` nativo | — |
| `adapters/hermes/SKILL.md` (`app-builder`) | skill generada `abm-playbooks` en `.agents/skills/` | — |
| `CLAUDE.md` (puntero en texto) | `CLAUDE.md` generado con `@AGENTS.md` | — |
| `mcps/inventory.md` | `docs/tooling/mcp-inventory.md` | — |
| `skills/inventory.md` | `docs/tooling/skills-inventory.md` | — |
| `docs/run_metadata.md` | ledger (`ops/tokens/ledger.jsonl`) + `TOKENS.md` | se conserva como histórico (`status: deprecated`) |
| frontmatter `timestamp` | `generated: { by, at }` | `abm okf validate` lo señala |
| `status: stub` | `status: draft` + etiqueta `stub` | — |
| convención OKF de `knowledge/README.md` | OKF v0.2 + `okf/PROFILE.md` | v0.2 acepta bundles v0.1 |
| Identity "Quality over speed, always" / "ask the user" | turbo + bloqueantes (ADR 0014) | modo `checkpoint` en `abm.yaml` para el comportamiento anterior |
| "Context pressure signals" (cortar sesión al leer 8 archivos) | carga progresiva + presupuestos + `PROGRESS` | — |
| 6 comandos | 36 comandos | mismos nombres para los 6 |
| Profiles en inglés, `type: asset-profile` | en español, `type: Asset Profile` + `ads_contract_level` | claves de campos sin cambio |

## Pasos para un proyecto v4.1

1. Copia `scripts/`, `abm`, `abm.cmd`, `abm.yaml`, `okf/`, `contract/`, `templates/agentic/`, `adapters/tools.yaml` y el nuevo `AGENTS.md`.
2. `./abm sync` para regenerar adaptadores.
3. `./abm okf validate` y corrige lo que señale (sobre todo `timestamp` y `status: stub`).
4. Crea `ads.yaml` desde `templates/agentic/ads.yaml` y ejecuta `./abm ads-check`.
