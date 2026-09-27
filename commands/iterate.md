---
type: Playbook
title: iterate — cambios post-entrega
description: Aplica un cambio, mejora o corrección tras la entrega, con spec-delta antes de tocar código.
args: "[<pedido del usuario>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# iterate

## Propósito

Aplica un cambio pedido después de la entrega, siempre con un spec-delta antes de tocar código, para mantener trazabilidad entre intención, spec y código.

## Cuándo usarlo

- El ADS ya fue entregado y el usuario pide un cambio.

## Entradas

- `docs/project_memory.md`, `implementation/task_tracker.md`, `implementation/user_units.md`.

## Pasos

1. [verde] Clasifica el pedido: corrección de bug, hueco de planeación (ya implícito en el alcance), mejora (modifica una unidad existente), o funcionalidad nueva (unidad nueva).
2. [verde] Emite el spec-delta antes de cualquier cambio: agregado, modificado, eliminado, docs y knowledge afectados, riesgo de regresión.
3. [amarillo] Para mejora o funcionalidad nueva: presenta el spec-delta al humano y espera aprobación, o encólalo en turbo si es reversible.
4. [verde] Corrección de bug y hueco de planeación proceden directo — ya estaban en alcance.
5. [verde] Aplica el flujo estándar por unidad (perfil, quality gate, `governed_by` si es compuesto).
6. [verde] Verifica que la funcionalidad existente sigue funcionando (regresión) antes de cerrar.
7. [verde] Actualiza `task_tracker.md`, `work_log.md`, `project_memory.md` y `knowledge/` si el esquema o contrato cambió.

## Salidas

- Spec-delta en `docs/work_log.md`.
- Unidad o unidades actualizadas.

## Gates

Ningún cambio de comportamiento sin documentar por qué; regresión verificada; schema o contrato sin su design doc actualizado es bloqueante de cierre.

## Fallback

Redacta el spec-delta como nota de una página y sigue el mismo orden a mano.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `docs/work_log.md` → spec-delta → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook"; `./abm pending add --json` para encolar la aprobación en turbo.
