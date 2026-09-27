---
type: Template
title: requirements.md — requisitos EARS (SDD)
description: Requisitos en formato EARS con ID único, usados por SDD para trazar TASK↔REQ↔TEST.
tags: [template, sdd, ears, requirements]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Requisitos: `<módulo>`

Modo: SDD (`/methodology/sdd.md`). Formato EARS: "Cuando `<evento>`, el sistema debe `<respuesta>`".
Cada requisito tiene un ID único `REQ-NNN`, referenciado luego en `design.md` y `tasks.md`.

## REQ-001 — `<título corto>`
Cuando `<evento o condición>`, el sistema debe `<respuesta observable>`.

- Criterio de aceptación: `<cómo se verifica; debe ser comprobable por un test>`
- Disparador de escalamiento asociado: `<ninguno | payments | auth | personal-data | health | regulated>`

## REQ-002 — `<título corto>`
Cuando `<evento o condición>`, el sistema debe `<respuesta observable>`.

- Criterio de aceptación: `<...>`
- Disparador de escalamiento asociado: `<...>`

<!-- Repetir REQ-NNN por cada requisito. No dejar un REQ sin criterio de aceptación verificable. -->

## Fuera de alcance
- `<lo que este conjunto de requisitos explícitamente no cubre>`

## Trazabilidad
Cada `REQ-NNN` debe aparecer en `design.md` (qué lo satisface) y en `tasks.md` (qué tarea y qué test lo
cubren). Un `REQ` sin tarea o sin test bloquea el `closeout` (`/methodology/drift.md`).
