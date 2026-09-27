---
type: ADR
title: "ADR 0011 — Capa System One (Jev)"
description: Interfaz de decisión tipada con confianza, primer adaptador Jev y fallback obligatorio.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0011 — Capa System One (Jev)

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Jev (TypeSafe AI) devuelve decisiones tipadas (choice, score, noul) con probabilidades; está en early access (ver 03-investigacion-agentica). No es un modelo para programar.

## Decisión
- **Interfaz neutral** `decide(state, questions) → answers` con tipos `choice`, `score` y `boolean` (Noul). Cada respuesta: valor, probabilidades y confianza; para `boolean`, confianza = |2p − 1|.
- **Cadena de proveedores** configurable (`abm.yaml → decision.providers`): `typesafe-jev` (HTTP, `TYPESAFE_API_KEY`) → `llm` (endpoint compatible con la interfaz de chat estándar, salida JSON) → `rules` (determinista, offline). Se usa el primero disponible; ante error, el siguiente.
- **Routing por confianza** (`integrations/decision/thresholds.yaml`): actuar ≥ 0,85 (Enterprise-Regulado ≥ 0,92); zona gris ≥ 0,60 → LLM o cola; menor → humano.
- **Usos en ABM:** inferencia de dimensiones del router, semáforo de riesgo, filtro de prompt injection, triage de revisión y sugerencia de comando.
- **Datos:** sin datos personales hacia proveedores externos salvo que el perfil lo permita; consumo al ledger (`provider-usage`).

## Consecuencias
- ABM funciona igual sin Jev; la calidad del fallback `rules` es `no-verificado` para texto libre.

## Alternativas descartadas
- Depender solo de Jev: early access y proveedor único.
