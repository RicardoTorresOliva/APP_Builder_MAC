---
type: Manual Page
title: assess — inventario de brownfield/legacy
description: Inventaría un stack existente y propone el patrón de integración más simple que funcione.
tags: [manual, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:54:43Z }
---

# assess

## Qué hace y cuándo usarlo

Antes de tocar un sistema que ya existe y está en uso, lo inventaría (qué tecnología usa, qué bases de datos, qué conexiones tiene) y propone la forma más simple y segura de integrarse o reemplazarlo poco a poco. Úsalo cuando el proyecto convive con, o reemplaza, algo ya en producción.

## Qué escribes

```text
/assess "sistema de facturación actual, hecho en Java"
```

## Qué hará el agente y qué obtienes

- Revisa el sistema existente con acceso de solo lectura: lenguaje, base de datos, despliegue, restricciones de red.
- Identifica cómo inician sesión los usuarios y si hay restricciones corporativas.
- Propone el patrón de integración más simple que funcione, y explica por qué descartó los más invasivos.

**Obtienes:** un documento con el inventario del sistema existente y la estrategia de integración recomendada.

## Errores comunes y cómo salir

- El diagnóstico pide credenciales de producción o permiso de escritura → se detiene: necesita tu aprobación explícita.
- Sin acceso técnico directo → entrevista a quien conoce el sistema y completa el inventario con esas respuestas.

## Cómo invocarlo en cada herramienta

| Herramienta | Cómo invocarlo |
|---|---|
| Claude Code | `/assess` en el chat. |
| Codex | Sin comandos de proyecto: activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/assess.md`". |
| Antigravity | `/assess` (workflow en `.agents/workflows/`). |
| VS Code + Copilot | `/assess` (prompt file en `.github/prompts/`). |
| Cursor | Pide "usa la skill abm-playbooks y ejecuta assess" o "ejecuta el playbook `commands/assess.md`". |
| Gemini CLI | `/assess` (`.gemini/commands/assess.toml`). |
| Windsurf / Devin Desktop | `/assess` (workflow en `.devin/workflows/`). |
| Kiro | Menciona el steering manual `#abm-playbooks` y pide "ejecuta assess". |
| Hermes | Activa la skill `abm-playbooks` o pide "ejecuta el playbook `commands/assess.md`". |
| Cualquier otra herramienta | "Lee y ejecuta `commands/assess.md`". |

Playbook completo: [`/commands/assess.md`](/commands/assess.md).
