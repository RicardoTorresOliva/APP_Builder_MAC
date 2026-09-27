---
type: Playbook
title: fix — corrige un bug
description: Reproduce el bug, escribe el test que falla, aplica el cambio mínimo y verifica sin regresión.
args: "[<bug>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# fix

## Propósito
Corrige un bug reproducible con el flujo mínimo verificable: reproducir, test que falla, cambio mínimo, verificación sin regresión.

## Cuándo usarlo
- El ADS tiene un comportamiento incorrecto y reproducible.

## Entradas
- Reporte del bug o comportamiento observado.

## Pasos
1. [verde] Reproduce el bug de forma determinista antes de tocar código.
2. [verde] Escribe un test que falle exactamente por esta causa (evidencia de que el bug existe).
3. [amarillo] Aplica el cambio mínimo que hace pasar el test, sin aprovechar para refactorizar de paso.
4. [verde] Verifica que el test nuevo pasa y que la suite existente sigue en verde (sin regresión).
5. [rojo] Si el fix requiere tocar datos ya guardados en producción, es bloqueante (a): necesita un plan de migración aparte.
6. [verde] Documenta la causa raíz y el fix en `docs/work_log.md`.

## Salidas
- Test de regresión nuevo.
- Fix aplicado.
- Entrada en `work_log.md`.

## Gates
El test que reproduce el bug existe y pasa; la suite completa está en verde antes de cerrar.

## Fallback
Sin runner de tests, verifica manualmente el antes y el después, y documenta ambos.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: suite de tests → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
"lee y ejecuta este playbook"; registra tokens con `./abm tokens estimate --unit fix-<id> <archivos>`.
