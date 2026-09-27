---
type: Playbook
title: review — revisión independiente
description: Lanza un revisor con contexto limpio que verifica la última unidad o milestone completado.
args: ""
tags: [comando, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# review

## Propósito
Lanza una revisión independiente, con contexto limpio, de la última unidad o milestone completado — nunca la hace quien construyó.

## Cuándo usarlo
- Tras cada milestone.
- Siempre antes de `closeout`.

## Entradas
- `implementation/task_tracker.md`, `implementation/user_units.md`.
- Perfil activo.

## Pasos
1. [verde] Lanza el revisor con contexto limpio — nunca quien construyó la unidad.
2. [verde] Lee `task_tracker.md` y `user_units.md`; identifica unidades completadas y su criterio de aceptación.
3. [verde] Verifica que cada DU cumple la regla de completitud del perfil de punta a punta, con un consumidor real.
4. [verde] Ejecuta `./abm check` (todos los validadores) e interpreta los resultados.
5. [verde] Busca huecos: estados vacíos o de error faltantes, navegación rota, afirmaciones sin respaldo, datos sin validar.
6. [amarillo] Escribe los hallazgos en `docs/work_log.md` bajo "## Review", con severidad y recomendación.
7. [rojo] Si hay un hallazgo crítico, detén el avance a trabajo nuevo hasta corregirlo.

## Salidas
- Entrada "## Review" en `docs/work_log.md`.

## Gates
`./abm check` sin errores duros; hallazgos críticos resueltos antes de seguir.

## Fallback
Pide a otra persona o sesión que revise con los mismos 5 puntos, sin ver cómo se construyó.

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
`./abm check --json`.
