---
type: Analysis
title: Investigación agéntica — Hermes, Jev, protocolos y telemetría
description: Hechos verificados para diseñar la superficie agéntica, la capa System One y el espacio de tokens de ABM y sus ADS.
tags: [analisis, agentes, hermes, jev, mcp, a2a, telemetria]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:17:38Z }
stale_after: 2026-12-27T00:00:00Z
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
  - id: ts-routing
    resource: https://docs.typesafe.ai/patterns/confidence-routing
    title: Confidence-gated routing
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
  - id: ts-python-responses
    resource: https://docs.typesafe.ai/sdk/python/api/types/responses
    title: Answers and responses — Python SDK
  - id: ts-legal
    resource: https://docs.typesafe.ai/legal
    title: Legal — TypeSafe AI
  - id: mcp-spec-2025-11
    resource: https://modelcontextprotocol.io/specification/2025-11-25
    title: Specification — Model Context Protocol (2025-11-25)
  - id: mcp-lifecycle
    resource: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle
    title: Lifecycle — MCP
  - id: mcp-tools
    resource: https://modelcontextprotocol.io/specification/2025-11-25/server/tools
    title: Tools — MCP
  - id: mcp-resources
    resource: https://modelcontextprotocol.io/specification/2025-11-25/server/resources
    title: Resources — MCP
  - id: mcp-auth
    resource: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
    title: Authorization — MCP
  - id: mcp-latest
    resource: https://modelcontextprotocol.io/specification/2026-07-28
    title: Specification — MCP (2026-07-28, "latest")
  - id: mcp-annotations-blog
    resource: https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/
    title: Tool Annotations as Risk Vocabulary — MCP blog
  - id: a2a-spec
    resource: https://a2a-protocol.org/latest/specification/
    title: Agent2Agent (A2A) Protocol Specification
  - id: a2a-lf-press
    resource: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    title: A2A Protocol Surpasses 150 Organizations — Linux Foundation
  - id: llms-txt
    resource: https://llmstxt.org/
    title: The /llms.txt file, v2
  - id: agentskills-spec
    resource: https://agentskills.io/specification
    title: Specification — Agent Skills
  - id: gh-issue-25380
    resource: https://github.com/anthropics/claude-code/issues/25380
    title: SKILL.md validator only recognizes Agent Skills standard fields
  - id: otel-genai-registry
    resource: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/gen-ai.md
    title: Gen AI attribute registry — semantic-conventions-genai
  - id: otel-genai-old-registry
    resource: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
    title: Gen AI (moved) — OpenTelemetry semantic conventions
  - id: otel-genai-blog
    resource: https://opentelemetry.io/blog/2026/genai-observability/
    title: Inside the LLM Call — GenAI Observability with OpenTelemetry
  - id: hermes-mcp-config
    resource: https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
    title: MCP Config Reference — Hermes Agent
  - id: hermes-cli
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/cli
    title: CLI Interface — Hermes Agent
  - id: hermes-cli-commands
    resource: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
    title: CLI Commands Reference — Hermes Agent
  - id: hermes-context-files
    resource: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/context-files.md
    title: Context Files (AGENTS.md) — Hermes Agent
  - id: hermes-skills
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
    title: Skills System — Hermes Agent
  - id: hermes-creating-skills
    resource: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
    title: Creating Skills — Hermes Agent
  - id: hermes-config
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
    title: Configuration — Hermes Agent
  - id: hermes-home
    resource: https://hermes-agent.nousresearch.com/
    title: Hermes Agent — Nous Research
  - id: hermes-license
    resource: https://github.com/NousResearch/hermes-agent/blob/main/LICENSE
    title: LICENSE — NousResearch/hermes-agent
  - id: hermes-adapter-local
    resource: adapters/hermes/SKILL.md
    title: Adaptador Hermes de ABM (repo local)
  - id: owasp-llm-2025
    resource: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
    title: OWASP Top 10 for LLM Applications 2025
  - id: owasp-llm-2026
    resource: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
    title: OWASP GenAI LLM Top 10 2026
  - id: owasp-agentic-2026
    resource: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
    title: OWASP Top 10 for Agentic Applications 2026
  - id: rfc9457
    resource: https://www.rfc-editor.org/info/rfc9457/
    title: "RFC 9457: Problem Details for HTTP APIs"
