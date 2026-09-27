---
type: Integration Guide
title: Observabilidad — espacio de tokens en producción (N3)
description: Backends posibles, presupuestos y alertas por tenant/funcionalidad, chargeback y qué no capturar por PII.
tags: [observabilidad, otel, tokens, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: otel-genai-registry
    resource: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/gen-ai.md
    title: Gen AI attribute registry — semantic-conventions-genai
---

# Observabilidad — espacio de tokens en producción (N3)

Nivel N3 del espacio de control de tokens (`/docs/adr/0013-espacio-de-tokens.md`): dashboard en vivo
sobre la pila de observabilidad elegida, para ADS enterprise o regulados que ya operan con tráfico
real.

## Qué resuelve N3 que N1/N2 no
N1 (`TOKENS.md`) y N2 (dashboard HTML estático) sirven para construcción y para un producto en
operación con bajo volumen. N3 es para cuando el volumen exige alertas en tiempo real, presupuesto
por tenant/funcionalidad y series históricas que un archivo estático no sostiene.

## Backends posibles (categoría, con ejemplos)
| Categoría | Ejemplos |
|---|---|
| Backend de trazas/métricas autoalojado | Jaeger, Prometheus + Grafana |
| Backend SaaS de observabilidad | Plataformas comerciales de APM con soporte OTLP nativo |
| Backend gestionado por la nube | Servicios de trazas/métricas de AWS, Azure o GCP |

Cualquiera que hable **OTLP** (OpenTelemetry Protocol) sirve como destino — ABM no ata el pipeline a
un backend específico. Detalle técnico y config de ejemplo: [n3-otel.md](n3-otel.md) y
`otel-collector.example.yaml`.

## Presupuestos y alertas
Definidos en `ads.yaml → tokens.budgets`, por sesión, FU/DU/WU y funcionalidad (ADR 0013). Umbral
blando → entra a la cola de pendientes; tope duro → `abm tokens budget` falla y bloquea CI. En N3,
el mismo umbral dispara una alerta en el backend de observabilidad, no solo en CI — un tenant que se
dispara en producción se detecta sin esperar al próximo build.

## Chargeback
Con el ledger etiquetado por tenant y funcionalidad (esquema del evento en ADR 0013), N3 permite
atribuir costo real (cuando hay precio en `pricing.yaml`) o consumo medido (cuando no) a quien lo
generó — insumo para chargeback interno, no solo para observar tendencia.

## Qué NO capturar por PII
Los siguientes campos de las convenciones GenAI de OpenTelemetry están marcados explícitamente como
posible información sensible y no se capturan por defecto sin control de redacción:
`gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`,
`gen_ai.tool.call.arguments`/`.result`[^otel-genai-registry]. El ledger de tokens de ABM registra
recuentos y metadatos (proveedor, modelo, tool, actor, comando, tenant, costo) — nunca el contenido
de los mensajes.

[^otel-genai-registry]: Gen AI attribute registry — semantic-conventions-genai
