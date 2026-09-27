---
type: Stack Sheet
title: Patrones de integración con legacy corporativo
description: Catálogo de patrones de integración, conectores típicos, SSO corporativo y redes privadas, y su uso desde el comando assess.
tags: [stacks, legacy, portabilidad, integraciones]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:58:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: strangler-fig
    resource: https://martinfowler.com/bliki/StranglerFigApplication.html
    title: "Martin Fowler — StranglerFigApplication"
  - id: acl-pattern
    resource: https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
    title: "Azure Architecture Center — Anti-corruption Layer pattern"
  - id: cdc-debezium
    resource: https://debezium.io/documentation/
    title: Debezium — Change Data Capture
  - id: sap-odata
    resource: https://api.sap.com/
    title: SAP API Business Hub (OData / RFC / BAPI)
  - id: entra-saml-oidc
    resource: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
    title: "Microsoft Entra ID — OAuth 2.0 / OIDC / SAML protocols"
  - id: rpa-uipath
    resource: https://docs.uipath.com/
    title: UiPath Docs
---

# Patrones de integración con legacy corporativo

## Catálogo de patrones

| Patrón | Cuándo usar | Cuándo NO usar |
|---|---|---|
| Strangler fig[^strangler-fig] | Reemplazar un sistema grande de forma incremental: rutas nuevas al sistema nuevo, el resto sigue en el viejo hasta migrarlo por partes | El sistema viejo se apaga por completo en un solo corte (big bang), o es tan pequeño que reescribirlo es más barato que envolverlo |
| Anti-corruption layer (ACL)[^acl-pattern] | El modelo de dominio del legacy contamina el dominio nuevo (nombres, unidades, reglas implícitas); se necesita una traducción explícita en la frontera | Los dos sistemas ya comparten el mismo modelo de dominio — la capa solo añadiría indirección sin valor |
| Fachada API | Exponer una API moderna (REST/GraphQL) sobre un sistema legacy sin API propia (SOAP viejo, procedimientos almacenados, archivos planos) | El legacy ya expone una API razonable — construir una fachada duplicaría el contrato sin necesidad |
| CDC / eventos[^cdc-debezium] | Sincronizar datos casi en tiempo real sin tocar el sistema origen (lee el log de cambios de la base de datos) | El origen no expone log de cambios accesible (algunos mainframes) o la latencia de CDC no es aceptable para el caso de uso |
| Batch / SFTP / EDI | Integraciones nocturnas o por lotes con socios/sistemas que solo hablan archivos planos o EDI (retail, banca, logística) | Se necesita consistencia en tiempo real; el volumen o la frecuencia hacen el batch inviable |
| Mensajería corporativa | El legacy ya publica/consume en un bus corporativo (MQ, ESB) y sumarse a ese bus es más barato que integrarlo directo | No existe bus corporativo y crear uno solo para esta integración es sobre-ingeniería |
| RPA (último recurso) | No existe ninguna API, base de datos accesible ni archivo de intercambio — solo una UI de escritorio o web sin contrato | Cualquiera de los patrones anteriores es viable: RPA es frágil (se rompe con cambios de UI), difícil de auditar y de escalar |

Orden de preferencia: API/eventos > batch/archivo > RPA. RPA se documenta siempre como solución
temporal con fecha de reemplazo, nunca como arquitectura objetivo.

## Conectores típicos

| Sistema legacy | Vía de integración |
|---|---|
| SQL Server / Oracle / DB2 | Driver JDBC/ODBC de solo lectura con credenciales de mínimo privilegio; CDC sobre el log de transacciones cuando el motor lo soporta |
| Servicios SOAP/WSDL | Cliente SOAP generado desde el WSDL; envolver con una fachada REST/GraphQL si hay más de un consumidor nuevo |
| ERPs tipo SAP[^sap-odata] | OData (lectura/escritura moderna), RFC/BAPI (llamadas a función remotas) según lo que exponga la instancia; nunca acceso directo a las tablas |
| Mainframe | Colas MQ, o APIs REST cuando el mainframe las expone (muchos ya tienen una capa de modernización); evitar acceso directo a datasets |

## SSO corporativo y redes

- **SAML / OIDC**: el ADS delega autenticación al IdP corporativo (Entra ID/Azure AD u otro
  directorio SAML/OIDC[^entra-saml-oidc]) en vez de tener su propia base de usuarios. El ADS nunca
  guarda contraseñas del directorio corporativo.
- **Proxies y redes privadas**: cuando el legacy vive en una red que no es accesible desde internet,
  la integración corre detrás de un proxy corporativo o una VPN/red privada (peering, túnel, agente
  saliente) — documenta el requisito de red en `ads.yaml` para que el despliegue no falle en
  silencio por un firewall.
- **On-prem**: el patrón elegido debe funcionar sin salida a internet si esa es la restricción; evita
  diseñar una integración que asuma acceso público al legacy.

## RPA como último recurso

Si tras revisar API, base de datos, archivo/EDI y bus corporativo ninguno es viable, RPA
(UiPath[^rpa-uipath] u otra herramienta de automatización de UI) es la opción restante. Documenta
siempre: qué pantalla automatiza, qué rompe el flujo (cambios de versión, layout, captcha), quién es
dueño del mantenimiento, y el plan para reemplazarlo por una integración real cuando exista.

## Uso desde `assess`

El comando `assess` (Fase 4, encargo de portabilidad) inventaría el stack existente y lo registra en
OKF: lenguajes y frameworks en uso, bases de datos y su motor/versión, middleware (bus, ESB, colas),
IdP y protocolo (SAML/OIDC/LDAP), pipeline de CI/CD, nube u on-prem, y restricciones de red
(proxies, VPN, listas de acceso). A partir de ese inventario:

1. Clasifica cada sistema que el nuevo ADS debe tocar según el catálogo de patrones de arriba.
2. Prioriza según el diagnóstico: lo que ya tiene API se integra directo; lo que no, entra en la
   cola de "necesita fachada/ACL"; lo que es solo UI entra en la cola de RPA solo si no hay
   alternativa.
3. Registra el inventario y las decisiones de patrón en OKF para que el resto de la construcción
   (planificación, contrato ADS, revisión) las lea sin tener que re-descubrir el legacy.

Ver también `stacks/languages.md` (interoperabilidad por lenguaje) y `stacks/clouds.md`
(equivalencias si el legacy migra de nube u on-prem a nube).

[^strangler-fig]: Martin Fowler — StranglerFigApplication
[^acl-pattern]: Azure Architecture Center — Anti-corruption Layer pattern
[^cdc-debezium]: Debezium — Change Data Capture
[^sap-odata]: SAP API Business Hub (OData / RFC / BAPI)
[^entra-saml-oidc]: Microsoft Entra ID — OAuth 2.0 / OIDC / SAML protocols
[^rpa-uipath]: UiPath Docs
