---
type: Manual Page
title: init-project — planifica un proyecto nuevo
description: Elige perfil y ceremonia, clasifica la metodología, explora el stack con el humano y publica el plan.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# init-project

## Qué hace y cuándo usarlo

Planifica un proyecto nuevo de principio a fin: entiende qué quieres construir, elige cuánta formalidad necesita, te presenta opciones de tecnología para que tú elijas, y publica un plan — sin escribir código todavía. Úsalo al arrancar un proyecto nuevo.

## Qué escribes

```text
describe tu proyecto en el chat, o completa antes START_PROJECT.md y luego "/init-project"
```

## Qué hará el agente y qué obtienes

- Si es la primera vez en el repositorio, corre `bootstrap` antes.
- Lee lo que describiste y elige el tipo de proyecto (perfil) que mejor encaja.
- Decide cuánta formalidad necesita el proyecto (un prototipo rápido no se trata igual que un sistema regulado).
- Te presenta 2 o 3 opciones de tecnología con ventajas y desventajas: la decisión final es tuya.
- Divide el trabajo en tareas ordenadas y publica el plan completo.

**Obtienes:** un plan publicado con las tareas ordenadas, la tecnología elegida, y los documentos de arranque del proyecto. Nada de código todavía.

## Errores comunes y cómo salir

- No sabes qué describir → usa `START_PROJECT.md` como guía: tiene las preguntas ya armadas.
- No entiendes una opción de tecnología → pide que te la expliquen sin jerga antes de elegir: espera tu respuesta.
- El proyecto toca pagos, datos personales o de salud → pasará por más revisión: es normal, no un error.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/init-project` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/init-project.md`". |
| Antigravity | `/init-project` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/init-project` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta init-project" o "ejecuta el playbook `commands/init-project.md`". |
| Gemini CLI | `/init-project` (`.gemini/commands/init-project.toml`). |
| Windsurf / Devin Desktop | `/init-project` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta init-project". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/init-project.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/init-project.md`". |

Playbook completo: [`/commands/init-project.md`](/commands/init-project.md).
