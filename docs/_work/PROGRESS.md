---
type: Progress
title: Progreso de la repotenciación de ABM
description: Estado vivo de la ejecución del prompt maestro v3 (modo TURBO) para sobrevivir a la compactación de contexto.
tags: [abm, progreso, turbo]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:11:41Z }
---

# Progreso — repotenciación ABM (prompt maestro v3, modo TURBO)

## Estado
- **Fase actual:** 1 — Análisis (solo lectura).
- **Rama:** `claude/jolly-davinci-m2wcju`.
- **Próximo paso:** consolidar diagnóstico, benchmark e investigación agéntica → Fase 2.

## Línea base (antes)
| Métrica | Valor | Fuente |
|---|---|---|
| Tokens siempre cargados (Claude Code: AGENTS.md + CLAUDE.md + 4 archivos "always load") | ≈ 3 697 (14 791 caracteres / 4) | medición local |
| `AGENTS.md` | 169 líneas, ≈ 2 482 tokens | medición local |
| Comandos (playbooks) | 6 | `commands/` |
| Herramientas con adaptador | 4 (Claude Code, Cursor, Antigravity, Hermes) | `adapters/` |
| Checks de CI activos | 0 (4 en un ejemplo no instalado: `ci/app-builder-gates.yml`) | `ci/` |
| Documentos `.md` sin frontmatter OKF | 18 de 53 | medición local |
| Capacidades agénticas (MCP, CLI `--json`, manifiesto) | 0 (solo skill de Hermes) | `adapters/hermes/` |
| Espacio de tokens | tabla manual `docs/run_metadata.md` | `docs/` |

## Decisiones tomadas
- D-001: MODO TURBO; el plan se publica y su aprobación queda en PENDIENTES (P-001).

## WU
| WU | Estado | Commit |
|---|---|---|
| Fase 0 | hecho | — |

## Consumo de tokens (estimado)
| Fase/WU | Tokens | Fuente |
|---|---|---|
