---
type: ADR
title: "ADR 0015 — Protocolo de salida"
description: Comunicación concreta y verificable de todo agente que opere ABM o construya un ADS.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0015 — Protocolo de salida

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto

El usuario pide que el agente no converse: acciones y medidas concretas.

## Decisión

- Sección breve en `AGENTS.md` (prohibiciones y formato) + `standards/communication.md` con ejemplos.
- **Semáforo por acción:** `[verde]` sin anuncio; `[amarillo]` una línea antes (qué, por qué, cómo se deshace); `[rojo]` bloqueante, tres líneas máximo.
- **Formato de reporte** fijo (≤ 12 líneas) al cerrar una unidad o fase; cada playbook trae su `## Reporte`.
- **Cumplimiento mecánico:** `abm lint playbooks` exige secciones, semáforo en cada paso y plantilla ≤ 12 líneas.
- En operación, los agentes de un ADS heredan la brevedad salvo que el brief pida otro tono.

## Consecuencias

- La verbosidad en tiempo real no es lintable: se mide en los recorridos de la Fase 4.

## Alternativas descartadas

- Solo una instrucción de estilo: no verificable.