---

# Investigación agéntica — Hermes, Jev, protocolos y telemetría

## 1. TypeSafe AI / Jev

- Endpoint único: `POST https://api.typesafe.ai/v1/systemone`, auth `Authorization: Bearer <API_KEY>`, `Content-Type: application/json`[^ts-api]. Listado de modelos: `GET https://api.typesafe.ai/v1/models`[^ts-models].
- Env var del SDK Python: `TYPESAFE_API_KEY` (se lee automáticamente si no se pasa `api_key`)[^ts-quickstart].
- Request: `{state, model, questions: {<id>: Question}}`. `state` es string, object o array. `model` acepta alias (`jev-latest`, `jev-preview`) o id versionado (`jev-1.13.0`)[^ts-api].
- Tres tipos de `Question`, todos con `type` + `instructions` (string/object/array):
  - `noul`: sin campo adicional obligatorio; `criteria.true`/`criteria.false` opcionales describen qué significa sí/no[^ts-api].
  - `choice`: `criteria` es `map<string, string|object|array|null>`, máx. 255 opciones[^ts-api].
  - `score`: `criteria` es array ordenado de 2 a 10 niveles[^ts-api].
- Response: `{model, answers: {<id>: Answer}, usage: {input_tokens, output_tokens}}`[^ts-api]. Output tokens no se cobran (ver precios)[^ts-models].
- `Answer` por tipo: `noul` → `{type, noul}` (0–1); `choice` → `{type, choice, probabilities, confidence}`; `score` → `{type, score, legend, probabilities, confidence}`. Solo choice/score llevan `confidence`, derivado de `probabilities`[^ts-api][^ts-confidence].
- Errores HTTP: `401` (key inválida), `422` (validación), `429` (rate limit) y `529` (sobrecarga); SDKs reintentan con backoff exponencial por defecto[^ts-api].
- Modelo vigente: `jev-1.13.0`, alias `jev-latest`/`jev-preview` apuntan a él (sin preview real todavía)[^ts-models].
- Precio: **$42 por Btok / $0.042 por Mtok** de entrada; salida gratis[^ts-models].
- Rate limits (ajustándose dinámicamente, sujetos a cambio sin aviso): **250 000 tokens/s** y **1 200 requests/min**[^ts-models].
- Contexto: 64k tokens totales (`state` + todas las `questions`); 32k para `state` + la pregunta más larga. Solo texto (string/JSON), sin imagen/audio/video[^ts-models].
- Estado: **early access** (confirmado por el proveedor, sin fecha de GA publicada); no hay SLA de estabilidad de rate limits[^ts-models].
- SDKs oficiales: `typesafe-sdk` (PyPI, Python ≥3.10, con extra `[http2]`) y `@typesafe-ai/sdk` (JavaScript/TypeScript), ambos exponen `usage` en cada respuesta[^ts-python-sdk][^ts-api].
- `SystemOneResponse` (Python) trae `model`, `usage: Usage{input_tokens, output_tokens}` y `answers: dict[str, Answer]`, más accesores tipados `.nouls`, `.choices`, `.scores`[^ts-python-responses].
- Agent skill oficial: instalable vía `claude plugin marketplace add typesafe-ai/skills` + `claude plugin install typesafe@typesafe-ai`, o `npx skills add typesafe-ai/skills --skill typesafe-ai` (compatible con el estándar agentskills.io); fuente en `github.com/typesafe-ai/skills`[^ts-skill].
- **Jev no es un LLM de chat/código**: no genera texto ni reemplaza al LLM de un coding agent; se usa *desde* código para decisiones tipadas (routing, scoring, guardrails)[^ts-coding-agents].
- Limitaciones conocidas (jaggedness jev-1.13, revisado 2026-09-17): lectura literal de instrucciones, mala en aritmética/conteo, mala en comparación de fechas, se degrada con indirección o `state` con ruido irrelevante (context rot), vulnerable a contenido adversarial en `state`, sin invariantes estructurales garantizadas entre Noul/Choice equivalentes, no genera texto[^ts-jaggedness].
- Datos: no se entrena con requests/responses de clientes; Data Processing Agreement, Privacy Policy y **zero data retention (ZDR)** disponibles para enterprise (contacto comercial)[^ts-legal][^ts-models].
- No existe (a la fecha) un servidor MCP oficial documentado para Jev — solo API HTTP, SDKs y agent skill[^ts-api][^ts-skill] (no-verificado: podría existir uno de terceros no listado en `llms.txt`).

