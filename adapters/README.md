---
type: Reference
title: adapters/ — generador de adaptadores por herramienta
description: Cómo abm sync genera, desde fuentes neutrales, lo que cada herramienta de IA necesita leer; plantillas turbo.
tags: [adaptadores, herramientas, sync]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:46:03Z }
---

# adapters/ — generador de adaptadores

La gobernanza vive solo en `AGENTS.md`. Cada herramienta la encuentra con archivos **generados** por `./abm sync` desde fuentes neutrales (`commands/`, `skills/`, `agents/`, `AGENTS.md`). Decisión: `/docs/adr/0002-fuente-unica-generador-adaptadores.md`. Rutas y formatos verificados: `/docs/compat-matrix.md`.

## Contenido

| Archivo | Para qué |
|---|---|
| `tools.yaml` | Herramientas habilitadas, servidor MCP de ABM, patrones de ignore y listas turbo |
| `.generated.json` | Registro de archivos generados (ruta → sha256); `sync --check` lo usa para detectar desfases y huérfanos |
| `hermes/config.example.yaml` | Fragmento para `~/.hermes/config.yaml` (Hermes solo admite MCP a nivel usuario) |
| `turbo/` | Plantillas de permisos por herramienta (ADR 0014); no se activan solas |

## Qué se genera

| Herramienta | Salidas |
|---|---|
| Claude Code | `CLAUDE.md` (importa `@AGENTS.md`), `.claude/commands/`, `.claude/skills/`, `.claude/agents/`, `.mcp.json` |
| Codex | `.codex/skills/` (incluye `abm-playbooks`: Codex no tiene comandos de proyecto), `.codex/config.toml` (MCP); lee `AGENTS.md` nativo |
| Antigravity | `.agents/workflows/`, `.agents/skills/`, `.agents/mcp_config.json`; lee `AGENTS.md` nativo |
| VS Code + Copilot | `.github/copilot-instructions.md`, `.github/prompts/*.prompt.md`, `.github/agents/*.agent.md`, `.vscode/mcp.json` |
| Cursor | `.cursor/mcp.json`, `.cursorignore`; lee `AGENTS.md` y `.agents/skills`, `.claude/skills`, `.claude/agents` nativo |
| Gemini CLI | `.gemini/settings.json` (`context.fileName: AGENTS.md` + MCP), `.gemini/commands/*.toml`, `.gemini/agents/`, `.geminiignore` |
| Windsurf / Devin Desktop | `.devin/rules/abm.md`, `.windsurf/rules/abm.md` (legado), `.devin/workflows/`, `.devinignore` |
| Kiro | `.kiro/steering/abm.md` (siempre), `.kiro/steering/abm-playbooks.md` (manual), `.kiro/settings/mcp.json`, `.kiroignore` |
| Hermes | `.agents/skills/` (incluye `abm-playbooks`); lee `AGENTS.md` nativo; MCP en `hermes/config.example.yaml` |
| Otras (Zed, Junie, Cline, OpenCode, Amp…) | `AGENTS.md` como fallback universal |

## Uso

- `./abm sync` — regenera todo. `./abm sync --check` — falla en CI si algo está desfasado o editado a mano.
- `./abm sync --apply-turbo` — instala las plantillas de `turbo/` en las rutas activas (Claude Code, Codex, Gemini CLI, VS Code). Cambia permisos del agente: decisión humana.
- Añadir una herramienta: entrada en `tools.yaml` + emisor en `scripts/abmkit/sync.py` + fila en `docs/compat-matrix.md`.
- `install-adapter.sh` queda como shim de `./abm sync` (compatibilidad v4.1).

## Límites conocidos (verificación de Fase 4, `/docs/analysis/verificacion/adaptadores.md`)

- **Antigravity:** la documentación vigente describe reglas (`.agents/rules/`) y skills (`.agents/skills/`); `.agents/workflows/` tiene fuentes contradictorias (`no-verificado`). Los playbooks también llegan como la skill `abm-playbooks`.
- **VS Code + Copilot:** los prompt files no se cargan en Agent Host; por eso los playbooks también se generan como skills en `.github/skills/`. La plantilla turbo `chat.tools.terminal.autoApprove` solo aplica al agente local.
- **Windsurf / Devin Desktop:** `.devin/*` y `.windsurf/*` aplican al agente Cascade (legado); el agente local actual se configura aparte.
- **Codex:** `.codex/config.toml` de proyecto solo se lee si el proyecto está marcado como de confianza.
- **Hermes:** carga `.agents/skills/`; la carga nativa de `AGENTS.md` y las claves `tools.resources`/`tools.prompts` tienen fuentes contradictorias (`no-verificado`).
- **Windows:** las configuraciones MCP usan `python3`; en Windows cambia `mcp_server.command` a `python` (o `py`) en `tools.yaml` y ejecuta `abm.cmd sync`.
