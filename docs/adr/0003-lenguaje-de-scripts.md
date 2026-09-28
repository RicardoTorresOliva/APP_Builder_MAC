---
type: ADR
title: "ADR 0003 — Lenguaje de los scripts"
description: El tooling de ABM se escribe en Python 3.9+ solo con biblioteca estándar.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0003 — Lenguaje de los scripts

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto

Los scripts actuales son bash: no corren de forma nativa en Windows. Se necesitan validadores, generador, CLI con `--json` y un servidor MCP.

## Decisión

- **Python ≥ 3.9, solo biblioteca estándar.** Paquete `scripts/abmkit/`, entrada `scripts/abm.py`.
- Lanzadores: `./abm` (macOS/Linux) y `abm.cmd` (Windows) en la raíz.
- YAML: parser propio del subconjunto usado (`abmkit/yamlmini.py`), con resultados idénticos en todas las plataformas (las fechas quedan como texto).
- Toda orden admite `--json` (salida para agentes) y, si escribe, `--dry-run`.
- Los `.sh` antiguos se conservan como shims que llaman a `abm` (compatibilidad; ver `MIGRATION.md`).

## Consecuencias

- Requisito único: Python 3.9+ (lo verifica `abm doctor`).
- Sin dependencias externas: nada que instalar ni auditar en la cadena de suministro del tooling.

## Alternativas descartadas

- Bash: sin Windows nativo.
- Node.js: necesita paquetes de npm para YAML y tampoco viene preinstalado.
- Binario compilado: opaco para un vibe coder y exige pipeline de build.
