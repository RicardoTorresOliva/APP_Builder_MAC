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
| P-001 | aprobación | Plan de la repotenciación (Fase 2) | Se ejecuta el plan publicado en `docs/analysis/04-plan.md` | Pausar y ajustar el plan | Ninguno: todo está en la rama y es reversible | resuelto: aprobado por el humano (2026-09-28); plan ejecutado y fusionado en main (PR #1, dd6b9a3) |
| P-002 | decisión | Alinear `conocimiento/` de AGE_Builder a OKF v0.2 (fuera de este repo) | No se toca AGE_Builder | Abrir una tarea en ese repo | La interoperabilidad se mantiene (v0.2 acepta v0.1) | resuelto: tarea creada en RicardoTorresOliva/AGE_Builder_MAC#1 (alineación de plantilla-arnes/conocimiento/ a OKF v0.2) |
| P-003 | decisión | Licencia definitiva de ABM (hoy: todos los derechos reservados, SLG) | Propietaria SLG en LICENSE y en las skills | MIT o Apache-2.0 si se publica | Nadie externo puede reutilizar ABM | resuelto: propietaria SLG definitiva (decisión humana 2026-09-28); LICENSE sin nota provisional |
| P-004 | revisión | Presupuesto blando superado en Fase-1 (≈936 k) y WU5 (≈417 k tokens); sin tope duro | Continuar; investigación y 36 playbooks justifican el consumo | Reducir alcance de investigación en futuras WU | Ninguno inmediato | resuelto: sustituido por P-008 y P-009 (encolados por abm tokens budget --queue) |
| P-005 | revisión | Hermes en vivo: sin credenciales de LLM no se ejecutó la prueba one-shot (agent-conformance --hermes) | Conformidad verificada con cliente MCP genérico; Hermes no-verificado | Instalar Hermes con credenciales y ejecutar ./abm agent-conformance --hermes | La compatibilidad con Hermes descansa en documentación | abierto |
| P-006 | credencial | Jev real: sin TYPESAFE_API_KEY la capa System One usó el proveedor de reglas | Fallback de reglas activo; Jev no-verificado en vivo | Definir TYPESAFE_API_KEY y repetir ./abm decide --provider typesafe-jev | Sin medición de latencia ni tokens de Jev | abierto |
| P-007 | decisión | Activar permisos turbo en las herramientas (cambia permisos del agente) | No activado: plantillas en adapters/turbo/ | ./abm sync --apply-turbo | El agente pedirá más confirmaciones de las necesarias | abierto |
| P-008 | revisión | Presupuesto blando superado: unit:Fase-1 (936,221 > 400,000) | continuar (sin tope duro) | reducir alcance o cambiar de modelo | más costo | resuelto: aceptado por el humano (2026-09-28); umbral blando de 400 k por unidad se mantiene |
| P-009 | revisión | Presupuesto blando superado: unit:WU5 (417,466 > 400,000) | continuar (sin tope duro) | reducir alcance o cambiar de modelo | más costo | resuelto: aceptado por el humano (2026-09-28); umbral blando de 400 k por unidad se mantiene |
| P-010 | revisión | Presupuesto blando superado: unit:Fase-4 (887,087 > 400,000) | continuar (sin tope duro) | reducir alcance o cambiar de modelo | más costo | resuelto: aceptado por el humano (2026-09-28); umbral blando de 400 k por unidad se mantiene |
| P-011 | revisión | Presupuesto blando superado: unit:Orquestador (509,186 > 400,000) | continuar (sin tope duro) | reducir alcance o cambiar de modelo | más costo | resuelto: aceptado por el humano (2026-09-28); umbral blando de 400 k por unidad se mantiene |
