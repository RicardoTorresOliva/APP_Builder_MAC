---
type: Design Doc
title: Contratos de API — panel de ventas
description: Endpoints, autenticación, autorización por rol y errores problem+json del panel de ventas (design doc HIGH).
tags: [api, openapi, problem-json, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:26Z }
---

# Contratos de API

Fuente de verdad: [OpenAPI 3.1](../api/openapi.yaml). Implementación: `app/server.py`.

| Método y ruta | Auth | Rol | CSRF | Respuestas |
|---|---|---|---|---|
| `GET /healthz` | no | — | — | 200 |
| `GET /login`, `POST /login` | no | — | token de pre-sesión | 303, 401, 403, 429 |
| `POST /logout` | sesión | todos | campo `csrf` | 303 |
| `GET /dashboard` | sesión (si no, 303 a `/login`) | todos | — | 200 HTML |
| `GET /api/ventas` | sesión | vendedor: solo propias; admin: todas | — | 200, 401, 422 |
| `POST /api/ventas` | sesión | vendedor: a su nombre; admin: cualquiera | `X-CSRF-Token` | 201, 200 (idempotente), 403, 415, 422 |
| `DELETE /api/ventas/{id}` | sesión | admin | `X-CSRF-Token` | 204, 403, 404 |
| `GET /api/resumen` | sesión | igual que listado | — | 200, 401, 422 |

## Errores

- `application/problem+json` con `type` (`urn:panel-ventas:problem:<slug>`), `title`, `status`, `detail`,
  `instance` (id de petición) y `errors[]` (`pointer`, `detail`) en validación.
- 500 nunca incluye trazas; la traza va a stderr con el mismo id de petición.

## Cabeceras de seguridad

CSP `default-src 'none'` con `script-src 'self'` y `style-src 'self'`, `X-Frame-Options: DENY`,
`X-Content-Type-Options: nosniff`, `Referrer-Policy: same-origin`, `Cache-Control: no-store`.

## Superficie agéntica

Mismas reglas de negocio (`app/db.py`) expuestas por MCP (`ops/mcp_server.py`) y CLI (`app/cli.py`);
ver [manual de operación](../docs/manual/operacion.md).
