---
type: Manual Page
title: spec — especificación verificable
description: Convierte la intención en requirements, design y tasks verificables (formato EARS).
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# spec

## Qué hace y cuándo usarlo

Convierte la intención en una especificación clara y verificable: qué debe pasar exactamente, decisiones de diseño, y tareas concretas. Úsalo después de `intent`, antes de planear o construir, sobre todo en tareas más formales.

## Qué escribes

```text
/spec pedidos
```

## Qué hará el agente y qué obtienes

- Escribe los requisitos en formato "dado/cuando/entonces", fáciles de verificar uno por uno.
- Documenta las decisiones técnicas necesarias para cumplir esos requisitos.
- Descompone todo en tareas verificables, conectadas a la lista de trabajo del proyecto.

**Obtienes:** tres documentos (`requirements.md`, `design.md`, `tasks.md`) que describen exactamente qué se va a construir.

## Errores comunes y cómo salir

- Un requisito queda asumido y es importante → se envía a la cola de pendientes o directo a ti, según qué tan reversible sea.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/spec` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/spec.md`". |
| Antigravity | `/spec` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/spec` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta spec" o "ejecuta el playbook `commands/spec.md`". |
| Gemini CLI | `/spec` (`.gemini/commands/spec.toml`). |
| Windsurf / Devin Desktop | `/spec` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta spec". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/spec.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/spec.md`". |

Playbook completo: [`/commands/spec.md`](/commands/spec.md).
