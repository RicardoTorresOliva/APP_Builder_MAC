---
type: Manual Page
title: session-start — inicio de sesión
description: Lee la memoria del proyecto y la cola de pendientes, y dice por dónde retomar el trabajo.
tags: [manual, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# session-start

## Qué hace y cuándo usarlo

Retoma una sesión de trabajo ya empezada: lee un resumen del proyecto (sin releer todo desde cero) y te dice por dónde seguir. Úsalo al empezar cada sesión sobre un proyecto ya iniciado.

## Qué escribes

```text
/session-start
```

## Qué hará el agente y qué obtienes

- Lee el resumen del proyecto: perfil elegido, última tarea terminada, siguiente tarea, y si hay algo bloqueado.
- Revisa la lista de tareas y encuentra la que está en curso, o la siguiente pendiente.
- Revisa la cola de pendientes y cuenta cuántas decisiones están esperando tu revisión.

**Obtienes:** un resumen breve de en qué quedó el proyecto y cuál es el siguiente paso concreto. No modifica nada.

## Errores comunes y cómo salir

- No existe el archivo de tareas del proyecto → nunca corriste `init-project`: hazlo primero.
- Hay muchos pendientes acumulados → revísalos con `/pending` antes de seguir construyendo.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/session-start` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/session-start.md`". |
| Antigravity | `/session-start` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/session-start` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta session-start" o "ejecuta el playbook `commands/session-start.md`". |
| Gemini CLI | `/session-start` (`.gemini/commands/session-start.toml`). |
| Windsurf / Devin Desktop | `/session-start` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta session-start". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/session-start.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/session-start.md`". |

Playbook completo: [`/commands/session-start.md`](/commands/session-start.md).
