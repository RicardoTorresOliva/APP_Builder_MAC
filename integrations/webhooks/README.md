---
type: Integration Guide
title: Webhooks — recepción segura de eventos
description: Verificación de firma HMAC, timestamp y replay, idempotencia y cola de procesamiento.
tags: [webhooks, seguridad, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
---

# Webhooks — recepción segura de eventos

## Verificación de firma HMAC

El proveedor firma cada payload con una clave secreta compartida; el receptor recalcula la firma
sobre el **cuerpo crudo** (antes de parsear JSON) y la compara con una comparación de tiempo
constante:

```text
firma_esperada = HMAC-SHA256(secreto_webhook, cuerpo_crudo_bytes)
si no constant_time_eq(firma_esperada, header["X-Signature"]):
    responder 401, descartar
```

Nunca recalcular la firma sobre el JSON reserializado: el reordenamiento de claves o un espacio
distinto rompe la comparación aunque el evento sea legítimo.

## Timestamp y replay

El header de firma casi siempre incluye un timestamp; el receptor lo valida contra una ventana de
tolerancia (p. ej. 5 minutos) antes de aceptar el evento, y guarda el id del evento ya procesado
para descartar reentregas fuera de esa ventana:

```text
si abs(ahora() - timestamp_header) > 300s:
    responder 401, descartar  # posible replay
```

## Idempotencia

El proveedor puede reentregar el mismo evento (timeout de su lado, reintento propio). El receptor
guarda el `event_id` procesado (tabla o caché con TTL) y responde 200 sin reprocesar si ya existe:

```text
si event_id in procesados:
    responder 200          # ya procesado, no repetir efectos
sino:
    encolar(evento)
    procesados.add(event_id)
```

## Cola de procesamiento, no lógica en el handler HTTP

El endpoint que recibe el webhook solo verifica firma + timestamp + idempotencia y encola el evento;
el procesamiento real (efectos de negocio) corre async, fuera del ciclo de request/response del
proveedor. Así un procesamiento lento no causa que el proveedor reintente por timeout, duplicando
el evento:

```text
POST /webhooks/proveedor:
    verificar_firma(cuerpo, header)
    verificar_timestamp(header)
    si not visto(event_id): encolar(evento); marcar_visto(event_id)
    return 200              # inmediato, antes de procesar
```

## Checklist mínimo

- [ ] Firma verificada con comparación de tiempo constante, sobre el cuerpo crudo
- [ ] Timestamp dentro de la ventana de tolerancia
- [ ] `event_id` deduplicado antes de encolar
- [ ] Procesamiento async, respuesta HTTP inmediata
- [ ] Secreto del webhook fuera del repo (`/integrations/secrets.md`)
