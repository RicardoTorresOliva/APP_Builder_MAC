---
type: Manual Page
title: stack — elige el stack con el humano
description: Explora 2-3 opciones de stack con trade-offs y espera la elección del humano (HITL).
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# stack

## Qué hace y cuándo usarlo

Explora opciones de tecnología y las elige junto contigo — nunca por su cuenta. Muestra 2 o 3 alternativas con ventajas, desventajas y cuándo NO conviene cada una. Úsalo durante `init-project`, o cuando aparece una pieza nueva de tecnología durante la construcción.

## Qué escribes

```text
/stack "base de datos"
```

## Qué hará el agente y qué obtienes

- Parte de categorías de tecnología sugeridas, nunca de un producto ya decidido.
- Busca ejemplos parecidos a tu proyecto para comparar opciones reales.
- Presenta 2-3 alternativas con costo, madurez, y qué tan fácil sería cambiarla después.

**Obtienes:** la tecnología elegida, registrada en el historial de decisiones del proyecto.

## Errores comunes y cómo salir

- No entiendes una opción → pide que te la expliquen en palabras simples: esta decisión siempre espera tu respuesta (salvo un prototipo muy simple, donde se aplica la opción recomendada y se anota para confirmar después).

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/stack` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/stack.md`". |
| Antigravity | `/stack` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/stack` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta stack" o "ejecuta el playbook `commands/stack.md`". |
| Gemini CLI | `/stack` (`.gemini/commands/stack.toml`). |
| Windsurf / Devin Desktop | `/stack` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta stack". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/stack.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/stack.md`". |

Playbook completo: [`/commands/stack.md`](/commands/stack.md).