## 2. MCP (Model Context Protocol)

- Versión ampliamente desplegada y estable: **`2025-11-25`**[^mcp-spec-2025-11]. Versión "latest" a la fecha: **`2026-07-28`**, que cambia el modelo base a *stateless, self-contained requests* con negociación de capacidades por request (en vez de la sesión con handshake de versiones previas) y retira `sampling`/`roots`/`tasks` del núcleo a extensiones opcionales[^mcp-latest].
- Transportes: `stdio` y `Streamable HTTP` (JSON-RPC 2.0 sobre ambos)[^mcp-spec-2025-11].
- Autorización (HTTP únicamente; stdio usa credenciales de entorno, no OAuth): basada en **OAuth 2.1** (draft-ietf-oauth-v2-1-13) + OAuth 2.0 Protected Resource Metadata (RFC 9728, obligatorio) + Authorization Server Metadata (RFC 8414) o OpenID Connect Discovery + PKCE obligatorio con `S256` + Resource Indicators (RFC 8707)[^mcp-auth]. Client ID Metadata Documents (CIMD) es el mecanismo preferido sobre Dynamic Client Registration (RFC 7591, mantenido por compatibilidad)[^mcp-auth].
- Handshake `initialize` (request mínimo):

  ```json
  {"jsonrpc":"2.0","id":1,"method":"initialize",
   "params":{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"MyClient","version":"1.0.0"}}}
  ```

  Response: `{"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25","capabilities":{...},"serverInfo":{"name":"MyServer","version":"1.0.0"}}}`. Luego el cliente envía `{"jsonrpc":"2.0","method":"notifications/initialized"}`[^mcp-lifecycle].
- `tools/list` → `{"result":{"tools":[{"name","description","inputSchema","icons?","execution?"}],"nextCursor"}}`. `tools/call` con `{"name","arguments"}` → `{"result":{"content":[...],"isError":false,"structuredContent"?}}`[^mcp-tools].
- Anotaciones de tool (`ToolAnnotations`, no obligatorias, tratar como no confiables salvo servidor de confianza): `readOnlyHint` (default `false`), `destructiveHint` (default `true`), `idempotentHint` (default `false`), `openWorldHint` (default `true`)[^mcp-annotations-blog][^mcp-tools].
- `resources/list` → `{"resources":[{"uri","name","title?","description?","mimeType?"}],"nextCursor"}`. `resources/read` con `{"uri"}` → `{"contents":[{"uri","mimeType","text"} | {"uri","mimeType","blob"}]}`[^mcp-resources].
- Nombres de tool recomendados: 1–128 caracteres, solo `A-Za-z0-9_-.`, sensibles a mayúsculas, únicos por servidor[^mcp-tools].

## 3. A2A (Agent2Agent)

