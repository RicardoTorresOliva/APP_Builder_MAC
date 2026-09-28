---
type: Manual Page
title: deploy — publica el ADS
description: Publica el ADS en su entorno de destino tras pasar la checklist previa y con rollback listo.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# deploy

## Qué hace y cuándo usarlo

Publica el proyecto en el lugar donde va a usarse de verdad, solo después de pasar todas las verificaciones y con un plan claro de cómo revertir si algo sale mal. Úsalo después de pasar `review`, `security` y `ads-check`.

## Qué escribes

```text
/deploy staging
```

## Qué hará el agente y qué obtienes

- Verifica que todo esté en orden: pruebas en verde, verificaciones generales sin errores, sin contraseñas expuestas.
- Prepara cómo revertir la publicación antes de hacerla, no después.
- Publica primero a un entorno de prueba (staging) si existe, antes que al real.

**Obtienes:** el proyecto publicado y documentado (versión, entorno, hora).

## Errores comunes y cómo salir

- Publicar al entorno real, cobrar dinero de verdad, o exponer credenciales reales → siempre se detiene y pide tu confirmación explícita, con una opción recomendada.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/deploy` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/deploy.md`". |
| Antigravity | `/deploy` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/deploy` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta deploy" o "ejecuta el playbook `commands/deploy.md`". |
| Gemini CLI | `/deploy` (`.gemini/commands/deploy.toml`). |
| Windsurf / Devin Desktop | `/deploy` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta deploy". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/deploy.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/deploy.md`". |

Playbook completo: [`/commands/deploy.md`](/commands/deploy.md).
