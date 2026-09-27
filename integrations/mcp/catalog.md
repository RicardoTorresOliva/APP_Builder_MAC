---
type: Reference
title: Catálogo de servidores MCP verificados
description: Servidores MCP oficiales o verificados por categoría, con transporte, auth y modo recomendado.
tags: [mcp, catalogo, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: gh-mcp
    resource: https://github.com/github/github-mcp-server
    title: GitHub MCP Server (repo oficial)
  - id: gh-mcp-remote
    resource: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server
    title: Setting up the GitHub MCP Server
  - id: sb-mcp
    resource: https://github.com/supabase/mcp
    title: Supabase MCP Server (repo oficial)
  - id: aws-mcp
    resource: https://awslabs.github.io/mcp/
    title: Open Source MCP Servers for AWS (AWS Labs)
  - id: notion-mcp
    resource: https://developers.notion.com/guides/mcp/get-started-with-mcp
    title: Connect to Notion MCP
  - id: atl-mcp
    resource: https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/
    title: Get started with the Atlassian MCP server
  - id: pw-mcp
    resource: https://github.com/microsoft/playwright-mcp
    title: Playwright MCP (Microsoft, repo oficial)
  - id: cf-mcp
    resource: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/
    title: Cloudflare's own MCP servers
  - id: aws-ga
    resource: https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/
    title: The AWS MCP Server is now generally available
  - id: az-mcp
    resource: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/
    title: Azure MCP Server documentation
  - id: stripe-mcp
    resource: https://docs.stripe.com/mcp
    title: Model Context Protocol (MCP) — Stripe Documentation
  - id: sentry-mcp
    resource: https://github.com/getsentry/sentry-mcp
    title: sentry-mcp (repo oficial)
  - id: grafana-mcp
    resource: https://github.com/grafana/mcp-grafana
    title: Grafana MCP server (repo oficial)
---

# Catálogo de servidores MCP verificados

Cada fila exige URL oficial del proveedor (nunca un mirror de terceros), transporte confirmado y
auth confirmado. "Modo recomendado" es el mínimo privilegio operable para uso agéntico — casi
siempre solo lectura. Mínimo exigido: 12 servidores; van 13 para tener margen.

| Servidor | Categoría | Transporte | Auth | Modo recomendado |
|---|---|---|---|---|
| GitHub MCP Server[^gh-mcp][^gh-mcp-remote] | Repos/código | HTTP remoto (`api.githubcopilot.com/mcp/`) o stdio local (Docker `ghcr.io/github/github-mcp-server`) | OAuth o PAT (`GITHUB_PERSONAL_ACCESS_TOKEN`) | `GITHUB_READ_ONLY=1`; `GITHUB_TOOLSETS` acotado |
| Supabase MCP[^sb-mcp] | Bases de datos | HTTP remoto (`mcp.supabase.com/mcp`) | OAuth a la cuenta Supabase, o token de proyecto | Flag `--read-only`; alcance a un solo proyecto |
| Amazon Aurora PostgreSQL MCP Server[^aws-mcp] | Bases de datos | stdio (`uvx`, paquete `awslabs.postgres-mcp-server`) | Credenciales IAM (rol de mínimo privilegio) | Rol IAM de solo lectura sobre el cluster |
| Notion MCP[^notion-mcp] | Docs | HTTP remoto (`mcp.notion.com/mcp`) o stdio local (`npx @notionhq/notion-mcp-server`) | OAuth (remoto) o integration token (local) | Integración con acceso solo a las páginas compartidas necesarias |
| Atlassian Remote MCP Server[^atl-mcp] | Docs / tickets | HTTP remoto (`mcp.atlassian.com/v2/mcp`) | OAuth (Atlassian Rovo) | Scopes limitados a los proyectos Jira/espacios Confluence del ADS |
| AWS Documentation MCP Server[^aws-mcp] | Docs | stdio (`uvx`, paquete `awslabs.aws-documentation-mcp-server`) | Ninguna (documentación pública) | Solo lectura por naturaleza |
| Playwright MCP[^pw-mcp] | Navegador | stdio (`npx @playwright/mcp@latest`) o HTTP standalone (`--port`) | Ninguna (controla un navegador local) | Perfil de navegador aislado/efímero; nunca contra sesiones con credenciales de producción |
| Cloudflare MCP[^cf-mcp] | Nube | HTTP remoto (`mcp.cloudflare.com/mcp`) | OAuth a la cuenta Cloudflare | Cuenta/zona acotada; revisar scopes del token OAuth |
| AWS MCP Server (GA)[^aws-ga] | Nube | HTTP remoto vía proxy firmado (`mcp-proxy-for-aws`, endpoint regional) | IAM/SigV4, con registro en CloudTrail | Rol IAM de solo lectura; auditoría vía CloudTrail obligatoria |
| Azure MCP Server[^az-mcp] | Nube | stdio local (CLI vía `npx`/herramienta `dotnet`) | Credenciales Azure CLI / Entra ID | Rol Azure RBAC de solo lectura (`Reader`) |
| Stripe MCP[^stripe-mcp] | Pagos | HTTP remoto (`mcp.stripe.com`) o paquete local `@stripe/mcp` | Bearer (API key restringida) | Clave restringida de solo lectura; nunca la clave secreta completa |
| Sentry MCP[^sentry-mcp] | Observabilidad | HTTP remoto (`mcp.sentry.dev/mcp`) o stdio (`npx @sentry/mcp-server`) | OAuth (remoto) o `SENTRY_ACCESS_TOKEN` (local) | Restringir por organización/proyecto vía path (`/:organization/:project`) |
| Grafana MCP[^grafana-mcp] | Observabilidad | stdio (`uvx mcp-grafana` o binario) | `GRAFANA_SERVICE_ACCOUNT_TOKEN` | Cuenta de servicio con rol `Viewer` |

## Notas de verificación

- No existe (a la fecha) un servidor MCP oficial documentado para la capa de decisión (Jev/TypeSafe
  AI) — solo API HTTP, SDKs y agent skill; ver `/integrations/decision/typesafe-jev.md`.
- Varios de estos servidores pasaron de comunitario a oficial durante 2026 y cambian endpoints/flags
  con frecuencia — re-verificar URL, transporte y auth antes de `stale_after`, no asumir que siguen
  igual.
- Añadir un servidor nuevo a esta tabla exige la misma verificación: URL del repo/documentación
  oficial del proveedor, no un artículo de terceros.

[^gh-mcp]: GitHub MCP Server (repo oficial)
[^gh-mcp-remote]: Setting up the GitHub MCP Server
[^sb-mcp]: Supabase MCP Server (repo oficial)
[^aws-mcp]: Open Source MCP Servers for AWS (AWS Labs)
[^notion-mcp]: Connect to Notion MCP
[^atl-mcp]: Get started with the Atlassian MCP server
[^pw-mcp]: Playwright MCP (Microsoft, repo oficial)
[^cf-mcp]: Cloudflare's own MCP servers
[^aws-ga]: The AWS MCP Server is now generally available
[^az-mcp]: Azure MCP Server documentation
[^stripe-mcp]: Model Context Protocol (MCP) — Stripe Documentation
[^sentry-mcp]: sentry-mcp (repo oficial)
[^grafana-mcp]: Grafana MCP server (repo oficial)
