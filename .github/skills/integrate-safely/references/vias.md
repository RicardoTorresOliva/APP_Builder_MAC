---
type: Reference
title: Vías de integración por categoría
description: Comparación de vías de integración (API directa, webhook, MCP, cola de eventos, automatización de navegador) con su superficie de riesgo, sin nombrar productos.
tags: [referencia, integraciones, seguridad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Vías de integración

| Vía | Cuándo es la de menor privilegio | Superficie de riesgo principal | Mitigación mínima |
|---|---|---|---|
| API directa (solicitud saliente) | El ADS necesita leer o escribir algo puntual, bajo su control | Credencial con scope amplio si el proveedor no permite acotar | Scope mínimo posible; rotación periódica |
| Webhook entrante | El proveedor debe avisar al ADS de un evento, sin que el ADS tenga que sondear | Endpoint público, payload no confiable | Firma verificada (secreto compartido), payload tratado como dato |
| Servidor MCP | El ADS expone o consume capacidades a otro agente, con necesidad de auditoría por tool | Tool con privilegio mayor al que declara (`readOnlyHint`/`destructiveHint` incorrectos) | Hints correctos, `dry_run` por defecto en escritura, log de auditoría |
| Cola de eventos / mensajería | Desacoplar productor y consumidor, o absorber picos de tráfico | Mensaje malformado o repetido (falta de idempotencia) | Procesamiento idempotente, cola de reintento con tope |
| Automatización de navegador / RPA | No existe API ni webhook y la interacción es de bajo volumen | Credencial de usuario humano reutilizada por el agente, acciones difíciles de auditar | Cuenta de servicio dedicada si el proveedor la ofrece; HITL antes de cualquier acción irreversible |

## Regla de decisión

1. Si existe una API o webhook con scope acotado: úsala antes que automatización de navegador.
2. Si el ADS mismo debe ser operable por otros agentes: la vía es un servidor MCP, no una API ad
   hoc — así el mínimo privilegio queda declarado por tool (`readOnlyHint`/`destructiveHint`), no
   solo por credencial.
3. Automatización de navegador es el último recurso: mayor superficie de riesgo y menor
   auditabilidad; documenta explícitamente por qué no alcanzó ninguna otra vía.

## Fallback ante fallo del proveedor externo

Ninguna integración falla en silencio: reintento acotado con backoff, cola de reintento visible, o
degradación explícita (el ADS informa que esa función no está disponible) — nunca un error tragado
que deje al consumidor sin saber qué pasó.
