---
type: Research
title: Verificación de adaptadores contra la documentación oficial
description: Contraste de cada salida de abm sync con la documentación oficial vigente de su herramienta.
tags: [verificacion, adaptadores, fase-4]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:59:03Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: cc-memory
    resource: https://code.claude.com/docs/en/memory
    title: How Claude remembers your project
  - id: cc-skills
    resource: https://code.claude.com/docs/en/skills
    title: Extend Claude with skills
  - id: cc-subagents
    resource: https://code.claude.com/docs/en/sub-agents
    title: Create custom subagents
  - id: cc-permissions
    resource: https://code.claude.com/docs/en/permissions
    title: Configure permissions
  - id: cc-settings-ref
    resource: https://code.claude.com/docs/en/settings-reference
    title: All settings
  - id: codex-config-ref
    resource: https://developers.openai.com/codex/config-reference
    title: Codex Configuration Reference
  - id: ag-rules
    resource: https://antigravity.google/docs/rules/
    title: Rules (Google Antigravity Docs)
  - id: ag-skills
    resource: https://antigravity.google/docs/skills/
    title: Agent Skills (Google Antigravity Docs)
  - id: ag-cli-features
    resource: https://antigravity.google/docs/cli/features/
    title: Features (Antigravity CLI)
  - id: ag-mcp
    resource: https://antigravity.google/docs/mcp/
    title: MCP (Google Antigravity Docs)
  - id: vscode-custom-instructions
    resource: https://code.visualstudio.com/docs/agent-customization/custom-instructions
    title: Use custom instructions in VS Code
  - id: vscode-prompt-files
    resource: https://code.visualstudio.com/docs/agent-customization/prompt-files
    title: Use prompt files in VS Code
  - id: vscode-custom-agents
    resource: https://code.visualstudio.com/docs/agent-customization/custom-agents
    title: Custom agents in VS Code
  - id: vscode-mcp-servers
    resource: https://code.visualstudio.com/docs/agent-customization/mcp-servers
    title: Add and manage MCP servers in VS Code
  - id: vscode-approvals
    resource: https://code.visualstudio.com/docs/agents/run/approvals
    title: Manage approvals and permissions
  - id: cursor-rules
    resource: https://cursor.com/docs/rules
    title: Rules (Cursor Docs)
  - id: cursor-skills
    resource: https://cursor.com/docs/skills
    title: Agent Skills (Cursor Docs)
  - id: gcli-gemini-md
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
    title: "Gemini CLI: Provide context with GEMINI.md files"
  - id: gcli-commands
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/custom-commands.md
    title: Gemini CLI Custom commands
  - id: gcli-subagents
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
    title: Gemini CLI Subagents
  - id: gcli-config-ref
    resource: https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md
    title: Gemini CLI Configuration reference
  - id: devin-memories
    resource: https://docs.devin.ai/desktop/cascade/memories
    title: Cascade Memories (Devin Desktop docs)
  - id: devin-mcp
    resource: https://docs.devin.ai/desktop/cascade/mcp
    title: Cascade MCP Integration
  - id: devin-terminal
    resource: https://docs.devin.ai/desktop/terminal
    title: "Terminal (auto-execution levels: Turbo)"
  - id: devin-ignore
    resource: https://docs.devin.ai/desktop/context-awareness/devin-ignore
    title: Devin Desktop .devinignore
  - id: kiro-steering
    resource: https://kiro.dev/docs/steering/
    title: Steering (Kiro Docs)
  - id: kiro-mcp
    resource: https://kiro.dev/docs/mcp/configuration/
    title: MCP Configuration (Kiro Docs)
  - id: kiro-permissions
    resource: https://kiro.dev/docs/permissions/
    title: Permissions (Kiro Docs)
  - id: hermes-config
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
    title: Hermes Agent Configuration
  - id: hermes-skills
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
    title: "Hermes Agent: Skills System"
  - id: compat-matrix
    resource: /docs/compat-matrix.md
    title: Matriz de compatibilidad multi-herramienta (investigación previa, no re-verificada al 100% en esta pasada)
---

# Verificación de adaptadores contra la documentación oficial

