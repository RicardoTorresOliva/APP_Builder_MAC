---
type: Integration Guide
title: Integraciones seguras — mapa de vías
description: Orden de preferencia y matriz de riesgo/esfuerzo para conectar un ADS a sistemas externos.
tags: [integrations, mcp, api, seguridad]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
---

# Integraciones seguras — mapa de vías

El núcleo de ABM no nombra productos (regla 7); este catálogo sí, verificados y con fecha de
revisión — ver `/docs/adr/0016-categorias-y-productos.md`. El comando `/integrate <plataforma>`
(§4.11 del prompt maestro) recorre el orden de abajo y usa la primera vía disponible y segura para
el caso concreto.

## Orden de preferencia

1. **MCP oficial** — catálogo curado, mínimo privilegio, solo lectura por defecto.
2. **API oficial + cliente tipado generado desde OpenAPI.**
3. **SDK oficial** del proveedor, cuando no publica OpenAPI.
4. **Webhooks firmados** — eventos entrantes, evita polling.
5. **Colas y eventos** — desacoplado, alto volumen, reintentos.
6. **iPaaS** (n8n, Make, Zapier) — no-code, sin ingeniería de plataforma dedicada.
7. **Import/export CSV o Excel** — migraciones puntuales sin API disponible.
8. **SQL directo** — último recurso, solo con credenciales de mínimo privilegio.

Bajar en la lista solo cuando la vía anterior no existe o no es viable para el caso — no por
comodidad ni porque sea la que el agente conoce mejor.

## Matriz vía × riesgo × esfuerzo

| Vía | Riesgo | Esfuerzo | Cuándo |
|---|---|---|---|
| MCP oficial | Bajo (con `tools.include` y solo lectura) | Bajo | Existe servidor oficial/verificado |
| API + cliente tipado (OpenAPI) | Bajo-medio | Medio | Hay spec OpenAPI publicada |
| SDK oficial | Medio | Bajo | Sin OpenAPI, pero con SDK mantenido |
| Webhooks firmados | Medio | Medio | Eventos entrantes, evitar polling |
| Colas / eventos | Medio | Alto | Desacoplar sistemas, alto volumen |
| iPaaS | Medio-alto (un tercero ve los datos en tránsito) | Bajo | Prototipos, equipos sin plataforma |
| CSV / Excel | Bajo técnico, alto operativo (manual, frágil) | Bajo | Migración puntual sin API |
| SQL directo | Alto (acopla al esquema interno, sin contrato) | Medio | Último recurso; mínimo privilegio |

## Estructura del catálogo

| Ruta | Contenido |
|---|---|
| [mcp/](mcp/README.md) | Servidores MCP verificados, plantillas por herramienta, seguridad |
| [api/README.md](api/README.md) | Clientes tipados, reintentos, idempotencia, errores `problem+json` |
| [webhooks/README.md](webhooks/README.md) | Firma HMAC, replay, idempotencia, cola de procesamiento |
| [auth/README.md](auth/README.md) | OAuth2/OIDC, PKCE, client credentials, scopes mínimos |
| [agents/](agents/README.md) | Hermes y A2A — cómo un agente externo opera un ADS |
| [decision/](decision/README.md) | Capa System One (Jev) — decisión tipada con confianza |
| [llm-gateway/README.md](llm-gateway/README.md) | Gateway multi-proveedor de LLM |
| [observability/](observability/README.md) | Espacio de tokens en N3 (OTel), backends posibles |
| [other-ways.md](other-ways.md) | SDKs, colas, iPaaS, CSV/Excel, SQL |
| [secrets.md](secrets.md) | `.env.example`, gestor de secretos, secret scanning |

Ver también: `/docs/adr/0010-superficie-agentica.md`, `/docs/adr/0011-capa-system-one.md`,
`/docs/adr/0016-categorias-y-productos.md`, `/docs/compat-matrix.md`.
