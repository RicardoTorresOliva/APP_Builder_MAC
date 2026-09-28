---
type: Manual Page
title: release — cierra una versión
description: Cierra una versión del ADS con semver, changelog y verificación previa completa.
tags: [manual, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# release

## Qué hace y cuándo usarlo

Cierra una versión del proyecto — le pone número, escribe qué cambió, y confirma que todo pasó revisión — antes de considerarla lista. Úsalo al completar un bloque de trabajo que se entrega como versión.

## Qué escribes

```text
/release 1.2.0
```

## Qué hará el agente y qué obtienes

- Confirma que todas las tareas del bloque pasaron `review` y `ads-check`.
- Sube el número de versión y escribe qué se agregó, cambió o corrigió.
- Etiqueta la versión (reversible: es solo una etiqueta).

**Obtienes:** la nueva versión, con su registro de cambios (changelog).

## Errores comunes y cómo salir

- Hay hallazgos graves sin resolver de `review`, `security` o `ads-check` → ninguna versión se libera así.
- Publicarla como disponible para terceros (paquete público, aviso a clientes) → siempre pide tu confirmación.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/release` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/release.md`". |
| Antigravity | `/release` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/release` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta release" o "ejecuta el playbook `commands/release.md`". |
| Gemini CLI | `/release` (`.gemini/commands/release.toml`). |
| Windsurf / Devin Desktop | `/release` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta release". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/release.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/release.md`". |

Playbook completo: [`/commands/release.md`](/commands/release.md).
