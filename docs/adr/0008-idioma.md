---
type: ADR
title: "ADR 0008 — Idioma"
description: Idioma de la documentación, los playbooks y los identificadores.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0008 — Idioma

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
El núcleo estaba en inglés y la guía en español formal (usted): inconsistente para el usuario.

## Decisión
- **Español neutro, tuteo**, en todo lo que lee una persona: `AGENTS.md`, playbooks, estándares, manual, guías, salida del CLI.
- Términos técnicos estándar en inglés (spec, commit, deploy, token, prompt injection…).
- Identificadores en inglés: nombres de archivos, comandos, claves de frontmatter y de YAML.

## Consecuencias
- El español cuesta más tokens que el inglés; se compensa con un `AGENTS.md` más corto y con carga bajo demanda (presupuestos en CI).

## Alternativas descartadas
- Núcleo en inglés: más barato en tokens, pero el usuario objetivo lee español.
