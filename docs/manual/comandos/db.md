---
type: Manual Page
title: db — construye el modelo de datos
description: Modela y migra el esquema de datos de una unidad con migraciones reversibles.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# db

## Qué hace y cuándo usarlo

Diseña o cambia la forma en que se guardan los datos del proyecto, siempre con la posibilidad de deshacer el cambio. Úsalo cuando la tarea crea, modifica o usa el modelo de datos.

## Qué escribes

```text
/db pedidos
```

## Qué hará el agente y qué obtienes

- Diseña la estructura de datos a partir del diseño de la tarea.
- Todo cambio de estructura se escribe junto con su reversa, antes de aplicarlo.
- Revisa si hay datos sensibles antes de crear datos de ejemplo.

**Obtienes:** la estructura de datos y sus cambios, todos reversibles.

## Errores comunes y cómo salir

- Un cambio no se puede deshacer, o se borran datos fuera de tu rama de trabajo → se detiene siempre: necesita tu aprobación explícita.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/db` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/db.md`". |
| Antigravity | `/db` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/db` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta db" o "ejecuta el playbook `commands/db.md`". |
| Gemini CLI | `/db` (`.gemini/commands/db.toml`). |
| Windsurf / Devin Desktop | `/db` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta db". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/db.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/db.md`". |

Playbook completo: [`/commands/db.md`](/commands/db.md).
