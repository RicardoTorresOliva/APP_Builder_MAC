---
type: Manual Page
title: tokens — espacio de control de tokens
description: Registra, reporta y verifica el consumo y presupuesto de tokens de cada unidad.
tags: [manual, medir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# tokens

## Qué hace y cuándo usarlo

Lleva la cuenta de cuánto "combustible" (tokens) usó cada tarea, genera reportes fáciles de leer, y avisa si te acercas o te pasas de tu presupuesto. Úsalo al cerrar cada tarea, y cuando quieras revisar el costo del proyecto.

## Qué escribes

```text
/tokens report
```

## Qué hará el agente y qué obtienes

- Registra el consumo de la tarea: medido si hay datos exactos, o estimado (caracteres del texto producido, entre 4) si no los hay.
- Genera un reporte simple (`TOKENS.md`) y, si el proyecto lo exige, un panel visual.
- Verifica los presupuestos: pasar el umbral de aviso solo anota una nota en la cola; pasar el tope máximo detiene la tarea.

**Obtienes:** el reporte de tokens y el estado de tus presupuestos, con semáforo verde/amarillo/rojo. Ver `/docs/manual/tokens.md` para leerlo en detalle.

## Errores comunes y cómo salir

- Superaste el tope máximo (rojo) → la tarea se detiene hasta que decidas: ampliar el presupuesto o recortar lo que falta.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/tokens` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/tokens.md`". |
| Antigravity | `/tokens` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/tokens` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta tokens" o "ejecuta el playbook `commands/tokens.md`". |
| Gemini CLI | `/tokens` (`.gemini/commands/tokens.toml`). |
| Windsurf / Devin Desktop | `/tokens` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta tokens". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/tokens.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/tokens.md`". |

Playbook completo: [`/commands/tokens.md`](/commands/tokens.md).
