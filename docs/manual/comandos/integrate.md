---
type: Manual Page
title: integrate — integra una plataforma externa
description: Conecta el ADS con un tercero por la vía más segura disponible, de MCP a SQL de mínimo privilegio.
tags: [manual, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# integrate

## Qué hace y cuándo usarlo

Conecta el proyecto con un servicio externo (pagos, mensajería, un sistema de clientes) eligiendo siempre la forma más segura disponible. Úsalo cuando el proyecto necesita hablar con un tercero (nombra la plataforma real).

## Qué escribes

```text
/integrate stripe
```

## Qué hará el agente y qué obtienes

- Evalúa las formas de conectarse de la más a la menos segura, y elige la primera que resuelva el caso.
- Configura el inicio de sesión que pida ese servicio, sin usar nunca credenciales reales en el código.
- Revisa que no haya contraseñas ni llaves de acceso filtradas en el proyecto.

**Obtienes:** la integración documentada, con un plan de cómo salir de ella si hiciera falta cambiar de proveedor.

## Errores comunes y cómo salir

- Enviar datos reales a un tercero, o activar la conexión en producción → siempre se detiene hasta que lo confirmes.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/integrate` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/integrate.md`". |
| Antigravity | `/integrate` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/integrate` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta integrate" o "ejecuta el playbook `commands/integrate.md`". |
| Gemini CLI | `/integrate` (`.gemini/commands/integrate.toml`). |
| Windsurf / Devin Desktop | `/integrate` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta integrate". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/integrate.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/integrate.md`". |

Playbook completo: [`/commands/integrate.md`](/commands/integrate.md).