- Versión estable actual: **1.0** (identificada por `Major.Minor`; los patch no afectan compatibilidad ni se usan en negociación)[^a2a-spec]. Liberada en marzo de 2026 con "Signed Agent Cards" y arquitectura web-aligned[^a2a-lf-press].
- Gobernanza: proyecto de la **Linux Foundation**; A2A se integró en agosto de 2026 a la **Agentic AI Foundation (AAIF)**, el mismo hogar neutral que ahora aloja también MCP[^a2a-lf-press].
- Descubrimiento: Agent Card publicada en `https://{server_domain}/.well-known/agent-card.json` (GET sin autenticar)[^a2a-spec].
- Campos obligatorios del `AgentCard`: `name`, `description`, `supportedInterfaces` (array de `AgentInterface`), `version`, `capabilities` (`AgentCapabilities`), `defaultInputModes`, `defaultOutputModes`, `skills` (array de `AgentSkill`). Opcionales: `provider`, `documentationUrl`, `securitySchemes`, `securityRequirements`, `signatures`, `iconUrl`[^a2a-spec].
- `AgentInterface` (transporte): `{url, protocolBinding, protocolVersion, tenant?}`; bindings soportados: `JSONRPC`, `GRPC`, `HTTP+JSON`[^a2a-spec].
- `AgentSkill`: `{id, name, description, tags[]}` obligatorios; `examples`, `inputModes`, `outputModes`, `securityRequirements` opcionales[^a2a-spec].
- Ejemplo mínimo real de fetch (fragmento de respuesta):

  ```json
  {"capabilities":{"extendedAgentCard":true},
   "securitySchemes":{"google":{"openIdConnectSecurityScheme":{"openIdConnectUrl":"https://accounts.google.com/.well-known/openid-configuration"}}}}
  ```

  obtenido vía `GET /.well-known/agent-card.json`[^a2a-spec].
- Agent Cards pueden firmarse con JWS (RFC 7515) sobre JSON canonicalizado (RFC 8785); campo `signatures`[^a2a-spec].
- A2A se declara **complementario a MCP, no un reemplazo**: MCP conecta un agente a herramientas/datos; A2A conecta agentes entre sí[^a2a-lf-press].

## 4. llms.txt

- Especificación vigente: **v2** (revisión de la propuesta original de 2024), mantenida en `llmstxt.org`[^llms-txt].
- Estructura obligatoria del archivo `/llms.txt` (o en cualquier subruta, cubriendo esa ruta): BOM opcional → **un único H1** (nombre del proyecto, única sección requerida) → **blockquote** con resumen breve → secciones markdown libres (sin headings) → cero o más secciones **H2** con listas de enlaces `[nombre](url): notas opcionales`[^llms-txt].
- Convención: una sección H2 llamada "Optional" señala enlaces que un agente puede omitir si necesita contexto más corto[^llms-txt].
- Complementa (no reemplaza) a `sitemap.xml`/`robots.txt`; se recomienda además publicar versión `.md` de cada página HTML relevante (`page.html.md` o `page.md`) enlazada vía `rel="alternate" type="text/markdown"` y `rel="describedby"`[^llms-txt].

## 5. Agent Skills (agentskills.io)

- Layout de directorio: `skill-name/SKILL.md` (requerido) + `scripts/`, `references/`, `assets/` (opcionales, sin restricción de qué más puede haber)[^agentskills-spec].
- Frontmatter YAML — únicos dos campos **requeridos**: `name` y `description`[^agentskills-spec].
  - `name`: 1–64 caracteres, solo minúsculas unicode alfanuméricas y guiones, no empieza/termina en guion, sin guiones consecutivos, **debe coincidir con el nombre del directorio padre**.
  - `description`: 1–1024 caracteres, no vacío, debe describir qué hace y cuándo usarlo.
