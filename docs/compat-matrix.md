---
type: Compat Matrix
title: Matriz de compatibilidad multi-herramienta
description: Cómo consume cada herramienta de IA las instrucciones, reglas, comandos, skills, subagentes, hooks, MCP, ignore, turbo y telemetría.
tags: [compatibilidad, adaptadores, herramientas]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:50:00Z }
stale_after: 2026-12-27T00:00:00Z
sources:
  - id: cc-memory
    resource: https://code.claude.com/docs/en/memory
    title: How Claude remembers your project
  - id: cc-skills
    resource: https://code.claude.com/docs/en/skills
    title: Extend Claude with skills
  - id: cc-hooks
    resource: https://code.claude.com/docs/en/hooks
    title: Hooks reference
  - id: cc-directory
    resource: https://code.claude.com/docs/en/claude-directory
    title: Explore the .claude directory
  - id: cc-permissions
    resource: https://code.claude.com/docs/en/permissions
    title: Configure permissions
  - id: cc-settings-ref
    resource: https://code.claude.com/docs/en/settings-reference
    title: Settings reference
  - id: cc-subagents
    resource: https://code.claude.com/docs/en/sub-agents
    title: Subagents
  - id: codex-config-ref
    resource: https://developers.openai.com/codex/config-reference
    title: Codex configuration reference
  - id: codex-agents-md
    resource: https://learn.chatgpt.com/docs/agent-configuration/agents-md
    title: Custom instructions with AGENTS.md (Codex)
  - id: codex-docs-config
    resource: https://github.com/openai/codex/blob/main/docs/config.md
    title: "codex/docs/config.md (hooks, managed-only note)"
  - id: ag-rules-workflows
    resource: https://antigravity.google/docs/rules-workflows/
    title: Rules (Google Antigravity Docs)
  - id: ag-skills
    resource: https://antigravity.google/docs/skills/
    title: Agent skills (Google Antigravity Docs)
  - id: ag-cli-features
    resource: https://antigravity.google/docs/cli/features/
    title: Antigravity CLI Features
  - id: ag-mcp
    resource: https://antigravity.google/docs/mcp/
    title: MCP (Google Antigravity Docs)
  - id: ag-codelab
    resource: https://codelabs.developers.google.com/autonomous-ai-developer-pipelines-antigravity
    title: Build Autonomous Developer Pipelines using agents.md and skills.md in Antigravity
  - id: vscode-custom-instructions
    resource: https://code.visualstudio.com/docs/agent-customization/custom-instructions
    title: Use custom instructions in VS Code
  - id: gh-repo-instructions
    resource: https://docs.github.com/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
    title: Adding repository custom instructions for GitHub Copilot
  - id: gh-copilot-agentsmd-changelog
    resource: https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/
    title: Copilot coding agent now supports AGENTS.md custom instructions
  - id: vscode-mcp-servers
    resource: https://code.visualstudio.com/docs/agent-customization/mcp-servers
    title: Add and manage MCP servers in VS Code
  - id: gh-copilot-mcp-config
    resource: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers
    title: Configure MCP servers for your repository
  - id: gh-copilot-cli-agents
    resource: https://github.com/github/copilot-cli-for-beginners/blob/main/04-agents-custom-instructions/README.md
    title: "copilot-cli-for-beginners: Using Agents (.agent.md)"
  - id: gh-copilot-enterprise-perms
    resource: https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations/
    title: Enterprise-managed permissions for GitHub Copilot agent operations
  - id: cursor-rules
    resource: https://cursor.com/docs/rules
    title: Rules (Cursor Docs)
  - id: cursor-skills
    resource: https://cursor.com/docs/skills
    title: Skills (Cursor Docs)
  - id: cursor-subagents
    resource: https://cursor.com/docs/subagents
    title: Subagents (Cursor Docs)
  - id: cursor-mcp
    resource: https://cursor.com/docs/mcp
    title: Model Context Protocol (MCP) (Cursor Docs)
  - id: cursor-ignore
    resource: https://cursor.com/docs/reference/ignore-file
    title: Ignore File (Cursor Docs)
  - id: cursor-run-modes
    resource: https://cursor.com/docs/agent/security/run-modes
    title: Run Modes (Cursor Docs)
  - id: gcli-gemini-md
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
    title: "Gemini CLI: Provide context with GEMINI.md files"
  - id: gcli-ignore
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-ignore.md
    title: "Gemini CLI: Ignoring files (.geminiignore)"
  - id: gcli-subagents
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
    title: Gemini CLI Subagents
  - id: gcli-commands
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/custom-commands.md
    title: Gemini CLI Custom commands
  - id: gcli-mcp
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md
    title: MCP servers with Gemini CLI
  - id: gcli-skills
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
    title: Gemini CLI Agent Skills
  - id: gcli-telemetry
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/telemetry.md
    title: Gemini CLI Observability with OpenTelemetry
  - id: gcli-config-ref
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md
    title: Gemini CLI Configuration reference
  - id: devin-memories
    resource: https://docs.windsurf.com/windsurf/cascade/memories
    title: "Cascade Memories (Devin Desktop docs; Windsurf legacy)"
  - id: devin-workflows
    resource: https://docs.windsurf.com/windsurf/cascade/workflows
    title: "Cascade workflows (Devin Desktop docs; Windsurf legacy)"
  - id: devin-mcp
    resource: https://docs.devin.ai/desktop/cascade/mcp
    title: Cascade MCP Integration
  - id: devin-terminal
    resource: https://docs.devin.ai/desktop/terminal
    title: "Terminal (auto-execution levels: Turbo)"
  - id: devin-ignore
    resource: https://docs.devin.ai/desktop/context-awareness/windsurf-ignore
    title: Devin Desktop Ignore (.devinignore)
  - id: kiro-steering
    resource: https://kiro.dev/docs/steering/
    title: Steering (Kiro Docs)
  - id: kiro-hooks
    resource: https://kiro.dev/docs/hooks/
    title: Hooks (Kiro Docs)
  - id: kiro-mcp
    resource: https://kiro.dev/docs/mcp/configuration/
    title: MCP Configuration (Kiro Docs)
  - id: kiro-permissions
    resource: https://kiro.dev/docs/permissions/
    title: Permissions (Kiro Docs)
  - id: kiro-agents
    resource: https://kiro.dev/docs/custom-agents/
    title: Custom agents (Kiro Docs)
  - id: kiro-ignore
    resource: https://kiro.dev/docs/kiroignore/
    title: .kiroignore (referenced from Kiro Docs: Built-in tools)
  - id: hermes-config
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
    title: Hermes Agent Configuration
  - id: hermes-skills
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
    title: "Hermes Agent: Skills System"
  - id: hermes-security
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/security
    title: "Hermes Agent: Security"
  - id: hermes-repo
    resource: https://github.com/NousResearch/hermes-agent
    title: NousResearch/hermes-agent (repo root, AGENTS.md, skills/)
  - id: hermes-bundled
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-hermes-agent
    title: "Hermes Agent bundled skill: Key Paths"
  - id: zed-instructions
    resource: https://zed.dev/docs/ai/instructions
    title: Agent Instructions (Zed)
  - id: junie-guidelines
    resource: https://junie.jetbrains.com/docs/guidelines-and-memory.html
    title: Guidelines and memory (Junie)
  - id: cline-rules
    resource: https://docs.cline.bot/customization/cline-rules
    title: Rules (Cline)
  - id: opencode-rules
    resource: https://opencode.ai/docs/rules/
    title: Rules (opencode)
  - id: opencode-instructions-v2
    resource: https://opencode.ai/v2/docs/instructions/
    title: Instructions (opencode v2)
  - id: amp-agentsmd
    resource: https://ampcode.com/docs/customize/agents-md
    title: AGENTS.md (Amp Docs)
  - id: aider-conventions
    resource: https://aider.chat/docs/usage/conventions.html
    title: Specifying coding conventions (Aider)
  - id: roocode-agentsmd-issue
    resource: https://github.com/RooCodeInc/Roo-Code/issues/5966
    title: "Add Support for Agent Rules Standard via Project Root AGENTS.md (Roo Code issue)"
