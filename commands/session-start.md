---
type: Playbook
title: session-start — inicio de sesión
description: Lee la memoria del proyecto y la cola de pendientes, y dice por dónde retomar el trabajo.
args: ""
tags: [comando, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# session-start

## Propósito

Reanuda una sesión de trabajo leyendo solo la memoria mínima necesaria, sin releer diseño completo ni historial que ya está resumido.

## Cuándo usarlo

- Al inicio de cada sesión de trabajo sobre un proyecto ya iniciado.

## Entradas

- `docs/project_memory.md`
- `implementation/task_tracker.md`
- `docs/_work/PENDIENTES.md`
- `knowledge/index.md`

## Pasos

1. [verde] Lee `docs/project_memory.md`: perfil activo, última unidad completada, siguiente unidad, bloqueos.
2. [verde] Lee `implementation/task_tracker.md`; identifica la unidad `in_progress` o, si no hay, la siguiente `pending`.
3. [verde] Lee `docs/_work/PENDIENTES.md`; agrupa por tipo y resume cuántas hay abiertas.
4. [verde] Carga `knowledge/index.md` para orientarte; no abras design docs completos todavía.
5. [verde] Publica el resumen de arranque: perfil, estado, última/siguiente unidad, bloqueos, pendientes abiertos.
6. [verde] Retoma desde la siguiente unidad sin releer lo que ya está capturado en `project_memory.md`.

## Salidas

- Ninguno (comando de lectura); el resumen queda en el reporte de la sesión.

## Gates

Si `implementation/task_tracker.md` no existe, el proyecto no pasó por `init-project`: sugiérelo antes de seguir.

## Fallback

Abre los 4 archivos de entrada con el editor o `cat` y resume a mano los mismos 5 puntos del resumen.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm pending list` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm pending list --json` para el resumen de cola; sin orden CLI propia — "lee y ejecuta este playbook".
