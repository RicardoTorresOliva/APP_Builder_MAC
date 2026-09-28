---
type: Analysis
title: Benchmark de referentes
description: Referentes de desarrollo agent-native verificados a la fecha y las ideas que ABM adopta de cada uno.
tags: [analisis, benchmark, metodologia]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:18:31Z }
stale_after: 2026-12-27T00:00:00Z
sources:
  - id: speckit-gh
    resource: https://github.com/github/spec-kit
    title: "GitHub - github/spec-kit"
  - id: speckit-releases
    resource: https://github.com/github/spec-kit/releases
    title: "Releases · github/spec-kit"
  - id: kiro-specs
    resource: https://kiro.dev/docs/specs/
    title: "Specs - Docs - Kiro"
  - id: kiro-steering
    resource: https://kiro.dev/docs/steering/
    title: "Steering - Docs - Kiro"
  - id: kiro-pricing
    resource: https://kiro.dev/pricing/
    title: "Pricing - Kiro"
  - id: bmad-repo
    resource: https://github.com/bmad-code-org/BMAD-METHOD
    title: "GitHub - bmad-code-org/BMAD-METHOD"
  - id: bmad-license
    resource: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/LICENSE
    title: "BMAD-METHOD LICENSE"
  - id: agentos-repo
    resource: https://github.com/buildermethods/agent-os
    title: "GitHub - buildermethods/agent-os"
  - id: agentos-v3
    resource: https://github.com/buildermethods/agent-os/discussions/310
    title: "Agent OS v3 - Leaner and more aligned for 2026"
  - id: agentsmd-repo
    resource: https://github.com/agentsmd/agents.md
    title: "GitHub - agentsmd/agents.md"
  - id: agentsmd-site
    resource: https://agents.md/
    title: "AGENTS.md"
  - id: linuxfoundation-aaif
    resource: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
    title: "Linux Foundation announces the Agentic AI Foundation (AAIF)"
  - id: agentskills-repo
    resource: https://github.com/agentskills/agentskills
    title: "GitHub - agentskills/agentskills"
  - id: agentskills-site
    resource: https://agentskills.io/home
    title: "Agent Skills Overview"
  - id: simonwillison-skills
    resource: https://simonwillison.net/2025/Dec/19/agent-skills/
    title: "Agent Skills (Simon Willison)"
  - id: cursor-rules-docs
    resource: https://cursor.com/docs/context/rules
    title: "Rules - Cursor Docs"
  - id: copilot-instructions-docs
    resource: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide
    title: "Adding repository custom instructions for GitHub Copilot in your IDE"
  - id: anthropic-skills-repo
    resource: https://github.com/anthropics/skills
    title: "GitHub - anthropics/skills"
  - id: openai-skills-repo
    resource: https://github.com/openai/skills
    title: "GitHub - openai/skills"
  - id: openai-codex-issue
    resource: https://github.com/openai/codex/issues/40185
    title: "Open Source docs point to the deprecated skills repo"
  - id: gw-requesty
    resource: https://www.requesty.ai/blog/litellm-vs-portkey-vs-openrouter-best-llm-gateway-2026
    title: "LiteLLM vs Portkey vs OpenRouter vs Requesty"
  - id: gw-dibi8
    resource: https://dibi8.com/resources/llm-frameworks/llm-gateway-portkey-litellm-openrouter-comparison-2026/
    title: "Portkey vs LiteLLM vs OpenRouter: LLM Gateway 2026"
  - id: cs-idd
    resource: https://www.codysandahl.com/2026/07/14/kill-the-ceremony-intent-driven-development-and-the-minimum-viable-spec/
    title: "Kill the Ceremony - Intent-Driven Development and the Minimum Viable Spec"
  - id: wr-spdd
    resource: https://www.webreactiva.com/blog/spdd
    title: "SPDD vs SDD y por qué importan los prompts estructurados"
  - id: pp-aidd
    resource: https://pasqualepillitteri.it/es/news/3384/aidd-vs-vibe-coding-spec-driven-development-2026-es
    title: "AIDD vs Vibe Coding vs Spec-Driven Development (2026)"
  - id: dt-sdd2026
    resource: https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2
    title: "Spec-Driven Development in 2026: What It Is, the Tooling, and How Teams Actually Use It"
  - id: idd-landscape
    resource: https://www.intent-driven-development.com/landscape
    title: "The landscape of spec, intent, and AI-native development"
  - id: idd-dev-knowledge
    resource: https://intent-driven.dev/knowledge/intent-driven-development/
    title: "Intent-Driven Development: Definition & Practices"
  - id: li-idd-sdd
    resource: https://www.linkedin.com/pulse/intent-driven-development-idd-spec-driven-sdd-bhupendra-4t1we
    title: "Intent-Driven Development (IDD) vs Spec-Driven (SDD)"
