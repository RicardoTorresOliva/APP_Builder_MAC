---
type: Reference
title: Estándar de frontend — índice
description: Alcance del estándar de frontend y cómo se relaciona con sus archivos hermanos.
tags: [frontend, estandares, indice]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Frontend — índice

Cubre cualquier interfaz con usuario humano: apps web, dashboards, portales, apps móviles con
framework de componentes. No cubre CLIs (ver `standards/agentic/README.md`) ni APIs (ver
`standards/backend/`).

| Archivo | Para qué |
|---|---|
| `standard.md` | design system y tokens, componentes, accesibilidad, responsive, Core Web Vitals, estado y formularios, i18n/SEO, estados vacíos/error |
| `checklist-dod.md` | casillas verificables antes de dar por hecha una FU/DU de UI |
| `review-criteria.md` | qué mira el revisor y con qué severidad |
| `testing.md` | tests unitarios, de componente y E2E: qué cubren y cuándo |

Transversal obligatorio: `standards/a11y/README.md` (WCAG 2.2 AA), `standards/testing/README.md`
(pirámide y CI), `standards/observability/README.md` si la UI reporta errores de cliente.
