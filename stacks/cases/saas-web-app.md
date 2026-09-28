---
type: Stack Sheet
title: "Caso: Web app SaaS"
description: Paquetes FE+BE+DB+auth+pagos+deploy para una aplicación SaaS multi-tenant, con equivalencias por nube.
tags: [stacks, saas, web-app, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:10:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: vercel-pricing
    resource: https://vercel.com/pricing
    title: Vercel — Pricing
  - id: supabase-billing
    resource: https://supabase.com/docs/guides/platform/billing-on-supabase
    title: Supabase Docs — Billing
  - id: neon-pricing
    resource: https://neon.com/pricing
    title: Neon — Pricing
  - id: clerk-pricing
    resource: https://clerk.com/pricing
    title: Clerk — Pricing
  - id: auth0-pricing
    resource: https://auth0.com/pricing
    title: Auth0 — Pricing
  - id: stripe-pricing
    resource: https://stripe.com/pricing
    title: Stripe — Pricing
  - id: flyio-pricing
    resource: https://fly.io/docs/about/pricing/
    title: Fly.io — Resource pricing
  - id: hetzner-cloud
    resource: https://www.hetzner.com/cloud/
    title: Hetzner Cloud — Precios
  - id: coolify
    resource: https://coolify.io/self-hosted
    title: Coolify — Self-hosted
  - id: keycloak-2670
    resource: https://www.keycloak.org/2026/07/keycloak-2670-released
    title: Keycloak 26.7.0 released
  - id: okta-pricing
    resource: https://www.okta.com/pricing/
    title: Okta — Pricing
---

# Caso: Web app SaaS

## Cuándo aplica

Aplicación con cuentas, suscripción y datos por cliente (multi-tenant), consumida vía navegador.
Perfil de ADS: **software-app** (nivel extendido si tiene SLO propios y varios entornos).

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Next.js 16 (App Router) + Tailwind [^vercel-pricing] | Next.js 16 + servicios backend dedicados (Node/NestJS) | Next.js 16 (mismo código, otro deploy) | Frontend corporativo (Angular/.NET Blazor) según estándar interno |
| Backend | Route Handlers de Next.js sobre Supabase | NestJS/FastAPI en contenedor propio | NestJS/FastAPI en contenedor propio | .NET/Java sobre el middleware corporativo existente |
| Base de datos | Supabase Postgres (Free→Pro) [^supabase-billing] | Neon Postgres dedicado (Launch/Scale) [^neon-pricing] o Supabase Team | Postgres autoalojado en Docker | SQL Server/Oracle corporativo, ya operado por TI |
| Auth | Auth de Supabase (incluida) [^supabase-billing] | Clerk (multi-tenant, mejor DX) [^clerk-pricing] o Auth0 [^auth0-pricing] | Keycloak self-hosted [^keycloak-2670] | Azure AD B2C / Okta (SSO ya contratado) [^okta-pricing] |
| Pagos | Stripe Billing (suscripciones) [^stripe-pricing] | Stripe Billing [^stripe-pricing] | Stripe Billing (sin alternativa self-host razonable para tarjetas) [^stripe-pricing] | Pasarela corporativa ya contratada (Adyen/Braintree): n/d (no-verificado) |
| Deploy/hosting | Vercel Hobby→Pro [^vercel-pricing] | Vercel Pro + Fly.io/Render para servicios de larga duración [^flyio-pricing] | VPS Hetzner + Coolify (PaaS autoalojado, gratis) [^hetzner-cloud][^coolify] | Azure App Service / AWS ECS, ya contratado |
| LLM/System One | Opcional: chat de soporte vía gateway LLM (ver `/stacks/llm-providers.md`) | Gateway LLM con ruteo de modelos y medición por feature | Igual, modelo económico o autoalojado | Gateway LLM corporativo ya aprobado por seguridad |
| Costo aprox./mes (2026-09) | US$0–20 (Vercel) + US$0–25 (Supabase Pro) + comisión Stripe 2.9%+US$0.30 [^vercel-pricing][^supabase-billing][^stripe-pricing] | US$20/asiento (Vercel Pro) + ~US$15–40 (Neon Launch, uso) + US$25 (Clerk Pro) + US$5–29 (Fly.io) ≈ US$65–125 [^vercel-pricing][^neon-pricing][^clerk-pricing][^flyio-pricing] | ~US$12–25 (1–2 VPS Hetzner CX23) + Coolify gratis + Keycloak gratis [^hetzner-cloud][^coolify][^keycloak-2670] | Variable, ya contratado; Okta desde US$6–17/usuario/mes si se añade [^okta-pricing]; el resto: n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media | Media–alta (operar Postgres/Keycloak) | Alta |

## Cuándo NO usar cada opción

- **Vibe coder (Next.js+Supabase):** no usar si hay requisitos de aislamiento por tenant regulados
  (p. ej. HIPAA) desde el lanzamiento, o volumen de escritura que exceda el plan Free/Pro sin
  ajustar cómputo dedicado.
- **Pro/escalable:** sobra para un MVP de validación de mercado; son más piezas (Neon + Clerk +
  Fly.io) que un backend-as-a-service único.
- **Low-cost/self-hosted:** no usar si el equipo no puede operar backups, parches y HA de Postgres
  y Keycloak — no hay soporte comercial detrás.
- **Corporativa/legacy:** no usar para una startup sin contrato Azure/Okta ya vigente; el piso de
  costo y los tiempos de aprobación de TI son altos para un ADS nuevo.

## Comprar vs construir

Auth y pagos casi siempre se "compran" (Clerk/Auth0/Okta, Stripe): reimplementar OAuth/OIDC o
cumplimiento PCI-DSS no es diferenciador para un SaaS. La lógica de negocio, el modelo de datos
multi-tenant y las reglas de facturación por uso sí se construyen.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Compute | Lambda / Fargate | Functions / App Service | Cloud Run / GKE | Kubernetes propio |
| Base de datos gestionada | RDS/Aurora Postgres | Database for PostgreSQL | Cloud SQL Postgres | Postgres en VM |
| Auth | Cognito | Azure AD B2C | Identity Platform | Keycloak on-prem [^keycloak-2670] |
| Almacenamiento de objetos | S3 | Blob Storage | Cloud Storage | MinIO on-prem |

## Superficie agéntica y tokens por defecto

Nivel **extendido** del Contrato ADS (software con SLO y varios entornos). Dashboard de tokens
**N2** como mínimo (tokens por feature/usuario); **N3** si hay varios modelos o tenants con
presupuestos propios. Expone API REST/OpenAPI para cuentas y suscripciones, y opcionalmente un
servidor MCP con scopes mínimos para que un agente opere cuentas y planes en modo `--dry-run` antes
de confirmar.

## Riesgos de lock-in y plan de salida

- **Supabase (BaaS):** riesgo medio — exportar el esquema como SQL Postgres estándar, evitar RPC
  propietario más allá de RLS; el plan de salida es un Postgres gestionado cualquiera.
- **Clerk/Auth0:** riesgo bajo–medio — ambos hablan OIDC estándar; el plan de salida es migrar el
  flujo OAuth a otro proveedor OIDC sin reescribir la app.
- **Vercel:** riesgo bajo — Next.js corre en cualquier host Node; el plan de salida documentado es
  un contenedor Docker en Fly.io/Render (ver `/docs/adr/0012-portabilidad.md`).

[^vercel-pricing]: Vercel — Pricing
[^supabase-billing]: Supabase Docs — Billing
[^neon-pricing]: Neon — Pricing
[^clerk-pricing]: Clerk — Pricing
[^auth0-pricing]: Auth0 — Pricing
[^stripe-pricing]: Stripe — Pricing
[^flyio-pricing]: Fly.io — Resource pricing
[^hetzner-cloud]: Hetzner Cloud — Precios
[^coolify]: Coolify — Self-hosted
[^keycloak-2670]: Keycloak 26.7.0 released
[^okta-pricing]: Okta — Pricing
