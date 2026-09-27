---
type: Standard
title: Tests de frontend
description: Qué tests se escriben, qué cubren y en qué momento corren.
tags: [frontend, tests, pirueta-de-tests]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Tests de frontend

Ver la pirámide general en `standards/testing/README.md`. Aquí, lo específico de UI.

| Nivel | Cubre | Cuándo corre |
|---|---|---|
| Unitario | lógica pura: funciones de formato, reducers de estado, hooks/composables sin DOM | en cada commit, local y en CI |
| Componente | render, interacción (click/teclado/foco) y accesibilidad (rol y nombre accesible) de un componente aislado | en cada PR que toque el componente |
| E2E | rutas críticas de negocio de punta a punta (alta, checkout, login, la ruta que el perfil declare crítica) contra un entorno cercano a producción | antes de cerrar una DU y antes de cada release |
| Visual (opcional) | diferencias de píxel en componentes de design system, si el perfil lo exige | en cambios al design system |

## Reglas

- Ningún test E2E reemplaza un test unitario: el E2E prueba integración, no lógica de detalle.
- Un componente sin estado vacío/error definido no tiene test de componente completo.
- Los mocks de red usan los mismos contratos (`application/problem+json`) que produce el backend,
  para no divergir del comportamiento real (`standards/backend/standard.md`).
- Cobertura mínima de lógica crítica la fija el perfil activo; no se persigue el 100 % por sí mismo.
