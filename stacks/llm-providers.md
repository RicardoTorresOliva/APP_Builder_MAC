---
type: Stack Sheet
title: Proveedores LLM y capa System One
description: Gateway LLM como categoría, matriz de capacidades y precios con fecha, y la capa de decisión tipada System One.
tags: [stacks, llm, portabilidad, system-one]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:55:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: anthropic-pricing
    resource: https://platform.claude.com/docs/en/about-claude/pricing
    title: Claude Platform Docs — Pricing
  - id: openai-pricing
    resource: https://developers.openai.com/api/docs/pricing
    title: OpenAI API — Pricing
  - id: google-gemini-pricing
    resource: https://ai.google.dev/gemini-api/docs/pricing
    title: Gemini Developer API pricing
  - id: typesafe-models
    resource: https://docs.typesafe.ai/models
    title: TypeSafe AI — Models
  - id: bedrock-claude
    resource: https://aws.amazon.com/bedrock/pricing/
    title: Amazon Bedrock — Pricing
  - id: vertex-claude
    resource: https://cloud.google.com/vertex-ai/generative-ai/pricing
    title: Vertex AI — Generative AI pricing
  - id: azure-foundry
    resource: https://azure.microsoft.com/en-us/pricing/details/ai-foundry-models/
    title: Azure AI Foundry — Model pricing
  - id: mistral-pricing
    resource: https://mistral.ai/pricing
    title: Mistral AI — Pricing
  - id: openrouter
    resource: https://openrouter.ai/docs
    title: OpenRouter — Docs
  - id: litellm
    resource: https://docs.litellm.ai/
    title: LiteLLM — Docs
  - id: portkey
    resource: https://portkey.ai/docs
    title: Portkey — Docs
  - id: ollama
    resource: https://ollama.com
    title: Ollama
  - id: vllm
    resource: https://docs.vllm.ai/
    title: vLLM — Docs
---

# Proveedores LLM y capa System One

## Gateway LLM (categoría)

Todo ADS habla con los modelos a través de una **interfaz de chat compatible** (el formato de facto
que exponen la mayoría de proveedores y gateways: mensajes con rol, `tool_calls`, `response_format`
JSON) como lingua franca. El proveedor y el modelo se fijan por variables de entorno
(`LLM_PROVIDER`, `LLM_MODEL`, `LLM_BASE_URL`, `LLM_API_KEY`); el código de la aplicación nunca
importa el SDK propietario de un proveedor directamente, solo el cliente del gateway.

| Opción de gateway | Qué es | Licencia/hosting |
|---|---|---|
| LiteLLM[^litellm] | Proxy/SDK que normaliza 100+ proveedores tras la interfaz de chat compatible | Open source (self-host) o Enterprise gestionado |
| Portkey[^portkey] | Gateway con cache, retries, guardrails y observabilidad integrada | SaaS gestionado; core open source |
| OpenRouter[^openrouter] | Gateway multi-proveedor con un único endpoint y facturación consolidada | SaaS gestionado, pago por uso |

Elige LiteLLM para self-host sin dependencia de un tercero facturador; Portkey cuando el equipo
quiere observabilidad y guardrails sin construirlos; OpenRouter para prototipar rápido con un solo
API key. Los tres exponen la misma interfaz de chat compatible, así que migrar entre ellos —o
prescindir del gateway y hablar directo con el proveedor— es cambio de configuración, no de código.

## Matriz de capacidades (vigente al 2026-09-27)

| Proveedor / modelo | Tool use | Salida estructurada | Contexto | Entrada USD/Mtok | Salida USD/Mtok |
|---|---|---|---|---|---|
| Anthropic `claude-sonnet-5`[^anthropic-pricing] | Sí | Sí (JSON Schema) | 1M | $2 | $10 |
| Anthropic `claude-opus-5-5`[^anthropic-pricing] | Sí | Sí | 1M | $4 | $20 |
| Anthropic `claude-haiku-4-5`[^anthropic-pricing] | Sí | Sí | 200K | $1 | $5 |
| OpenAI `gpt-6-sol`[^openai-pricing] | Sí | Sí (`response_format`) | 1.05M | $2 | $10 |
| OpenAI `gpt-6-luna`[^openai-pricing] | Sí | Sí | 1.05M | $0.10 | $0.50 |
| OpenAI `gpt-6-astra`[^openai-pricing] | Sí | Sí | 1.05M | $10 | $50 |
| Google `gemini-3.1-pro-preview`[^google-gemini-pricing] | Sí | Sí | 200K (est. estándar) | $2 | $12 |
| Google `gemini-3-flash-preview`[^google-gemini-pricing] | Sí | Sí | 1M | $0.50 | $3 |
| Azure AI Foundry (Claude/GPT/Mistral gestionados)[^azure-foundry] | Según modelo base | Según modelo base | Según modelo base | Tarifa del modelo + uplift de la plataforma | ídem |
| AWS Bedrock (Claude/Nova/Mistral/Llama)[^bedrock-claude] | Según modelo base | Según modelo base | Según modelo base | Tarifa del modelo, facturada por AWS | ídem |
| Vertex AI (Gemini/Claude/Llama)[^vertex-claude] | Según modelo base | Según modelo base | Según modelo base | Tarifa del modelo, facturada por GCP | ídem |
| Mistral (`mistral-large`, `mistral-small`)[^mistral-pricing] | Sí | Sí | 128K–256K | Ver mistral.ai/pricing (variable, no fijado aquí) | — |
| Modelos abiertos locales (Llama/Qwen/Mistral vía Ollama[^ollama]/vLLM[^vllm]) | Depende del modelo | Depende del modelo | Depende del modelo | $0 de licencia; costo = cómputo propio | — |