---

# Matriz de compatibilidad multi-herramienta

Fuente para un generador que emita adapters desde una fuente neutral única
(`AGENTS.md` + `commands/*.md` + `skills/<name>/SKILL.md` + `agents/<role>.md` + `standards/`).
Todo lo marcado `no-verificado` no debe usarse para generar rutas: requiere verificación humana
antes de codificarse en el generador.

## 1. Claude Code

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `./CLAUDE.md` o `./.claude/CLAUDE.md` (proyecto) + `~/.claude/CLAUDE.md` (usuario). Lee `AGENTS.md` nativamente desde v2.1.277: por defecto (`claude-md-or-agents-md`) solo si no hay `CLAUDE.md`/`CLAUDE.local.md` en el cwd o superiores; `claude-md-and-agents-md` carga ambos (CLAUDE.md primero). Nested: cada subdirectorio con `AGENTS.md` se carga al leer un archivo ahí. Import `@AGENTS.md` desde CLAUDE.md como alternativa. | [^cc-memory] |
| b. Reglas path-scoped | `.claude/rules/*.md` (recursivo), frontmatter YAML `paths:` (glob list o CSV). Sin `paths` = siempre activa. Budget: 1000 patrones expandidos / 4 MiB por regla. `~/.claude/rules/` = global. | [^cc-memory] |
| c. Comandos/prompts | `.claude/commands/*.md` (legacy, sigue funcionando) fusionado dentro de Skills: frontmatter `description`, invocación `/nombre`. | [^cc-skills] |
| d. Skills | `.claude/skills/<name>/SKILL.md` (proyecto) y `~/.claude/skills/<name>/SKILL.md` (usuario). Estándar Agent Skills (agentskills.io) + extensiones: invocation control, subagent execution, dynamic context injection. | [^cc-skills] |
| e. Subagentes | `.claude/agents/*.md` (proyecto) + `~/.claude/agents/*.md` (usuario, menor prioridad), recursivo. Frontmatter: `name`, `description`, `tools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, etc. | [^cc-subagents] |
| f. Hooks | `hooks` en `settings.json` (`~/.claude/settings.json` user, `.claude/settings.json` proyecto, `.claude/settings.local.json` local, managed policy). Eventos: `PreToolUse`, `PostToolUse`, `SessionStart`, etc. También en frontmatter de skill/subagent. | [^cc-hooks] |
| g. MCP | `.mcp.json` en la raíz del proyecto (`{"mcpServers": {...}}`); también `~/.claude.json` (usuario) y `managed-mcp.json` (managed). Aprobación vía `enabledMcpjsonServers`/`disabledMcpjsonServers`/`enableAllProjectMcpServers` en `settings.local.json`. | [^cc-settings-ref] |
| h. Ignore | No hay archivo de ignore dedicado; se usa `permissions.deny` con reglas `Read(...)`/`Edit(...)` sobre paths, más `respectGitignore` (activa por defecto). | [^cc-settings-ref] |
| i. Límites | CLAUDE.md recomendado <200 líneas (afecta adherencia, no es límite duro). Frontmatter `paths` de una regla: 1000 patrones expandidos / 4 MiB. Descripciones combinadas de subagentes >15 000 tokens generan warning. | [^cc-memory] [^cc-subagents] |
| j. Turbo | `permissions.allow` / `permissions.ask` / `permissions.deny` (sintaxis `Tool(specifier)`, ej. `Bash(npm run *)`, `Read(./.env)`); evaluación `deny > ask > allow`. `permissions.defaultMode`: `default`\|`acceptEdits`\|`plan`\|`auto`\|`dontAsk`\|`bypassPermissions`. Todo en `.claude/settings.json`. | [^cc-settings-ref] [^cc-permissions] |
| k. Telemetría | `CLAUDE_CODE_ENABLE_TELEMETRY=1` + `OTEL_EXPORTER_OTLP_*` / `OTEL_LOGS_EXPORTER` / `OTEL_METRICS_EXPORTER` / `OTEL_TRACES_EXPORTER` (OpenTelemetry). `/usage` en CLI. `modelPricing` permite reportar costo a tarifa propia. | [^cc-settings-ref] |

## 2. OpenAI Codex (CLI, extensión IDE, cloud)

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `AGENTS.md` nativo (lo lee "before doing any work"), lookup por directorio desde la raíz del repo hasta el cwd: `AGENTS.override.md` → `AGENTS.md` → `project_doc_fallback_filenames` (array de nombres extra, ej. `CLAUDE.md`). `project_doc_max_bytes` limita bytes leídos (config.toml). No hay `CODEX.md` propio. | [^codex-agents-md] [^codex-config-ref] |
| b. Reglas path-scoped | No hay mecanismo de glob-scoped rules nativo separado de AGENTS.md anidados (jerarquía por directorio del propio AGENTS.md cumple ese rol). `no-verificado` para un formato de frontmatter con `globs` dedicado. | no-verificado |
| c. Comandos/prompts | `~/.codex/prompts/*.md`: prompts personalizados expuestos como slash commands en sesión interactiva. **Solo a nivel usuario** — no hay convención `.codex/prompts/` a nivel de proyecto documentada (issue abierto pidiéndolo). Equipo Codex recomienda usar Skills en su lugar para lo compartible en repo. | [^codex-config-ref] |
| d. Skills | `SKILL.md` en `~/.codex/skills/<name>/` (personal) y `.codex/skills/<name>/` (proyecto, relativo al repo). Config fino en `config.toml`: `skills.config[].path`, `skills.config[].enabled`, `skills.max_context_tokens`. `features.skill_mcp_dependency_install`. | [^codex-config-ref] |
| e. Subagentes | No hay archivo de subagente dedicado tipo Claude Code; Codex expone "apps" (`apps.<id>`) y políticas de aprobación por app, no un formato `agents/<role>.md`. `no-verificado` como equivalente directo. | no-verificado |
| f. Hooks | `hooks` inline en `config.toml` o `hooks.json`, mismo schema de eventos (`PreToolUse`, `PermissionRequest`, `PostToolUse`, `SessionStart`, `SubagentStart`, etc.). `features.hooks` activa la carga. `allow_managed_hooks_only` solo en `requirements.toml` (managed). | [^codex-config-ref] [^codex-docs-config] |
| g. MCP | `[mcp_servers.<id>]` en `config.toml`: `command`/`args`/`env`/`url` (HTTP), `auth`, `default_tools_approval_mode`, `enabled_tools`/`disabled_tools`, `startup_timeout_sec`. Config de usuario en `~/.codex/config.toml`; overrides de proyecto en `.codex/config.toml` (solo si el proyecto es *trusted*). | [^codex-config-ref] |
| h. Ignore | `no-verificado` — no se encontró un `.codexignore` documentado; el control de acceso a archivos pasa por `sandbox_mode`/`sandbox_workspace_write.writable_roots` y `trust_level` por proyecto. | no-verificado |
| i. Límites | `project_doc_max_bytes` (default 32768 según plantilla comunitaria, confirmado como key oficial: "Maximum bytes read from AGENTS.md"). `skills.max_context_tokens` cap explícito en 10000 tokens. | [^codex-config-ref] |
| j. Turbo | `approval_policy`: `on-request`\|`never`\|`{granular:{sandbox_approval,rules,mcp_elicitations,request_permissions,skill_approval}}` (ya no soporta `untrusted`; `on-failure` deprecado). `sandbox_mode`: `read-only`\|`workspace-write`\|`danger-full-access`. `approvals_reviewer`: `user`\|`auto_review`. Todo en `config.toml` (raíz o `~/.codex/config.toml`). | [^codex-config-ref] |
| k. Telemetría | `[otel]` en config.toml: `otel.exporter` (`none`\|`otlp-http`\|`otlp-grpc`), `otel.trace_exporter`, `otel.metrics_exporter` (default `statsig`), `otel.log_user_prompt`, endpoints/headers/TLS por exportador. Variables de telemetría ignoradas si se ponen en `.codex/config.toml` de proyecto (deben ir en config de usuario). | [^codex-config-ref] |

## 3. Google Antigravity

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | Lee `AGENTS.md`, `GEMINI.md` o `.agents/rules/*.md` nativamente en la raíz del workspace o subdirectorios ("workspace rules"). Global: `~/.gemini/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.gemini/config/rules/*.md` (IDE) o `~/.gemini/antigravity-cli/rules/*.md` (CLI). | [^ag-rules-workflows] |
| b. Reglas path-scoped | Frontmatter YAML en `.agents/rules/*.md` con `activation`: `model_decision` (progressive disclosure, solo `description` se inyecta), `always_on` (contenido completo cada turno), `glob` (`globs: [...]` comma-separated). `AGENTS.md`/`GEMINI.md` sin frontmatter = siempre `always_on`. Soporta file-includes dentro de cualquier rule file. | [^ag-rules-workflows] |
| c. Comandos/prompts | Workflows en `.agents/workflows/<name>.md` (workspace) o `~/.gemini/config/global_workflows/` (global); invocados como `/name`. | [^ag-codelab] [^ag-cli-features] |
| d. Skills | `<workspace-root>/.agents/skills/<skill-folder>/SKILL.md` (workspace) y `~/.gemini/config/skills/<skill-folder>/` (global; CLI usa `~/.gemini/antigravity-cli/skills/`). Plugin-provided skills en `~/.gemini/antigravity-cli/plugins/<name>/skills/`. | [^ag-skills] |
| e. Subagentes | Definidos vía `agents.md` como "equipo" de personas/roles dentro del propio workspace (patrón de codelab), no un directorio `agents/*.md` por-archivo documentado de forma estable como en Claude/Cursor/Gemini CLI. Plugins sí exponen `agents/` como carpeta. `parcial`. | [^ag-codelab] |
| f. Hooks | Plugins soportan `hooks.json` (eventos) dentro de `~/.gemini/antigravity-cli/plugins/<name>/hooks.json`. No confirmado un hooks.json a nivel de proyecto fuera de plugins. | [^ag-cli-features] |
| g. MCP | `~/.gemini/config/mcp_config.json` (global) o `.agents/mcp_config.json` (workspace local); plugins añaden `mcp_config.json` propio. Shape `{"mcpServers": {...}}`. | [^ag-mcp] |
| h. Ignore | `no-verificado` (no se localizó `.antigravityignore` o `.aiexclude` documentado específico de Antigravity 2.0 en las páginas revisadas). | no-verificado |
| i. Límites | `no-verificado` (sin cifra de límite de caracteres/bytes documentada en las páginas revisadas). | no-verificado |
| j. Turbo | `settings.json` → `permissions.allow` / `permissions.deny` con sintaxis `command(<cmd>)`, ej. `"allow": ["command(git)", "command(npm test)"], "deny": ["command(rm -rf)"]`. | [^ag-cli-features] |
| k. Telemetría | `no-verificado`. | no-verificado |

## 4. VS Code + GitHub Copilot (agent mode / coding agent)

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `AGENTS.md` (soportado por Copilot coding agent y por el "Local agent" de VS Code desde `chat.useAgentsMdFile`), uno o varios por repo — el más cercano al path editado gana. También `.github/copilot-instructions.md` (repo-wide, always-on) y `~/.copilot/copilot-instructions.md` (personal, Agent Host). Nested AGENTS.md configurable con `chat.useNestedAgentsMdFiles` (off por defecto). | [^gh-repo-instructions] [^vscode-custom-instructions] [^gh-copilot-agentsmd-changelog] |
| b. Reglas path-scoped | `.github/instructions/*.instructions.md`, frontmatter `applyTo: "<glob>"` (comma-separated para varios patrones) + opcional `excludeAgent: "code-review"\|"cloud-agent"`. Sin `applyTo` = inerte hasta adjuntarlo manualmente. | [^gh-repo-instructions] [^vscode-custom-instructions] |
| c. Comandos/prompts | `.github/prompts/*.prompt.md` (compartido, team) o perfil de usuario de VS Code (personal); invocación `/nombre`. Frontmatter: `name`, `agent` (`ask`\|`agent`\|`plan`\|nombre de agente custom), `tools`, `model`. Soporta `${input:variable}`. | [^vscode-custom-instructions] |
| d. Skills | `.github/skills/<name>/SKILL.md` (también compatible con `.claude/skills`). Estándar Agent Skills; activadas automáticamente por descripción o vía CLI. | (comunidad/GitHub org discussion, no doc oficial dedicado) no-verificado |
| e. Subagentes | `.github/agents/<name>.agent.md`: Markdown + frontmatter YAML (metadata) + cuerpo = system prompt. Config de MCP servers también soportada en el frontmatter del agente (custom-agents-configuration). | [^gh-copilot-cli-agents] |
| f. Hooks | `no-verificado` — no se encontró un mecanismo de hooks de ciclo de vida propio de Copilot (paralelo a Claude Code/Codex/Kiro) en las páginas oficiales revisadas. | no-verificado |
| g. MCP | `.vscode/mcp.json` (VS Code local, key `servers`) — el Agent Host NO lo lee directo, VS Code lo reenvía salvo inputs interactivos. Para Agent Host / Copilot CLI portable: `.mcp.json` (workspace) o `~/.copilot/mcp-config.json` (usuario), key `mcpServers`. Para Copilot cloud agent / code review: config JSON pegada en Settings del repo en GitHub.com (compartida entre ambos). | [^vscode-mcp-servers] [^gh-copilot-mcp-config] |
| h. Ignore | `no-verificado` — no existe un `.copilotignore` de repo documentado como estándar; el control es vía "content exclusion" a nivel organización (política, no archivo de repo). | no-verificado |
| i. Límites | Prompt de generación recomienda instrucciones "no longer than 2 pages" para `copilot-instructions.md` (guía, no límite duro de la plataforma). | [^gh-repo-instructions] |
| j. Turbo | `chat.tools.global.autoApprove` (bool) y `chat.tools.terminal.autoApprove` (mapa comando→bool, soporta regex) en `settings.json` de VS Code/usuario. `chat.agent.maxRequests` limita iteraciones. Nivel Enterprise: `managed-settings.json` con reglas `deny`/`ask`/`allow` por shell/archivo/dominio — precedencia `deny > ask > allow`, y puede desactivar el auto-approve del developer (`permissions.disableBypassPermissionsMode`). | [^gh-copilot-enterprise-perms] |
| k. Telemetría | `no-verificado` a nivel de sesión/proyecto (no se encontró exportador OTel documentado); GitHub expone métricas de uso de Copilot a nivel organización vía API/dashboard, no por proyecto. | no-verificado |

## 5. Cursor

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `AGENTS.md` en la raíz y subdirectorios ("nested AGENTS.md" — instrucciones se combinan, la más específica gana) como alternativa simple a `.cursor/rules`. No hay `CURSOR.md` propio. | [^cursor-rules] |
| b. Reglas path-scoped | `.cursor/rules/*.mdc` (extensión `.mdc` obligatoria; un `.md` sin frontmatter es ignorado). Frontmatter: `description`, `globs`, `alwaysApply`. Combinaciones: `alwaysApply:true` = always; `globs` sin alwaysApply = auto-attached; solo `description` = agent-decided; ninguno = manual (`@rule`). Precedencia: Team Rules → Project Rules → User Rules. | [^cursor-rules] |
| c. Comandos/prompts | Slash-commands legacy migrados a Skills (`/migrate-to-skills` en Cursor 2.4+); `/create-rule` y `/create-skill` generan archivos. No hay ya un directorio `.cursor/commands/` separado y estable. | [^cursor-skills] |
| d. Skills | `.cursor/skills/<name>/SKILL.md` (proyecto) y `~/.cursor/skills/` (usuario), también `.agents/skills/` y `~/.agents/skills/` como alias interoperable. Compat cross-tool: también lee `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`. Frontmatter opcional `paths:` para scoping. | [^cursor-skills] |
| e. Subagentes | `.cursor/agents/*.md` (proyecto) + `~/.cursor/agents/*.md` (usuario); compat cross-tool: también `.claude/agents/`, `.codex/agents/` (y sus equivalentes `~/`). Conflicto de nombres: `.cursor/` gana sobre `.claude/`/`.codex/`. Frontmatter: `name`, `description`, `model` (`inherit` o ID + `[opciones]`), `readonly`, `is_background`. | [^cursor-subagents] |
| f. Hooks | `cursor.com/docs/hooks` existe como página dedicada (no explorada en profundidad en esta pasada) — mencionada como mecanismo para post-procesar salida de subagentes. `parcial`. | [^cursor-subagents] |
| g. MCP | `.cursor/mcp.json` (proyecto) y `~/.cursor/mcp.json` (global), key `mcpServers`; soporta `stdio`/`SSE`/`Streamable HTTP`, `auth` (OAuth estático), interpolación `${env:VAR}`, `${workspaceFolder}`. | [^cursor-mcp] |
| h. Ignore | `.cursorignore` (best-effort, excluye de AI features + indexing) y `.cursorindexingignore` (solo indexing/búsqueda), sintaxis `.gitignore`. | [^cursor-ignore] |
| i. Límites | Guía de buenas prácticas recomienda reglas <500 líneas (no es límite duro de la plataforma). | [^cursor-rules] |
| j. Turbo | "Run Modes": `Auto-review` (allowlist → sandbox → classifier subagent, reduce prompts ~84%) vs `Run Everything` (ex-YOLO, sin verificación). Config en Settings → Agents → Approvals & Execution (no es un archivo versionable en el repo; es config de la app/usuario). MCP admin allowlist en el dashboard Team/Enterprise. | [^cursor-run-modes] |
| k. Telemetría | `no-verificado` a nivel de export OTel de proyecto; existe analítica de equipo en el dashboard de Cursor (nivel organización), no un archivo/env var de proyecto. | no-verificado |

## 6. Gemini CLI

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `GEMINI.md` por defecto, jerárquico: global `~/.gemini/GEMINI.md` → workspace/parent dirs → JIT al abrir archivos de un subdirectorio. Nombre configurable con `context.fileName` en `settings.json` (acepta array, ej. `["AGENTS.md","CONTEXT.md","GEMINI.md"]`) — así se logra soporte de `AGENTS.md`, pero no es automático sin ese ajuste. Imports con `@file.md`. | [^gcli-gemini-md] |
| b. Reglas path-scoped | No hay un formato de "regla" separado con `globs` propio (el propio `GEMINI.md`/`AGENTS.md` jerárquico + JIT-loading por directorio cumple ese rol). | [^gcli-gemini-md] |
| c. Comandos/prompts | `.gemini/commands/*.toml` (proyecto, override) y `~/.gemini/commands/*.toml` (usuario/global). Namespacing por subdirectorio (`git/commit.toml` → `/git:commit`). Campos: `prompt` (requerido), `description` (opcional). Soporta `{{args}}`, `!{shell}`, `@{file}`. | [^gcli-commands] |
| d. Skills | `.gemini/skills/` o alias `.agents/skills/` (workspace); `~/.gemini/skills/` o `~/.agents/skills/` (usuario). Estándar Agent Skills (agentskills.io). Precedencia: built-in < extension < user < workspace; dentro de un tier, `.agents/skills/` > `.gemini/skills/`. | [^gcli-skills] |
| e. Subagentes | `.gemini/agents/*.md` (proyecto) + `~/.gemini/agents/*.md` (usuario). Frontmatter: `name`, `description`, `kind` (`local`\|`remote`), `tools` (con wildcards `*`, `mcp_*`, `mcp_<server>_*`), `mcpServers` (inline), `model`, `temperature`, `max_turns`, `timeout_mins`. Sin recursión (un subagente no puede lanzar otro). | [^gcli-subagents] |
| f. Hooks | `hooks.<Event>` en `settings.json`: `BeforeTool`, `AfterTool`, `BeforeAgent`, `AfterAgent`, `Notification`, `SessionStart`, `SessionEnd`, `PreCompress`, `BeforeModel`, `AfterModel`, `BeforeToolSelection`. | [^gcli-config-ref] |
| g. MCP | `mcpServers` en `settings.json` (proyecto `.gemini/settings.json` o usuario `~/.gemini/settings.json`); campos `command`/`args`/`env`/`cwd`/`timeout`/`trust`/`includeTools`/`excludeTools`/OAuth. Control global en `mcp.allowed`/`mcp.excluded`/`mcp.serverCommand`. CLI: `gemini mcp add/list/remove/enable/disable`. | [^gcli-mcp] |
| h. Ignore | `.geminiignore` en la raíz del proyecto, sintaxis `.gitignore` (soporta `!` negación); análogo a `.aiexclude` de Gemini Code Assist. | [^gcli-ignore] |
| i. Límites | Sin cifra de tamaño de archivo de contexto documentada; `skills.max_context_tokens` no aplica aquí (es de Codex). | no-verificado |
| j. Turbo | `general.defaultApprovalMode` en `settings.json`: `default`\|`auto_edit`\|`plan` (YOLO/auto-approve-todo solo vía flag CLI `--yolo` o `--approval-mode=yolo`, no seteable en `settings.json`). Además `--allowed-tools` por sesión y Policy Engine (`policy.toml`) para reglas finas por subagente/tool. | [^gcli-config-ref] |
| k. Telemetría | `telemetry.*` en `.gemini/settings.json` (`enabled`, `target`: `gcp`\|`local`, `otlpEndpoint`, `otlpProtocol`, `outfile`, `logPrompts`) + env vars `GEMINI_TELEMETRY_ENABLED`/`GEMINI_TELEMETRY_OTLP_ENDPOINT`/etc. Exporta a Google Cloud Trace/Monitoring/Logging o a un `.log` local. Eventos GenAI semantic-convention (`gen_ai.client.token.usage`, etc.). | [^gcli-telemetry] |

## 7. Windsurf (ahora "Devin Desktop", Cascade) — Cognition AI

> Nota de vigencia: Windsurf fue adquirido/fusionado por Cognition AI. La documentación vive ahora en `docs.devin.ai` bajo el agente **Cascade** dentro de **Devin Desktop**; `docs.windsurf.com` redirige ahí. Las rutas `.windsurf/*` siguen funcionando como *fallback* legacy, pero la ruta preferida es `.devin/*`.

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | No lee `AGENTS.md` como archivo de instrucción monolítico dedicado fuera del sistema de Rules; un `AGENTS.md` en cualquier directorio del workspace se procesa por el mismo motor de Rules (root = always-on, subdirectorio = auto-glob para esa carpeta). Legacy: `.windsurfrules` (single file, raíz) sigue leyéndose. | [^devin-memories] |
| b. Reglas path-scoped | `.devin/rules/*.md` (preferido) o `.windsurf/rules/*.md` (fallback legacy) — un archivo por regla, frontmatter YAML `trigger:` (`always_on`\|`model_decision`\|`glob`+`globs:`\|`manual`). Global: `~/.codeium/windsurf/memories/global_rules.md` (siempre on, sin frontmatter). Enterprise: `/etc/devin/rules/*.md` (o legacy `/etc/windsurf/rules/*.md`). | [^devin-memories] |
| c. Comandos/prompts | Workflows en `.devin/workflows/*.md` (preferido) o `.windsurf/workflows/*.md` (fallback), invocados `/[workflow-name]`; solo manuales (nunca automáticos). Global: `~/.codeium/windsurf/global_workflows/*.md`. Enterprise: `/etc/devin/workflows/*.md`. | [^devin-workflows] |
| d. Skills | Cascade tiene un sistema de "Skills" separado de Workflows/Rules (reemplaza el uso de Memories para conocimiento durable); ruta exacta de archivo `no-verificado` en esta pasada. | no-verificado |
| e. Subagentes | `no-verificado` (no localizado un mecanismo de subagentes tipo `agents/*.md` en Cascade/Devin Desktop). | no-verificado |
| f. Hooks | `no-verificado`. | no-verificado |
| g. MCP | `mcp_config.json`, global en `~/.codeium/windsurf/mcp_config.json` (o gestionado vía UI: icono MCP → Configure); shape `{"mcpServers": {"name": {"command","args","env"}}}`. Enterprise: allow/deny lists de servidores. | [^devin-mcp] |
| h. Ignore | `.devinignore` en la raíz (nuevo nombre; antes `.codeiumignore`/implícito `.windsurfignore`), sintaxis tipo `.gitignore`. | [^devin-ignore] |
| i. Límites | Reglas de workspace: **12 000 caracteres por archivo** (`.devin/rules/*.md` o `.windsurf/rules/*.md`); regla global (`global_rules.md`): **6 000 caracteres**. Workflows: **12 000 caracteres por archivo**. | [^devin-memories] [^devin-workflows] |
| j. Turbo | "Auto-Execution Levels" en Terminal settings: **Turbo** = auto-ejecuta todo excepto lo listado en deny list; niveles intermedios más conservadores existen por debajo. Enterprise: allow/deny lists organization-wide para auto-ejecución de comandos. | [^devin-terminal] |
| k. Telemetría | `no-verificado` (no se encontró exportador OTel de proyecto documentado; puede existir analítica a nivel Enterprise/dashboard). | no-verificado |

## 8. Kiro (AWS)

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | No usa `AGENTS.md` como archivo raíz único; usa **Steering** (ver b). `no-verificado` si Kiro además lee `AGENTS.md` de forma nativa como fallback. | no-verificado |
| b. Reglas path-scoped | `.kiro/steering/*.md` (workspace) o `~/.kiro/steering/` (global). Frontmatter YAML: `inclusion: always` (default, siempre cargado) \| `fileMatch` + `fileMatchPattern: [...]` (glob) \| `manual` (`#steering-file-name` en chat) \| auto (por `description`, con `name`+`description` requeridos). | [^kiro-steering] |
| c. Comandos/prompts | No hay slash-commands de usuario tipo `.md`/`.toml` documentados; el equivalente son **Hooks** (ver f) y **Specs** (`.kiro/specs/`, flujo spec-driven, no explorado en profundidad). "Powers" (`.kiro/` plugin format: `plugin.json` + `skills/` + `mcp.json`) agrupa comportamiento reutilizable con `always`/`auto`/`fileMatch`/`manual`. | [^kiro-steering] |
| d. Skills | Vía **Powers**: `plugin.json` (manifest) + `skills/<name>/SKILL.md` + `mcp.json` opcional. También referenciable desde un custom agent con `resources: ["skill://<name>"]`. Ruta exacta de "skills sueltas" fuera de Powers: `no-verificado`. | no-verificado |
| e. Subagentes | **Custom agents**: `.kiro/agents/<name>.json` o `.kiro/agents/<name>.md` (proyecto, requiere workspace trust) + `~/.kiro/agents/<name>.{json,md}` (global, menor prioridad). Campos: `name`, `description`, `tools`, `excludedTools`, `includeMcpJson`, `includePowers`, `resources`, `permissions.rules`, `prompt`, `model`. Nested dirs soportados (nombre = path relativo sin extensión). | [^kiro-agents] |
| f. Hooks | `.kiro/hooks/<id>.json` (formato v1, IDE 1.0/CLI 3.0+). Triggers: `PromptSubmit`, `AgentStop`, `SessionStart` (IDE), `AgentSpawn` (CLI), `PreToolUse`, `PostToolUse`, `FileCreate`/`FileSave`/`FileDelete`, `PreTaskExecution`/`PostTaskExecution` (specs). Acción `command` (shell, stdin=JSON) o `agent` (prompt inyectado); campo `confirm` para pedir aprobación. | [^kiro-hooks] |
| g. MCP | `.kiro/settings/mcp.json` (workspace) + `~/.kiro/settings/mcp.json` (usuario) — se fusionan, workspace gana; prioridad real: Agent Config `mcpServers` > Workspace > Global. Campos: `command`/`args`/`env`/`url`/`headers`/`disabled`/`autoApprove` (array o `"*"`)/`disabledTools`/`oauth`. Hot-reload al guardar. | [^kiro-mcp] |
| h. Ignore | `.kiroignore` en la raíz, sintaxis `.gitignore`; soporte varía por superficie (IDE/CLI/Web). Kiro-scope hardcoded: siempre pide confirmación (`ask`) escribir en `.kiroignore` aunque un preset dé `allow-all`. | [^kiro-ignore] [^kiro-permissions] |
| i. Límites | Sin cifra de tamaño de steering file documentada. | no-verificado |
| j. Turbo | Dos capas: (1) **Agent Autonomy** IDE-level (`kiroAgent.agentAutonomy`): `Autopilot` (procede sin preguntar en lo permitido) vs `Supervised` (siempre pregunta). (2) **`permissions.yaml`** capability-based: `~/.kiro/settings/permissions.yaml` (usuario) y `~/.kiro/workspace-roots/<hash>/permissions.yaml` (workspace, **fuera del repo**, por-usuario). Capacidades: `fs_read`, `fs_write`, `shell`, `web_fetch`, `web_search`, `mcp`, `subagent`, `skill`, `power`, etc.; efectos `deny`>`ask`>`allow`; `match`/`exclude` glob. Kiro-scope hardcoded: siempre deniega escritura a `~/.kiro/settings/`, `.kiro/settings/`, `~/.kiro/workspace-roots/`. | [^kiro-permissions] |
| k. Telemetría | `no-verificado` (uso/costo se gestiona vía AWS/consola de Kiro, sin export OTel de proyecto documentado en esta pasada). | no-verificado |

## 9. Hermes Agent (Nous Research)

| Capacidad | Valor | Fuente |
|---|---|---|
| a. Instrucciones | `AGENTS.md`: "Project-specific instructions, coding conventions", scope "Recursive directory walk" (nativo, sin configuración). También `SOUL.md` en `~/.hermes/SOUL.md` (identidad del agente, slot #1 del system prompt, no es instrucción de proyecto). | [^hermes-config] |
| b. Reglas path-scoped | `no-verificado` — no se localizó un mecanismo de reglas con `globs`/frontmatter separado de `AGENTS.md`. | no-verificado |
| c. Comandos/prompts | Slash-commands documentados como built-in de sesión (`references/slash-commands.md` en el skill bundled); no se confirmó un directorio de comandos custom versionable por proyecto. `parcial`. | [^hermes-bundled] |
| d. Skills | **Fuente de verdad**: `~/.hermes/skills/` (global — bundled + hub-installed + agent-created; el agente puede modificar/borrar cualquiera). Proyecto: `<project-root>/.hermes/skills/` (nativo) y `<project-root>/.agents/skills/` (alias cross-tool). Escritura por el agente gateada por `skills.write_approval` (`false` por defecto = escribe libre). | [^hermes-skills] |
| e. Subagentes | No hay archivo `agents/<role>.md`; se delega vía tool `delegate_task` / spawning de instancias `hermes` adicionales (terminal, tmux, Docker, SSH, etc.) — "Delegates and parallelizes" es una capacidad de runtime, no de archivo de configuración por rol. | [^hermes-repo] |
| f. Hooks | `no-verificado` (no se encontró un sistema de hooks de ciclo de vida en la documentación revisada). | no-verificado |
| g. MCP | Vía `config.yaml` → `mcp_servers.<name>` (`command`/`args`/`env`), o CLI `hermes mcp`. También `MCP Config Reference` dedicada. No se confirmó archivo de MCP a nivel de proyecto separado del `config.yaml` global en `~/.hermes/config.yaml`. | [^hermes-bundled] |
| h. Ignore | `no-verificado`. | no-verificado |
| i. Límites | `no-verificado` (sin cifra de tamaño de AGENTS.md/skill documentada). | no-verificado |
| j. Turbo | `approvals.mode` en `config.yaml`: `smart`\|`manual`\|`off`. Capa adicional: `security.tirith_enabled` (scanner de comandos peligrosos pre-ejecución, con `tirith_fail_open`). "Dangerous command approval" es explícitamente una de las 8 capas de seguridad documentadas. | [^hermes-config] [^hermes-security] |
| k. Telemetría | Transcripts de sesión en `~/.hermes/sessions/*.jsonl` (gateway routing index + request dumps). `dashboard.show_token_analytics` (bool, default `false`) habilita analítica de tokens/costo **local-estimate-only** en el dashboard. No se confirmó exportador OTel. | [^hermes-config] |

## Resumen: herramientas × capacidades

✔ = soportado y verificado · parcial = soportado con matices/no confirmado del todo · ✖ = no encontrado / no aplica

| Capacidad | Claude Code | Codex | Antigravity | Copilot | Cursor | Gemini CLI | Windsurf/Devin | Kiro | Hermes |
|---|---|---|---|---|---|---|---|---|---|
| a. AGENTS.md nativo | ✔ (v2.1.277+) | ✔ | ✔ | ✔ | ✔ | parcial (vía `context.fileName`) | parcial (motor de Rules) | ✖ (no-verificado) | ✔ |
| b. Reglas path-scoped | ✔ `.claude/rules/` | ✖ | ✔ `.agents/rules/` | ✔ `.github/instructions/` | ✔ `.cursor/rules/*.mdc` | ✖ (usa jerarquía GEMINI.md) | ✔ `.devin\|.windsurf/rules/` | ✔ `.kiro/steering/` | ✖ |
| c. Comandos/workflows | ✔ (fusionado en skills) | parcial (`~/.codex/prompts`, user-only) | ✔ `.agents/workflows/` | ✔ `.github/prompts/*.prompt.md` | parcial (migrado a skills) | ✔ `.gemini/commands/*.toml` | ✔ `.devin\|.windsurf/workflows/` | parcial (Hooks/Specs/Powers) | parcial |
| d. Skills (SKILL.md) | ✔ `.claude/skills/` | ✔ `.codex/skills/` | ✔ `.agents/skills/` | ✔ `.github/skills/` (no-verificado oficial) | ✔ `.cursor/skills/` (+cross-tool) | ✔ `.gemini/skills/` | parcial | parcial (vía Powers) | ✔ `.hermes/skills/` |
| e. Subagentes | ✔ `.claude/agents/*.md` | ✖ | parcial | ✔ `.github/agents/*.agent.md` | ✔ `.cursor/agents/*.md` (+cross-tool) | ✔ `.gemini/agents/*.md` | ✖ | ✔ `.kiro/agents/*.json\|.md` | parcial (delegate_task, no archivo) |
| f. Hooks | ✔ `settings.json` | ✔ `hooks.json`/inline | parcial (solo plugins) | ✖ | parcial | ✔ `settings.json` | ✖ | ✔ `.kiro/hooks/*.json` | ✖ |
| g. MCP | ✔ `.mcp.json` | ✔ `config.toml` | ✔ `mcp_config.json` | ✔ `.vscode\|.mcp.json` | ✔ `.cursor/mcp.json` | ✔ `settings.json` | ✔ `mcp_config.json` | ✔ `.kiro/settings/mcp.json` | ✔ `config.yaml` |
| h. Ignore | ✖ (usa `permissions.deny`) | ✖ | ✖ | ✖ | ✔ `.cursorignore` | ✔ `.geminiignore` | ✔ `.devinignore` | ✔ `.kiroignore` | ✖ |
| i. Límites conocidos | parcial (~200 líneas rec.) | ✔ `project_doc_max_bytes` | ✖ | parcial (~2 páginas rec.) | parcial (~500 líneas rec.) | ✖ | ✔ 12k/6k caracteres | ✖ | ✖ |
| j. Turbo/auto-approve | ✔ `permissions.*` | ✔ `approval_policy`/`sandbox_mode` | ✔ `permissions.*` | ✔ `chat.tools.autoApprove` | ✔ Run Modes | ✔ `defaultApprovalMode` | ✔ Auto-Execution "Turbo" | ✔ `permissions.yaml` + Autopilot | ✔ `approvals.mode` |
| k. Telemetría | ✔ OTel + `/usage` | ✔ `[otel]` en config.toml | ✖ | ✖ | ✖ | ✔ OTel + GCP export | ✖ | ✖ | parcial (transcripts + estimate local) |

## Fallback universal (lectores nativos de AGENTS.md)

Verificación breve, no exhaustiva, de qué otras herramientas leen `AGENTS.md` de forma nativa —
útiles como "red de seguridad" cuando el generador no tiene un adapter dedicado.

| Herramienta | Lee AGENTS.md | Detalle | Fuente |
|---|---|---|---|
| Zed | ✔ | `AGENTS.md` es el archivo primario de instrucciones (proyecto y personal en `~/.config/zed/AGENTS.md`, `%APPDATA%\Zed\AGENTS.md` en Windows). Orden documentado de 9 entradas, AGENTS.md por encima de CLAUDE.md. | [^zed-instructions] |
| JetBrains Junie | ✔ | Junie CLI: `.junie/AGENTS.md` primero; si no existe, `AGENTS.md` de la raíz combinado con `.junie/playbook.md` + `.junie/rules/*.md`. AGENTS.md es ahora el archivo de guidelines por defecto. | [^junie-guidelines] |
| Cline / Roo (Roo Code) | Cline: ✔ · Roo: parcial | Cline lee `AGENTS.md` en la raíz del proyecto y `~/.agents/AGENTS.md` (global), junto a `.clinerules/`/`.cline/rules/`. Roo Code tiene un issue abierto para soportarlo vía `.roomodes`/Custom Modes; el repo aparece archivado según fuentes de comparación — estado de soporte actual `no-verificado`. | [^cline-rules] [^roocode-agentsmd-issue] |
| Aider | ✖ (sin auto-discovery) | No descubre ningún archivo de convención automáticamente. Requiere `/read CONVENTIONS.md`, `--read CONVENTIONS.md`, o `read: AGENTS.md` en `.aider.conf.yml`. | [^aider-conventions] |
| OpenCode | ✔ | `AGENTS.md` es la instrucción activa v2; carga global (`~/.config/opencode/AGENTS.md`) + cada `AGENTS.md` desde el workspace actual hacia el home. También cae de vuelta a `CLAUDE.md` si no hay `AGENTS.md` local (desactivable con `OPENCODE_DISABLE_CLAUDE_CODE=1`). | [^opencode-rules] [^opencode-instructions-v2] |
| Amp (Sourcegraph) | ✔ | `AGENTS.md` en cwd/parents/subtrees; fallback por directorio a `AGENT.md` (sin "S") o `CLAUDE.md` si `AGENTS.md` no existe ahí. Personal: `~/.config/amp/AGENTS.md`. Sistema: `/etc/ampcode/AGENTS.md`. No aplica a subagentes ni "raw custom agents". | [^amp-agentsmd] |

## Notas de generador (qué NO generar / solo user-level)

- **Codex**: `~/.codex/prompts/*.md` es **solo de usuario** — el generador no debe emitir un `commands/`→`.codex/prompts/` a nivel de proyecto; en su lugar, mapear los playbooks de `commands/` a `.codex/skills/<name>/SKILL.md` (proyecto).
- **Cursor Team Rules**: viven en el dashboard de Cursor (no en el repo) — no generables como archivo.
- **Cursor Run Modes / Auto-review**: configuración de la app/usuario (Settings → Agents), no un archivo versionable — no generar, solo documentar en README del adapter.
- **Kiro workspace `permissions.yaml`**: vive en `~/.kiro/workspace-roots/<hash>/permissions.yaml`, **fuera del repo** — no se debe intentar commitear; el generador solo puede emitir `.kiro/agents/*.json` con `permissions.rules` embebidas si se necesita algo versionable.
- **GitHub Copilot enterprise `managed-settings.json`**: es política de organización fuera del repo — no generar.
- **Windsurf/Devin**: preferir siempre `.devin/*` sobre `.windsurf/*` al generar (legacy fallback), salvo que el usuario siga en una versión pre-migración confirmada.
- **Antigravity/Gemini CLI AGENTS.md**: Gemini CLI solo lo lee si `context.fileName` en `settings.json` lo incluye explícitamente — el generador debe emitir ese ajuste, no asumir lectura nativa.

[^cc-memory]: How Claude remembers your project
[^cc-skills]: Extend Claude with skills
[^cc-hooks]: Hooks reference
[^cc-permissions]: Configure permissions
[^cc-settings-ref]: Settings reference
[^cc-subagents]: Subagents
[^codex-config-ref]: Codex configuration reference
[^codex-agents-md]: Custom instructions with AGENTS.md (Codex)
[^codex-docs-config]: codex/docs/config.md (hooks, managed-only note)
[^ag-rules-workflows]: Rules (Google Antigravity Docs)
[^ag-skills]: Agent skills (Google Antigravity Docs)
[^ag-cli-features]: Antigravity CLI Features
[^ag-mcp]: MCP (Google Antigravity Docs)
[^ag-codelab]: Build Autonomous Developer Pipelines using agents.md and skills.md in Antigravity
[^vscode-custom-instructions]: Use custom instructions in VS Code
[^gh-repo-instructions]: Adding repository custom instructions for GitHub Copilot
[^gh-copilot-agentsmd-changelog]: Copilot coding agent now supports AGENTS.md custom instructions
[^vscode-mcp-servers]: Add and manage MCP servers in VS Code
[^gh-copilot-mcp-config]: Configure MCP servers for your repository
[^gh-copilot-cli-agents]: copilot-cli-for-beginners: Using Agents (.agent.md)
[^gh-copilot-enterprise-perms]: Enterprise-managed permissions for GitHub Copilot agent operations
[^cursor-rules]: Rules (Cursor Docs)
[^cursor-skills]: Skills (Cursor Docs)
[^cursor-subagents]: Subagents (Cursor Docs)
[^cursor-mcp]: Model Context Protocol (MCP) (Cursor Docs)
[^cursor-ignore]: Ignore File (Cursor Docs)
[^cursor-run-modes]: Run Modes (Cursor Docs)
[^gcli-gemini-md]: Gemini CLI: Provide context with GEMINI.md files
[^gcli-ignore]: Gemini CLI: Ignoring files (.geminiignore)
[^gcli-subagents]: Gemini CLI Subagents
[^gcli-commands]: Gemini CLI Custom commands
[^gcli-mcp]: MCP servers with Gemini CLI
[^gcli-skills]: Gemini CLI Agent Skills
[^gcli-telemetry]: Gemini CLI Observability with OpenTelemetry
[^gcli-config-ref]: Gemini CLI Configuration reference
[^devin-memories]: Cascade Memories (Devin Desktop docs; Windsurf legacy)
[^devin-workflows]: Cascade workflows (Devin Desktop docs; Windsurf legacy)
[^devin-mcp]: Cascade MCP Integration
[^devin-terminal]: Terminal (auto-execution levels: Turbo)
[^devin-ignore]: Devin Desktop Ignore (.devinignore)
[^kiro-steering]: Steering (Kiro Docs)
[^kiro-hooks]: Hooks (Kiro Docs)
[^kiro-mcp]: MCP Configuration (Kiro Docs)
[^kiro-permissions]: Permissions (Kiro Docs)
[^kiro-agents]: Custom agents (Kiro Docs)
[^kiro-ignore]: .kiroignore (referenced from Kiro Docs: Built-in tools)
[^hermes-config]: Hermes Agent Configuration
[^hermes-skills]: Hermes Agent: Skills System
[^hermes-security]: Hermes Agent: Security
[^hermes-repo]: NousResearch/hermes-agent (repo root, AGENTS.md, skills/)
[^hermes-bundled]: Hermes Agent bundled skill: Key Paths
[^zed-instructions]: Agent Instructions (Zed)
[^junie-guidelines]: Guidelines and memory (Junie)
[^cline-rules]: Rules (Cline)
[^opencode-rules]: Rules (opencode)
[^opencode-instructions-v2]: Instructions (opencode v2)
[^amp-agentsmd]: AGENTS.md (Amp Docs)
[^aider-conventions]: Specifying coding conventions (Aider)
[^roocode-agentsmd-issue]: Add Support for Agent Rules Standard via Project Root AGENTS.md (Roo Code issue)
