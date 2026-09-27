---
type: Playbook
title: refactor — mejora la estructura sin cambiar comportamiento
description: Reestructura código manteniendo la suite de tests en verde antes y después, sin cambiar comportamiento.
args: "[<unidad>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# refactor

## Propósito
Mejora la estructura interna del código sin cambiar su comportamiento observable, verificando la suite de tests antes y después.

## Cuándo usarlo
- El código funciona pero su forma dificulta el siguiente cambio.

## Entradas
- La unidad a refactorizar.
- Su suite de tests existente.

## Pasos
1. [verde] Verifica que la suite de tests existente está en verde antes de empezar (línea base).
2. [verde] Si la cobertura de la ruta a tocar es insuficiente, añade tests de caracterización antes de refactorizar.
3. [amarillo] Aplica el refactor en pasos pequeños y reversibles; confirma cada paso que deja la suite en verde.
4. [verde] Verifica que la suite sigue en verde después de cada paso — ningún comportamiento cambia.
5. [rojo] Si el refactor termina cambiando comportamiento observable, detente: eso es una unidad nueva, no un refactor, y necesita su propio spec-delta.
6. [verde] Documenta el refactor y por qué en `docs/work_log.md`.

## Salidas
- Código reestructurado.
- Suite de tests en verde antes y después.
- Entrada en `work_log.md`.

## Gates
Comportamiento observable idéntico; suite en verde antes y después.

## Fallback
Sin runner de tests, verifica manualmente los mismos casos antes y después del refactor.

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
"lee y ejecuta este playbook".
