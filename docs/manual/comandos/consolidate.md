---
type: Manual Page
title: consolidate — lleva lo aprendido a diseño real
description: Convierte los aprendizajes de un explore en spec y diseño definitivos (IDD/SDD).
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# consolidate

## Qué hace y cuándo usarlo

Toma lo aprendido en una exploración (`explore`) y lo convierte en un diseño y una implementación de verdad, con la calidad que corresponde — no la de un experimento rápido. Úsalo justo después de un `explore` que ya respondió su pregunta.

## Qué escribes

```text
/consolidate "límites del proveedor de pagos"
```

## Qué hará el agente y qué obtienes

- Revisa qué de lo probado sirve y qué se descarta, y por qué.
- Reescribe el diseño y la especificación con la calidad definitiva; no copia el código de prueba tal cual.
- Archiva o borra la rama de prueba una vez que lo aprendido ya quedó documentado.

**Obtienes:** la especificación y el diseño actualizados con lo aprendido, listos para construirse en serio.

## Errores comunes y cómo salir

- Apareció algo sensible (pagos, datos personales) en el camino → este paso sube el nivel de rigor automáticamente: es intencional.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/consolidate` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/consolidate.md`". |
| Antigravity | `/consolidate` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/consolidate` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta consolidate" o "ejecuta el playbook `commands/consolidate.md`". |
| Gemini CLI | `/consolidate` (`.gemini/commands/consolidate.toml`). |
| Windsurf / Devin Desktop | `/consolidate` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta consolidate". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/consolidate.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/consolidate.md`". |

Playbook completo: [`/commands/consolidate.md`](/commands/consolidate.md).
