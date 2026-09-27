---
type: Stack Sheet
title: "Caso: E-commerce"
description: Paquetes de tienda en línea (SaaS vs headless self-hosted vs corporativo), comprar vs construir y equivalencias por nube.
tags: [stacks, e-commerce, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:20:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: shopify-pricing
    resource: https://www.shopify.com/pricing
    title: Shopify — Pricing
  - id: medusa
    resource: https://medusajs.com/
    title: Medusa — Open-source commerce platform
  - id: stripe-pricing
    resource: https://stripe.com/pricing
    title: Stripe — Pricing
  - id: hetzner-cloud
    resource: https://www.hetzner.com/cloud/
    title: Hetzner Cloud — Precios
  - id: coolify
    resource: https://coolify.io/self-hosted
    title: Coolify — Self-hosted
  - id: woocommerce-cost
    resource: https://www.swell.is/content/woocommerce-pricing
    title: "WooCommerce Pricing in 2026: Full Cost Breakdown"
  - id: neon-pricing
    resource: https://neon.com/pricing
    title: Neon — Pricing
  - id: vercel-pricing
    resource: https://vercel.com/pricing
    title: Vercel — Pricing
---

# Caso: E-commerce

## Cuándo aplica

Tienda en línea con catálogo, carrito, checkout y pagos con tarjeta. Perfil de ADS: **software-app**
(nivel extendido: transacciones de dinero son acciones rojas del §4.17 del prompt maestro, HITL
obligatorio en reembolsos/cancelaciones).

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Tema/checkout de Shopify Basic [^shopify-pricing] | Tema/checkout de Shopify Grow/Advanced [^shopify-pricing] | Next.js 16 como storefront headless [^vercel-pricing] | Frontend del suite corporativo (SAP Commerce/Salesforce Commerce Cloud) o WooCommerce sobre WordPress gestionado |
| Backend | Motor de comercio de Shopify (gestionado) [^shopify-pricing] | Motor de comercio de Shopify Grow/Advanced (gestionado) [^shopify-pricing] | Medusa.js (headless, MIT) autoalojado [^medusa] | Motor de comercio corporativo (SAP/Salesforce), ya operado por TI |
| Base de datos | Gestionada por Shopify (no expuesta) | Gestionada por Shopify (no expuesta) | Postgres self-hosted o Neon [^neon-pricing] | Base de datos del suite corporativo, ya operada |
| Auth | Cuentas de cliente de Shopify (incluida) | Cuentas de cliente + SSO en Plus | Auth propia sobre Medusa (JWT) | SSO corporativo (Azure AD/Okta) |
| Pagos | Shopify Payments (Stripe por debajo) 2.9%+US$0.30 [^shopify-pricing] | Shopify Payments 2.6–2.7%+US$0.30 según plan [^shopify-pricing] | Stripe directo 2.9%+US$0.30 [^stripe-pricing] | Pasarela corporativa ya contratada: n/d (no-verificado) |
| Deploy/hosting | Incluido en Shopify (SaaS) [^shopify-pricing] | Incluido en Shopify (SaaS) [^shopify-pricing] | Storefront en Vercel [^vercel-pricing] + backend en VPS Hetzner + Coolify [^hetzner-cloud][^coolify] | On-prem o en el tenant SAP/Salesforce ya contratado |
| LLM/System One | Opcional: buscador/recomendador vía gateway LLM (ver `/stacks/llm-providers.md`) | Igual, con medición de tokens por catálogo | Igual, modelo económico o autoalojado | Copilot del suite corporativo, si lo incluye: n/d (no-verificado) |
| Costo aprox./mes (2026-09) | US$39 + 2.9%+US$0.30/transacción [^shopify-pricing] | US$105–399 + 2.6–2.7%+US$0.30/transacción [^shopify-pricing] | US$0 licencia (Medusa MIT) + ~US$12–25 VPS [^medusa][^hetzner-cloud] + 2.9%+US$0.30 Stripe [^stripe-pricing] | Variable, contrato ya existente; WooCommerce gestionado US$20–200+/mes según tienda [^woocommerce-cost] |
| Curva de aprendizaje | Baja | Baja–media | Media–alta (operar checkout e infraestructura) | Alta |

## Cuándo NO usar cada opción

- **Shopify Basic:** no usar si el checkout debe personalizarse por completo o el modelo es B2B con
  listas de precio complejas desde el lanzamiento.
- **Shopify Grow/Advanced:** sobra costo si el catálogo es pequeño (menos de ~50 SKUs) y no hay
  equipo dedicado.
- **Medusa self-hosted:** no usar si no hay quien opere la infraestructura (parches, backups, el
  alcance PCI del checkout) — sin soporte comercial detrás.
- **SAP/Salesforce Commerce Cloud:** no usar para un catálogo chico o una startup — la implementación
  toma meses y el costo mínimo es alto.

## Comprar vs construir

El core de carrito/checkout casi siempre se "compra" (Shopify) salvo que el modelo de negocio
(marketplace multi-vendedor, B2B con reglas de precio complejas) no encaje en un SaaS de comercio —
ahí Medusa.js (headless, código propio) es la vía de "construir" sin perder el checkout probado de
Stripe por debajo.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Frontend storefront | Amplify Hosting / CloudFront | Static Web Apps | Firebase Hosting / Cloud Run | Nginx + contenedor propio |
| Backend de comercio headless | ECS Fargate | Container Apps | Cloud Run | Kubernetes propio |
| Base de datos | RDS/Aurora Postgres [^neon-pricing] | Database for PostgreSQL | Cloud SQL Postgres | Postgres en VM |
| Pagos | Stripe (SaaS, no cambia por nube) [^stripe-pricing] | Stripe (igual) | Stripe (igual) | Pasarela local del banco adquirente |

## Superficie agéntica y tokens por defecto

Nivel **extendido** obligatorio (dinero de por medio). Dashboard de tokens **N2/N3** si hay
recomendador o buscador con LLM. Expone la Admin API/Storefront API de Shopify (OpenAPI) o una API
REST propia en Medusa; servidor MCP opcional con scopes mínimos (catálogo de solo lectura por
defecto). Todo reembolso, cancelación o cambio de precio ejecutado por un agente requiere HITL
(§4.17 del prompt maestro).

## Riesgos de lock-in y plan de salida

- **Shopify:** riesgo alto (plantillas Liquid, apps propietarias). Plan de salida: mantener catálogo
  y pedidos exportables vía Admin API; migrar a Medusa si el costo o las limitaciones lo justifican.
- **Medusa:** riesgo bajo (MIT, Postgres estándar, sin acoplamiento a un proveedor de nube).
- **SAP/Salesforce Commerce Cloud:** riesgo muy alto. Plan de salida: cláusula de portabilidad de
  datos negociada en el contrato y exportaciones periódicas del catálogo/pedidos (ver
  `/docs/adr/0012-portabilidad.md`).

[^shopify-pricing]: Shopify — Pricing
[^medusa]: Medusa — Open-source commerce platform
[^stripe-pricing]: Stripe — Pricing
[^hetzner-cloud]: Hetzner Cloud — Precios
[^coolify]: Coolify — Self-hosted
[^woocommerce-cost]: WooCommerce Pricing in 2026 — Full Cost Breakdown
[^neon-pricing]: Neon — Pricing
[^vercel-pricing]: Vercel — Pricing