Precios de nubes gestionadas (Azure AI Foundry, Bedrock, Vertex AI) heredan la tarifa del modelo
base más un posible uplift de la plataforma o descuento por compromiso: no se fija un número único
porque varía por SKU, región y contrato — verifica en la fuente antes de presupuestar. Precio de
Mistral: no fijado en esta ficha porque el plan gratuito y los tramos cambian con frecuencia;
"n/d (no-verificado)" hasta confirmar en `mistral.ai/pricing` al momento de decidir.

## Capa System One (decisión tipada, TypeSafe Jev)

Categoría en el núcleo: "modelo de decisión tipada con confianza calibrada" (interfaz
`decide(state, questions[]) → answers[]`, tipos `choice`, `score`, `boolean`/Noul). TypeSafe AI
(Jev) es el primer adaptador — ver ADR 0011 y `integrations/decision/typesafe-jev/`.

| Campo | Valor |
|---|---|
| Estado de acceso | Early access (verificar vigencia antes de comprometer un ADS a producción)[^typesafe-models] |
| Modelo vigente | `jev-1.13.0`, alias `jev-latest`[^typesafe-models] |
| Precio de entrada | $0.042 por Mtok de entrada[^typesafe-models] |
| Precio de salida | $0 (no medido; las respuestas tipadas no se facturan por tokens de salida)[^typesafe-models] |
| Límites | 32K tokens de estado + pregunta más larga; 64K estado + todas las preguntas juntas[^typesafe-models] |
| Fallback obligatorio | LLM con salida estructurada (JSON Schema) detrás de la misma interfaz `decide()`; el ADS funciona sin Jev |

Jev no es un modelo para conversar ni para generar texto libre: solo devuelve decisiones tipadas con
probabilidad. Úsalo para triage, ruteo, clasificación y semáforos de confianza; nunca como
reemplazo de un LLM generativo.

## Evals mínimos para cambiar de modelo con seguridad

Antes de mover un ADS de un modelo/proveedor a otro (o de subir/bajar de tier):

1. **Set de regresión** (20–50 casos reales del dominio, con salida esperada o criterio de
   aceptación) corrido contra el modelo actual y el candidato.
2. **Salida estructurada**: valida que el candidato respeta el JSON Schema declarado en el 100% de
   los casos (o define fallback de reintento con reparación de JSON).
3. **Tool use**: verifica que el candidato invoca las mismas tools con los mismos argumentos en un
   subconjunto de casos con herramientas.
4. **Costo y latencia**: compara `input_per_mtok`/`output_per_mtok` (`pricing.yaml`) y P50/P95 de
   latencia contra el SLO del ADS.
5. **Umbral de aprobación**: el candidato reemplaza al actual solo si iguala o mejora la tasa de
   aciertos del set de regresión y no degrada el SLO de latencia/costo — decisión registrada como
   `Attested Computation` (`abm tokens attest`) cuando el perfil lo exige.

## Cambio de proveedor por configuración

`LLM_PROVIDER`, `LLM_MODEL`, `LLM_BASE_URL` y `LLM_API_KEY` en `.env` (nunca en código). Son las variables del **ADS en operación**; el CLI de ABM usa las suyas (`ABM_LLM_BASE_URL`, `ABM_LLM_API_KEY`, `ABM_LLM_MODEL`) para el fallback `llm` de `abm decide` (ver `integrations/llm-gateway/README.md`).
Cambiar de Anthropic directo a la misma familia de modelos vía Azure AI Foundry, Bedrock o Vertex AI
es cambiar `LLM_BASE_URL` y las credenciales — el contrato de la interfaz de chat compatible no
cambia. `portability.exit_plan` en `ads.yaml` documenta a qué proveedor migraría el ADS y qué se
pierde (features propietarias, fine-tunes, cache específico) si el proveedor actual deja de estar
disponible.

[^anthropic-pricing]: Claude Platform Docs — Pricing
[^openai-pricing]: OpenAI API — Pricing
[^google-gemini-pricing]: Gemini Developer API pricing
[^typesafe-models]: TypeSafe AI — Models
[^bedrock-claude]: Amazon Bedrock — Pricing
[^vertex-claude]: Vertex AI — Generative AI pricing
[^azure-foundry]: Azure AI Foundry — Model pricing
[^mistral-pricing]: Mistral AI — Pricing
[^openrouter]: OpenRouter — Docs
[^litellm]: LiteLLM — Docs
[^portkey]: Portkey — Docs
[^ollama]: Ollama
[^vllm]: vLLM — Docs
