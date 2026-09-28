---
type: Manual Page
title: iterate — cambios post-entrega
description: Aplica un cambio, mejora o corrección tras la entrega, con spec-delta antes de tocar código.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# iterate

## Qué hace y cuándo usarlo

Aplica un cambio que pides después de que el proyecto ya se entregó — siempre documentando primero qué cambia, antes de tocar nada. Úsalo cuando el proyecto ya está entregado y quieres un cambio.

## Qué escribes

```text
/iterate "agrega un filtro por fecha en el listado de pedidos"
```

## Qué hará el agente y qué obtienes

- Clasifica tu pedido: ¿corregir un error, algo que se olvidó, una mejora, o algo totalmente nuevo?
- Escribe primero qué se agrega, cambia o elimina, y qué riesgo tiene de romper algo que ya funcionaba.
- Para mejoras o funcionalidad nueva, te presenta ese resumen y espera tu aprobación (o lo encola si es reversible y estás en turbo).

**Obtienes:** el cambio aplicado, con su documento de qué cambió y verificación de que nada existente se rompió.

## Errores comunes y cómo salir

- El cambio afecta la estructura de datos o un contrato ya existente → necesita su propio documento de diseño antes de cerrarse.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/iterate` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/iterate.md`". |
| Antigravity | `/iterate` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/iterate` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta iterate" o "ejecuta el playbook `commands/iterate.md`". |
| Gemini CLI | `/iterate` (`.gemini/commands/iterate.toml`). |
| Windsurf / Devin Desktop | `/iterate` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta iterate". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/iterate.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/iterate.md`". |

Playbook completo: [`/commands/iterate.md`](/commands/iterate.md).
