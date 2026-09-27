---
type: Integration Guide
title: N3 — exportar el ledger a OpenTelemetry
description: Mapeo de atributos gen_ai.*, la métrica de tokens y el pipeline OTel del nivel N3.
tags: [otel, tokens, observabilidad, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: otel-genai-old-registry
    resource: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
    title: Gen AI (moved) — OpenTelemetry semantic conventions
  - id: otel-genai-registry
    resource: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/gen-ai.md
    title: Gen AI attribute registry — semantic-conventions-genai
  - id: otel-genai-blog
    resource: https://opentelemetry.io/blog/2026/genai-observability/
    title: Inside the LLM Call — GenAI Observability with OpenTelemetry
---

# N3 — exportar el ledger a OpenTelemetry

## Estado de las convenciones GenAI
Todo atributo, span, métrica y evento `gen_ai.*` está marcado **"Development"** (antes
"experimental") — ninguno es "Stable" a la fecha[^otel-genai-old-registry]. Las convenciones viven
en un repo propio (`open-telemetry/semantic-conventions-genai`), separado del core, para iterar más
rápido[^otel-genai-blog]. Diseñar el pipeline N3 sabiendo que los nombres de atributos pueden cambiar
antes de estabilizarse.

## Mapeo del evento del ledger a atributos `gen_ai.*`
El esquema del evento de tokens (`contract/token-event.schema.json`, ADR 0013) mapea 1:1 a atributos
confirmados:

| Campo del ledger | Atributo OTel |
|---|---|
| proveedor | `gen_ai.provider.name` |
| modelo | `gen_ai.request.model` / `gen_ai.response.model` |
| herramienta / tool | `gen_ai.tool.name` |
| tokens de entrada | `gen_ai.usage.input_tokens` |
| tokens de salida | `gen_ai.usage.output_tokens` |
| tokens de caché | `gen_ai.usage.cache_read.input_tokens` / `.cache_creation.input_tokens` |
| comando / actor | `gen_ai.agent.id` / `gen_ai.agent.name` |

Cada desglose de tokens (caché, razonamiento) debe sumar también al total correspondiente
[^otel-genai-registry].

## Métrica: `gen_ai.client.token.usage`
Histograma con el tipo de token distinguido por `gen_ai.token.type` (`input`/`output`) y dimensiones
`gen_ai.operation.name`/`gen_ai.provider.name`/`gen_ai.request.model`[^otel-genai-old-registry]. Es
la métrica que alimenta presupuestos y alertas por tenant/funcionalidad en el backend elegido.

## Pipeline
1. El emisor del evento del ledger (agente, CLI, servidor MCP de ABM) publica el equivalente OTLP
   del evento — traza o métrica, según lo que soporte el emisor.
2. Un OpenTelemetry Collector recibe por OTLP y exporta al backend elegido (categoría en
   `/integrations/observability/README.md`). Config de ejemplo: `otel-collector.example.yaml`.
3. El backend calcula presupuesto/alerta por tenant y funcionalidad sobre las dimensiones del punto
   anterior.

## Qué no exportar
Ver la lista de campos marcados como PII potencial en `/integrations/observability/README.md` — el
contenido de mensajes y los argumentos/resultados de tools no salen del ledger sin redacción
explícita[^otel-genai-registry].

## Precios
Las cifras de costo del ledger (no las de la telemetría en sí) vienen de
`integrations/observability/pricing.yaml` (mantenido por otra unidad de trabajo; existe, con fuente
y fecha por proveedor — ADR 0013). Sin precio para un proveedor/modelo, el costo se reporta como
"n/d", nunca inventado.

[^otel-genai-old-registry]: Gen AI (moved) — OpenTelemetry semantic conventions
[^otel-genai-registry]: Gen AI attribute registry — semantic-conventions-genai
[^otel-genai-blog]: Inside the LLM Call — GenAI Observability with OpenTelemetry
