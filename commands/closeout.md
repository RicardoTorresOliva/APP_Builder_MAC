---
type: Playbook
title: closeout — cierra una unidad
description: Sincroniza intención, spec, contrato y código, registra tokens y actualiza la memoria del proyecto.
args: "[<unidad>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# closeout

## Propósito
Cierra una FU/DU sincronizando intención, spec, contrato de prompt y código, registrando su consumo de tokens y dejando la memoria del proyecto al día.

## Cuándo usarlo
- Al terminar cada FU/DU.

## Entradas
- `docs/intent/`, `docs/spec/`, `docs/prompt-contracts/`.
- Código de la unidad.

## Pasos
1. [verde] Verifica que intención, spec, contrato de prompt (si existe) y código coinciden; si no, ejecuta `drift` antes de cerrar.
2. [verde] Registra el consumo de tokens de la unidad con `./abm tokens estimate --unit <id> <archivos>`, o `record` si hay telemetría.
3. [verde] Actualiza `implementation/task_tracker.md` (estado) y `docs/work_log.md` (qué se hizo, evidencia del quality gate).
4. [verde] Actualiza `docs/project_memory.md`: última unidad completada, siguiente unidad, bloqueos.
5. [amarillo] Resuelve o traslada a la cola cualquier pendiente abierto que bloquee el cierre.
6. [verde] Emite el reporte de cierre de unidad según el protocolo de salida.

## Salidas
- `task_tracker.md`, `work_log.md`, `project_memory.md` y el ledger de tokens, todos al día.

## Gates
Sin deriva sin resolver; sin pendiente de tipo credencial o bloqueante abierto; reporte emitido.

## Fallback
Recorre la misma lista a mano, archivo por archivo.

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
`./abm tokens estimate --unit <id> <archivos> --json`; `./abm pending list --json` para verificar pendientes abiertos.
