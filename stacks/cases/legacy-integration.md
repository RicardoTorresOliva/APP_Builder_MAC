---
type: Stack Sheet
title: "Caso: integración sobre legacy corporativo"
description: Opciones de stack cuando el ADS es, en sí mismo, una capa de modernización o integración sobre sistemas corporativos existentes.
tags: [stacks, legacy, integracion, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:10:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: entra-id
    resource: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
    title: Microsoft Entra ID — protocols
  - id: sap-odata
    resource: https://api.sap.com/
    title: SAP API Business Hub (OData / RFC / BAPI)
  - id: do-pricing
    resource: https://www.digitalocean.com/pricing/droplets
    title: DigitalOcean — Droplet pricing
  - id: n8n-pricing
    resource: https://n8n.io/pricing/
    title: n8n — Pricing
---

# Caso: integración sobre legacy corporativo

## Cuándo aplica (perfil de ADS)

Perfil `software-app` (a veces `data-product` si el entregable es principalmente un flujo de datos)
cuyo propósito explícito es conectar un sistema nuevo con uno o más sistemas corporativos existentes:
una fachada API sobre un ERP, un puente de eventos entre el legacy y una app nueva, o un adaptador
que traduce el modelo de datos del legacy al del ADS nuevo. Ceremonia normalmente
Producto/Enterprise-Regulado desde el inicio, porque toca sistemas de los que ya depende el negocio.
Este caso complementa `/stacks/legacy.md` (el catálogo de patrones) con las opciones de stack para
construir la capa de integración misma; usa siempre `assess` primero para inventariar lo existente.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | N/D (la mayoría de estas capas no tienen UI propia) | Panel mínimo de estado/observabilidad de la integración | Igual, sin cambios | Consola de la plataforma de integración corporativa si ya existe |
| Backend | Script programado (batch) en Python | Servicio dedicado (fachada API o consumidor de eventos) en el lenguaje que ya domina el equipo | Motor de automatización self-hosted (n8n) para el flujo[^n8n-pricing] | Servicio en el lenguaje/plataforma que ya opera el legacy (Java/.NET) con conectores oficiales[^sap-odata] |
| Base de datos | Ninguna propia; lee/escribe directo sobre el legacy con credenciales de mínimo privilegio | Base de datos de staging propia (para reintentos, deduplicación, auditoría del puente) | Postgres autogestionado como staging | Base de datos corporativa existente + tabla/cola de staging bajo el mismo gobierno |
| Auth | Credencial de servicio de solo lectura sobre el legacy | Igual + rotación gestionada en un gestor de secretos | Igual + gestor de secretos self-hosted | SSO corporativo para la consola; cuenta de servicio de mínimo privilegio para la integración[^entra-id] |
| Pagos | N/D | N/D | N/D | N/D salvo que el flujo toque conciliación financiera |
| Deploy/hosting | Job programado (cron) en un runner existente | Contenedor con reintentos y colas | VPS único con el motor self-hosted[^do-pricing] | Nube corporativa u on-prem, dentro de la misma red que el legacy |
| LLM / System One | N/D (la traducción de datos rara vez necesita LLM) | Opcional: LLM para mapear campos ambiguos en la primera pasada de descubrimiento, con validación humana | N/D | Servicio LLM gestionado de la nube corporativa si el mapeo de datos lo justifica |
| Costo aproximado/mes | $0 (job en infraestructura ya existente) | $50–200 (contenedor + colas)[^do-pricing] | $6–24 de VPS[^do-pricing] | Variable por contrato; n/d (no-verificado) |
| Curva de aprendizaje | Baja–media | Media–alta (idempotencia, reintentos, conciliación) | Media | Alta (conectores oficiales, red corporativa) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar un script batch simple si el legacy no tolera lecturas frecuentes sin
  throttling, o si se necesita latencia casi real (usar CDC/eventos en su lugar, ver `/stacks/legacy.md`).
- **Pro/escalable**: sobra construir un servicio dedicado para una sincronización que corre una vez al
  día y tolera fallos manuales — un job programado simple es más barato de operar.
- **Low-cost/self-hosted**: no usar si el legacy exige estar dentro de una red privada específica que
  el VPS elegido no puede alcanzar sin una VPN adicional que complique más de lo que ahorra.
- **Corporativa/legacy**: no usar conectores oficiales pesados (RFC/BAPI completo) para una integración
  puntual y de bajo volumen donde una exportación batch cubre el caso igual de bien y más simple.

## Comprar vs construir

Rara vez hay un producto que "compre" la integración completa: se compra, a lo sumo, el **conector**
(driver JDBC/ODBC, SDK oficial de SAP, motor de automatización) y se construye la lógica de mapeo y
reconciliación específica del negocio, porque esa lógica es única de cada empresa. Una plataforma de
integración corporativa completa (ESB/iPaaS empresarial) se compra cuando la organización ya tiene o
va a tener decenas de integraciones similares — no se justifica para una sola.

## Equivalencias por nube

Ver `/stacks/clouds.md` para colas/eventos (backbone del patrón CDC/eventos) y secretos (credenciales
del legacy). La particularidad de este caso es que el cómputo elegido debe poder alcanzar la red del
legacy — si el legacy es on-prem, el cómputo en la nube necesita VPN/peering o un agente saliente
desde dentro de la red corporativa, documentado en `ads.yaml` como restricción de red.

## Superficie agéntica y tokens por defecto

- Todo acceso de un agente al legacy es de solo lectura por defecto; cualquier escritura hacia el
  legacy es una acción roja con HITL obligatorio, porque un error de escritura en un sistema del que
  depende el negocio es más costoso de revertir que en un sistema nuevo.
- Auditoría exhaustiva: qué leyó, qué transformó, qué escribió, con qué resultado — el legacy no
  siempre tiene su propio log de auditoría accesible, así que la capa de integración lo provee.
- **Dashboard de tokens por defecto**: N1, salvo que el mapeo de campos use LLM en cada ejecución, en
  cuyo caso N2 para llevar el costo variable bajo control.

## Riesgos de lock-in y plan de salida

- **Conector oficial de un ERP** (SAP u otro): el conector en sí es del proveedor del ERP, no de esta
  integración — el plan de salida real es documentar el mapeo de campos y reglas de negocio de forma
  independiente del conector, para poder re-implementarlo contra otro conector si el ERP cambia.
- **Motor de automatización self-hosted**: bajo riesgo si es open source (n8n); el flujo migra a la
  versión gestionada del mismo motor sin reescritura.
- **Acoplamiento al esquema interno del legacy**: el riesgo más alto de este caso — nunca leer/escribir
  contra tablas internas del legacy directamente si existe una API oficial; el esquema interno cambia
  sin aviso entre versiones del sistema legacy y rompe la integración en silencio.

[^entra-id]: Microsoft Entra ID — protocols
[^sap-odata]: SAP API Business Hub (OData / RFC / BAPI)
[^do-pricing]: DigitalOcean — Droplet pricing
[^n8n-pricing]: n8n — Pricing
