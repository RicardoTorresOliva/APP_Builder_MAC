---
type: Manual Page
title: decide — capa System One
description: Resuelve una decisión tipada (choice/score/boolean) con la capa de decisión y su routing por confianza.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# decide

## Qué hace y cuándo usarlo

Para decisiones chicas y repetitivas (¿esto es spam?, ¿qué tan riesgosa es esta acción?), usa un modelo más simple y barato que un asistente de IA completo. Úsalo para clasificar, calificar riesgo, o elegir entre opciones conocidas.

## Qué escribes

```text
/decide "¿este mensaje es spam? (sí/no)"
```

## Qué hará el agente y qué obtienes

- Formula la pregunta de forma cerrada: elegir una opción, poner un puntaje, o sí/no.
- Responde con un valor y qué tan segura está esa respuesta (su "confianza").
- Si la confianza es alta, actúa directo; si es media, pasa a un asistente más completo o a la cola; si es baja, pasa a una persona.

**Obtienes:** una respuesta con su nivel de confianza, registrada para poder revisarla después.

## Errores comunes y cómo salir

- Una decisión de baja confianza nunca se ejecuta sola: siempre queda en cola o pasa a una persona; es intencional, no un error.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/decide` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/decide.md`". |
| Antigravity | `/decide` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/decide` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta decide" o "ejecuta el playbook `commands/decide.md`". |
| Gemini CLI | `/decide` (`.gemini/commands/decide.toml`). |
| Windsurf / Devin Desktop | `/decide` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta decide". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/decide.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/decide.md`". |

Playbook completo: [`/commands/decide.md`](/commands/decide.md).
