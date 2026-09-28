---
type: Manual Page
title: prompt-contract — contrato de un agente o prompt
description: Fija entradas, salidas, límites y HITL de un prompt o agente antes de construirlo.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# prompt-contract

## Qué hace y cuándo usarlo

Antes de construir un agente o una función con inteligencia artificial generativa, fija por escrito qué entra, qué debe salir, qué límites tiene y cuándo necesita que una persona revise. (No confundir con la verificación general del proyecto: eso es `ads-check`.) Úsalo cuando el proyecto incluye un asistente, un prompt de sistema o un flujo con IA generativa.

## Qué escribes

```text
/prompt-contract asistente-pedidos
```

## Qué hará el agente y qué obtienes

- Define qué entra, qué debe salir (y en qué formato), el tono, y qué el asistente NO debe hacer.
- Deja explícito que lo que devuelve una herramienta externa se trata como un dato, nunca como una instrucción a seguir.
- Si el asistente puede hacer algo destructivo o de producción, exige que una persona lo confirme siempre.

**Obtienes:** un contrato escrito (`docs/prompt-contracts/<tarea>.md`) que guía cómo se construye y valida ese asistente.

## Errores comunes y cómo salir

- El asistente puede borrar datos o publicar algo sin confirmación → es un hueco de seguridad: pide que se agregue la confirmación humana.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/prompt-contract` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/prompt-contract.md`". |
| Antigravity | `/prompt-contract` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/prompt-contract` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta prompt-contract" o "ejecuta el playbook `commands/prompt-contract.md`". |
| Gemini CLI | `/prompt-contract` (`.gemini/commands/prompt-contract.toml`). |
| Windsurf / Devin Desktop | `/prompt-contract` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta prompt-contract". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/prompt-contract.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/prompt-contract.md`". |

Playbook completo: [`/commands/prompt-contract.md`](/commands/prompt-contract.md).
