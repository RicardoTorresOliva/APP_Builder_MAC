---
type: Stack Sheet
title: "Caso: ERP/CRM/backoffice"
description: Opciones de stack para un backoffice interno (ERP, CRM u operaciones), y cuándo comprar Odoo/ERPNext en vez de construir.
tags: [stacks, erp, crm, backoffice, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:05:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: vercel-pricing
    resource: https://vercel.com/docs/plans/hobby
    title: Vercel — Hobby plan
  - id: supabase-pricing
    resource: https://supabase.com/pricing
    title: Supabase — Pricing
  - id: do-pricing
    resource: https://www.digitalocean.com/pricing/droplets
    title: DigitalOcean — Droplet pricing
  - id: auth0-pricing
    resource: https://auth0.com/pricing
    title: Auth0 — Pricing
  - id: odoo-pricing
    resource: https://www.odoo.com/pricing
    title: Odoo — Pricing
  - id: frappe-pricing
    resource: https://frappe.io/erpnext/pricing
    title: "ERPNext (Frappe Cloud) — Pricing"
  - id: entra-id
    resource: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
    title: Microsoft Entra ID — protocols
---

# Caso: ERP/CRM/backoffice

## Cuándo aplica (perfil de ADS)

Perfil `software-app` (o `data-product` si el foco es solo reporting operativo), casi siempre con
`ads_contract_level: extendido` y ceremonia Producto o Enterprise-Regulado: usuarios internos
(empleados, no público), datos de negocio sensibles (clientes, inventario, facturación), necesidad
de auditoría y de integrarse con lo que la empresa ya usa (correo, IdP, banco, ERP existente).

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Framework de componentes + UI kit de tablas/formularios | Igual + design system propio, i18n | Igual, sin cambios | Framework de componentes integrado en el backend elegido (server-rendered) |
| Backend | BaaS con funciones (Supabase Edge Functions) | Framework de aplicación (Node/Python) con capa de dominio propia | Mismo framework, desplegado en un solo servidor | Backend JVM o .NET con capa de integración a los sistemas corporativos |
| Base de datos | Postgres gestionado del BaaS[^supabase-pricing] | Postgres gestionado con réplicas de lectura | Postgres autogestionado en el mismo servidor | SQL Server u Oracle ya operados por la empresa |
| Auth | Auth del BaaS (email/OAuth) | Delegada a IdP gestionado[^auth0-pricing] | Auth self-hosted (OIDC) | SSO corporativo (SAML/OIDC contra Entra ID)[^entra-id] |
| Pagos | N/D — backoffice interno no cobra directamente | N/D | N/D | Integración con el ERP/tesorería existente para conciliación |
| Deploy/hosting | PaaS gratuito para el frontend[^vercel-pricing] + BaaS | Contenedores en la nube con autoscaling | VPS único con Docker Compose[^do-pricing] | Nube corporativa (landing zone) u on-prem |
| LLM / System One | Gateway con un modelo económico para búsqueda/resumen | Gateway con routing por costo/latencia | Modelo local (Ollama) para tareas sin datos sensibles | Servicio LLM gestionado de la nube corporativa (gobernanza de datos) |
| Costo aproximado/mes | $0–25 (capas gratuitas)[^vercel-pricing][^supabase-pricing] | $75–400 según usuarios y datos[^supabase-pricing] | $6–24 (un droplet)[^do-pricing] | Variable por contrato; n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media–alta | Media (requiere operar infraestructura propia) | Alta (integraciones corporativas, cumplimiento) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar si hay más de un puñado de usuarios concurrentes con datos financieros
  sensibles, o si la empresa exige auditoría formal de accesos desde el día uno.
- **Pro/escalable**: sobra para un backoffice de 5 personas sin planes de crecer; el costo y la
  complejidad operativa no se justifican.
- **Low-cost/self-hosted**: no usar si el equipo no puede operar backups, parches de seguridad y
  monitoreo por sí mismo — un solo servidor sin ese cuidado es un riesgo, no un ahorro.
- **Corporativa/legacy**: no usar como punto de partida para un backoffice nuevo y pequeño sin
  legado que integrar; el costo de cumplir SSO/gobernanza corporativa desde cero no se paga solo.

## Comprar vs construir

Antes de construir un ERP/CRM a medida, evalúa comprar:

- **Odoo** (Community gratis y open source; Enterprise desde ≈$8.95–$76.20 por usuario/mes según
  plan y región, con descuento el primer año)[^odoo-pricing]: cubre CRM, inventario, facturación y
  más módulos listos; la app custom queda para lo que Odoo no cubre, integrada vía su API.
- **ERPNext** (open source; Frappe Cloud desde ≈$5/mes en hosting compartido, bench privado desde
  ≈$25/mes, sin cobro por usuario)[^frappe-pricing]: alternativa 100% open source a Odoo, con costo
  de hosting gestionado más bajo.
- **Construir a medida** se justifica cuando el proceso de negocio es el diferenciador competitivo
  (no un backoffice genérico), cuando Odoo/ERPNext no modelan bien el dominio sin una
  personalización mayor que reescribirlo, o cuando la integración con el legacy exige un control que
  un ERP empaquetado no da.
- Regla práctica: si más del 70% de los módulos que necesitas ya existen en Odoo/ERPNext, compra y
  personaliza; si es al revés, construye y usa Odoo/ERPNext solo como referencia de modelo de datos.

## Equivalencias por nube

Ver matriz completa en `/stacks/clouds.md`. Para este caso, los bloques más relevantes son base de
datos relacional gestionada (RDS/Aurora en AWS, Azure SQL/Database for PostgreSQL en Azure, Cloud
SQL/AlloyDB en GCP, Postgres autogestionado on-prem) e identidad (Entra ID en Azure/on-prem híbrido,
Cognito/IAM Identity Center en AWS, Identity Platform en GCP).

## Superficie agéntica y tokens por defecto

- **Descubrimiento**: `ads.yaml` + `AGENTS.md` propio del backoffice; servidor MCP con tools de
  solo lectura por defecto (consultar clientes, inventario, facturas) y tools de escritura detrás de
  scopes explícitos.
- **HITL obligatorio** en acciones rojas: emitir/anular facturas, mover dinero, cambiar permisos de
  usuario — nunca autónomas sin aprobación humana.
- **Auditoría**: cada acción de un agente sobre el backoffice queda registrada (quién, qué, cuándo,
  resultado).
- **Dashboard de tokens por defecto**: N2 (dashboard HTML estático desde el ledger) para ceremonia
  Producto; N3 (observabilidad en vivo con chargeback por tenant) si el perfil es
  Enterprise-Regulado o hay multi-tenant real.

## Riesgos de lock-in y plan de salida

- **BaaS (vibe coder)**: el mayor lock-in está en el auth y las funciones edge propietarias del BaaS.
  Plan de salida: mantener el esquema de Postgres portable (sin extensiones propietarias del BaaS en
  las tablas de negocio) y una capa de auth intercambiable detrás de una interfaz propia.
- **IdP gestionado (pro)**: migrar de un IdP a otro implica reconfigurar aplicaciones cliente.
  Mitigación: usar SAML/OIDC estándar y no features propietarias del proveedor de IdP.
- **Odoo/ERPNext**: los datos son propios (Postgres/MariaDB accesibles), pero los módulos y
  workflows personalizados no siempre migran limpio de uno a otro. Documentar cada personalización
  como si fuera código propio, con su propio control de versiones.
- **ERP corporativo existente (SAP u otro)**: nunca acoplar el ADS nuevo a un formato de datos
  interno del ERP; integrar siempre por su API oficial (OData/RFC/BAPI) para poder cambiar de ERP
  sin reescribir el backoffice nuevo.

[^vercel-pricing]: Vercel — Hobby plan
[^supabase-pricing]: Supabase — Pricing
[^do-pricing]: DigitalOcean — Droplet pricing
[^auth0-pricing]: Auth0 — Pricing
[^odoo-pricing]: Odoo — Pricing
[^frappe-pricing]: ERPNext (Frappe Cloud) — Pricing
[^entra-id]: Microsoft Entra ID — protocols