---

## Referentes

### 1. GitHub Spec Kit

- **Qué es:** CLI `specify` (`github/spec-kit`) que impone el flujo `constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`, con artefactos Markdown en `.specify/` y soporte multi-agente vía `--integration`.[^speckit-gh]
- **Vigencia:** v1.0.6 (10 sep 2026), llegó a 1.0 el 21 ago 2026, +180 tags desde v0.0.17 (sep 2025). Cadencia muy alta, proyecto activo.[^speckit-releases]
- **Licencia:** MIT.[^speckit-gh]
- **Ideas a adoptar:** `constitution.md` como principios no negociables por proyecto; separación estricta spec/plan/tasks con trazabilidad; comandos por fase.
- **Qué NO copiar:** acoplamiento a GitHub Issues (`/speckit.taskstoissues`, en camino a extensión aparte); nomenclatura de comandos ligada a la marca GitHub.

### 2. AWS Kiro

- **Qué es:** IDE agéntico (fork de Code OSS) donde cada feature genera `requirements.md` (notación EARS: "WHEN [condición] THE SYSTEM SHALL..."), `design.md` y `tasks.md`; el contexto persistente vive en `.kiro/steering/` con tres modos de inclusión por front-matter: `always`, `fileMatch` (+ `fileMatchPattern`) y `manual` (más un modo `auto` no configurable).[^kiro-specs][^kiro-steering]
- **Vigencia:** GA desde el 7 may 2026, sucesor oficial de Amazon Q Developer (retirado; altas nuevas bloqueadas desde el 15 may 2026). Activo, con planes de precio por créditos verificados jul 2026.[^kiro-pricing]
- **Licencia:** producto propietario de AWS (free tier + planes Pro/Pro+/Pro Max/Power); el formato de specs/steering no es un estándar independiente.[^kiro-pricing]
- **Ideas a adoptar:** notación EARS para requisitos verificables; los tres modos de inclusión de contexto (siempre / por patrón de archivo / manual bajo demanda) como mecanismo de presupuesto de tokens; trazabilidad requirements↔design↔tasks.
- **Qué NO copiar:** dependencia de IDE propietario y de Bedrock/Claude como único backend; modelo de créditos de pago.

### 3. BMAD Method

- **Qué es:** framework de agentes de rol (PM, Architect, Dev, QA, etc.) que organiza el desarrollo como un equipo ágil con handoffs explícitos y "story files" como unidad de contexto; se distribuye en módulos (BMM y otros) más una capa "BMad Builder".[^bmad-repo]
- **Vigencia:** BMM v6.8.0 y BMad Method v6.2.1 (may 2026); organización `bmad-code-org` activa.[^bmad-repo]
- **Licencia:** MIT.[^bmad-license]
- **Ideas a adoptar:** agente de rol = deliverable + punto de handoff explícito (mapea a "role agents" de ABM); "story file" como paquete de contexto transferible entre agentes.
- **Qué NO copiar:** paquete monolítico de ceremonial ágil completo; bundles web específicos por proveedor (Gemini/ChatGPT) como mecanismo de portabilidad.

### 4. Agent OS (Builder Methods)

