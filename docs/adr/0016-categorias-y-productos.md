---
type: ADR
title: "ADR 0016 — Categorías en el núcleo, productos en catálogos"
description: Reconciliación de la regla 7 con los productos que el prompt exige (Jev, Hermes, nubes, stacks).
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0016 — Categorías en el núcleo, productos en catálogos

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
La regla 7 prohíbe nombrar productos en el núcleo; el prompt pide integrar Jev, Hermes, AWS, Azure y un catálogo de stacks.

## Decisión
- **Núcleo** (sin productos): `AGENTS.md`, `commands/`, `methodology/`, `standards/`, `profiles/`, `contract/`, `templates/`, `agents/`, `skills/`, `okf/`.
- **Catálogos** (productos permitidos, con fecha de revisión): `adapters/`, `integrations/`, `stacks/`, `examples/`, `docs/` (manual, compat-matrix, análisis, guías).
- **`abm lint core`** busca nombres de productos (lista en `abm.yaml → lint.products`) en el núcleo y falla la CI.
- Los estándares abiertos (OKF, MCP, A2A, OpenAPI, OAuth, WCAG, OpenTelemetry, RFC) no son productos y se permiten en el núcleo.

## Consecuencias
- El núcleo dice "modelo de decisión tipada"; `integrations/decision/typesafe-jev.md` dice "Jev".

## Alternativas descartadas
- Relajar la regla 7: reintroduce lock-in en la gobernanza.
