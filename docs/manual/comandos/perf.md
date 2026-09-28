---
type: Manual Page
title: perf — rendimiento y escalabilidad
description: Verifica rendimiento, escalabilidad básica y costo por unidad antes de entregar.
tags: [manual, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# perf

## Qué hace y cuándo usarlo

Verifica que el proyecto responda rápido y aguante el uso esperado, incluido cuánto cuesta en tokens. Úsalo antes de publicar, y en tareas con mucho volumen de datos o tráfico esperado.

## Qué escribes

```text
/perf pedidos
```

## Qué hará el agente y qué obtienes

- Revisa que las partes críticas no dependan de un solo servidor y usen memoria caché donde ayude.
- Revisa que las consultas a la base de datos sean eficientes.
- Si el proyecto lo exige, corre una prueba de carga básica sobre los caminos más importantes.

**Obtienes:** el resultado de rendimiento y el costo por unidad, registrados.

## Errores comunes y cómo salir

- Correr una prueba de carga contra producción o un proveedor externo sin avisar antes → se detiene siempre.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/perf` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/perf.md`". |
| Antigravity | `/perf` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/perf` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta perf" o "ejecuta el playbook `commands/perf.md`". |
| Gemini CLI | `/perf` (`.gemini/commands/perf.toml`). |
| Windsurf / Devin Desktop | `/perf` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta perf". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/perf.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/perf.md`". |

Playbook completo: [`/commands/perf.md`](/commands/perf.md).
