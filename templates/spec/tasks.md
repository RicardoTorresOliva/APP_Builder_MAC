---
type: Template
title: tasks.md — tareas trazables (SDD)
description: Tabla TASK ↔ REQ ↔ TEST que descompone design.md en trabajo verificable.
tags: [template, sdd, tasks, trazabilidad]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Tareas: `<módulo>`

Modo: SDD (`/methodology/sdd.md`). Cada fila enlaza una tarea con el requisito que satisface y el test
que lo verifica. Una fila sin `REQ` o sin `TEST` bloquea el `closeout` (`/methodology/drift.md`).

## Matriz de trazabilidad

| TASK | Descripción | REQ | TEST | Estado |
|---|---|---|---|---|
| TASK-001 | `<qué se construye>` | REQ-001 | `<archivo o nombre del test>` | `pendiente \| en curso \| hecho` |
| TASK-002 | `<qué se construye>` | REQ-002 | `<archivo o nombre del test>` | `pendiente \| en curso \| hecho` |

<!-- Una tarea puede cubrir más de un REQ; un REQ puede necesitar más de una tarea. -->

## Verificación de cobertura antes de cerrar

- [ ] Todo `REQ-NNN` de `requirements.md` aparece en al menos una fila.
- [ ] Toda fila tiene un `TEST` identificable y ejecutable.
- [ ] Todas las tareas están en estado `hecho` o justificadas como pendiente en `docs/_work/PENDIENTES.md`.
