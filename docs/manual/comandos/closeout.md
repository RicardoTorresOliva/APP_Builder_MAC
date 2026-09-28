---
type: Manual Page
title: closeout — cierra una unidad
description: Sincroniza intención, spec, contrato y código, registra tokens y actualiza la memoria del proyecto.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# closeout

## Qué hace y cuándo usarlo

Cierra una tarea de forma prolija: confirma que todo coincide, registra cuánto costó, y deja el resumen del proyecto al día para la próxima sesión. Úsalo al terminar cada tarea.

## Qué escribes

```text
/closeout pedidos
```

## Qué hará el agente y qué obtienes

- Confirma que lo planeado, lo especificado y lo construido coinciden; si no, corrige el desajuste primero.
- Registra el consumo de tokens de la tarea.
- Actualiza el resumen del proyecto: qué se hizo, qué sigue, y si hay algo bloqueado.

**Obtienes:** el registro de progreso, el resumen del proyecto y el consumo de tokens, todos al día.

## Errores comunes y cómo salir

- Queda un pendiente de tipo "credencial", o algo que en realidad debía bloquear → resuélvelo antes de cerrar la tarea.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/closeout` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/closeout.md`". |
| Antigravity | `/closeout` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/closeout` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta closeout" o "ejecuta el playbook `commands/closeout.md`". |
| Gemini CLI | `/closeout` (`.gemini/commands/closeout.toml`). |
| Windsurf / Devin Desktop | `/closeout` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta closeout". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/closeout.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/closeout.md`". |

Playbook completo: [`/commands/closeout.md`](/commands/closeout.md).
