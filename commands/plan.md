---
type: Playbook
title: plan — publica el plan de ejecución
description: Ordena FU y DU en el tracker, redacta el plan y lo publica para su aprobación o cola.
args: "[<milestone>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# plan

## Propósito

Produce y publica el plan de ejecución de una unidad o milestone: nada se construye sin este paso (regla 1 de AGENTS.md).

## Cuándo usarlo

- Tras `spec` o `intent`, antes de `start-execution`.

## Entradas

- `implementation/user_units.md`, `implementation/task_tracker.md`.
- `templates/plan.md`.

## Pasos

1. [verde] Agrupa las FU primero, luego las DU por milestone, en `implementation/task_tracker.md`.
2. [verde] Redacta el plan (`templates/plan.md`): alcance, orden, riesgos, criterio de éxito por unidad.
3. [verde] Publica el plan.
4. [amarillo] En turbo (default): "Aprobar plan" entra en la cola (`./abm pending add`) y la ejecución reversible en rama continúa.
5. [rojo] En modo checkpoint, ceremonia Enterprise-Regulado, o ante un bloqueante: espera aprobación explícita antes de ejecutar.

## Salidas

- `implementation/task_tracker.md`.
- Plan publicado.

## Gates

Plan publicado antes de `start-execution`; aprobación explícita esperada solo en los casos del paso 5.

## Fallback

Comparte el plan como documento y pide luz verde por el canal que uses.

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

`./abm pending add --type approval --json` para encolar la aprobación; "lee y ejecuta este playbook" para el resto.
