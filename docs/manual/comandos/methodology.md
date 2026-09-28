---
type: Manual Page
title: methodology — clasifica el modo metodológico
description: Asigna VIBE, IDD, SDD, SPDD o AIDD a un módulo según sus seis dimensiones de riesgo.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# methodology

## Qué hace y cuándo usarlo

Decide, para cada parte del proyecto, cuánto rigor y revisión necesita: no todo merece el mismo cuidado. Úsalo al planificar una parte nueva, o cuando algo dejó de encajar con el nivel asignado.

## Qué escribes

```text
/methodology pagos
```

## Qué hará el agente y qué obtienes

- Evalúa el riesgo real de esa parte (qué tan crítica es, qué tan clara está, cuánta gente la usa).
- Si toca pagos, inicio de sesión, datos personales o de salud, o hay regulación, sube el nivel de revisión sin excepción.
- Registra el nivel elegido y por qué, en un documento del proyecto.

**Obtienes:** cada parte del proyecto con su nivel de rigor asignado y justificado.

## Errores comunes y cómo salir

- No estás seguro del riesgo → descríbelo en texto libre: el sistema lo infiere, y si tiene poca confianza, lo deja en la cola de pendientes para tu revisión.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/methodology` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/methodology.md`". |
| Antigravity | `/methodology` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/methodology` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta methodology" o "ejecuta el playbook `commands/methodology.md`". |
| Gemini CLI | `/methodology` (`.gemini/commands/methodology.toml`). |
| Windsurf / Devin Desktop | `/methodology` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta methodology". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/methodology.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/methodology.md`". |

Playbook completo: [`/commands/methodology.md`](/commands/methodology.md).