- Campos **opcionales** definidos por la spec: `license` (string), `compatibility` (máx. 500 caracteres), `metadata` (map string→string libre), `allowed-tools` (string separado por espacios, marcado experimental)[^agentskills-spec].
- **Claves extra no definidas por la spec (p. ej. un `type:` a nivel raíz) NO están contempladas por el validador de referencia** `skills-ref` (`skills-ref validate ./my-skill`): un caso documentado (validador de Claude Code, que solo reconoce `name/description/license/compatibility/metadata/allowed-tools`) genera advertencias/falsos positivos sobre frontmatter extendido no estándar[^gh-issue-25380]. Recomendación práctica: cualquier dato adicional debe anidarse bajo `metadata:` en vez de añadirse como clave de primer nivel (no-verificado como regla dura de rechazo universal en todo validador; confirmado como comportamiento real en al menos un validador de referencia).
- Divulgación progresiva en 3 niveles: metadata (`name`+`description`, ~100 tokens, cargado siempre) → cuerpo de `SKILL.md` (recomendado <5000 tokens, cargado al activarse) → archivos de `scripts/`/`references/`/`assets/` (cargados solo bajo demanda)[^agentskills-spec].

## 6. OpenTelemetry GenAI semantic conventions

- Estado de estabilidad: **todo** atributo, span, métrica y evento `gen_ai.*` está marcado **"Development"** (antes "experimental"); ninguno es "Stable" a la fecha[^otel-genai-old-registry][^otel-genai-blog]. Las convenciones GenAI viven ahora en un repo propio, `open-telemetry/semantic-conventions-genai`, separado del core para iterar más rápido[^otel-genai-blog][^otel-genai-registry].
- Atributos clave confirmados (nombres exactos): `gen_ai.provider.name` (discriminador de proveedor, ej. `openai`, `anthropic`, `aws.bedrock`, `gcp.vertex_ai`), `gen_ai.operation.name` (ej. `chat`, `generate_content`, `text_completion`), `gen_ai.request.model`, `gen_ai.response.model`, `gen_ai.conversation.id`, `gen_ai.agent.id`/`gen_ai.agent.name`, `gen_ai.tool.name`, `gen_ai.tool.call.id`/`.arguments`/`.result`, `gen_ai.data_source.id`[^otel-genai-old-registry][^otel-genai-registry].
- Atributos de tokens: `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, más desgloses opcionales `gen_ai.usage.cache_read.input_tokens`, `gen_ai.usage.cache_creation.input_tokens`, `gen_ai.usage.reasoning.output_tokens` (cada uno debe incluirse también en el total correspondiente)[^otel-genai-registry].
- Métrica de histograma: **`gen_ai.client.token.usage`**, con tipo de token distinguido por el atributo `gen_ai.token.type` (`input`/`output`) y las dimensiones `gen_ai.operation.name`/`gen_ai.provider.name`/`gen_ai.request.model`[^otel-genai-old-registry].
- `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.tool.call.arguments/result` están marcados explícitamente como **posible información sensible (PII)**; no capturar por defecto sin control de redacción[^otel-genai-registry].

## 7. Hermes Agent (Nous Research)

- Instalación: script de shell `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` (bootstrapea package manager, Python, dependencias y el launcher)[^hermes-skills].
- **AGENTS.md se autocarga: confirmado oficialmente.** "At session start, Hermes loads the AGENTS.md from your working directory into the system prompt"; además recorre la cadena de directorios (raíz del repo git → cwd) cargando cada `AGENTS.md` en orden, y descubre `AGENTS.md` de subdirectorios de forma progresiva cuando el agente lee archivos ahí — el más específico prevalece[^hermes-context-files].
- Directorio de skills: global/fuente de verdad en `~/.hermes/skills/`; proyecto-local en `<project-root>/.hermes/skills/` (nativo) o `<project-root>/.agents/skills/` (convención cross-tool compartida con otros CLIs de agentes)[^hermes-skills].
- Instalar skill desde ruta local: colocarla directamente en `~/.hermes/skills/` ("Drop it in `~/.hermes/skills/` and it's live"); desde repo/URL: `hermes skills install owner/repo/skill`, `hermes skills install https://.../SKILL.md`[^hermes-creating-skills][^hermes-skills].
- Modo no interactivo de un solo turno: `hermes chat -q "<prompt>"` (o `--query-file`/stdin) y `hermes -z "<prompt>"` (scripted one-shot; captura limpia de stdout, útil para pipelines); ambos aceptan `--model`/`--provider`[^hermes-cli][^hermes-cli-commands].
- `--usage-file PATH`: escribe un reporte JSON de costo/tokens/modelo/llamadas tras la ejecución, incluso si falla; permite `jq .total_including_auxiliary.estimated_cost_usd usage.json`[^hermes-cli-commands].
- Config MCP en `~/.hermes/config.yaml` → clave `mcp_servers.<name>`: soporta `command`/`args`/`env` (stdio) o `url`/`headers` (HTTP, con `ssl_verify`, `client_cert` mTLS), `enabled`, `timeout`, `auth: oauth` (OAuth 2.1 + PKCE con CIMD), y filtros `tools.include`/`tools.exclude` (nombres exactos o glob) + `tools.resources`/`tools.prompts` (booleanos)[^hermes-mcp-config]. Los tools se registran como `mcp__<server>__<tool>`[^hermes-mcp-config].
- Negociación de versión MCP: clave `protocol` por servidor — `auto` (handshake `initialize` clásico, cae a la sonda stateless `server/discover` de la spec 2026-07-28 si el servidor la exige), `stateless`, o `legacy`[^hermes-mcp-config]. Identificación de cliente OAuth vía **CIMD** (`Client ID Metadata Document`), el mecanismo que adoptó la spec MCP `2026-07-28` en reemplazo de Dynamic Client Registration[^hermes-mcp-config].
- Delegación a subagentes: confirmada en el adaptador local de ABM (`delegate_task`, subagentes sin visión de la conversación) y en la documentación de coordinación multi-agente vía sesiones tmux paralelas[^hermes-adapter-local][^hermes-cli].
- Headless/CI: sí — `hermes chat -q`/`hermes -z` son scriptables, devuelven código de salida `1` en fallo/parcial/presupuesto excedido, y componen con `--usage-file` para pipelines de costo[^hermes-cli-commands].
- Licencia: **MIT**, open-source y self-hosted[^hermes-home][^hermes-license].

