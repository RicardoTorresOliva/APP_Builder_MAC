---
type: Manual Page
title: security — auditoría de seguridad
description: Audita la unidad o el ADS contra OWASP y verifica que no haya secretos expuestos.
tags: [manual, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# security

## Qué hace y cuándo usarlo

Revisa la tarea o el proyecto completo en busca de problemas de seguridad conocidos, y confirma que no hay contraseñas ni llaves de acceso expuestas. Úsalo antes de publicar, y siempre en tareas que tocan inicio de sesión, pagos o datos personales.

## Qué escribes

```text
/security pedidos
```

## Qué hará el agente y qué obtienes

- Revisa la lista de problemas de seguridad conocidos según el tipo de tarea.
- Busca contraseñas, llaves o tokens filtrados en el código, los mensajes de error o la pantalla.
- Si la tarea usa IA generativa, revisa que no se pueda manipular con instrucciones escondidas en los datos.

**Obtienes:** los hallazgos de seguridad y cómo se corrigieron, registrados.

## Errores comunes y cómo salir

- Un problema real explotable en producción, o una credencial de producción expuesta → detiene todo hasta corregirlo.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/security` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/security.md`". |
| Antigravity | `/security` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/security` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta security" o "ejecuta el playbook `commands/security.md`". |
| Gemini CLI | `/security` (`.gemini/commands/security.toml`). |
| Windsurf / Devin Desktop | `/security` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta security". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/security.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/security.md`". |

Playbook completo: [`/commands/security.md`](/commands/security.md).
