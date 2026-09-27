---
type: Stack Sheet
title: "Caso: App móvil"
description: Paquetes multiplataforma (Expo/RN, Flutter) con backend, tiendas y equivalencias por nube.
tags: [stacks, mobile, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:25:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: expo-plans
    resource: https://docs.expo.dev/billing/plans/
    title: Expo — Subscriptions, plans, and add-ons
  - id: expo-sdk
    resource: https://expo.dev/changelog/sdk-57
    title: Expo SDK 57 — Changelog
  - id: flutter-release
    resource: https://docs.flutter.dev/release/release-notes
    title: Flutter — Release notes
  - id: supabase-billing
    resource: https://supabase.com/docs/guides/platform/billing-on-supabase
    title: Supabase Docs — Billing
  - id: clerk-pricing
    resource: https://clerk.com/pricing
    title: Clerk — Pricing
  - id: neon-pricing
    resource: https://neon.com/pricing
    title: Neon — Pricing
  - id: apple-sbp
    resource: https://developer.apple.com/app-store/small-business-program/
    title: Apple — App Store Small Business Program
  - id: hetzner-cloud
    resource: https://www.hetzner.com/cloud/
    title: Hetzner Cloud — Precios
  - id: keycloak-2670
    resource: https://www.keycloak.org/2026/07/keycloak-2670-released
    title: Keycloak 26.7.0 released
---

# Caso: App móvil

## Cuándo aplica

Aplicación nativa o multiplataforma distribuida por App Store/Google Play, con backend propio o
compartido con una web app. Perfil de ADS: **software-app**.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Expo (React Native, SDK 57) [^expo-sdk] | React Native con dev client (Expo) + módulos nativos | Flutter (sin cuota de build service) [^flutter-release] | React Native o nativo (Swift/Kotlin) integrado a MDM corporativo |
| Backend | Supabase (BE+DB+Auth) [^supabase-billing] | Node/NestJS dedicado + Postgres | API propia autoalojada (Docker) | .NET/Java del backend corporativo existente |
| Base de datos | Postgres de Supabase [^supabase-billing] | Neon Postgres (Launch/Scale) [^neon-pricing] | Postgres self-hosted en VPS [^hetzner-cloud] | SQL Server/Oracle corporativo |
| Auth | Auth de Supabase (incluida) [^supabase-billing] | Clerk (soporta React Native) [^clerk-pricing] | Keycloak self-hosted [^keycloak-2670] | Auth corporativa (Azure AD/Okta) + MDM |
| Pagos | Compras dentro de la app (IAP) de la tienda, 15% hasta US$1M/año [^apple-sbp] | IAP + Stripe para pagos fuera de la app si aplica | Igual que vibe coder (comisión de tienda no es evitable en IAP) | Distribución interna (Enterprise Program), sin comisión de tienda pública |
| Deploy/hosting (build/distribución) | EAS Build/Submit/Update Free (15 builds/mes) [^expo-plans] | EAS Starter (US$19/mes, créditos de build prioritario) [^expo-plans] | CI propio (GitHub Actions) para compilar Flutter | Distribución vía MDM corporativo (Intune/Workspace ONE), sin tiendas públicas |
| LLM/System One | Opcional: asistente en la app vía gateway LLM (ver `/stacks/llm-providers.md`) | Igual, con medición de tokens por usuario | Igual, modelo económico o autoalojado | Gateway LLM corporativo ya aprobado |
| Costo aprox./mes (2026-09) | US$0–25 (Supabase) + US$0 (EAS Free) + US$99/año cuenta Apple + US$25 único Google Play [^supabase-billing][^expo-plans] | US$19–199 (EAS) [^expo-plans] + ~US$15–40 (Neon) + US$25 (Clerk) [^neon-pricing][^clerk-pricing] | ~US$12–25/mes VPS (Hetzner) [^hetzner-cloud] + Keycloak gratis [^keycloak-2670] | Variable, ya contratado; n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media | Media–alta | Alta |

Comisión de tienda: Apple 15% hasta US$1M/año de proceeds (30% por encima); Google Play 15% en el
primer US$1M/año (30% por encima, y 15% en suscripciones desde el día uno) [^apple-sbp].

## Cuándo NO usar cada opción

- **Expo + Supabase:** no usar si se necesitan módulos nativos muy específicos sin librería Expo, o
  cifrado/hardware particular que exija un dev client permanente desde el inicio.
- **React Native pro/escalable:** sobra para un MVP de validación; EAS de pago y un backend dedicado
  son costo/operación innecesarios si Supabase alcanza.
- **Flutter low-cost/self-hosted:** no usar si el equipo ya domina el ecosistema React/TypeScript —
  Dart es un cambio de stack completo.
- **Corporativa (MDM):** no usar para un producto de consumo masivo fuera de la organización — la
  distribución interna no llega a tiendas públicas.

## Comprar vs construir

El runtime multiplataforma (Expo/Flutter) siempre se "compra" (se adopta open-source/gestionado); lo
que se construye es la lógica de negocio y, si aplica, la sincronización offline-first.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Backend API | Lambda/Fargate | Functions/App Service | Cloud Run | Kubernetes propio |
| Base de datos | RDS/Aurora Postgres | Database for PostgreSQL | Cloud SQL Postgres | Postgres en VM |
| Push notifications | SNS Mobile Push | Notification Hubs | Firebase Cloud Messaging | Servidor XMPP/APNs directo |
| Distribución de builds | S3+CloudFront (artefactos) | Blob+Front Door | Cloud Storage+CDN | Servidor de artefactos interno |

## Superficie agéntica y tokens por defecto

Nivel **mínimo** si es una app sin backend propio (solo consume APIs de terceros); **extendido** si
tiene backend y varios entornos. Dashboard de tokens **N1**, **N2** si incluye asistente con LLM.
Expone API propia vía OpenAPI si el backend es propio; servidor MCP opcional para operar cuentas de
usuario con scopes mínimos.

## Riesgos de lock-in y plan de salida

- **Expo/EAS:** riesgo bajo–medio — el código React Native es portable a un flujo de build propio
  (`expo prebuild` + Xcode/Gradle directos) si se abandona EAS.
- **Apple/Google (tiendas):** riesgo alto por comisión y reglas de revisión; no hay plan de salida
  real para distribución masiva, solo mitigación (distribución directa/Enterprise para casos B2B).
- **Supabase/Clerk:** riesgo bajo–medio, igual que en el caso SaaS web app (ver
  `/stacks/cases/saas-web-app.md` y `/docs/adr/0012-portabilidad.md`).

[^expo-plans]: Expo — Subscriptions, plans, and add-ons
[^expo-sdk]: Expo SDK 57 — Changelog
[^flutter-release]: Flutter — Release notes
[^supabase-billing]: Supabase Docs — Billing
[^clerk-pricing]: Clerk — Pricing
[^neon-pricing]: Neon — Pricing
[^apple-sbp]: Apple — App Store Small Business Program
[^hetzner-cloud]: Hetzner Cloud — Precios
[^keycloak-2670]: Keycloak 26.7.0 released
