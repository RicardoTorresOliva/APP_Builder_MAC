---
type: Manual Page
title: help — índice de comandos
description: Muestra el catálogo de comandos por fase y resuelve alias en español.
tags: [manual, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# help

## Qué hace y cuándo usarlo

Muestra el catálogo completo de comandos agrupado por etapa, y entiende alias en español si no recuerdas el nombre en inglés. Úsalo cuando no sabes qué comando corresponde a lo que quieres hacer.

## Qué escribes

```text
/help pendientes
```

## Qué hará el agente y qué obtienes

- Muestra los comandos agrupados por etapa: arranque, descubrir, construir, asegurar, medir, entregar.
- Traduce alias en español: "pendientes"→`pending`, "diagnóstico"→`doctor`, "iniciar"→`init-project`, "ejecutar"→`start-execution`, "revisar"→`review`, y otros similares.
- Si describes lo que quieres hacer en vez de nombrar un comando, sugiere el que mejor encaja.

**Obtienes:** el nombre del comando correcto para tu necesidad, o el catálogo completo.

## Errores comunes y cómo salir

- Ningún alias encaja → revisa `docs/manual/cheatsheet.md`: lista los 36 comandos en una sola página.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/help` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/help.md`". |
| Antigravity | `/help` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/help` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta help" o "ejecuta el playbook `commands/help.md`". |
| Gemini CLI | `/help` (`.gemini/commands/help.toml`). |
| Windsurf / Devin Desktop | `/help` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta help". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/help.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/help.md`". |

Playbook completo: [`/commands/help.md`](/commands/help.md).
