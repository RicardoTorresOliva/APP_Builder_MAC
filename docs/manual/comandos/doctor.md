---
type: Manual Page
title: doctor — diagnóstico del entorno
description: Diagnostica el entorno (Python, git, estructura, config) en lenguaje simple y sugiere arreglos.
tags: [manual, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# doctor

## Qué hace y cuándo usarlo

Revisa tu computadora y el proyecto, y te dice en palabras simples qué falta y cómo arreglarlo. Úsalo cuando algo no funciona y no sabes por qué, o antes de avisar que algo está roto.

## Qué escribes

```text
/doctor
```

## Qué hará el agente y qué obtienes

- Revisa si tienes Python 3.9 o más nuevo, git, y si estás en la carpeta correcta del proyecto.
- Marca cada cosa con ✔ (bien), ✖ (falta, es obligatorio) o – (falta, es opcional).
- Si algo obligatorio falta, explica el paso exacto para instalarlo.

**Obtienes:** un reporte de estado y, si falta algo, el paso exacto para arreglarlo.

## Errores comunes y cómo salir

- `✖ python` → instala Python 3.9 o superior desde python.org y vuelve a abrir la terminal.
- `✖ git` → instala Git (git-scm.com); lo necesitas para guardar puntos de control y poder deshacer cambios.
- Falta `AGENTS.md` o `abm.yaml` → no estás dentro de la carpeta del proyecto; abre la terminal ahí.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/doctor` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/doctor.md`". |
| Antigravity | `/doctor` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/doctor` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta doctor" o "ejecuta el playbook `commands/doctor.md`". |
| Gemini CLI | `/doctor` (`.gemini/commands/doctor.toml`). |
| Windsurf / Devin Desktop | `/doctor` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta doctor". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/doctor.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/doctor.md`". |

Playbook completo: [`/commands/doctor.md`](/commands/doctor.md).
