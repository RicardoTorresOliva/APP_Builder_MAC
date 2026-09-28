---
type: Playbook
title: consolidate — lleva lo aprendido a diseño real
description: Convierte los aprendizajes de un explore en spec y diseño definitivos (IDD/SDD).
args: "[<tema>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# consolidate

## Propósito

Traslada lo aprendido en un `explore` a IDD/SDD real: diseño e implementación definitivos, con la calidad del modo metodológico asignado, no la del sandbox.

## Cuándo usarlo

- Después de un `explore` que ya respondió su pregunta.

## Entradas

- `docs/explore-log/<tema>.md`.

## Pasos

1. [verde] Extrae del explore-log lo que sirve: decisiones validadas, descartadas y por qué.
2. [verde] Redacta o actualiza la spec (`spec`) y el design doc con lo aprendido; no copies el código del sandbox tal cual.
3. [amarillo] Reescribe con el nivel de calidad del modo metodológico asignado (IDD/SDD), no el del sandbox.
4. [verde] Actualiza `methodology-map.md` si el modo del módulo cambia tras lo aprendido.
5. [verde] Descarta o archiva la rama sandbox; documenta la decisión en `docs/work_log.md`.

## Salidas

- Spec y design doc actualizados.
- `docs/work_log.md`.

## Gates

Nada de código sandbox pasa a producción sin este paso.

## Fallback

Escribe un resumen de "qué cambia en el diseño real" y aplícalo a mano.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate docs/spec` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook".
