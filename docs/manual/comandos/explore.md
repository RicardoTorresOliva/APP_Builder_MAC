---
type: Manual Page
title: explore — spike acotado en sandbox
description: Prueba y descarta en una rama sandbox con tiempo acotado para resolver una incertidumbre.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# explore

## Qué hace y cuándo usarlo

Cuando hay mucha incertidumbre sobre si algo va a funcionar, prueba una versión rápida y desechable en una rama aparte (sandbox), con un tiempo límite fijo, en vez de planear a ciegas. Úsalo cuando conviene probar antes de comprometerte a un diseño.

## Qué escribes

```text
/explore "¿el proveedor de pagos soporta webhooks firmados?" --tiempo 60
```

## Qué hará el agente y qué obtienes

- Crea una rama aparte (nunca la rama principal del proyecto) y fija el tiempo límite antes de empezar.
- Prueba rápido, sin preocuparse por dejar el código prolijo: el objetivo es aprender, no entregar.
- Al terminar, resume qué funcionó, qué no, y qué se aprendió.

**Obtienes:** un registro de la exploración (`explore-log`) con la recomendación de qué hacer después. El código de prueba se descarta o se archiva; nunca pasa a producción directamente.

## Errores comunes y cómo salir

- El tiempo se acaba y la pregunta sigue sin respuesta → cierra igual con lo aprendido hasta ahí; no extiendas el plazo sin decirlo.
- El código de esta rama nunca se mezcla con el trabajo principal sin pasar antes por `consolidate`.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/explore` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/explore.md`". |
| Antigravity | `/explore` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/explore` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta explore" o "ejecuta el playbook `commands/explore.md`". |
| Gemini CLI | `/explore` (`.gemini/commands/explore.toml`). |
| Windsurf / Devin Desktop | `/explore` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta explore". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/explore.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/explore.md`". |

Playbook completo: [`/commands/explore.md`](/commands/explore.md).
