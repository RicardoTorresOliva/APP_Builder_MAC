---
type: Reference
title: Estándar de backend — índice
description: Alcance del estándar de backend y cómo se relaciona con sus archivos hermanos.
tags: [backend, estandares, indice]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Backend — índice

Cubre cualquier superficie de API: REST, GraphQL o RPC tipado, incluida la superficie que un agente
externo opera. No cubre la base de datos (ver `standards/database/`) ni la UI (ver `standards/frontend/`).

| Archivo | Para qué |
|---|---|
| `standard.md` | diseño de API, errores, authN/authZ, jobs/colas/caché, observabilidad, idempotencia, escalabilidad, superficie agéntica |
| `checklist-dod.md` | casillas verificables antes de dar por hecha una FU/DU de API |
| `review-criteria.md` | qué mira el revisor y con qué severidad |
| `testing.md` | tests unitarios, de integración y de contrato: qué cubren y cuándo |

Transversal obligatorio: `standards/security/web-api.md` (OWASP Top 10 + ASVS), `standards/agentic/README.md`
si expone superficie agéntica, `standards/observability/README.md`, `standards/finops/README.md` si
consume modelos de lenguaje.
