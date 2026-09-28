---
type: Pending Queue
title: Cola de pendientes
description: Decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado.
tags: [turbo, pendientes]
status: draft
generated: { by: process:abm-pending, at: 2026-09-28T00:07:52Z }
---

# Cola de pendientes

Cada ítem ya tiene su default aplicado. Responde solo si quieres cambiarlo (`abm pending resolve P-00N --answer "..."`).

| ID | Tipo | Contexto | Default aplicado | Alternativa | Impacto si no se responde | Estado |
|---|---|---|---|---|---|---|
| P-001 | decisión | Metodología: 5 dimensiones con confianza 0 (incertidumbre, horizonte, equipo, brownfield, autonomía) | 1, 1, 0, 0, 1 (defaults del router) | otro nivel 0–2 por dimensión | podría cambiar el modo de dashboard (no el de auth) | abierto |
| P-002 | decisión | Stack: stdlib Python + SQLite + HTML/SVG por la restricción 'sin instalar nada' | aplicado (docs/decision_log.md D-001) | opciones B o C del decision_log | migrar según docs/exit-plan.md | abierto |
| P-003 | revisión | Revisión humana del módulo auth (SDD, disparador auth) | tests de auth en verde; sin revisión humana aún | — | no publicar fuera de localhost sin esta revisión | abierto |
| P-004 | revisión | Review independiente de M1 y M2 con contexto limpio (start-execution paso 5) | no ejecutado en el ejemplo | — | hallazgos no detectados por quien construyó | abierto |
| P-005 | aprobación | Aprobar plan (init-project paso 12, turbo) | ejecución reversible en local | checkpoint | ninguno mientras siga en local | abierto |
