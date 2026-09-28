---
type: Manual Page
title: plan — publica el plan de ejecución
description: Ordena FU y DU en el tracker, redacta el plan y lo publica para su aprobación o cola.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# plan

## Qué hace y cuándo usarlo

Ordena el trabajo en tareas y lo publica para avanzar con aprobación, o en cola si estás en modo rápido (turbo). Nada se construye sin este paso. Úsalo después de `spec` o `intent`, antes de construir.

## Qué escribes

```text
/plan "milestone 1"
```

## Qué hará el agente y qué obtienes

- Agrupa primero las tareas de base, luego las que entrega el usuario final, por bloques.
- Escribe el plan: alcance, orden, riesgos, y cómo se sabe que cada tarea salió bien.
- Publica el plan. En turbo (el modo normal), "aprobar el plan" entra en la cola y lo reversible sigue andando; en modo con revisión obligatoria o proyectos muy regulados, espera tu aprobación explícita.

**Obtienes:** un plan publicado, listo para que `start-execution` empiece a construir.

## Errores comunes y cómo salir

- El proyecto es de tipo muy regulado (p. ej. datos de salud) → el plan espera tu "sí" explícito: es la ceremonia correcta, no un error.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/plan` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/plan.md`". |
| Antigravity | `/plan` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/plan` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta plan" o "ejecuta el playbook `commands/plan.md`". |
| Gemini CLI | `/plan` (`.gemini/commands/plan.toml`). |
| Windsurf / Devin Desktop | `/plan` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta plan". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/plan.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/plan.md`". |

Playbook completo: [`/commands/plan.md`](/commands/plan.md).
