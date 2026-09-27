---
type: Playbook
title: test — pirámide de pruebas
description: Verifica la unidad con la pirámide de pruebas del perfil, priorizando rutas críticas.
args: "[<unidad>]"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# test

## Propósito

Verifica una unidad con la pirámide de pruebas que exige su perfil y su criticidad, priorizando siempre las rutas críticas sobre la cobertura total.

## Cuándo usarlo

- Al cerrar cada unidad.
- Siempre antes de `review`.

## Entradas

- `standards/testing/` (pirámide, criterios por capa).

## Pasos

1. [verde] Cubre unidad, integración y end-to-end según lo exija el perfil y la criticidad del módulo.
2. [verde] Prioriza rutas críticas: caminos felices, estados vacíos, estados de error.
3. [amarillo] Si el módulo escaló a SDD (pagos, auth, datos personales o de salud, regulación), exige revisión humana de los tests críticos.
4. [verde] Ejecuta la suite y registra el resultado en `docs/work_log.md`.
5. [rojo] Ningún test que toque producción, pagos reales o datos personales reales corre sin confirmación explícita.

## Salidas

- Suite de tests de la unidad.
- Resultado registrado en `work_log.md`.

## Gates

Rutas críticas cubiertas antes de marcar la unidad como hecha; ningún test rojo sin explicar por qué.

## Fallback

Sin runner automatizado, verifica manualmente cada ruta crítica y documenta el resultado igual.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: suite de tests de la unidad → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook"; registra tokens con `./abm tokens estimate --unit test-<id> <archivos>`.
