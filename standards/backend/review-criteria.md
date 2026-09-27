---
type: Reference
title: Criterios de revisión — backend
description: Qué mira el revisor independiente de API y con qué severidad.
tags: [backend, revision, severidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Criterios de revisión — backend

El revisor usa un contexto limpio (nunca quien construyó, AGENTS.md §Unidades de trabajo).

## Bloqueante
- Endpoint mutante sin autenticación o autorización explícita.
- Operación mutante no idempotente que puede duplicar efecto (cobro, envío, alta) ante un reintento.
- Secreto, credencial o dato personal expuesto en un log, error o respuesta.
- Error que no sigue `problem+json` y oculta la causa real al consumidor.

## Mayor
- Falta rate limiting en un endpoint público de alto costo.
- Job sin reintento ni cola de fallidos: un fallo se pierde en silencio.
- Contrato de API (OpenAPI/schema) desactualizado respecto a la implementación.
- Test de contrato ausente en un cambio que toca el esquema publicado.

## Menor
- Nombre de recurso o campo inconsistente con el resto de la API.
- Log estructurado con campos faltantes que no impiden correlacionar la solicitud.
- SLO declarado pero sin métrica todavía conectada (aceptable en prototipo, no en producto).

## Evidencia esperada
Contrato publicado, ejemplo de respuesta de error real, resultado de los tests (unitarios,
integración, contrato) por archivo, y traza o log de una solicitud representativa.