Verificación independiente (Fase 4) de `./abm sync` en la rama `claude/jolly-davinci-m2wcju`, fecha
2026-09-28. Por cada herramienta se abrieron 1–2 archivos generados representativos (registrados en
`adapters/.generated.json`, producidos por `scripts/abmkit/sync.py`) y se contrastaron ruta, nombre,
extensión, claves de frontmatter/JSON/TOML y semántica contra la documentación oficial vigente,
obtenida en vivo con Firecrawl (no solo `docs/compat-matrix.md`, que se usó únicamente como pista de
partida). Donde la fuente en vivo no fue concluyente se marca `no-verificado` en vez de inventar.

## 1. Claude Code

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `CLAUDE.md` → `@AGENTS.md` | OK | El import `@archivo` para inyectar otro Markdown dentro de `CLAUDE.md` es sintaxis nativa documentada. | [^cc-memory] |
| `.claude/commands/<n>.md` (`description`, `argument-hint`, `$ARGUMENTS`) | OK | `argument-hint` es una clave de frontmatter oficial vigente para el sistema unificado de comandos/skills; `$ARGUMENTS` es el placeholder documentado para comandos "legacy" (siguen funcionando fusionados en Skills). | [^cc-skills] |
| `.claude/skills/<n>/SKILL.md` (`name`, `description`, `license`, `metadata`) | OK | Las cuatro claves están en la lista oficial vigente de frontmatter de `SKILL.md` (que también incluye `allowed-tools`, `argument-hint`, `model`, etc., no usadas aquí pero no requeridas). | [^cc-skills] |
| `.claude/agents/<rol>.md` (`name`, `description`, `model: haiku\|inherit`) | OK | `model` acepta exactamente `sonnet\|opus\|haiku\|fable\|<model-id>\|inherit`; `haiku` e `inherit` (los dos valores que emite el generador) son válidos. | [^cc-subagents] |
| `.mcp.json` (`mcpServers`) | OK | Ruta y clave raíz confirmadas para MCP a nivel de proyecto. | [^cc-settings-ref] |

## 2. Codex

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.codex/skills/<n>/SKILL.md` | OK | Confirmado en vivo: "Skills are loaded from the `.codex/skills` path within a project" (no `.agents/skills`). | [^codex-config-ref] |
| `.codex/config.toml` → `[mcp_servers.abm]` (`command`, `args`) | DISCREPANCIA (parcial) | Ruta y forma de la tabla son correctas, pero la fuente oficial precisa: "Project-scoped overrides can be placed in `.codex/config.toml`... only read when the project is trusted." El generador no deja constancia de ese requisito, por lo que el MCP server puede quedar silenciosamente inactivo en un proyecto no marcado como *trusted*. | [^codex-config-ref] |

## 3. Google Antigravity

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.agents/workflows/<n>.md` (frontmatter `description`) | DISCREPANCIA | La documentación oficial vigente de Antigravity (páginas *Rules*, *Agent Skills* y *CLI Features*) **no menciona `.agents/workflows/` en absoluto**. Solo documenta Rules (`AGENTS.md`/`GEMINI.md`/`.agents/rules/*.md`, frontmatter `trigger:`, no `activation:` como decía la pasada previa) y Agent Skills (`.agents/skills/<carpeta>/SKILL.md`, invocadas como slash-command); la página de CLI Features solo asocia "workflows" al comando `/skills` ("encapsulated agent workflows"), sugiriendo que la función fue absorbida por Skills. | [^ag-rules] [^ag-skills] [^ag-cli-features] |
| `.agents/skills/` | OK | Ruta exacta confirmada: `<workspace-root>/.agents/skills/<skill-folder>/SKILL.md`; único campo requerido es `description` (`name` es opcional). | [^ag-skills] |
| `.agents/mcp_config.json` (`mcpServers`) | OK | Ruta y clave raíz confirmadas para el nivel de workspace. | [^ag-mcp] |

