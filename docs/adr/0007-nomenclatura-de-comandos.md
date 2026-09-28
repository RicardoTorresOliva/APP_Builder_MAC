---
type: ADR
title: "ADR 0007 — Nomenclatura de comandos"
description: Nombres de comandos y política de alias.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0007 — Nomenclatura de comandos

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto

El prompt siembra ~36 comandos. Hay colisión entre `contract` (SPDD) y "Contrato ADS".

## Decisión

- Nombres en inglés, kebab-case, verbo o sustantivo corto. Se conservan los 6 existentes sin cambios.
- `contract` → **`prompt-contract`**; la verificación del Contrato ADS es **`ads-check`**.
- Catálogo (36): arranque `bootstrap`, `doctor`, `session-start`, `help`, `pending` · descubrir/definir `init-project`, `assess`, `methodology`, `intent`, `spec`, `prompt-contract`, `plan`, `stack`, `explore`, `consolidate` · construir `start-execution`, `ui`, `api`, `db`, `connect`, `decide`, `integrate`, `test` · asegurar `review`, `security`, `drift`, `perf`, `a11y`, `ads-check` · medir `tokens` · entregar e iterar `deploy`, `release`, `closeout`, `iterate`, `fix`, `refactor`.
- **Alias en español** solo en el manual y en `help` (p. ej., "pendientes" → `pending`); no se generan archivos duplicados (evita ruido en menús y tokens).

## Consecuencias

- La CI verifica que cada comando tenga página de manual y viceversa (`abm lint manual`).

## Alternativas descartadas

- Comandos en español: rompe la convención de las herramientas y duplica el catálogo.
