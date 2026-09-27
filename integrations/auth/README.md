---
type: Integration Guide
title: Auth para integraciones — OAuth2/OIDC
description: Flujos, PKCE, client credentials y scopes mínimos por agente para integraciones externas.
tags: [oauth, oidc, seguridad, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: mcp-auth
    resource: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
    title: Authorization — MCP
---

# Auth para integraciones — OAuth2/OIDC

## Cuándo cada flujo
- **Authorization Code + PKCE**: un humano autoriza una vez y el ADS actúa en su nombre (p. ej. un
  agente que lee su Notion o su Drive). Obligatorio incluso para clientes confidenciales desde
  OAuth 2.1.
- **Client credentials**: servicio a servicio, sin usuario humano detrás (p. ej. el ADS llamando a
  la API de facturación de la plataforma). El "usuario" es la propia aplicación.
- **Device code**: cliente sin navegador embebido (CLI, terminal) que necesita autorización de un
  humano en otro dispositivo.

## PKCE, siempre
Todo flujo con redirección usa PKCE con `S256` — no solo clientes públicos. Evita interceptación
del código de autorización incluso en clientes confidenciales; es requisito explícito de OAuth 2.1
y del perfil de autorización de MCP para transporte HTTP[^mcp-auth].

## Scopes mínimos por agente
Cada agente (o cada ADS) recibe un scope acotado a lo que necesita hacer, no el scope más amplio
disponible del proveedor. Un agente que solo lee no recibe `write`; un agente que opera un solo
proyecto no recibe el scope de la organización completa. El scope se declara junto al servidor MCP
o cliente API que lo usa — `tools.include` y el alcance del token deben coincidir.

## Tokens revocables y de corta duración
- Preferir tokens de acceso de vida corta (minutos-horas) + refresh token, sobre un token estático
  de larga duración.
- Todo token debe poder revocarse desde la consola del proveedor sin rotar credenciales de toda la
  organización.
- Un secreto de larga vida (API key clásica) se trata como excepción, no como default — documentar
  por qué el proveedor no ofrece OAuth cuando ocurra.

## Resource Indicators (RFC 8707)
Cuando el proveedor lo soporta, el cliente solicita el token ya acotado al recurso concreto
(`resource=https://api.proveedor.com/proyecto-x`), para que un token robado de un flujo no sirva
contra otro recurso del mismo proveedor[^mcp-auth].

## Descubrimiento del authorization server
OAuth 2.0 Authorization Server Metadata (RFC 8414) u OpenID Connect Discovery permiten que el
cliente encuentre los endpoints del authorization server sin configuración manual — preferible a
hardcodear URLs de `token`/`authorize`.

[^mcp-auth]: Authorization — MCP