- **Qué es:** sistema que extrae y "inyecta" estándares del propio código (brownfield) y ayuda a redactar mejores specs; en v3 dejó de orquestar implementación, delegándola al agente/modelo frontera.[^agentos-repo]
- **Vigencia:** v3.0.0 (20 ene 2026); alcance reenfocado solo a `standards/` + `specs/` + `product/`.[^agentos-v3]
- **Licencia:** MIT.[^agentos-repo]
- **Ideas a adoptar:** "discover standards" desde código existente para brownfield; carpeta `standards/` simple y portable entre herramientas de agente.
- **Qué NO copiar:** el recorte de alcance de v3 (ya no cubre implementación/orquestación) — ABM sí necesita ese tramo end-to-end.

### 5. AGENTS.md (estándar abierto)

- **Qué es:** archivo Markdown plano (sin frontmatter obligatorio; v1.1 propone `description`/`tags` opcionales) que documenta a un agente cómo trabajar en el repo; en monorepos se anida por paquete y aplica precedencia "closest file wins" (el más profundo se combina y prevalece sobre el raíz).[^agentsmd-site]
- **Vigencia:** formalizado ago 2025 (OpenAI, Google, Cursor, Factory); donado en dic 2025 a la Agentic AI Foundation (Linux Foundation); +60 000 proyectos adoptantes a esa fecha, sigue activo en 2026.[^linuxfoundation-aaif]
- **Licencia:** MIT (`agentsmd/agents.md`).[^agentsmd-repo]
- **Ideas a adoptar:** ya es la base de ABM (`CLAUDE.md` apunta a `AGENTS.md`); confirmar la regla de anidación "más específico gana" para módulos de un mismo ADS.
- **Qué NO copiar:** nada — es el estándar neutral que ABM adopta directamente como fuente única.

### 6. Agent Skills (agentskills.io)

- **Qué es:** estándar abierto para "skills": carpeta con `SKILL.md` (solo `name` y `description` obligatorios) más scripts/referencias/assets opcionales, cargados en tres etapas — *discovery* (metadata, ~30-50 tokens por skill), *activation* (cuerpo completo al coincidir la tarea) y *execution* (recursos bajo demanda).[^agentskills-repo][^simonwillison-skills]
- **Vigencia:** publicado por Anthropic el 18 dic 2025, cedido a la Agentic AI Foundation; adopción rápida (Microsoft/OpenAI en 48h; ~40 productos compatibles a jun 2026: Codex, Copilot, Cursor, Gemini CLI, VS Code).[^agentskills-site][^simonwillison-skills]
- **Licencia:** especificación abierta (`agentskills/agentskills`).[^agentskills-repo]
- **Ideas a adoptar:** progressive disclosure de 3 niveles como mecanismo central de presupuesto de tokens de ABM; formato mínimo de 2 campos obligatorios.
- **Qué NO copiar:** nada — es la base que ABM adopta directamente para su capa `skills/`.

### 7. Cursor rules y GitHub Copilot custom instructions (solo ideas de diseño)

- **Qué es:** (a) Cursor: `.cursor/rules/*.mdc` con frontmatter (`description`, `alwaysApply`, `globs`) y cuatro modos de activación — Always / Auto Attached (por glob) / Agent Requested (por descripción) / Manual — que reemplazó al `.cursorrules` legado (ignorado en modo Agent).[^cursor-rules-docs] (b) Copilot: `.github/copilot-instructions.md` (siempre cargado) más "prompt files" reutilizables invocables por comando, con referencias `@ruta` a otros archivos incluido `AGENTS.md`/`CLAUDE.md`.[^copilot-instructions-docs]
- **Vigencia:** ambas activas en 2026 como features de producto (no versionan como estándar independiente).
- **Licencia:** no aplica (funciones propietarias de cada IDE).
- **Ideas a adoptar:** activación condicional por glob/tipo de archivo o por descripción, para no cargar reglas irrelevantes (presupuesto de tokens); referencia cruzada entre convenciones (`@archivo`).
- **Qué NO copiar:** fragmentación de formato por editor (`.mdc` vs `.md` vs `copilot-instructions.md`) — ABM mantiene fuente única y genera adaptadores.

### 8. anthropics/skills y openai/skills

