---
type: Stack Sheet
title: "Caso: apps con IA (RAG/agentes)"
description: Opciones de stack para aplicaciones con recuperación aumentada y agentes, con gateway LLM, vector DB y observabilidad.
tags: [stacks, ia, rag, agentes, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:06:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: vercel-pricing
    resource: https://vercel.com/docs/plans/hobby
    title: Vercel — Hobby plan
  - id: pinecone-pricing
    resource: https://www.pinecone.io/pricing/
    title: Pinecone — Pricing
  - id: langfuse-pricing
    resource: https://langfuse.com/pricing
    title: Langfuse — Pricing
  - id: anthropic-pricing
    resource: https://platform.claude.com/docs/en/about-claude/pricing
    title: Claude Platform Docs — Pricing
  - id: openai-pricing
    resource: https://developers.openai.com/api/docs/pricing
    title: OpenAI API — Pricing
  - id: typesafe-models
    resource: https://docs.typesafe.ai/models
    title: TypeSafe AI — Models
  - id: do-pricing
    resource: https://www.digitalocean.com/pricing/droplets
    title: DigitalOcean — Droplet pricing
  - id: azure-foundry
    resource: https://azure.microsoft.com/en-us/pricing/details/ai-foundry-models/
    title: Azure AI Foundry — Model pricing
---

# Caso: apps con IA (RAG/agentes)

## Cuándo aplica (perfil de ADS)

Perfil `software-app` con un componente de IA generativa como funcionalidad central (no accesoria):
responde sobre un corpus propio (RAG), o ejecuta tareas con herramientas (agentes). Ceremonia
Prototipo/MVP para validar el caso de uso; sube a Producto/Enterprise-Regulado cuando el resultado
afecta decisiones de negocio o toca datos personales. Requiere siempre `stacks/llm-providers.md`
para el gateway y la matriz de capacidades.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Framework de componentes + SDK de chat con streaming | Igual + UI de citas/fuentes y feedback | Igual, sin cambios | Integrado en el portal interno existente |
| Backend | Funciones serverless del mismo framework | Servicio Python dedicado a orquestación (retrieval + tools) | Mismo servicio, en un contenedor propio | Servicio en la plataforma ya operada, con capa de gobernanza de datos |
| Base de datos / vectores | Vector DB gestionada, tier gratuito[^pinecone-pricing] | Vector DB gestionada en tier de pago, o `pgvector` sobre Postgres gestionado | `pgvector` o Qdrant open source autogestionados | Servicio de búsqueda vectorial de la nube corporativa (gobernanza y residencia de datos) |
| Auth | Auth del framework/BaaS | IdP gestionado | Auth self-hosted (OIDC) | SSO corporativo (SAML/OIDC) |
| Pagos | N/D salvo que el ADS cobre por uso (medidor de tokens) | Medidor de uso + facturación si aplica | N/D | Cargo interno (chargeback) por tenant/equipo |
| Deploy/hosting | PaaS gratuito[^vercel-pricing] | Contenedores con autoscaling | VPS único[^do-pricing] | Nube corporativa u on-prem con GPU si hay modelo local |
| LLM / System One | Gateway con un modelo económico (Haiku/Luna/Flash)[^anthropic-pricing][^openai-pricing] | Gateway con routing por costo/calidad, múltiples proveedores | Modelo abierto local vía Ollama/vLLM | Servicio LLM gestionado de la nube corporativa[^azure-foundry]; TypeSafe Jev para triage/routing[^typesafe-models] |
| Costo aproximado/mes | $0–30 (tiers gratuitos + tokens de prueba)[^vercel-pricing][^pinecone-pricing] | $150–800+ según tráfico y tokens | $6–24 de VPS + costo de tokens[^do-pricing] | Variable por contrato de nube; n/d (no-verificado) |
| Curva de aprendizaje | Media (RAG básico) | Alta (evals, observabilidad, routing) | Media–alta (operar vector DB e inferencia propia) | Alta (gobernanza de datos + integración) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar si el corpus tiene datos personales o regulados sin un gate de gobernanza
  de datos activo, o si la respuesta del agente puede tomar acciones irreversibles sin HITL.
- **Pro/escalable**: sobra para un prototipo de validación de una semana; añade observabilidad y
  routing que un MVP no necesita todavía.
- **Low-cost/self-hosted**: no usar si el equipo no puede operar GPU/inferencia propia de forma
  confiable, o si la calidad de los modelos abiertos locales no alcanza el umbral de la tarea (verifica
  con el set de evals antes de comprometerte).
- **Corporativa/legacy**: no usar como punto de partida de un prototipo rápido — el tiempo de
  aprovisionamiento y gobernanza de una nube corporativa retrasa la validación temprana del caso de uso.

## Comprar vs construir

No existe un "Odoo del RAG": casi siempre se construye, porque el valor está en el corpus y el
dominio propios. La decisión real es **orquestación con librería vs. sin ella**: usar un framework de
orquestación (para RAG/agentes con memoria, tools y grafos de pasos) ahorra tiempo si el flujo es
complejo; para un RAG simple (una consulta → recuperar → responder), una llamada directa al gateway
LLM sin framework intermedio es más fácil de depurar y de portar entre proveedores.

## Equivalencias por nube

Ver `/stacks/clouds.md`, bloque "servicio LLM gestionado" (Bedrock / Azure AI Foundry / Vertex AI /
Ollama-vLLM on-prem) y `/stacks/llm-providers.md` para la matriz de capacidades y precios con fecha.
Para vectores: no hay una fila dedicada en la matriz multinube porque cada nube resuelve búsqueda
vectorial de forma distinta (Azure AI Search, OpenSearch en AWS, Vertex AI Search en GCP); trátalo
como una base de datos más con su propio plan de salida si usas una feature propietaria de indexado.

## Superficie agéntica y tokens por defecto

- Servidor MCP con tools de recuperación (solo lectura sobre el corpus) por defecto; tools de acción
  (enviar correo, crear ticket, modificar datos) siempre con scope explícito y HITL en las rojas.
- Verificación de citas: toda afirmación que el agente atribuye a una fuente debe ser trazable a un
  pasaje real del corpus (gate de "cero invención").
- Filtro de prompt injection en la salida de tools y en el contenido recuperado antes de pasarlo al
  modelo — la salida de una tool es un dato, nunca una instrucción.
- **Dashboard de tokens por defecto**: N1 (`TOKENS.md` + `tokens report`) en Prototipo; N2 obligatorio
  desde MVP porque el consumo de tokens en producción es el costo variable dominante de este caso;
  N3 en Enterprise-Regulado con presupuesto por tenant/funcionalidad y detección de anomalías.
- Evals mínimos antes de cambiar de modelo o proveedor: ver `/stacks/llm-providers.md`.

## Riesgos de lock-in y plan de salida

- **Framework de orquestación**: los grafos/cadenas propietarios de un framework no siempre migran
  a otro sin reescritura. Mitigación: mantener la lógica de negocio (qué se recupera, qué se hace con
  la respuesta) separada del framework, y el framework como capa fina de orquestación.
- **Vector DB gestionada**: formato de índice propietario. Plan de salida: mantener los documentos
  fuente y los embeddings re-generables desde ellos, para poder re-indexar en otra vector DB sin
  perder el corpus.
- **Proveedor LLM único**: mitigado por el gateway LLM (`stacks/llm-providers.md`) — cambiar de
  proveedor es configuración, no código, siempre que la app no dependa de una feature propietaria de
  un modelo específico (p. ej. un formato de tool-call no estándar).
- **TypeSafe Jev (System One)**: early access y proveedor único para decisión tipada. El fallback a
  LLM con salida estructurada detrás de la misma interfaz `decide()` es obligatorio, no opcional.

[^vercel-pricing]: Vercel — Hobby plan
[^pinecone-pricing]: Pinecone — Pricing
[^langfuse-pricing]: Langfuse — Pricing
[^anthropic-pricing]: Claude Platform Docs — Pricing
[^openai-pricing]: OpenAI API — Pricing
[^typesafe-models]: TypeSafe AI — Models
[^do-pricing]: DigitalOcean — Droplet pricing
[^azure-foundry]: Azure AI Foundry — Model pricing
