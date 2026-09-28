---
type: Manual Page
title: connect — superficie agéntica del ADS
description: Da al ADS su superficie agéntica (ads.yaml, skill, MCP, API) para que otro agente lo opere.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# connect

## Qué hace y cuándo usarlo

Prepara el proyecto para que otro agente de inteligencia artificial (no una persona) pueda descubrirlo y operarlo de forma segura, sin integraciones a medida. Úsalo al cerrar la primera entrega funcional, o cuando cambie cómo otros agentes lo usan.

## Qué escribes

```text
/connect
```

## Qué hará el agente y qué obtienes

- Confirma que el proyecto tiene su ficha de identidad y sus reglas de gobierno al día.
- Genera la "habilidad" que le permite a otro agente entender cómo operar este proyecto.
- Revisa que nada destructivo o de producción quede ejecutable por otro agente sin confirmación previa.

**Obtienes:** el proyecto listo para que otro agente lo opere, verificado automáticamente.

## Errores comunes y cómo salir

- La verificación encuentra algo destructivo sin confirmación humana → corrígelo antes de dar esto por cerrado.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/connect` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/connect.md`". |
| Antigravity | `/connect` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/connect` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta connect" o "ejecuta el playbook `commands/connect.md`". |
| Gemini CLI | `/connect` (`.gemini/commands/connect.toml`). |
| Windsurf / Devin Desktop | `/connect` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta connect". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/connect.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/connect.md`". |

Playbook completo: [`/commands/connect.md`](/commands/connect.md).
