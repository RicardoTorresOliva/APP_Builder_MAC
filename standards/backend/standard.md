---
type: Standard
title: Estándar de backend
description: Qué construye y cómo cualquier superficie de API producida por ABM.
tags: [backend, estandares, api]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Estándar de backend

## Diseño de API
- REST con OpenAPI como contrato primero (el contrato se escribe antes o junto con la
  implementación, no se genera después como documentación de relleno); o GraphQL con schema
  tipado; o RPC tipado. La elección queda en `stacks/` según el ADS.
- Versionado explícito y compatible hacia atrás dentro de una versión mayor; recursos nombrados de
  forma consistente; paginación basada en cursor para colecciones que pueden crecer.
- La superficie agéntica (cómo un agente externo descubre y opera esta API) se diseña junto con la
  API, no como un añadido: ver `standards/agentic/README.md`.

## Validación y errores
- Errores en `application/problem+json` (RFC 9457): `type`, `title`, `status`, `detail`,
  `instance`, y extensiones propias del dominio (p. ej. `errors[]` por campo).
- La validación de entrada ocurre en el borde de la API, antes de tocar lógica de negocio; el
  mensaje de error identifica el campo y la razón, nunca solo "solicitud inválida".

## AuthN/authZ y rate limiting
- Autenticación con un estándar abierto (OAuth 2.1/OIDC como categoría); autorización explícita por
  endpoint y por acción (RBAC o ABAC), nunca implícita en el cliente.
- Rate limiting declarado por endpoint o por cliente; respuesta `429` con cabecera `Retry-After` y
  cuerpo `problem+json`.

## Jobs, colas y caché
- Trabajo asíncrono en cola con reintentos y backoff exponencial; un job fallido tras el máximo de
  reintentos va a una cola de fallidos visible, nunca se pierde en silencio.
- Caché con invalidación explícita (por evento o por TTL documentado); nunca caché "hasta que
  alguien reinicie el proceso".

## Observabilidad
- Logs estructurados (JSON) con id de correlación por solicitud, propagado entre servicios.
- OpenTelemetry (trazas, métricas y logs) como estándar de instrumentación; ver
  `standards/observability/README.md`.

## Idempotencia
- Toda operación que muta estado y puede reintentarse (por el cliente, por una cola o por un
  agente) es idempotente: llave de idempotencia en la cabecera o upsert semántico por clave natural.
- Reintentar la misma solicitud con la misma llave devuelve el mismo resultado, no un efecto duplicado.

## Escalabilidad
- Servicios sin estado (el estado vive en base de datos, caché o cola, no en memoria del proceso).
- SLO/SLI declarados por endpoint crítico (disponibilidad, latencia p95/p99).
- Costo por unidad de negocio, incluido el costo de tokens si la API invoca un modelo de lenguaje
  (ver `standards/finops/README.md`).

## Tests
Ver `standards/testing.md` de esta carpeta: unitarios (lógica de dominio), de integración (contra
dependencias reales o equivalentes) y de contrato (el esquema publicado no rompe a sus consumidores).
