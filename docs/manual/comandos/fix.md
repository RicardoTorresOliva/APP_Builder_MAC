---
type: Manual Page
title: fix — corrige un bug
description: Reproduce el bug, escribe el test que falla, aplica el cambio mínimo y verifica sin regresión.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# fix

## Qué hace y cuándo usarlo

Corrige un error reproducible con el mínimo cambio posible: primero confirma el error, después escribe una prueba que lo demuestre, y recién ahí lo arregla. Úsalo cuando algo se comporta mal y puedes reproducirlo.

## Qué escribes

```text
/fix "el botón de pagar no responde en móvil"
```

## Qué hará el agente y qué obtienes

- Reproduce el error de forma consistente antes de tocar nada.
- Escribe una prueba que falle exactamente por esa causa: queda demostrado que el error existe.
- Aplica el cambio mínimo que hace pasar la prueba, sin aprovechar para reorganizar código de paso.

**Obtienes:** el error corregido, con una prueba nueva que evita que vuelva a pasar sin darte cuenta.

## Errores comunes y cómo salir

- Arreglarlo implica tocar datos ya guardados en producción → se detiene: eso necesita un plan aparte.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/fix` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/fix.md`". |
| Antigravity | `/fix` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/fix` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta fix" o "ejecuta el playbook `commands/fix.md`". |
| Gemini CLI | `/fix` (`.gemini/commands/fix.toml`). |
| Windsurf / Devin Desktop | `/fix` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta fix". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/fix.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/fix.md`". |

Playbook completo: [`/commands/fix.md`](/commands/fix.md).
