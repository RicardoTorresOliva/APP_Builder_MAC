---
type: Playbook
title: start-execution — ejecución autónoma
description: Verifica que el plan esté listo y ejecuta las FU y DU aprobadas hasta la entrega.
args: ""
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# start-execution

## Propósito

Ejecuta de forma autónoma el plan ya publicado (y aprobado o en cola reversible): primero las FU, luego las DU por milestone, con el quality gate del perfil en cada unidad.

## Cuándo usarlo

- El plan está publicado y, según ADR 0014, aprobado o en cola con ejecución reversible habilitada.

## Entradas

- `implementation/task_tracker.md`, `implementation/user_units.md`, `docs/project_memory.md`.

## Pasos

1. [verde] Verifica el readiness con `./abm preflight` (user_units, task_tracker, knowledge/index, project_memory, perfil activo, `ads.yaml`); si falla, completa el plan antes de construir.
2. [verde] Ejecuta primero todas las FU en el orden del tracker.
3. [verde] Ejecuta luego las DU por milestone; aplica la regla de completitud y el quality gate del perfil activo (o del `governed_by` de la unidad si el perfil es compuesto).
4. [amarillo] Tras cada unidad: `closeout` (actualiza `task_tracker.md` y `work_log.md`, registra tokens con `./abm tokens record` o `estimate`) y verifica con `./abm units`.
5. [verde] Tras cada milestone: ejecuta `review` con contexto limpio y registra sus hallazgos.
6. [rojo] Detente solo ante un bloqueante de `AGENTS.md` (a–f), p. ej. requisito ambiguo sin default razonable o decisiones contradictorias. Integración que falla, complejidad mayor a la planeada o cambio de alcance → `./abm pending add` con el default aplicado y sigue con lo independiente.
7. [verde] Antes de entregar: datos de ejemplo realistas, todo renderiza o corre, estados vacíos y de error cubiertos, auditoría final del perfil, riesgos residuales en `work_log.md`.

## Salidas

- Unidades construidas.
- `task_tracker.md`, `work_log.md` y ledger de tokens actualizados.

## Gates

Quality gate del perfil por unidad; auditoría holística antes de entregar; ninguna FU/DU se da por hecha sin uso de punta a punta (regla 5).

## Fallback

Sigue el mismo orden a mano, verificando cada punto de la lista de readiness antes de construir.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm check` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm tokens estimate --unit <id> <archivos> --json`; "lee y ejecuta este playbook" para el flujo completo.
