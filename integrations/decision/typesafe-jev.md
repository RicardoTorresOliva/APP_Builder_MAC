---
type: Integration Guide
title: Jev (TypeSafe AI) — primer adaptador de System One
description: Endpoint, forma de request/response, precios y límites, SDKs, limitaciones y recetas de Jev.
tags: [jev, typesafe, decision, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: ts-api
    resource: https://docs.typesafe.ai/api
    title: API reference — TypeSafe AI
  - id: ts-quickstart
    resource: https://docs.typesafe.ai/introduction/quickstart
    title: Quick start — TypeSafe AI
  - id: ts-coding-agents
    resource: https://docs.typesafe.ai/introduction/coding-agents
    title: Jev with coding agents
  - id: ts-confidence
    resource: https://docs.typesafe.ai/confidence
    title: Confidence — TypeSafe AI
  - id: ts-skill
    resource: https://docs.typesafe.ai/agent-skill
    title: Agent skill — TypeSafe AI
  - id: ts-models
    resource: https://docs.typesafe.ai/models
    title: Models — TypeSafe AI
  - id: ts-jaggedness
    resource: https://docs.typesafe.ai/model-jaggedness/jev-1.13
    title: Jev 1.13 jaggedness
  - id: ts-python-sdk
    resource: https://docs.typesafe.ai/sdk/python
    title: TypeSafe Python SDK
  - id: ts-legal
    resource: https://docs.typesafe.ai/legal
    title: Legal — TypeSafe AI
---

# Jev (TypeSafe AI) — primer adaptador de System One

Jev es el modelo insignia "System One" de TypeSafe AI: no genera texto — evalúa preguntas tipadas
contra un `state` y devuelve valores tipados con probabilidades que el código consume directamente,
sin parsear lenguaje natural[^ts-coding-agents].

## Endpoint y auth
`POST https://api.typesafe.ai/v1/systemone`, header `Authorization: Bearer <API_KEY>`,
`Content-Type: application/json`[^ts-api]. Listado de modelos: `GET
https://api.typesafe.ai/v1/models`[^ts-models]. La clave se lee de `TYPESAFE_API_KEY` (el SDK
Python la toma sola si no se pasa `api_key`)[^ts-quickstart] — nunca en código, ver
`/integrations/secrets.md`.

## Forma de la llamada
Request: `{state, model, questions: {<id>: Question}}`; `state` es string, objeto o
array[^ts-api]. Tres tipos de `Question`:
- **`choice`**: `criteria` mapa de hasta 255 opciones → `{choice, probabilities, confidence}`.
- **`score`**: `criteria` array ordenado de 2 a 10 niveles → `{score, legend, probabilities,
  confidence}`.
- **`noul`**: probabilidad 0–1 de un enunciado → `{noul}` (sin `confidence`)[^ts-api][^ts-confidence].

Response: `{model, answers, usage: {input_tokens, output_tokens}}`; la salida no se
cobra[^ts-api][^ts-models].

## Modelos, precio y límites (re-verificar antes de `stale_after`)
- Modelo vigente: `jev-1.13.0`; alias `jev-latest`/`jev-preview` apuntan a él[^ts-models].
- Precio: **$0,042 por Mtok de entrada**, salida gratis[^ts-models].
- Límites: 250 000 tokens/s, 1 200 requests/min (ajustables, sin SLA de estabilidad)[^ts-models].
  Contexto: 64k tokens totales (32k para `state` + la pregunta más larga), solo texto[^ts-models].
- Estado: **early access**, sin fecha de disponibilidad general publicada[^ts-models].
- Errores: `401`/`422`/`429`/`529`; los SDKs reintentan con backoff exponencial por
  defecto[^ts-api].

## SDKs y agent skill
`typesafe-sdk` (Python ≥3.10) y `@typesafe-ai/sdk` (JS/TS), ambos exponen `usage` en cada
respuesta[^ts-python-sdk]. Agent skill oficial instalable vía `claude plugin marketplace add
typesafe-ai/skills` o `npx skills add typesafe-ai/skills --skill typesafe-ai` (compatible con el
estándar agentskills.io)[^ts-skill].

## Qué NO es
**No es un modelo de chat/código**: no genera texto, no reemplaza al LLM de un coding agent — se
llama *desde* código para decisiones tipadas (routing, scoring, guardrails)[^ts-coding-agents].

## Limitaciones conocidas ("jaggedness", jev-1.13, revisado 2026-09-17)
Lectura literal de instrucciones; débil en aritmética, conteo y comparación de fechas; se degrada
con indirección o ruido irrelevante en `state` (context rot); vulnerable a contenido adversarial en
`state`; sin invariantes garantizadas entre tipos equivalentes; no genera texto[^ts-jaggedness].

## Datos
No se entrena con requests/responses de clientes; DPA, Privacy Policy y zero data retention (ZDR)
disponibles para enterprise, previo contacto comercial[^ts-legal][^ts-models].

## Recetas para ADS (con fallback)
1. **Intent routing** de solicitudes a handler determinista / LLM barato / LLM potente / humano —
   *fallback*: LLM con salida estructurada tras el mismo umbral de confianza.
2. **Guardrails de entrada/salida de LLM** (patrón oficial `llm_guardrails`) — *fallback*: reglas
   regex/deny-list + LLM juez.
3. **Filtrado/scoring de pasajes RAG** (patrón oficial `classifying_rag_passages`) — *fallback*:
   reranker clásico o LLM scorer.
4. **Verificación de citas** (patrón oficial `citation_check`) — *fallback*: LLM de verificación con
   instrucciones equivalentes.
5. **Extracción verificada / cascada de datos** (patrón oficial `sde_cascade`) — *fallback*: LLM de
   extracción con JSON Schema.
6. **Clasificación jerárquica con confianza** (patrón oficial `hierarchical_classification`) —
   *fallback*: clasificador clásico o LLM con function calling.
7. **Scoring compuesto con pesos en código** (patrón oficial `composite-scoring`) — *fallback*: LLM
   único con rúbrica combinada (menos auditable).

## Usos en ABM (≥3, ver detalle en [README.md](README.md))
Router metodológico, semáforo de riesgo, filtro de prompt injection en la salida de tools, triage de
hallazgos de `review`, sugerencia de comando/skill (patrón oficial de sugerencia sobre un catálogo
de comandos).

En todas: el umbral de confianza escala con el riesgo de la acción; confianza baja → cola de
pendientes o humano, nunca "adivinar".

[^ts-api]: API reference — TypeSafe AI
[^ts-quickstart]: Quick start — TypeSafe AI
[^ts-coding-agents]: Jev with coding agents
[^ts-confidence]: Confidence — TypeSafe AI
[^ts-skill]: Agent skill — TypeSafe AI
[^ts-models]: Models — TypeSafe AI
[^ts-jaggedness]: Jev 1.13 jaggedness
[^ts-python-sdk]: TypeSafe Python SDK
[^ts-legal]: Legal — TypeSafe AI
