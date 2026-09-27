---
type: ADR
title: "ADR 0005 — Estándar de skills"
description: Las skills siguen Agent Skills (agentskills.io) y se distribuyen a cada herramienta por generación.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0005 — Estándar de skills

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Agent Skills es el estándar abierto adoptado por decenas de herramientas (ver 02-benchmark). Su validador de referencia marca claves de frontmatter no estándar.

## Decisión
- Fuente: `skills/<name>/SKILL.md` con `name` (= carpeta, kebab-case, ≤ 64) y `description` (≤ 1024, dice qué hace y cuándo usarla), `license` opcional y `metadata` (`okf_type: Skill`, `abm_version`).
- Cuerpo corto (presupuesto de tokens); el detalle va en `references/` y se carga bajo demanda.
- **Skills ≠ comandos.** Comando = playbook que invoca el usuario. Skill = capacidad que el agente activa por su descripción (p. ej., `okf-author`, `ui-builder`, `api-design`, `db-design`, `integrate-safely`, `token-ledger`, `system-one`, `operate-abm`).
- `abm sync` copia las skills a las rutas de cada herramienta (`.claude/skills/`, `.agents/skills/`, etc., según `docs/compat-matrix.md`).

## Consecuencias
- Una skill se escribe una vez y llega a todas las herramientas que soportan el estándar.

## Alternativas descartadas
- Añadir `type:` de primer nivel para OKF: rompe validadores de Agent Skills.