## 8. OWASP (LLM y aplicaciones agénticas)

- **OWASP Top 10 for LLM Applications 2025** (marzo 2025): vigente hasta la publicación 2026, cubre prompt injection, sensitive information disclosure, supply chain, data/model poisoning, improper output handling, excessive agency, system prompt leakage, vector/embedding weaknesses, misinformation, unbounded consumption[^owasp-llm-2025].
- **Reemplazo/actualización ya publicada a la fecha de este documento: "OWASP GenAI LLM Top 10 2026"** (v1.0, publicado 3 ago. 2026, anunciado 1 sep. 2026 junto con un nuevo "Agent Control Standard"); mapea riesgos contra NIST, MITRE ATLAS, CWE y el propio Top 10 for Agentic Applications[^owasp-llm-2026]. **ABM debe referenciar la edición 2026, no la 2025, al citar OWASP.**
- **OWASP Top 10 for Agentic Applications 2026** (publicado 9 dic. 2025): framework revisado por pares que distila la guía OWASP GenAI Security para riesgos de sistemas agénticos/autónomos[^owasp-agentic-2026].
- Todas las publicaciones están bajo el **OWASP GenAI Security Project** (`genai.owasp.org`)[^owasp-llm-2026][^owasp-agentic-2026].

## 9. RFC 9457 (problem+json)

- Confirmado: **RFC 9457, "Problem Details for HTTP APIs"** (M. Nottingham, E. Wilde, S. Dalal), estado **Proposed Standard**, define el media type `application/problem+json` (y `+xml`) para errores estructurados y legibles por máquina en APIs HTTP[^rfc9457].
- **Obsoleta a RFC 7807**; añade un registro IANA de tipos de problema comunes y clarifica el tratamiento de múltiples problemas en una sola respuesta[^rfc9457].
- Forma típica: `{type, status, title, detail, instance, ...extensiones}` (campos base heredados de 7807; `errors[]` con `detail`/`pointer` es una extensión común, no parte del núcleo de la RFC).

