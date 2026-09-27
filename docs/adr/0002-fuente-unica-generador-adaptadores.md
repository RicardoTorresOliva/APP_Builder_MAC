---
type: ADR
title: "ADR 0002 — Fuente única y generador de adaptadores"
description: Los adaptadores por herramienta se generan desde fuentes neutrales con `abm sync`.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0002 — Fuente única y generador de adaptadores

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Hoy los adaptadores son copias manuales (`adapters/claude-code/.claude` es idéntico a `.claude/`). Hay que soportar 9 herramientas con formatos distintos (ver `docs/compat-matrix.md`).

## Decisión
- **Fuentes neutrales:** `AGENTS.md`, `commands/*.md`, `skills/<name>/SKILL.md`, `agents/<rol>.md` y `standards/**` (reglas por ruta con `applies_to` en el frontmatter).
- **Registro de herramientas:** `adapters/tools.yaml` declara, por herramienta, qué salidas emite y dónde. El código de cada emisor vive en `scripts/abmkit/sync.py`.
- **`abm sync`** escribe las salidas; **`abm sync --check`** falla en CI si alguna difiere de lo que se generaría.
- Cada archivo generado lleva una marca "GENERADO por abm sync. No editar." (en JSON/TOML, el registro de generados `adapters/.generated.json` lista rutas y hashes).
- Las salidas se versionan en el repo: el proyecto sigue funcionando sin paso de instalación.
- Se eliminan las copias manuales de `adapters/<tool>/`; `install-adapter.sh` pasa a ser un shim de `abm sync --tool` (ver `MIGRATION.md`).
- **Degradación elegante:** si una herramienta no soporta comandos, skills o subagentes, el puntero indica "ejecuta el playbook `commands/<x>.md`".

## Consecuencias
- Añadir una herramienta = una entrada en `tools.yaml` + un emisor.
- Editar un adaptador a mano es un error que la CI detecta.

## Alternativas descartadas
- Symlinks: no funcionan de forma fiable en Windows ni en todas las herramientas.
- Plantillas por herramienta copiadas a mano: es la deuda actual.
