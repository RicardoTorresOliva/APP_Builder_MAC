---
type: Stack Sheet
title: Lenguajes dominantes en entornos corporativos
description: Versiones LTS vigentes, frameworks típicos por capa e interoperabilidad con legacy para TS/JS, Python, Java/Kotlin, C#/.NET, Go y PHP.
tags: [stacks, lenguajes, portabilidad, legacy]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:59:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: node-releases
    resource: https://nodejs.org/en/about/previous-releases
    title: Node.js — Releases
  - id: typescript-npm
    resource: https://www.npmjs.com/package/typescript
    title: TypeScript — npm
  - id: python-downloads
    resource: https://www.python.org/downloads/
    title: Python — Downloads
  - id: java-roadmap
    resource: https://www.oracle.com/java/technologies/java-se-support-roadmap.html
    title: Oracle Java SE Support Roadmap
  - id: kotlin-releases
    resource: https://kotlinlang.org/docs/releases.html
    title: Kotlin release process
  - id: dotnet-10
    resource: https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/
    title: Announcing .NET 10
  - id: php-versions
    resource: https://www.php.net/supported-versions.php
    title: "PHP: Supported Versions"
  - id: go-releases
    resource: https://go.dev/doc/devel/release
    title: Go — Release History
---

# Lenguajes dominantes en entornos corporativos

Versiones y estado de soporte verificados el 2026-09-27. Verifica de nuevo antes de fijar una
versión en un `ads.yaml`: los ciclos de EOL avanzan con el calendario, no con esta ficha.

## TypeScript / JavaScript

- **Runtime**: Node.js 24 es la Active LTS vigente; Node.js 22 sigue en Maintenance LTS; Node.js 26
  (Current desde mayo de 2026) entra a LTS en octubre de 2026[^node-releases].
- **Lenguaje**: TypeScript 7.0 es la versión estable vigente — primera versión con el compilador
  nativo (portado a Go), con builds 8–12× más rápidos que el compilador anterior; aún sin API
  programática estable (llega en 7.1)[^typescript-npm].
- **Frameworks típicos por capa**: frontend — framework de componentes con SSR/SSG; backend —
  framework HTTP minimalista o framework de aplicación con ORM/data-access integrado; el propio
  `abm.yaml → lint.products` lista las opciones nombrables fuera del núcleo.
- **Interoperabilidad con legacy**: cliente HTTP tipado generado desde OpenAPI para hablar con
  servicios Java/.NET; SDKs oficiales de colas (MQ, Kafka) tienen soporte maduro en Node; para SOAP
  legacy, un cliente SOAP-a-REST intermedio suele ser más barato que consumir WSDL directo desde JS.

## Python

- **Versión**: 3.14 es la recomendada para producción nueva (3.14.7, agosto de 2026); 3.13 recibe
  correcciones de bugs hasta octubre de 2026 y solo seguridad después, hasta 2029 — es la opción
  conservadora si el ecosistema de dependencias aún no soporta 3.14[^python-downloads].
- **Frameworks típicos por capa**: backend — framework de aplicación con ORM async o framework
  minimalista con validación de tipos en el borde; datos/IA — el ecosistema de Python es el
  estándar de facto para pipelines de datos y RAG/agentes.
- **Interoperabilidad con legacy**: drivers ODBC/JDBC-equivalentes maduros para SQL Server/Oracle;
  cliente SOAP con generación de stubs desde WSDL; buen soporte de bibliotecas para EDI/CSV/Excel en
  integraciones batch.

## Java / Kotlin

- **Java**: 25 es la LTS vigente (disponibilidad general 2025-09-16, soporte Premier de Oracle hasta
  2030); 21 y 17 siguen siendo LTS anteriores soportadas; la siguiente LTS planificada es Java 29
  (2027)[^java-roadmap].