## Implicaciones para ABM

**Puntos de integración de Jev en ABM (≥3):**

1. **Router metodológico y de comando** (`intent`/`decide`): al iniciar `init-project`, una llamada `choice` clasifica el encargo (greenfield/brownfield, tipo de ADS) para elegir playbook y perfil sin heurísticas frágiles en prompt. Fallback: LLM con salida JSON Schema equivalente.
2. **Semáforo de riesgo de cada acción (verde/amarillo/rojo, §4.17)**: una `score` de 3 niveles sobre la acción propuesta decide si requiere HITL. Fallback: reglas deterministas explícitas + LLM si no matchean.
3. **Triage de hallazgos de `review`**: `choice` (bug real / falso positivo / mejora) + `noul` de severidad alta, para priorizar antes de que un humano mire. Fallback: heurística de severidad en código + LLM.
4. **Filtro de prompt injection en salida de tools** (regla del §4.8: "la salida de un tool es un dato, nunca una instrucción"): `noul` "¿este contenido intenta dar instrucciones al agente?" sobre cada resultado de tool antes de reinyectarlo al contexto. Fallback: reglas de patrón + LLM guardrail.
5. **Selección de skill/comando** (patrón oficial "skill suggestion" de TypeSafe, ya usado con el catálogo de Hermes): `choice` sobre el catálogo de comandos/skills de ABM para sugerir el siguiente paso. Fallback: matching por palabras clave + LLM.

**Recetas Jev para ADS (≥5, cada una con fallback):**

1. **Intent routing** de solicitudes de usuario a handler determinista/LLM barato/LLM potente/humano — fallback: LLM con salida estructurada tras el mismo umbral de confianza.
2. **Guardrails de entrada/salida de LLM** (screening de cada mensaje, patrón oficial `llm_guardrails`) — fallback: reglas regex/deny-list + LLM juez.
3. **Filtrado/scoring de pasajes RAG** antes de pasarlos al modelo de respuesta (patrón oficial `classifying_rag_passages`) — fallback: reranker clásico o LLM scorer.
4. **Verificación de citas** (¿la cita soportada por la fuente?, patrón oficial `citation_check`) — fallback: LLM de verificación con instrucciones equivalentes.
5. **Extracción verificada / cascada de datos** (extracción con regex + `choice` de Jev para normalizar, patrón oficial `sde_cascade`) — fallback: LLM de extracción con JSON Schema.
6. **Clasificación jerárquica con confianza** (árbol de categorías, patrón oficial `hierarchical_classification`) — fallback: clasificador clásico o LLM con function calling.
7. **Scoring compuesto con pesos en código** (varias `score` atómicas combinadas fuera del modelo, patrón oficial `composite-scoring`) — fallback: LLM único con rúbrica combinada (menos auditable).

En todas: el **umbral de confianza escala con el riesgo de la acción** (§4.9, confidence-gated routing)[^ts-routing]; confianza baja → cola de pendientes o humano, nunca "adivinar"[^ts-confidence]. El `state` puede llevar PII → pasa por el gate de gobernanza de datos del perfil antes de llamar a Jev; la clave (`TYPESAFE_API_KEY`) solo vive en variables de entorno/gestor de secretos, nunca en código[^ts-quickstart][^ts-legal].

**Qué necesita un ADS para ser operable por Hermes sin fricción:**

- `AGENTS.md` en la raíz (Hermes lo autocarga; no requiere flag ni configuración)[^hermes-context-files].
- Un `SKILL.md` de operación del ADS con frontmatter mínimo (`name`+`description`, sin claves extra de primer nivel no estándar) en `<repo>/.agents/skills/<nombre>/` para que Hermes y otros agentes lo descubran por la convención cross-tool[^hermes-skills][^agentskills-spec].
- Servidor MCP propio (o al menos CLI con `--json`/`--dry-run`) con tools de descripción corta, `readOnlyHint`/`destructiveHint` correctos, y plantilla lista para `mcp_servers` de Hermes (`tools.include` acotado, `trust: untrusted` si el ADS no es first-party)[^mcp-tools][^hermes-mcp-config].
- Errores en `application/problem+json` (RFC 9457) para que el manejo de errores de agentes sea uniforme entre ADS[^rfc9457].
- `llms.txt` propio si el ADS expone documentación extensa navegable por agentes[^llms-txt].
- Endpoint o recurso MCP de solo lectura para el resumen de consumo de tokens (§4.12), consumible sin credenciales de escritura.

