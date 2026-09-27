---
type: Progress
title: Progreso de la repotenciación de ABM
description: Estado vivo de la ejecución del prompt maestro v3 (modo TURBO) para sobrevivir a la compactación de contexto.
tags: [abm, progreso, turbo]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:44:18Z }
---

# Progreso — repotenciación ABM (prompt maestro v3, modo TURBO)

## Estado

- **Fase actual:** 3 — Implementación por WU (TURBO).
- **Rama:** `claude/jolly-davinci-m2wcju`.
- **Próximo paso:** integrar WU5 (comandos, roles, skills), WU9/10 (stacks), WU11 (integraciones); luego WU2 `sync` real, WU14 manual, WU15 ejemplo + CI, WU16 docs, Fase 4.

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
- D-002: ADR 0001–0016 aceptados (docs/adr/).
- D-003: plantillas turbo de permisos en adapters/turbo/; solo se instalan con `abm sync --apply-turbo` (no se alteran permisos activos sin decisión humana).
- D-004: Cursor lee AGENTS.md nativo; el puntero `.cursor/rules/app-builder.md` (formato ignorado por Cursor) se elimina.

## WU

| WU | Estado | Commit |
|---|---|---|
| Fase 0 | hecho | a390856 |
| Fase 1 | hecho | 6ce0b0b |
| Fase 2 | hecho | 8a302e1 |
| WU1 núcleo | hecho | 724de65 |
| WU3 contrato | hecho | 79656a7 |
| WU6 estándares | hecho | d213440 |
| WU4 metodología | hecho | 0ab84bd |
| WU8 System One | hecho | 038f75a |
| WU12 tokens | hecho | 2ea3b50 |
| WU13 cola | parcial (falta turbo en sync y lint) | ecf1a24 |
| WU7 superficie agéntica | hecho | 99fc17f |
| WU2, WU5, WU9, WU10, WU11, WU14–16 | en curso | — |

## Consumo de tokens (estimado)

| Fase/WU | Tokens | Fuente |
|---|---|---|
