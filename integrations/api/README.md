---
type: Integration Guide
title: Integraciones vía API — clientes tipados
description: Clientes generados desde OpenAPI, reintentos con jitter, idempotencia, timeouts y errores problem+json.
tags: [api, openapi, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: rfc9457
    resource: https://www.rfc-editor.org/info/rfc9457/
    title: "RFC 9457: Problem Details for HTTP APIs"
---

# Integraciones vía API — clientes tipados

## Cliente tipado desde OpenAPI, no a mano
Un cliente escrito a mano contra una API de terceros diverge de la spec en la primera actualización
que no rompe compatibilidad pero cambia un tipo. Generar el cliente desde el `openapi.yaml`/`.json`
oficial del proveedor (categoría: generador de clientes desde OpenAPI) mantiene el cliente
sincronizado con cada regeneración, y falla en build si la spec cambia de forma incompatible.

Si el proveedor no publica OpenAPI pero sí un SDK oficial, usa el SDK
(`/integrations/other-ways.md`) antes que escribir un cliente a mano.

## Reintentos con backoff exponencial y jitter
Reintentar sin jitter sincroniza los reintentos de múltiples clientes y agrava una sobrecarga
(thundering herd). Patrón mínimo:
- reintentar solo códigos idempotentes o marcados con `Retry-After`/`429`/`5xx`;
- backoff exponencial con jitter completo (`espera = aleatorio(0, base * 2^intento)`);
- tope de intentos y de tiempo total — nunca reintento infinito.

## Idempotency keys
Toda operación que muta estado (un POST que crea un recurso, p. ej. un cobro o un envío) lleva una
clave de idempotencia generada por el cliente (un UUID por intento lógico, no por intento de red)
en un header (`Idempotency-Key` es la convención más extendida). El servidor debe devolver el mismo
resultado ante la misma clave — sin eso, un reintento tras timeout puede duplicar la operación.

## Timeouts y rate limits
- Timeout explícito por llamada (conexión + lectura), nunca "espera indefinida": un tercero caído
  no debe colgar al ADS.
- Respetar los rate limits declarados del proveedor (headers `X-RateLimit-*` o `Retry-After`); un
  cliente que los ignora arriesga el baneo temporal de la cuenta completa.

## Errores estructurados: `application/problem+json`
**RFC 9457, "Problem Details for HTTP APIs"** (obsoleta a RFC 7807) define el media type para
errores legibles por máquina: `{type, status, title, detail, instance, ...extensiones}`[^rfc9457].
Un ADS que expone su propia API HTTP devuelve sus errores en este formato (§4.8 del prompt maestro)
— así el manejo de errores es uniforme entre ADS, y un agente que los consume no necesita parsear
texto libre para decidir si reintentar, escalar o abortar.

[^rfc9457]: RFC 9457: Problem Details for HTTP APIs
