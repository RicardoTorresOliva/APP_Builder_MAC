---
type: Manual Page
title: review — revisión independiente
description: Lanza una revisión independiente, con contexto limpio, de la última unidad o milestone completado.
tags: [manual, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# review

## Qué hace y cuándo usarlo

Pide una segunda opinión, independiente de quien construyó, sobre la última tarea o bloque terminado. Úsalo después de cada bloque de trabajo, siempre antes de `closeout`.

## Qué escribes

```text
/review
```

## Qué hará el agente y qué obtienes

- El que revisa nunca es el mismo que construyó: mirada nueva, sin ideas preconcebidas.
- Verifica que la tarea se pueda usar de principio a fin, con un usuario real (persona o agente).
- Busca huecos: pantallas vacías o de error que faltan, cosas sin verificar, datos sin validar.

**Obtienes:** los hallazgos de la revisión, con qué tan grave es cada uno y qué se recomienda hacer.

## Errores comunes y cómo salir

- Aparece un hallazgo grave → el trabajo nuevo se detiene hasta corregirlo: así no se acumulan problemas.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/review` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/review.md`". |
| Antigravity | `/review` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/review` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta review" o "ejecuta el playbook `commands/review.md`". |
| Gemini CLI | `/review` (`.gemini/commands/review.toml`). |
| Windsurf / Devin Desktop | `/review` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta review". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/review.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/review.md`". |

Playbook completo: [`/commands/review.md`](/commands/review.md).