## 4. VS Code + GitHub Copilot

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.github/copilot-instructions.md` | OK | Sigue siendo la ubicación recomendada para instrucciones repo-wide en sesiones Copilot Agent Host. | [^vscode-custom-instructions] |
| `.github/prompts/<n>.prompt.md` (`description`, `agent: agent`, `${input:args}`) | DISCREPANCIA | Las claves son sintácticamente correctas (`agent` acepta `ask\|agent\|plan\|<agente-custom>`; `${input:variable}` es el placeholder documentado), pero la doc oficial (actualizada 2026-09-16) dice textualmente: *"Prompt files are deprecated for Agent Host sessions and aren't loaded by Agent Host. They continue to work with the Local agent for now, but the Local agent will be removed in a future release. Use prompt file migration to convert existing prompts to agent skills."* Agent Host es la superficie de Copilot coding agent / Copilot CLI — el target real de este adaptador — así que estos archivos no se cargarán ahí. | [^vscode-prompt-files] |
| `.github/agents/<rol>.agent.md` (`name`, `description`) | OK | Ambos campos están en la tabla oficial de frontmatter de `.agent.md`; la ubicación de workspace es exactamente `.github/agents` folder. | [^vscode-custom-agents] |
| `.vscode/mcp.json` (`servers`, `type: stdio`) | OK | Confirmado verbatim: clave raíz `servers` (no `mcpServers`) y `"type": "stdio"` obligatorio por servidor stdio — coincide exactamente con lo generado. | [^vscode-mcp-servers] |

## 5. Cursor

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.cursor/mcp.json` (`mcpServers`) | OK | Formato estándar sin cambios detectados. | [^cursor-skills] |
| `.cursorignore` | OK | Sigue siendo el nombre y sintaxis (`.gitignore`-like) vigentes. | [^cursor-rules] |
| Lee `AGENTS.md` y `.agents/skills`/`.claude/skills` | OK | Confirmado en vivo: AGENTS.md es "Simple alternative to `.cursor/rules`"; el orden de precedencia de skills es `.agents/skills/` → `.cursor/skills/` → `~/.agents/skills/` → `~/.cursor/skills/`, con compatibilidad adicional hacia `.claude/skills/` y `.codex/skills/`. | [^cursor-rules] [^cursor-skills] |

## 6. Gemini CLI

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.gemini/settings.json` → `context.fileName: ["AGENTS.md"]` | OK | Coincide carácter a carácter con el ejemplo oficial (`{"context": {"fileName": [...]}}`). | [^gcli-gemini-md] |
| `.gemini/commands/<n>.toml` (`description`, `prompt`, `{{args}}`) | OK | Ambas claves TOML confirmadas; `{{args}}` es el placeholder documentado para argumentos. | [^gcli-commands] |
| `.gemini/agents/<rol>.md` (`name`, `description`) | OK | Únicos dos campos requeridos por el spec de subagentes; el resto (`kind`, `tools`, `model`, etc.) es opcional y el generador no los emite, lo cual es válido. | [^gcli-subagents] |

## 7. Windsurf / Devin Desktop

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.devin/rules/abm.md` y `.windsurf/rules/abm.md` (`trigger: always_on`) | DISCREPANCIA (de alcance, no de sintaxis) | Ruta y valor de `trigger` siguen vigentes, pero la documentación oficial aclara ahora que estas rutas — junto con `.devin/workflows/*.md`, el nivel de auto-ejecución "Turbo" y `mcp_config.json` de Cascade — **aplican solo al agente Cascade, marcado como legacy**. El agente por defecto de las pestañas nuevas de Devin Desktop, "Devin Local agent", no lee `AGENTS.md` de forma nativa ni estas rutas; usa los *Devin CLI config files* para MCP y "su propio modelo de permisos" en vez de Turbo. | [^devin-memories] [^devin-mcp] [^devin-terminal] |
| `.devin/workflows/<n>.md` | DISCREPANCIA (mismo alcance) | Igual que la fila anterior: solo lo consume el agente Cascade (legacy). | [^devin-memories] |
| `.devinignore` | OK | Nombre y ubicación (raíz del repo) vigentes; es agnóstico de agente (Cascade y Devin Local comparten indexación). | [^devin-ignore] |

## 8. Kiro (AWS)

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `.kiro/steering/abm.md` (`inclusion: always`) | OK | Campo `inclusion` y valor `always` confirmados. | [^kiro-steering] |
| `.kiro/steering/abm-playbooks.md` (`inclusion: manual`) | OK | Valor `manual` confirmado como válido. | [^kiro-steering] |
| `.kiro/settings/mcp.json` (`mcpServers.<n>.command/args`) | OK | Ruta y forma exactas; el generador emite un subconjunto válido del schema completo (`command`, `args`, `env`, `disabled`, `autoApprove`, `disabledTools`, `url`, `headers`). | [^kiro-mcp] |
| `.kiroignore` | OK (no-verificado en esta pasada) | No se recontrastó en vivo esta ronda; se mantiene el veredicto de la investigación previa. | [^compat-matrix] |