**Versión de MCP recomendada para ABM:** apuntar a **`2025-11-25`** como base de compatibilidad (es la que más servidores/clientes ya implementan, con OAuth 2.1 + Protected Resource Metadata maduros)[^mcp-spec-2025-11], diseñando el adaptador de forma que tolere degradarse a `2026-07-28` (modelo stateless, `server/discover`) cuando el cliente lo exija — el propio Hermes ya negocia ambas con `protocol: auto`[^hermes-mcp-config]. No apuntar solo a `2026-07-28` todavía: es reciente y cambia supuestos base (sesión con estado → requests autocontenidos) que pueden romper servidores MCP existentes del catálogo curado de ABM.

[^ts-api]: API reference — TypeSafe AI
[^ts-quickstart]: Quick start — TypeSafe AI
[^ts-coding-agents]: Jev with coding agents
[^ts-confidence]: Confidence — TypeSafe AI
[^ts-routing]: Confidence-gated routing
[^ts-skill]: Agent skill — TypeSafe AI
[^ts-models]: Models — TypeSafe AI
[^ts-jaggedness]: Jev 1.13 jaggedness
[^ts-python-sdk]: TypeSafe Python SDK
[^ts-python-responses]: Answers and responses — Python SDK
[^ts-legal]: Legal — TypeSafe AI
[^mcp-spec-2025-11]: Specification — Model Context Protocol (2025-11-25)
[^mcp-lifecycle]: Lifecycle — MCP
[^mcp-tools]: Tools — MCP
[^mcp-resources]: Resources — MCP
[^mcp-auth]: Authorization — MCP
[^mcp-latest]: Specification — MCP (2026-07-28, "latest")
[^mcp-annotations-blog]: Tool Annotations as Risk Vocabulary — MCP blog
[^a2a-spec]: Agent2Agent (A2A) Protocol Specification
[^a2a-lf-press]: A2A Protocol Surpasses 150 Organizations — Linux Foundation
[^llms-txt]: The /llms.txt file, v2
[^agentskills-spec]: Specification — Agent Skills
[^gh-issue-25380]: SKILL.md validator only recognizes Agent Skills standard fields
[^otel-genai-registry]: Gen AI attribute registry — semantic-conventions-genai
[^otel-genai-old-registry]: Gen AI (moved) — OpenTelemetry semantic conventions
[^otel-genai-blog]: Inside the LLM Call — GenAI Observability with OpenTelemetry
[^hermes-mcp-config]: MCP Config Reference — Hermes Agent
[^hermes-cli]: CLI Interface — Hermes Agent
[^hermes-cli-commands]: CLI Commands Reference — Hermes Agent
[^hermes-context-files]: Context Files (AGENTS.md) — Hermes Agent
[^hermes-skills]: Skills System — Hermes Agent
[^hermes-creating-skills]: Creating Skills — Hermes Agent
[^hermes-home]: Hermes Agent — Nous Research
[^hermes-license]: LICENSE — NousResearch/hermes-agent
[^hermes-adapter-local]: Adaptador Hermes de ABM (repo local)
[^owasp-llm-2025]: OWASP Top 10 for LLM Applications 2025
[^owasp-llm-2026]: OWASP GenAI LLM Top 10 2026
[^owasp-agentic-2026]: OWASP Top 10 for Agentic Applications 2026
[^rfc9457]: RFC 9457: Problem Details for HTTP APIs
