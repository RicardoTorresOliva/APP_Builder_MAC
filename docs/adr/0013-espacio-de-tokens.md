---
type: ADR
title: "ADR 0013 — Espacio de control de tokens"
description: Ledger, fuentes, niveles de dashboard y presupuestos.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0013 — Espacio de control de tokens

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Solo existía una tabla manual por milestone. OTel GenAI está en estado "Development".

## Decisión
- **Evento** (`contract/token-event.schema.json`): `ts`, `phase` (build/run), `source` (telemetry/provider-usage/estimate), tokens de entrada/salida/caché, proveedor, modelo, herramienta, actor, unidad, comando, funcionalidad, tenant, costo. Mapeo 1:1 a atributos `gen_ai.*`.
- **Ledger** JSONL en la ruta de `ads.yaml → tokens.ledger` (por defecto `ops/tokens/ledger.jsonl`).
- **Precios** en `integrations/observability/pricing.yaml` con fuente y fecha; sin precio, el costo es "n/d" (nunca inventado).
- **Niveles:** N1 `TOKENS.md` (`abm tokens report`); N2 HTML estático (`abm tokens dashboard`); N3 guía de pipeline OTel hacia la pila de observabilidad elegida.
- **Presupuestos** (`ads.yaml → tokens.budgets`): umbral blando → cola; tope duro → bloqueante (`abm tokens budget` falla).
- **Cifras oficiales** como concepto OKF `Attested Computation` con atestador determinista (`abm tokens attest`).
- Expuesto a agentes: recurso MCP `abm://tokens/summary`.

## Consecuencias
- Toda WU y todo DU registran su consumo (medido o `estimate`).

## Alternativas descartadas
- Solo telemetría de la herramienta: no existe en todas; el estimado explícito es mejor que nada.
