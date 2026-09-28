---
type: Manual Page
title: ui — construye la interfaz
description: Construye la capa de interfaz de una unidad siguiendo el standard de frontend y su quality gate.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# ui

## Qué hace y cuándo usarlo

Construye las pantallas, formularios o componentes que ve la persona que usa el proyecto, cuidando que también funcionen los casos de error y las pantallas vacías. Úsalo en cualquier tarea con una pantalla o interacción visible.

## Qué escribes

```text
/ui pedidos
```

## Qué hará el agente y qué obtienes

- Construye siguiendo las reglas de calidad visual del proyecto.
- Cubre no solo el camino feliz: también qué se ve cuando no hay datos todavía, o cuando algo falla.
- Revisa accesibilidad básica: contraste de colores, uso solo con teclado, etiquetas claras.

**Obtienes:** la pantalla o componente terminado, con su checklist de calidad cumplido.

## Errores comunes y cómo salir

- Ves datos de ejemplo poco realistas en la versión final (como "Lorem ipsum") → pide que se reemplacen antes de cerrar la tarea.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/ui` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/ui.md`". |
| Antigravity | `/ui` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/ui` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta ui" o "ejecuta el playbook `commands/ui.md`". |
| Gemini CLI | `/ui` (`.gemini/commands/ui.toml`). |
| Windsurf / Devin Desktop | `/ui` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta ui". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/ui.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/ui.md`". |

Playbook completo: [`/commands/ui.md`](/commands/ui.md).
