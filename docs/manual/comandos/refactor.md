---
type: Manual Page
title: refactor — mejora la estructura sin cambiar comportamiento
description: Reestructura código manteniendo la suite de tests en verde antes y después, sin cambiar comportamiento.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# refactor

## Qué hace y cuándo usarlo

Mejora cómo está organizado el código por dentro, sin cambiar lo que el proyecto hace hacia afuera. Úsalo cuando algo funciona pero su forma actual complica el siguiente cambio.

## Qué escribes

```text
/refactor pedidos
```

## Qué hará el agente y qué obtienes

- Confirma que las pruebas existentes pasan antes de tocar nada (punto de partida).
- Aplica el cambio en pasos chicos y reversibles, confirmando que las pruebas siguen pasando en cada paso.
- Si en el camino el comportamiento cambiara, se detiene: eso ya sería una tarea nueva, no un refactor.

**Obtienes:** el código reorganizado, con las mismas pruebas pasando antes y después.

## Errores comunes y cómo salir

- Terminó cambiando algo que el usuario nota → no es un refactor: pide que se documente como un cambio nuevo.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/refactor` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/refactor.md`". |
| Antigravity | `/refactor` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/refactor` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta refactor" o "ejecuta el playbook `commands/refactor.md`". |
| Gemini CLI | `/refactor` (`.gemini/commands/refactor.toml`). |
| Windsurf / Devin Desktop | `/refactor` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta refactor". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/refactor.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/refactor.md`". |

Playbook completo: [`/commands/refactor.md`](/commands/refactor.md).
