---
type: Work Units
title: Unidades de trabajo — panel de ventas
description: FU y DU del panel de ventas con criterio de aceptación atado a la regla de completitud de software-app.
tags: [unidades, fu, du, plan, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:42Z }
---

# Unidades de trabajo

Regla de completitud (perfil `software-app`): backend + interfaz + uso de punta a punta con estados vacíos
y de error + capacidad en `ads.yaml` operable por agentes + quality gate + tests de rutas críticas + tokens en el ledger.

| ID | Tipo | Módulo (modo) | Qué entrega | Requisitos | Criterio de aceptación |
|---|---|---|---|---|---|
| FU-01 | Foundation | ventas (SDD) | Capa de datos: migraciones up/down, seeds, reglas de negocio | REQ-014 | `test_db` en verde; up → down → up sin pérdida de integridad; seed idempotente |
| FU-02 | Foundation | auth (SDD, revisión humana) | Identidad: PBKDF2, sesiones, roles, CSRF, límite de intentos, problem+json | REQ-001–006, REQ-015 | `test_auth` y rutas de auth de `test_api` en verde |
| FU-03 | Foundation | transversal | Superficie agéntica base: `ads.yaml`, `AGENTS.md`, skill, `llms.txt`, servidor MCP, ledger | REQ-013 | `ads-check` sin errores |
| DU-01 | Deliverable | ventas (SDD) | Registrar, listar y borrar ventas (web + API) | REQ-007–009, REQ-012 | Un vendedor registra una venta desde el formulario y la ve en la tabla; validación por campo; admin borra con confirmación |
| DU-02 | Deliverable | dashboard (SDD) | Dashboard con KPIs, gráficos SVG, tabla, tema oscuro y estados | REQ-010, REQ-011 | Carga, vacío y error visibles; tooltips con teclado; sin scroll horizontal en móvil; sin errores de consola |
| DU-03 | Deliverable | transversal | Operación por agentes: CLI y MCP con status, resumen, crear (dry-run) y borrar (HITL) | REQ-013 | `test_mcp` y `agent-conformance` en verde; borrar sin confirmación es rechazado |

Milestones y estado: [task tracker](task_tracker.md).
