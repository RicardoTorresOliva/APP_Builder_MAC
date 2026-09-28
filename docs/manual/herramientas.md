---
type: Reference
title: Herramientas de IA compatibles con ABM
description: Tabla maestra de cómo invocar comandos en cada herramienta, qué genera "./abm sync" para cada una, y qué no se puede generar.
tags: [manual, herramientas, adaptadores]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:02:00Z }
stale_after: 2027-01-15T00:00:00Z
sources:
  - id: compat-matrix
    resource: docs/compat-matrix.md
    title: Matriz de compatibilidad multi-herramienta
  - id: tools-yaml
    resource: adapters/tools.yaml
    title: Herramientas y plantillas turbo de abm sync
---

# Herramientas de IA compatibles con ABM

ABM no le pide nada a tu herramienta de IA: te adapta a ella. `./abm sync` lee los 36 comandos y la
gobernanza (`AGENTS.md`) y genera, para cada herramienta habilitada en `adapters/tools.yaml`, los
archivos que esa herramienta sabe leer. Vos no editás esos archivos a mano — se regeneran solos.

## Tabla maestra de invocación

| Herramienta | Cómo invocás un comando | Qué genera `./abm sync` |
|---|---|---|
| **Claude Code** | `/<comando>` en el chat | `.claude/commands/<comando>.md` por cada uno, `.claude/skills/abm-playbooks/`, `.claude/agents/<rol>.md`, `.mcp.json`, y `CLAUDE.md` (apunta a `AGENTS.md`) |
| **Codex** | No tiene comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/<comando>.md`" | `.codex/skills/abm-playbooks/SKILL.md`, `.codex/config.toml` (servidor MCP) |
| **Antigravity** | `/<comando>` | `.agents/workflows/<comando>.md` por cada uno, `.agents/skills/abm-playbooks/`, `.agents/mcp_config.json` |
| **VS Code + GitHub Copilot** | `/<comando>` | `.github/prompts/<comando>.prompt.md` por cada uno, `.github/agents/<rol>.agent.md`, `.vscode/mcp.json`, `.github/copilot-instructions.md` |
| **Cursor** | Pide "usa la skill abm-playbooks y ejecuta \<comando\>" o "ejecuta el playbook `commands/<comando>.md`" — lee `AGENTS.md` nativamente | `.agents/skills/abm-playbooks/`, `.cursor/mcp.json`, `.cursorignore` |
| **Gemini CLI** | `/<comando>` | `.gemini/commands/<comando>.toml` por cada uno, `.gemini/agents/<rol>.md`, `.gemini/settings.json` (incluye lectura de `AGENTS.md`), `.geminiignore` |
| **Windsurf / Devin Desktop** | `/<comando>` | `.devin/workflows/<comando>.md` por cada uno, `.devin/rules/abm.md` y `.windsurf/rules/abm.md`, `.devinignore` |
| **Kiro** | Menciona el steering manual `#abm-playbooks` y pide "ejecuta \<comando\>" | `.kiro/steering/abm.md` (siempre activo), `.kiro/steering/abm-playbooks.md` (manual), `.kiro/settings/mcp.json`, `.kiroignore` |
| **Hermes** | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/<comando>.md`" | `.agents/skills/abm-playbooks/`, `adapters/hermes/config.example.yaml` (fragmento para tu `~/.hermes/config.yaml`) |
| **Cualquier otra herramienta** | "Lee y ejecuta `commands/<comando>.md`" — este fallback funciona siempre, sea cual sea tu herramienta | Nada específico; el playbook neutral en `commands/` alcanza |

## Qué NO se puede generar dentro del repositorio

Algunas configuraciones viven a nivel de tu usuario o de la aplicación, no del proyecto, así que
`./abm sync` no puede escribirlas por vos — quedan como ejemplo para que las copies:

- **Cursor:** las reglas de equipo y el modo de ejecución (Run Modes) se configuran en la app
  (Settings → Agents), no en un archivo del repositorio.
- **Windsurf / Devin Desktop y Antigravity:** el nivel de auto-ejecución ("Turbo") se activa dentro
  de la app.
- **Kiro:** los permisos de usuario viven en `~/.kiro/settings/permissions.yaml`, fuera del
  repositorio — copiá el ejemplo de `adapters/turbo/kiro/`.
- **Hermes:** la configuración de aprobaciones vive en `~/.hermes/config.yaml`, fuera del
  repositorio — copiá el ejemplo de `adapters/turbo/hermes/`.
- **Codex:** los prompts de usuario (`~/.codex/prompts/`) son personales, no de proyecto; por eso
  Codex usa la skill `abm-playbooks` en vez de comandos propios del repositorio.

## Cómo saber si tus adaptadores están al día

```text
./abm sync --check
```

Si devuelve "desfasada" alguna salida, corré `./abm sync` (sin `--check`) para regenerarlas — es
reversible, son archivos generados, nunca tu trabajo.

Detalle técnico completo y fuentes verificadas de cada herramienta: `/docs/compat-matrix.md`.
