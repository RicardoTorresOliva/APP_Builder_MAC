---
type: Stack Sheet
title: "Caso: API/backend puro"
description: Paquetes para un servicio API sin UI propia, consumido por programas o agentes, con equivalencias por nube.
tags: [stacks, api, backend, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:35:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: render-pricing
    resource: https://render.com/pricing
    title: Render — Pricing
  - id: supabase-billing
    resource: https://supabase.com/docs/guides/platform/billing-on-supabase
    title: Supabase Docs — Billing
  - id: neon-pricing
    resource: https://neon.com/pricing
    title: Neon — Pricing
  - id: flyio-pricing
    resource: https://fly.io/docs/about/pricing/
    title: Fly.io — Resource pricing
  - id: auth0-pricing
    resource: https://auth0.com/pricing
    title: Auth0 — Pricing
  - id: clerk-pricing
    resource: https://clerk.com/pricing
    title: Clerk — Pricing
  - id: hetzner-cloud
    resource: https://www.hetzner.com/cloud/
    title: Hetzner Cloud — Precios
  - id: coolify
    resource: https://coolify.io/self-hosted
    title: Coolify — Self-hosted
  - id: keycloak-2670
    resource: https://www.keycloak.org/2026/07/keycloak-2670-released
    title: Keycloak 26.7.0 released
---

# Caso: API/backend puro

## Cuándo aplica

Servicio sin interfaz propia, consumido por programas u otros agentes (API REST/GraphQL, CLI o
servidor MCP). Perfil de ADS: **api-service** (nivel extendido siempre: es el mismo perfil de ABM,
ver `/docs/adr/0001-nomenclatura-abm-ads.md`).

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | No aplica (sin UI propia) | No aplica | No aplica | Portal de desarrolladores del gateway corporativo, si existe |
| Backend | FastAPI o NestJS en un solo servicio | NestJS/FastAPI en contenedores + Redis para caché/rate-limit | FastAPI/NestJS en Docker | .NET/Java desplegado en el middleware corporativo existente |
| Base de datos | Supabase Postgres [^supabase-billing] | Neon Postgres dedicado (Scale) [^neon-pricing] | Postgres self-hosted en VPS [^hetzner-cloud] | Postgres/Oracle corporativo |
| Auth | API key o JWT emitido por Supabase Auth [^supabase-billing] | OAuth2 client credentials vía Auth0/Clerk [^auth0-pricing][^clerk-pricing] | OAuth2 client credentials vía Keycloak [^keycloak-2670] | Client credentials/mTLS vía Azure AD/Okta |
| Pagos (si hay monetización por uso) | Cobro por uso vía la pasarela ya elegida en el ADS | Igual, con medidor de uso (metered billing) | Igual que vibe coder | Facturación interna entre áreas, sin pasarela pública |
| Deploy/hosting | Render Starter [^render-pricing] | Fly.io Scale + gateway de API (categoría: Kong/APISIX) [^flyio-pricing] | VPS Hetzner + Coolify [^hetzner-cloud][^coolify] | Azure API Management / AWS API Gateway ya contratado |
| LLM/System One | Opcional si expone endpoints de IA (ver `/stacks/llm-providers.md`) | Igual, con ruteo de modelos y medición por cliente | Igual, modelo económico o autoalojado | Gateway LLM corporativo ya aprobado |
| Costo aprox./mes (2026-09) | US$7 (Render Starter) + US$0–25 (Supabase) [^render-pricing][^supabase-billing] | US$29+ (Fly.io Scale, uso) + uso de Neon a US$0.222/CU-hora [^flyio-pricing][^neon-pricing] + US$150 (Auth0 Essentials B2B) si hay clientes M2M [^auth0-pricing] ≈ US$80–250 | ~US$12–25/mes VPS (Hetzner) + Coolify y Keycloak gratis [^hetzner-cloud][^coolify][^keycloak-2670] | Variable, ya contratado; nueva API bajo el mismo contrato: n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media | Media–alta (operar Postgres/Keycloak/gateway) | Alta |

## Cuándo NO usar cada opción

- **Vibe coder:** no usar si se necesita rate-limiting/cuotas por cliente sofisticadas o SLA
  contractual con terceros desde el lanzamiento.
- **Pro/escalable:** sobra para una API interna de bajo tráfico — Redis y un gateway dedicado son
  costo y operación innecesarios.
- **Low-cost/self-hosted:** no usar si los clientes de la API exigen certificaciones (SOC 2) que un
  VPS propio no puede ofrecer sin trabajo adicional de cumplimiento.
- **Corporativa/legacy:** no usar para una API pública nueva sin contrato Azure/AWS Enterprise ya
  vigente — el gateway corporativo agrega fricción y costo para volúmenes pequeños.

## Comprar vs construir

El gateway de API y el rate-limiting casi siempre se "compran" (categoría: Kong/APISIX o el gateway
gestionado de la nube); la lógica de negocio y los contratos de datos (OpenAPI/AsyncAPI) se
construyen, porque son el diferencial del ADS.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Compute | Fargate / API Gateway+Lambda | Container Apps / API Management | Cloud Run / Apigee | Kubernetes + Kong propio |
| Base de datos | RDS/Aurora Postgres [^neon-pricing] | Database for PostgreSQL | Cloud SQL Postgres | Postgres en VM |
| Cache/rate-limit | ElastiCache (Redis) | Cache for Redis | Memorystore | Redis en contenedor propio |
| Auth M2M | Cognito | Azure AD (client credentials) | Identity Platform | Keycloak on-prem [^keycloak-2670] |

## Superficie agéntica y tokens por defecto

Nivel **extendido** obligatorio (perfil api-service). Dashboard de tokens **N2/N3** según consumo de
LLM por cliente. Expone siempre OpenAPI (o AsyncAPI para eventos) y, cuando el consumidor típico es
un agente, un servidor MCP con tools 1:1 con los endpoints y scopes mínimos por API key; eventos y
webhooks firmados para notificar cambios sin polling.

## Riesgos de lock-in y plan de salida

- **Gateway gestionado de la nube (API Gateway/Apigee):** riesgo alto — mitigar con contratos OpenAPI
  portables y Kong/APISIX como capa de abstracción reemplazable.
- **Auth0/Clerk:** riesgo bajo–medio — interfaz OIDC/OAuth2 estándar, exit plan documentado hacia
  otro proveedor sin cambiar el contrato de la API.
- **Render/Fly.io:** riesgo bajo — contenedor Docker estándar, portable a cualquier orquestador (ver
  `/docs/adr/0012-portabilidad.md`).

[^render-pricing]: Render — Pricing
[^supabase-billing]: Supabase Docs — Billing
[^neon-pricing]: Neon — Pricing
[^flyio-pricing]: Fly.io — Resource pricing
[^auth0-pricing]: Auth0 — Pricing
[^clerk-pricing]: Clerk — Pricing
[^hetzner-cloud]: Hetzner Cloud — Precios
[^coolify]: Coolify — Self-hosted
[^keycloak-2670]: Keycloak 26.7.0 released