- **Kotlin**: 2.4.0 es la versión estable vigente (julio de 2026), con soporte para Java 26 y
  parámetros de contexto estables[^kotlin-releases]. Kotlin corre sobre la JVM, así que hereda la
  LTS de Java elegida para el runtime.
- **Frameworks típicos por capa**: backend empresarial — framework de aplicación JVM con inyección
  de dependencias e integración nativa con colas/mensajería corporativa.
- **Interoperabilidad con legacy**: es el lenguaje con más madurez para hablar con SAP (conectores
  RFC/BAPI oficiales), colas MQ y mainframes vía adaptadores certificados; suele ser la opción por
  defecto cuando el legacy ya es JVM (Java/Scala/Kotlin previos).

## C# / .NET

- **Versión**: .NET 10 es la LTS vigente (disponibilidad general 2025-11-11, soporte hasta
  2028-11-14); .NET 9 y .NET 8 llegan a fin de soporte el 2026-11-10, así que son candidatos
  urgentes de migración si un ADS legacy sigue en ellos[^dotnet-10].
- **Frameworks típicos por capa**: backend — framework de aplicación web integrado en el propio
  runtime, con ORM oficial de primera parte.
- **Interoperabilidad con legacy**: primera opción natural cuando el entorno corporativo ya es
  Microsoft (Active Directory/Entra ID, SQL Server, SharePoint); drivers oficiales para SAP OData y
  colas de Microsoft; buen soporte para exponer o consumir SOAP heredado.

## Go

- **Versión**: 1.27 es la estable vigente (1.27.1, septiembre de 2026); Go no declara "LTS" formal,
  pero cada versión mayor recibe parches durante aproximadamente un año (hasta que dos versiones
  después la reemplaza)[^go-releases].
- **Frameworks típicos por capa**: backend — la biblioteca estándar HTTP es suficiente para muchos
  servicios; un router minimalista cubre el resto sin un framework pesado.
- **Interoperabilidad con legacy**: excelente para fachadas API y proxies (binario único, bajo
  consumo) delante de un legacy SOAP o de colas MQ; menos madurez que Java/.NET para conectores
  SAP oficiales — normalmente se apoya en la capa OData/REST en vez de RFC/BAPI directo.

## PHP

- **Versión**: 8.5 es la más reciente (soporte activo hasta 2027-12-31, seguridad hasta 2029);
  8.4 tiene soporte activo hasta 2026-12-31; 8.3 ya está en solo-seguridad hasta 2027-12-31; 8.2
  llega a fin de vida el 2026-12-31 — cualquier ADS en 8.2 necesita plan de migración
  inmediato[^php-versions].
- **Frameworks típicos por capa**: backend/CMS — framework de aplicación full-stack con ORM propio,
  o un CMS/e-commerce consolidado cuando el caso es de contenido o tienda.
- **Interoperabilidad con legacy**: sigue siendo dominante en backoffice de PYMEs y e-commerce
  heredado; buena cobertura de clientes SOAP y drivers para SQL Server/MySQL; menos común como
  cliente de mainframe o SAP RFC/BAPI directo (se prefiere una fachada intermedia en Java/.NET/Go).

## Cómo priorizar

Con el inventario de `assess` (ver `stacks/legacy.md`) en mano: si el legacy ya está en una
plataforma (JVM, .NET, PHP), la opción de menor fricción es continuar en esa familia para el código
que integra directo con él, y reservar TS/Python/Go para servicios nuevos desacoplados (fachadas,
BFFs, jobs de datos) que no necesitan compartir runtime con el legacy.

[^node-releases]: Node.js — Releases
[^typescript-npm]: TypeScript — npm
[^python-downloads]: Python — Downloads
[^java-roadmap]: Oracle Java SE Support Roadmap
[^kotlin-releases]: Kotlin release process
[^dotnet-10]: Announcing .NET 10
[^php-versions]: "PHP: Supported Versions"
[^go-releases]: Go — Release History
