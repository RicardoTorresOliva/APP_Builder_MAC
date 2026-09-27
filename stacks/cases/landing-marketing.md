---
type: Stack Sheet
title: "Caso: Landing / sitio de marketing"
description: Paquetes FE+hosting+CMS+pagos para un sitio de marketing o landing, con equivalencias por nube.
tags: [stacks, landing, marketing, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:05:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: vercel-pricing
    resource: https://vercel.com/pricing
    title: Vercel — Pricing
  - id: cf-pages
    resource: https://developers.cloudflare.com/pages/functions/pricing/
    title: Cloudflare Pages Functions — Pricing
  - id: cf-workers
    resource: https://developers.cloudflare.com/workers/platform/pricing/
    title: Cloudflare Workers — Pricing
  - id: sanity-pricing
    resource: https://www.sanity.io/pricing
    title: Sanity — Pricing
  - id: framer-pricing
    resource: https://www.framer.com/pricing/
    title: Framer — Pricing
  - id: webflow-pricing
    resource: https://help.webflow.com/hc/en-us/articles/51059955082387-Updated-pricing-and-simplified-plans-for-May-2026
    title: Webflow Help Center — Updated pricing (May 2026)
  - id: amplify-pricing
    resource: https://aws.amazon.com/amplify/pricing/
    title: AWS Amplify — Pricing
  - id: cloudrun-pricing
    resource: https://cloud.google.com/run/pricing
    title: Google Cloud Run — Pricing
  - id: astro
    resource: https://astro.build
    title: Astro
  - id: nextjs
    resource: https://nextjs.org/blog
    title: Next.js — Blog (versión vigente)
---

# Caso: Landing / sitio de marketing

## Cuándo aplica

Sitio de contenido público orientado a conversión (landing, sitio corporativo, página de producto):
tráfico de lectura, formularios/CTA, sin lógica de negocio propia. Perfil de ADS: **software-app**
(variante "sitio de contenido"; sin `api_contracts` propios salvo el endpoint del formulario).

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Astro 5 + Tailwind (contenido en MDX) [^astro] | Next.js 16 (App Router, ISR) + Tailwind [^nextjs] | Astro 5 estático puro [^astro] | CMS corporativo ya licenciado (Adobe Experience Manager/Sitecore) o WordPress gestionado por TI |
| Backend | Función serverless para el formulario (misma plataforma de deploy) | Route Handlers de Next.js / funciones edge | Cloudflare Worker (free tier) para el formulario [^cf-workers] | Backend del CMS corporativo, operado por TI |
| Base de datos | No aplica (contenido en el repo) | CMS headless Sanity Growth para que marketing edite sin desplegar [^sanity-pricing] | No aplica (Markdown en el repo) | Base de datos del CMS corporativo (ya operada por TI) |
| Auth | No aplica (sitio público) | No aplica (SSO ligero solo para preview) | No aplica | SSO corporativo (SAML/OIDC) para el panel de edición |
| Pagos | Opcional: enlaces de pago de la pasarela ya elegida en el ADS | Checkout hospedado de la pasarela elegida, si hay preventa | Igual que vibe coder (no hay alternativa self-host razonable para tarjetas) | Pasarela ya contratada por la empresa |
| Deploy/hosting | Vercel Hobby→Pro [^vercel-pricing] | Vercel Pro / Netlify Pro | Cloudflare Pages (free) [^cf-pages] | CDN/hosting corporativo ya contratado |
| LLM/System One | Opcional: widget de FAQ vía gateway LLM (ver `/stacks/llm-providers.md`) | Igual, con moderación y medición de tokens | Igual, modelo económico | Gateway LLM ya aprobado por seguridad de la empresa |
| Costo aprox./mes (2026-09) | US$0–20 (Vercel Hobby/Pro) [^vercel-pricing] | US$20–45/asiento (Vercel Pro) + US$15/asiento (Sanity Growth) [^vercel-pricing][^sanity-pricing] | US$0 (Cloudflare Pages free) + dominio aparte [^cf-pages] | Variable, ya contratado; instancia nueva bajo el mismo contrato: n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media | Baja–media | Alta (procesos de aprobación de TI) |

Cada columna es un paquete: el FE elegido, su función de formulario y su hosting están pensados para
desplegarse juntos sin piezas sueltas.

## Cuándo NO usar cada opción

- **Vibe coder (Astro+Vercel):** no usar si marketing necesita editar contenido a diario sin tocar
  código, o si hay un SLA/soporte contractual exigido desde el día uno.
- **Pro/escalable (Next.js+Sanity):** sobra para una landing de una sola página; el CMS headless
  agrega costo y una segunda consola que aprender.
- **Low-cost/self-hosted (Cloudflare Pages):** no usar si se requiere soporte comercial con SLA o
  integración con el SSO corporativo del panel de edición.
- **Corporativa/legacy:** no usar para un MVP o validación rápida — los ciclos de aprobación de TI y
  el costo total de propiedad son altos frente a un sitio estático.

## Comprar vs construir

Si el equipo es no técnico y el diseño visual manda, "comprar" un builder no-code es válido y más
rápido: Framer (Free–US$30/mes por sitio, más asientos de workspace aparte) [^framer-pricing] o
Webflow (Starter free, Basic US$15/mes, Premium US$25–39/mes) [^webflow-pricing]. "Construir" con
Astro/Next.js tiene sentido cuando el sitio comparte repo, pipeline y componentes con el resto del
ADS, o cuando el SEO/performance exige control fino sobre el HTML generado.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Frontend estático/SSR | Amplify Hosting / CloudFront+S3 [^amplify-pricing] | Static Web Apps | Firebase Hosting / Cloud Run [^cloudrun-pricing] | Nginx + contenedor propio |
| Función del formulario | Lambda | Functions | Cloud Functions / Cloud Run | Contenedor con cola propia |
| CDN | CloudFront | Front Door | Cloud CDN | Cloudflare Enterprise / Varnish |
| CMS headless (si aplica) | ECS/EC2 con CMS autoalojado | App Service / VM | Cloud Run / GCE | Servidor propio de TI |

## Superficie agéntica y tokens por defecto

Nivel **mínimo** del Contrato ADS (sitio de contenido, sin `api_contracts` propios). Dashboard de
tokens **N1** (ledger simple), salvo que incluya el widget de FAQ con LLM, en cuyo caso **N2**. No
expone servidor MCP propio; si hay formulario, documenta su endpoint con OpenAPI mínimo para que un
agente pueda enviarlo sin credenciales.

## Riesgos de lock-in y plan de salida

- **Vercel/Netlify (deploy):** riesgo bajo — Next.js/Astro son estándar; el plan de salida es
  redeployar el mismo build en Cloudflare Pages o un contenedor Node.
- **Sanity (CMS headless):** riesgo medio — el contenido se exporta vía su API; mantener el esquema
  documentado fuera de la consola evita depender de su modelo de datos.
- **CMS corporativo (legacy):** riesgo alto — mitigar con una capa de abstracción de contenido
  (`portability.exit_plan` en `ads.yaml`, ver `/docs/adr/0012-portabilidad.md`) y exportaciones
  periódicas del contenido a un formato abierto (Markdown/JSON).

[^vercel-pricing]: Vercel — Pricing
[^cf-pages]: Cloudflare Pages Functions — Pricing
[^cf-workers]: Cloudflare Workers — Pricing
[^sanity-pricing]: Sanity — Pricing
[^webflow-pricing]: Webflow Help Center — Updated pricing (May 2026)
[^amplify-pricing]: AWS Amplify — Pricing
[^cloudrun-pricing]: Google Cloud Run — Pricing
[^astro]: Astro
[^nextjs]: Next.js — Blog (versión vigente)
[^framer-pricing]: Framer — Pricing