- **Qué es:** repos públicos de ejemplos de skills. `anthropics/skills`: ejemplos (algorithmic-art, brand-guidelines, internal-comms, etc.) más las skills de documentos (docx/pdf/pptx/xlsx) que usa Claude en producción. `openai/skills`: catálogo instalable para Codex vía `skill-installer`.[^anthropic-skills-repo][^openai-skills-repo]
- **Vigencia:** `anthropics/skills` activo. **`openai/skills` está marcado como deprecated en su propio README**, con migración recomendada a `openai/plugins`; sigue instalable en 2026 pero ya no es la vía canónica (Codex migra a `~/.agents/skills`).[^openai-codex-issue]
- **Licencia:** `anthropics/skills`: repo Apache-2.0, pero las skills de documentos son *source-available* (no libres para redistribuir sin revisar cada carpeta). `openai/skills`: licencia individual por skill (`LICENSE.txt` en cada carpeta).[^anthropic-skills-repo][^openai-skills-repo]
- **Ideas a adoptar:** patrón "ejemplo Apache-2.0 + nota source-available" para skills propias complejas de ABM; `LICENSE` por carpeta de skill cuando corresponda.
- **Qué NO copiar:** `openai/skills` como referencia de arquitectura activa — está en migración/obsolescencia declarada.

### 9. Categoría de LLM gateway (multi-LLM)

- **Qué ofrece la categoría:** capa de abstracción entre la app y varios proveedores LLM: API unificada (formato compatible OpenAI), enrutamiento y fallback entre modelos/proveedores, rate limiting, caché, observabilidad y control de costo — la pieza que sostiene portabilidad multi-LLM y multinube.[^gw-requesty]
- **3 opciones representativas:**
  - **LiteLLM** — proxy/SDK open source, autoalojado; núcleo MIT, carpeta enterprise bajo licencia comercial aparte; TCO real de autoalojar no es trivial (infraestructura + operación).[^gw-requesty]
  - **Portkey** — desde marzo 2026 su gateway es Apache-2.0 (autoalojable), con plataforma gestionada opcional para observabilidad/guardrails.[^gw-dibi8]
  - **OpenRouter** — marketplace hospedado, código cerrado, pago por uso, sin opción de autoalojamiento.[^gw-requesty]
- **Ideas a adoptar:** interfaz única compatible OpenAI para el ADR de portabilidad LLM, con fallback y límites de tasa centralizados.
- **Qué NO copiar:** el modelo hosted-only de OpenRouter si ABM requiere soberanía de datos on-prem/VPC.

## Ideas adoptadas en ABM

| Idea | Origen | Dónde aterriza en ABM |
|---|---|---|
| `constitution.md` (principios no negociables por proyecto) | GitHub Spec Kit | `methodology/` (modo SDD), `AGENTS.md` |
| Notación EARS para requisitos verificables | AWS Kiro | `templates/` (specs de modo SDD) |
| requirements → design → tasks con trazabilidad | Spec Kit + Kiro | `methodology/` (modo SDD) |
| 3 modos de inclusión de contexto (always/fileMatch/manual) | AWS Kiro (steering) | `skills/` + `commands/` (presupuesto de tokens) |
| Agente de rol = deliverable + handoff explícito | BMAD Method | `agents/` (role agents) |
| "Discover standards" desde código existente (brownfield) | Agent OS | `stacks/`, `init-project` |
| Fuente única + precedencia "closest file wins" en monorepo | Estándar AGENTS.md | `AGENTS.md` (anidado por módulo) |
| Progressive disclosure de 3 niveles (metadata → cuerpo → recursos) | Agent Skills / agentskills.io | `skills/` |
| Activación condicional por glob/descripción | Cursor rules | `commands/`, `skills/` |
| Referencia cruzada entre convenciones (`@archivo`) | Copilot custom instructions | generador de adaptadores |
| Ejemplo Apache-2.0 + nota source-available por skill compleja | anthropics/skills | `skills/` (licenciamiento) |
| API unificada multi-LLM con fallback y rate limiting | Categoría LLM gateway (LiteLLM/Portkey) | ADR de portabilidad LLM, `stacks/` |

