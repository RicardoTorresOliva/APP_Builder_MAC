---
type: Reference
title: Estándar de database — índice
description: Alcance del estándar de base de datos y cómo se relaciona con sus archivos hermanos.
tags: [database, estandares, indice]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Database — índice

Cubre el modelado, la evolución y la operación de cualquier almacén de datos relacional del ADS.
No cubre el acceso vía API (ver `standards/backend/`).

| Archivo | Para qué |
|---|---|
| `standard.md` | modelado (ERD), migraciones y seeds, índices e integridad, RLS y auditoría, backups, multi-tenant, tipos generados, privacidad, escalamiento |
| `checklist-dod.md` | casillas verificables antes de dar por hecha una FU/DU de datos |
| `review-criteria.md` | qué mira el revisor y con qué severidad |
| `testing.md` | tests de migraciones y de datos: qué cubren y cuándo |

Transversal obligatorio: `standards/security/web-api.md` (control de acceso a datos vía API),
`standards/finops/README.md` (costo de almacenamiento y consultas).
