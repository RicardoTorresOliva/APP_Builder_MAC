---
type: Manual Page
title: drift — deriva intención/spec/código
description: Detecta y resuelve la deriva entre intención, spec, contrato de prompt y código real.
tags: [manual, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# drift

## Qué hace y cuándo usarlo

Detecta cuándo lo que se planeó, lo que se especificó y lo que se construyó dejaron de coincidir, y decide qué corregir. Úsalo de vez en cuando mientras se construye, y siempre antes de `closeout`.

## Qué escribes

```text
/drift pedidos
```

## Qué hará el agente y qué obtienes

- Compara lo que dice la especificación contra cómo se comporta la tarea de verdad.
- Si hay una diferencia, decide y explica si se actualiza el documento o se corrige el código.
- Si la tarea toca pagos, inicio de sesión o datos personales, pide revisión humana antes de resolver.

**Obtienes:** el desajuste encontrado y cómo se resolvió, registrado.

## Errores comunes y cómo salir

- Ninguna tarea se cierra con un desajuste sin resolver o sin explicar por qué se acepta tal cual.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/drift` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/drift.md`". |
| Antigravity | `/drift` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/drift` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta drift" o "ejecuta el playbook `commands/drift.md`". |
| Gemini CLI | `/drift` (`.gemini/commands/drift.toml`). |
| Windsurf / Devin Desktop | `/drift` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta drift". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/drift.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/drift.md`". |

Playbook completo: [`/commands/drift.md`](/commands/drift.md).
