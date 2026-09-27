---
type: Stack Sheet
title: "Caso: Dashboard/BI interno"
description: Paquetes para un panel de inteligencia de negocio de uso interno, comprar vs construir y equivalencias por nube.
tags: [stacks, bi, dashboard, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:15:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: retool-pricing
    resource: https://retool.com/pricing
    title: Retool — Pricing
  - id: metabase-pricing
    resource: https://www.metabase.com/pricing
    title: Metabase — Pricing
  - id: powerbi-pricing
    resource: https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing
    title: Microsoft Power BI — Pricing
  - id: hetzner-cloud
    resource: https://www.hetzner.com/cloud/
    title: Hetzner Cloud — Precios
  - id: coolify
    resource: https://coolify.io/self-hosted
    title: Coolify — Self-hosted
  - id: okta-pricing
    resource: https://www.okta.com/pricing/
    title: Okta — Pricing
  - id: cloudrun-pricing
    resource: https://cloud.google.com/run/pricing
    title: Google Cloud Run — Pricing
---

# Caso: Dashboard/BI interno

## Cuándo aplica

Panel de consulta para decisiones internas: métricas, reportes, exploración de datos, sin exponerse
a clientes externos. Perfil de ADS: **data-product** (dataset/dashboard que se *consulta*); usar
**software-app** en su lugar solo si el panel incluye lógica de negocio de escritura compleja más
allá de consultar y filtrar.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | UI generada por Retool sobre la conexión a datos [^retool-pricing] | UI de Metabase Cloud (Starter/Pro) [^metabase-pricing] | UI de Metabase open-source (AGPL, gratis) | UI de Power BI / Tableau (cliente de escritorio o web) [^powerbi-pricing] |
| Backend | Ninguno propio: Retool consulta la base directamente | Ninguno propio: Metabase consulta el warehouse | Ninguno propio: Metabase consulta Postgres | Ninguno propio: motor de BI corporativo ya operado por TI |
| Base de datos | Postgres/Supabase del ADS de origen (solo lectura) | Warehouse (Postgres/BigQuery) con réplica de solo lectura | Postgres autoalojado (Docker) en el mismo VPS | SQL Server/Oracle/Snowflake corporativo |
| Auth | Auth integrada de Retool (SSO en planes pagos) [^retool-pricing] | SSO integrado del plan Metabase Pro | Auth básica de Metabase (usuarios locales) | SSO corporativo (Azure AD/Okta) [^okta-pricing] |
| Pagos | No aplica | No aplica | No aplica | No aplica |
| Deploy/hosting | Gestionado por Retool (SaaS) [^retool-pricing] | Metabase Cloud (gestionado) [^metabase-pricing] | Contenedor Metabase en VPS Hetzner + Coolify [^hetzner-cloud][^coolify] | On-prem o en el tenant de Microsoft/Salesforce ya contratado |
| LLM/System One | Opcional: preguntas en lenguaje natural sobre datos (ver `/stacks/llm-providers.md`) | Igual, con capa de traducción a SQL auditada | Igual, modelo económico o autoalojado | Copilot del proveedor de BI ya licenciado (n/d, no-verificado) |
| Costo aprox./mes (2026-09) | US$0 (Free, ≤5 usuarios) hasta ~US$10–12/builder + US$5/usuario interno (Team) [^retool-pricing] | US$100/mes ≤5 usuarios (Starter) o US$575/mes ≤10 usuarios (Pro) [^metabase-pricing] | US$0 licencia + ~US$12–25/mes de VPS (Hetzner CX23) [^hetzner-cloud] | US$14/usuario/mes (Power BI Pro) o US$24 (Premium por usuario) [^powerbi-pricing]; Tableau: n/d (no-verificado) |
| Curva de aprendizaje | Baja | Baja–media | Media (operar Postgres/Metabase) | Media–alta (gobierno de datos corporativo) |

## Cuándo NO usar cada opción

- **Retool:** no usar si el número de usuarios internos es alto (cientos) — el costo por builder e
  interno escala rápido frente a un BI de solo consulta.
- **Metabase Cloud:** no usar si el presupuesto es cero — la versión open-source cubre el mismo caso
  sin costo de licencia.
- **Metabase open-source self-hosted:** no usar si se necesita SSO o embedding avanzado sin pagar —
  esas funciones están en los planes de pago.
- **Power BI/Tableau corporativo:** no usar si la empresa no tiene ya licencias M365/Tableau — el
  costo por usuario es alto frente a Metabase open-source para un panel puntual.

## Comprar vs construir

BI interno casi siempre se "compra" (Retool/Metabase/Power BI): construir un dashboard a medida con
un framework de frontend solo se justifica cuando las visualizaciones son muy específicas del
dominio y no caben en una herramienta de BI genérica, o cuando el panel debe embeberse dentro de
otro ADS como parte de su propia UI.

## Equivalencias por nube

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Compute (Metabase self-hosted) | ECS Fargate | Container Apps | Cloud Run [^cloudrun-pricing] | Kubernetes/Docker propio |
| Warehouse | Redshift | Synapse Analytics | BigQuery | Postgres/warehouse propio |
| SSO | IAM Identity Center | Azure AD | Identity Platform | Active Directory on-prem |
| BI gestionado equivalente | QuickSight | Power BI (Azure) [^powerbi-pricing] | Looker | Power BI Report Server on-prem |

## Superficie agéntica y tokens por defecto

Nivel **mínimo** del Contrato ADS si el panel solo consulta; **extendido** si alimenta decisiones
automatizadas de otro ADS. Dashboard de tokens **N1** (no usa LLM) salvo que tenga preguntas en
lenguaje natural, en cuyo caso **N2**. Expone datos solo vía un conector SQL de **solo lectura** o
la API de la herramienta de BI; nunca acceso de escritura directo a producción.

## Riesgos de lock-in y plan de salida

- **Retool:** riesgo medio — las apps quedan definidas en su formato propio; mitigar manteniendo las
  queries SQL fuera de Retool, versionadas junto al ADS de origen.
- **Metabase:** riesgo bajo — open-source, las preguntas guardadas se exportan como SQL.
- **Power BI/Tableau:** riesgo alto si hay reportes complejos en su lenguaje propietario (DAX/Tableau
  calc); mitigar documentando las métricas como SQL versionado, no solo dentro del dashboard (ver
  `/docs/adr/0012-portabilidad.md`).

[^retool-pricing]: Retool — Pricing
[^metabase-pricing]: Metabase — Pricing
[^powerbi-pricing]: Microsoft Power BI — Pricing
[^hetzner-cloud]: Hetzner Cloud — Precios
[^coolify]: Coolify — Self-hosted
[^okta-pricing]: Okta — Pricing
[^cloudrun-pricing]: Google Cloud Run — Pricing
