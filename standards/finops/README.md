---
type: Reference
title: Estándar de FinOps y tokens — índice
description: Ledger, niveles de dashboard, presupuestos blando/duro y costo por unidad, incluidos tokens.
tags: [finops, tokens, costo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# FinOps y tokens — índice

Ver ADR 0013 (espacio de control de tokens) para la decisión completa. Este archivo fija el estándar
que backend y observabilidad consumen.

## Ledger

Evento por operación medible: timestamp, fase (construcción/operación), fuente (telemetría, uso
reportado por el proveedor, o estimación explícita marcada `estimado`), tokens de entrada/salida/
caché, modelo, herramienta, actor, unidad (FU/DU/WU), funcionalidad y tenant. Sin precio disponible,
el costo se marca "n/d", nunca se inventa (AGENTS.md regla 14).

## Niveles

| Nivel | Cuándo | Qué produce |
|---|---|---|
| N1 | prototipo o informe | reporte de tokens generado a partir del ledger |
| N2 | MVP o producto | dashboard estático generado desde el ledger, con presupuestos y alertas en CI |
| N3 | enterprise o regulado | dashboard en vivo sobre la pila de observabilidad elegida, con presupuesto por tenant/funcionalidad, chargeback y detección de anomalías |

El nivel mínimo lo fija el perfil activo; el humano puede pedir uno mayor.

## Presupuestos

- Umbral blando superado → entra a la cola de pendientes (`abm pending add`), el trabajo continúa.
- Tope duro superado → bloqueante (AGENTS.md §Bloqueantes, ítem f); se detiene y se informa.
- Presupuesto declarado por sesión, por FU/DU/WU y por funcionalidad.

## Costo por unidad

Todo endpoint o funcionalidad que invoca un modelo de lenguaje declara su costo por unidad de
negocio (por solicitud, por usuario, por tenant); ver `standards/backend/standard.md` §Escalabilidad.

## Verificación

`abm tokens report|dashboard|budget|attest`; recurso `abm://tokens/summary` para que un agente
externo lo consulte sin parsear texto. `skills/observability-setup/SKILL.md` conecta el ledger a la
instrumentación general.
