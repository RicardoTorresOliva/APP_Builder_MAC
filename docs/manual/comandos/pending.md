---
type: Manual Page
title: pending — cola de pendientes
description: Lista, agrega y resuelve en lote las decisiones y defaults que turbo dejó en cola.
tags: [manual, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# pending

## Qué hace y cuándo usarlo

Administra la cola de decisiones que el modo turbo dejó pendientes: cada una ya tiene una opción por defecto aplicada, y tú respondes todas juntas en vez de que te interrumpan una por una. Úsalo al cerrar una tarea, al empezar sesión, o cuando quieras revisar decisiones acumuladas.

## Qué escribes

```text
/pending list
```

## Qué hará el agente y qué obtienes

- Lista las decisiones abiertas, agrupadas, con el default ya aplicado a cada una.
- Si respondes, aplica tu respuesta a los ítems que elijas, en un solo paso.
- Si algo en la cola en realidad debía detener el trabajo, te avisa y lo trata como bloqueante.

**Obtienes:** el archivo `docs/_work/PENDIENTES.md` actualizado, con el estado de cada ítem (abierto o resuelto).

## Errores comunes y cómo salir

- Una fila dice "credencial" y sigue abierta → resuélvela pronto: sin ella, algo no va a funcionar.
- Sin la CLI a mano → edita el archivo a mano, una fila por ítem con las mismas columnas.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/pending` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/pending.md`". |
| Antigravity | `/pending` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/pending` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta pending" o "ejecuta el playbook `commands/pending.md`". |
| Gemini CLI | `/pending` (`.gemini/commands/pending.toml`). |
| Windsurf / Devin Desktop | `/pending` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta pending". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/pending.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/pending.md`". |

Playbook completo: [`/commands/pending.md`](/commands/pending.md).
