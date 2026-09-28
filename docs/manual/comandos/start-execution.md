---
type: Manual Page
title: start-execution — ejecución autónoma
description: Verifica que el plan esté listo y ejecuta las FU y DU aprobadas hasta la entrega.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# start-execution

## Qué hace y cuándo usarlo

Empieza a construir, de forma autónoma, el plan ya publicado y aprobado (o en cola con luz verde para lo reversible). Va tarea por tarea, con las verificaciones de calidad correspondientes. Úsalo cuando el plan está listo.

## Qué escribes

```text
/start-execution
```

## Qué hará el agente y qué obtienes

- Verifica que el plan esté completo antes de empezar; si falta algo, lo completa primero.
- Construye primero las tareas de base, luego las que usa el usuario final, agrupadas en bloques.
- Después de cada tarea, actualiza el registro de progreso y mide cuánto costó en tokens.
- Después de cada bloque, pide una revisión independiente de lo construido.
- Se detiene y te pregunta si algo es ambiguo, contradictorio, o si una integración no funciona como se esperaba.

**Obtienes:** las tareas construidas y verificadas de punta a punta, con el registro de progreso al día.

## Errores comunes y cómo salir

- Se detiene con una pregunta → encontró algo que de verdad necesita tu decisión: no es un fallo, el diseño funcionando.
- Algo salió mal a mitad de camino → revisa `docs/manual/como-deshacer.md` para volver a un punto anterior de forma segura.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/start-execution` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/start-execution.md`". |
| Antigravity | `/start-execution` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/start-execution` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta start-execution" o "ejecuta el playbook `commands/start-execution.md`". |
| Gemini CLI | `/start-execution` (`.gemini/commands/start-execution.toml`). |
| Windsurf / Devin Desktop | `/start-execution` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta start-execution". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/start-execution.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/start-execution.md`". |

Playbook completo: [`/commands/start-execution.md`](/commands/start-execution.md).