## 9. Hermes Agent (Nous Research)

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `adapters/hermes/config.example.yaml` → `tools.include/resources/prompts` | no-verificado | Dos consultas en vivo a la misma página dieron resultados **inconsistentes entre sí**: una sugiere que `resources`/`prompts` bajo una entrada de servidor MCP significan límites de cómputo (cpu/memory) y plantillas de prompt, no los interruptores de capacidad MCP que asume el generador; otra, pidiendo cita literal, devolvió una sección de config no relacionada (enrutamiento de modelo para títulos/triage). No hay fuente fiable en esta pasada para confirmar o refutar el schema tal como está. | [^hermes-config] |
| Lee `.agents/skills` + `AGENTS.md` | DISCREPANCIA/no-verificado | `.hermes/skills/` y `.agents/skills/` como directorios de proyecto quedaron **confirmados**. Pero la misma página de Skills afirma explícitamente *"AGENTS.md is not read natively for project instructions"*, lo que contradice la afirmación previa (de otra página) de que Hermes lee `AGENTS.md` de forma nativa por *recursive directory walk*. Ambas fuentes se llaman "oficiales"; se recomienda una verificación manual adicional (CLI `hermes --help` o repo) antes de confiar en cualquiera de las dos. | [^hermes-skills] [^hermes-config] |

## 10. Plantillas turbo (`adapters/turbo/`)

| Salida | Veredicto | Detalle | Fuente |
|---|---|---|---|
| `claude-code/settings.json` — `Bash(cmd:*)`, `Read(./path)`, `defaultMode: acceptEdits` | OK | Confirmado verbatim: *"The `:*` suffix is an equivalent way to write a trailing wildcard, so `Bash(ls:*)` matches the same commands as `Bash(ls *)`."* `Read(./secrets/**)` y `Read(./.env)` coinciden con los ejemplos oficiales; `acceptEdits` está en la lista vigente de valores de `permissions.defaultMode`. | [^cc-permissions] [^cc-settings-ref] |
| `codex/config.toml` — `approval_policy = "on-request"`, `sandbox_mode = "workspace-write"` | OK | Ambos valores están en las listas de enum vigentes (`on-request\|never\|{granular...}` y `read-only\|workspace-write\|danger-full-access`). | [^codex-config-ref] |
| `gemini-cli/settings.json` — `general.defaultApprovalMode: "auto_edit"` | OK | Ruta de clave y valor confirmados exactamente (`default\|auto_edit\|plan`). | [^gcli-config-ref] |
| `vscode/settings.json` — `chat.tools.terminal.autoApprove` | DISCREPANCIA (de alcance) | Nombre de la clave y forma (string → boolean) son correctos, pero la doc oficial dice explícitamente: *"This setting applies only to the Local agent."* El mismo agente que la doc de prompt-files marca para remoción futura. No tiene efecto sobre Copilot Agent Host / coding agent, que es donde correría Copilot en la mayoría de flujos actuales de ABM. | [^vscode-approvals] [^vscode-prompt-files] |
| `kiro/permissions.example.yaml` — `capability/match/effect`, valores `shell`/`fs_read` | OK | Schema y valores de `capability` confirmados. Nota de estilo (no bloqueante): los ejemplos oficiales agrupan varios patrones en un `match` de **lista** por regla; el generador emite una regla por comando con `match` como string suelto — no se encontró evidencia de que eso sea inválido, así que se deja como OK con observación. | [^kiro-permissions] |
| `hermes/config.example.yaml` — `approvals.mode: smart`, `security.tirith_enabled: true` | no-verificado | No se recontrastó en vivo esta ronda (mismo problema de fiabilidad de fuente que la fila 9); se mantiene el veredicto de la investigación previa sin confirmar ni refutar. | [^compat-matrix] |

## Correcciones propuestas para `scripts/abmkit/sync.py`

1. **Antigravity — dejar de generar `.agents/workflows/`.** En `emit_all`, dentro de
   `if "antigravity" in enabled:` (línea ~150), eliminar el bucle
   `for c in cmds: out[f".agents/workflows/{c['name']}.md"] = ...` y dejar solo
   `out[".agents/mcp_config.json"] = mcp_json(tools)`. El catálogo de playbooks ya queda expuesto por
   `.agents/skills/abm-playbooks/SKILL.md` (generado en `skills_to(".agents/skills")`, línea ~148), que
   es el mecanismo que sí documenta Antigravity. Fuente: [^ag-rules] [^ag-skills] [^ag-cli-features].

