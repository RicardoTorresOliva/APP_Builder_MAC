---
type: Manual Page
title: ads-check — verifica el Contrato ADS
description: Verifica que el ADS cumple su nivel del Contrato ADS, estático y dinámico.
tags: [manual, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# ads-check

## Qué hace y cuándo usarlo

Verifica que el proyecto cumple con lo mínimo que necesita para ser operado y auditado por otros agentes de forma confiable. Úsalo en `connect`, y siempre antes de publicar.

## Qué escribes

```text
/ads-check
```

## Qué hará el agente y qué obtienes

- Revisa la identidad del proyecto, sus capacidades declaradas, y que otro agente pueda descubrirlo y entenderlo.
- Si el nivel exigido es más alto, revisa también el panel de tokens y el registro de auditoría.
- Corre una prueba real: descubrir → listar capacidades → leer → probar en modo seguro → medir tokens.

**Obtienes:** el resultado de ambas verificaciones, con cualquier hallazgo a corregir.

## Errores comunes y cómo salir

- El proyecto declara un nivel más exigente y no lo cumple → no se puede publicar hasta corregirlo.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/ads-check` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/ads-check.md`". |
| Antigravity | `/ads-check` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/ads-check` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta ads-check" o "ejecuta el playbook `commands/ads-check.md`". |
| Gemini CLI | `/ads-check` (`.gemini/commands/ads-check.toml`). |
| Windsurf / Devin Desktop | `/ads-check` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta ads-check". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/ads-check.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/ads-check.md`". |

Playbook completo: [`/commands/ads-check.md`](/commands/ads-check.md).
