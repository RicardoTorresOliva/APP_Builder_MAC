---
type: Template
title: plan.md — plan de construcción
description: FU/DU por milestone con criterios de aceptación; base del Planning Gate y de start-execution.
tags: [template, plan, fu, du]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Plan: `<ADS>`

Perfil: `<profiles/<name>>` · Ceremonia: `<prototipo|mvp|producto|enterprise-regulado>`
(`/methodology/ceremony.md`). Este plan se aprueba (Planning Gate, `/docs/adr/0014-turbo-y-pendientes.md`)
antes de `start-execution`; en `turbo`, la aprobación se acumula en la cola y lo reversible avanza.

## Milestone 1 — `<nombre>`

### FU-01 — `<nombre de la Foundation Unit>`

- Modo: `<VIBE|IDD|SDD|SPDD|AIDD>` (`methodology-map.md`)
- Qué entrega: `<base sin salida consumible directa>`
- Criterio de aceptación: `<verificable>`

### DU-01 — `<nombre de la Deliverable Unit>`

- Modo: `<...>`
- Qué entrega: `<algo que un consumidor usa de punta a punta>`
- Criterio de aceptación: `<verificable, incluye estados vacíos y de error>`
- Depende de: `FU-01`

<!-- Repetir FU-NN / DU-NN por milestone. Las FU van antes que las DU que dependen de ellas. -->

## Milestone 2 — `<nombre>`

`<...>`

## Revisión entre milestones

Tras cada milestone: `review` con un revisor independiente (contexto limpio, nunca quien construyó).

## Riesgos conocidos al planificar

- `<riesgo>` → `<cómo se mitiga o por qué se acepta>`
