---
type: Manual Page
title: api — construye el servicio
description: Construye la capa de API/servicio de una unidad con contrato de errores y quality gate.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# api

## Qué hace y cuándo usarlo

Construye la parte del proyecto que conecta la pantalla con los datos (el servicio o API), con reglas claras de qué información entra, qué sale, y qué pasa cuando algo falla. Úsalo cuando la tarea expone o consume un servicio.

## Qué escribes

```text
/api pedidos
```

## Qué hará el agente y qué obtienes

- Define primero qué información entra y sale, antes de programar.
- Programa los errores de forma clara y accionable, no mensajes crípticos.
- Verifica que solo pueda usarlo quien debe, antes de exponerlo fuera de tu entorno de prueba.

**Obtienes:** el servicio construido, con su contrato documentado y su checklist de calidad cumplido.

## Errores comunes y cómo salir

- El servicio quedaría accesible con un dominio público o credenciales reales → se detiene: necesita tu confirmación explícita.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/api` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/api.md`". |
| Antigravity | `/api` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/api` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta api" o "ejecuta el playbook `commands/api.md`". |
| Gemini CLI | `/api` (`.gemini/commands/api.toml`). |
| Windsurf / Devin Desktop | `/api` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta api". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/api.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/api.md`". |

Playbook completo: [`/commands/api.md`](/commands/api.md).
