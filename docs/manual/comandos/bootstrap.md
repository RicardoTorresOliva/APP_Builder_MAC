---
type: Manual Page
title: bootstrap — chequeo único de plataforma
description: Detecta la plataforma, corre doctor y sync, y confirma que el repo está listo para trabajar.
tags: [manual, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# bootstrap

## Qué hace y cuándo usarlo

Comprueba, una sola vez al abrir el proyecto en una herramienta nueva, que todo está listo para trabajar: que tu computadora tiene lo necesario y que los archivos de tu herramienta están al día. Úsalo la primera vez que abres el repositorio o después de clonarlo; `init-project` lo llama solo si hace falta.

## Qué escribes

```text
/bootstrap
```

## Qué hará el agente y qué obtienes

- Detecta en qué herramienta estás trabajando.
- Corre el diagnóstico del entorno (`doctor`): revisa que tengas Python y git.
- Revisa que los archivos generados para tu herramienta (los comandos `/`, por ejemplo) estén al día; si no, los regenera.

**Obtienes:** un mensaje con la herramienta detectada, el resultado del diagnóstico y los comandos disponibles. Si algo estaba desactualizado, esos archivos quedan regenerados (reversible: son archivos generados, no tu trabajo).

## Errores comunes y cómo salir

- Python o git marcados como faltantes → son obligatorios: instálalos antes de seguir (ver `docs/troubleshooting.md`).
- Los archivos de tu herramienta estaban desactualizados → se regeneran solos, no se pierde nada tuyo.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/bootstrap` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/bootstrap.md`". |
| Antigravity | `/bootstrap` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/bootstrap` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta bootstrap" o "ejecuta el playbook `commands/bootstrap.md`". |
| Gemini CLI | `/bootstrap` (`.gemini/commands/bootstrap.toml`). |
| Windsurf / Devin Desktop | `/bootstrap` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta bootstrap". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/bootstrap.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/bootstrap.md`". |

Playbook completo: [`/commands/bootstrap.md`](/commands/bootstrap.md).
