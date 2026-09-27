---
type: Pending Queue
title: Cola de pendientes
description: Decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado.
tags: [abm, turbo, pendientes]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:11:41Z }
---

# Cola de pendientes

Cada ítem ya tiene su default aplicado. Responde solo si quieres cambiarlo.

| ID | Tipo | Contexto | Default aplicado | Alternativa | Impacto si no se responde | Estado |
|---|---|---|---|---|---|---|
| P-001 | aprobación | Plan de la repotenciación (Fase 2) | Se ejecuta el plan publicado en `docs/analysis/04-plan.md` | Pausar y ajustar el plan | Ninguno: todo está en la rama y es reversible | abierto |
| P-002 | decisión | Alinear `conocimiento/` de AGE_Builder a OKF v0.2 (fuera de este repo) | No se toca AGE_Builder | Abrir una tarea en ese repo | La interoperabilidad se mantiene (v0.2 acepta v0.1) | abierto |
| P-003 | decisión | Licencia definitiva de ABM (hoy: todos los derechos reservados, SLG) | Propietaria SLG en LICENSE y en las skills | MIT o Apache-2.0 si se publica | Nadie externo puede reutilizar ABM | abierto |
| P-004 | revisión | Presupuesto blando superado en Fase-1 (≈936 k) y WU5 (≈417 k tokens); sin tope duro | Continuar; investigación y 36 playbooks justifican el consumo | Reducir alcance de investigación en futuras WU | Ninguno inmediato | abierto |