2. **Codex — advertir sobre `trusted project`.** En el mismo bloque `if "codex" in enabled:` (línea
   ~144), cambiar el comentario de cabecera de
   `f"# {MARK}. No editar. Codex lee AGENTS.md de forma nativa.\n"` a
   `f"# {MARK}. No editar. Codex lee AGENTS.md de forma nativa. mcp_servers de este archivo de\n# proyecto solo se carga si el proyecto está marcado como 'trusted' en Codex.\n"`.
   Fuente: [^codex-config-ref].

3. **VS Code/Copilot — generar también `.github/skills/`.** En `if "copilot" in enabled:` (línea
   ~153), añadir `skills_to(".github/skills")` junto a la generación de `.github/prompts/*.prompt.md`
   y `.github/agents/*.agent.md`, ya que la documentación oficial pide migrar prompts a Agent Skills
   para que Agent Host los cargue. Mantener `.github/prompts/*.prompt.md` solo como fallback para el
   "Local agent" (documentar la deprecación en `adapters/README.md`). Fuente: [^vscode-prompt-files].

4. **Windsurf/Devin — documentar el alcance a Cascade (legacy).** En `if "windsurf" in enabled:`
   (línea ~177), cambiar `rule = "---\ntrigger: always_on\n---\n" + pointer_md()` a
   `rule = "---\ntrigger: always_on\n---\n" + pointer_md("> Nota: esta ruta la lee el agente Cascade (legacy) de Devin Desktop. El agente por defecto actual, 'Devin Local agent', no la lee; usa los Devin CLI config files para MCP y su propio modelo de permisos en vez de Turbo.")`.
   Fuente: [^devin-memories] [^devin-mcp] [^devin-terminal].

5. **Hermes — marcar el sub-schema de `tools` como no confirmado.** En `turbo_templates`/`emit_all`
   (bloque `if "hermes" in enabled:`, línea ~188), añadir una línea de comentario antes de
   `tools:\n  include: [...]` en `adapters/hermes/config.example.yaml`:
   `"    # NO-VERIFICADO: confirmar 'tools.resources'/'tools.prompts' contra`hermes mcp --help`o el código fuente antes de usar en producción.\n"`.
   Fuente: [^hermes-config].

[^cc-memory]: How Claude remembers your project
[^cc-skills]: Extend Claude with skills
[^cc-subagents]: Create custom subagents
[^cc-permissions]: Configure permissions
[^cc-settings-ref]: All settings
[^codex-config-ref]: Codex Configuration Reference
[^ag-rules]: Rules (Google Antigravity Docs)
[^ag-skills]: Agent Skills (Google Antigravity Docs)
[^ag-cli-features]: Features (Antigravity CLI)
[^ag-mcp]: MCP (Google Antigravity Docs)
[^vscode-custom-instructions]: Use custom instructions in VS Code
[^vscode-prompt-files]: Use prompt files in VS Code
[^vscode-custom-agents]: Custom agents in VS Code
[^vscode-mcp-servers]: Add and manage MCP servers in VS Code
[^vscode-approvals]: Manage approvals and permissions
[^cursor-rules]: Rules (Cursor Docs)
[^cursor-skills]: Agent Skills (Cursor Docs)
[^gcli-gemini-md]: Gemini CLI: Provide context with GEMINI.md files
[^gcli-commands]: Gemini CLI Custom commands
[^gcli-subagents]: Gemini CLI Subagents
[^gcli-config-ref]: Gemini CLI Configuration reference
[^devin-memories]: Cascade Memories (Devin Desktop docs)
[^devin-mcp]: Cascade MCP Integration
[^devin-terminal]: Terminal (auto-execution levels: Turbo)
[^devin-ignore]: Devin Desktop .devinignore
[^kiro-steering]: Steering (Kiro Docs)
[^kiro-mcp]: MCP Configuration (Kiro Docs)
[^kiro-permissions]: Permissions (Kiro Docs)
[^hermes-config]: Hermes Agent Configuration
[^hermes-skills]: Hermes Agent: Skills System
[^compat-matrix]: Matriz de compatibilidad multi-herramienta (investigación previa, no re-verificada al 100% en esta pasada)
