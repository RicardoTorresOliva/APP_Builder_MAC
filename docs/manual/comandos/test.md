---
type: Manual Page
title: test — pirámide de pruebas
description: Verifica la unidad con la pirámide de pruebas del perfil, priorizando rutas críticas.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# test

## Qué hace y cuándo usarlo

Verifica que la tarea funciona como debe, priorizando los caminos más importantes por sobre cubrir el 100 % de los casos. Úsalo al cerrar cada tarea, siempre antes de `review`.

## Qué escribes

```text
/test pedidos
```

## Qué hará el agente y qué obtienes

- Cubre los caminos principales: cuando todo sale bien, cuando no hay datos, y cuando algo falla.
- Si la tarea toca pagos, inicio de sesión o datos personales, pide que una persona revise las pruebas más críticas.
- Corre las pruebas y anota el resultado en el registro del proyecto.

**Obtienes:** las pruebas de la tarea y su resultado, registrados.

## Errores comunes y cómo salir

- Ninguna prueba que toque producción, pagos reales o datos personales reales corre sin tu confirmación explícita.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/test` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/test.md`". |
| Antigravity | `/test` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/test` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta test" o "ejecuta el playbook `commands/test.md`". |
| Gemini CLI | `/test` (`.gemini/commands/test.toml`). |
| Windsurf / Devin Desktop | `/test` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta test". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/test.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/test.md`". |

Playbook completo: [`/commands/test.md`](/commands/test.md).
