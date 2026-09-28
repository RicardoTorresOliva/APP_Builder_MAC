---
type: Manual Page
title: intent — captura la intención
description: Registra el qué y el por qué de una unidad antes de especificarla o construirla.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# intent

## Qué hace y cuándo usarlo

Antes de especificar o construir algo, deja por escrito qué problema resuelve, para quién, qué resultado se espera y qué NO va a hacer. Evita construir la cosa equivocada. Úsalo al empezar una tarea nueva.

## Qué escribes

```text
/intent pedidos
```

## Qué hará el agente y qué obtienes

- Redacta el problema, el usuario y el resultado esperado en un documento corto.
- Separa lo que dijiste explícitamente, lo que se sobreentiende, y lo que el agente asume por su cuenta.
- Si algo asumido sería caro o difícil de deshacer, te lo pregunta directamente en vez de asumirlo.

**Obtienes:** un documento corto (`docs/intent/<tarea>.md`) que sirve de base para especificar o construir esa tarea.

## Errores comunes y cómo salir

- Una tarea llega a construirse sin este documento → algo se saltó el orden: pide que se registre la intención primero.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/intent` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/intent.md`". |
| Antigravity | `/intent` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/intent` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta intent" o "ejecuta el playbook `commands/intent.md`". |
| Gemini CLI | `/intent` (`.gemini/commands/intent.toml`). |
| Windsurf / Devin Desktop | `/intent` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta intent". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/intent.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/intent.md`". |

Playbook completo: [`/commands/intent.md`](/commands/intent.md).