## Fuentes metodológicas (Anexo A)

| URL | Estado | Reclamo en una línea |
|---|---|---|
| codysandahl.com/.../kill-the-ceremony... | Viva (200) | IDD/Minimum Viable Spec: especificar el "intent" (resultado, expectativas, restricciones) y dejar el "cómo" al agente reduce ceremonia frente a SDD.[^cs-idd] |
| linkedin.com/pulse/.../bhupendra-4t1we | No verificable (LinkedIn bloquea scraping/requiere login; no confirmado como caída) | — |
| webreactiva.com/blog/spdd | Viva (200) | SPDD trata el prompt estructurado (REASONS Canvas) como contrato versionado y vivo, sincronizado en ambos sentidos con el código, a diferencia de la spec estática de SDD.[^wr-spdd] |
| pasqualepillitteri.it/.../aidd-vs-vibe-coding... | Viva (200) | AIDD combina vibe coding exploratorio con SDD/gobernanza en producción; cita el caso Mercari (+150% productividad) como evidencia de SDD maduro con revisión humana.[^pp-aidd] |
| dev.to/krlz/spec-driven-development-in-2026... | Viva (200) | SDD en 2026 tiene un modelo de madurez de 3 niveles (Spec-First/Spec-Anchored/Spec-as-Source) y herramientas de referencia (Spec Kit, Kiro, cc-sdd) con EARS.[^dt-sdd2026] |
| intent-driven-development.com/landscape | Viva (200) | Ubica IDD como capa "aguas arriba" de SDD (3 niveles) frente a 3 escuelas paralelas de IDD (Build-First, Implementation-Last, Tree-Structured Operational).[^idd-landscape] |
| intent-driven.dev/knowledge/intent-driven-development/ | Viva (200) | IDD es la práctica paraguas de estructurar intención y contexto (context engineering + SDD + harness engineering + Ralph Loops) para que el agente construya lo correcto.[^idd-dev-knowledge] |

[^speckit-gh]: GitHub - github/spec-kit
[^speckit-releases]: Releases · github/spec-kit
[^kiro-specs]: Specs - Docs - Kiro
[^kiro-steering]: Steering - Docs - Kiro
[^kiro-pricing]: Pricing - Kiro
[^bmad-repo]: GitHub - bmad-code-org/BMAD-METHOD
[^bmad-license]: BMAD-METHOD LICENSE
[^agentos-repo]: GitHub - buildermethods/agent-os
[^agentos-v3]: Agent OS v3 - Leaner and more aligned for 2026
[^agentsmd-site]: AGENTS.md
[^agentsmd-repo]: GitHub - agentsmd/agents.md
[^linuxfoundation-aaif]: Linux Foundation announces the Agentic AI Foundation (AAIF)
[^agentskills-repo]: GitHub - agentskills/agentskills
[^agentskills-site]: Agent Skills Overview
[^simonwillison-skills]: Agent Skills (Simon Willison)
[^cursor-rules-docs]: Rules - Cursor Docs
[^copilot-instructions-docs]: Adding repository custom instructions for GitHub Copilot in your IDE
[^anthropic-skills-repo]: GitHub - anthropics/skills
[^openai-skills-repo]: GitHub - openai/skills
[^openai-codex-issue]: Open Source docs point to the deprecated skills repo
[^gw-requesty]: LiteLLM vs Portkey vs OpenRouter vs Requesty
[^gw-dibi8]: Portkey vs LiteLLM vs OpenRouter: LLM Gateway 2026
[^cs-idd]: Kill the Ceremony - Intent-Driven Development and the Minimum Viable Spec
[^wr-spdd]: SPDD vs SDD y por qué importan los prompts estructurados
[^pp-aidd]: AIDD vs Vibe Coding vs Spec-Driven Development (2026)
[^dt-sdd2026]: Spec-Driven Development in 2026: What It Is, the Tooling, and How Teams Actually Use It
[^idd-landscape]: The landscape of spec, intent, and AI-native development
[^idd-dev-knowledge]: Intent-Driven Development: Definition & Practices
