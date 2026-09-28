---
type: Exit Plan
title: Plan de salida — panel de ventas
description: Cómo migrar el panel de ventas fuera del stack de demo sin reescribir reglas ni contratos.
tags: [portabilidad, salida, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:08:41Z }
---

# Plan de salida

| Pieza | Hoy | Salida | Qué se conserva |
|---|---|---|---|
| Servidor HTTP | servidor de la biblioteca estándar | framework web + servidor de aplicaciones detrás de TLS | contrato `api/openapi.yaml` y tests de `tests/test_api.py` |
| Base de datos | archivo SQLite | base relacional administrada o self-hosted | migraciones (SQL estándar salvo `GLOB`) y seeds |
| Datos | `data/panel.db` | volcado con `sqlite3 data/panel.db .dump` e importación | ids, montos en centavos, auditoría |
| Identidad | usuarios propios con PBKDF2 | proveedor de identidad (OIDC) | roles `admin` / `vendedor` |
| Agentes | MCP stdio + CLI | MCP remoto con OAuth 2.1 | nombres de tools y capacidades de `ads.yaml` |

Sin proveedores LLM ni nube: no hay lock-in contractual. Costo de salida estimado: bajo (reglas aisladas en `app/db.py`).
