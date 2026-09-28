---
type: Playbook
title: methodology — clasifica el modo metodológico
description: Asigna VIBE, IDD, SDD, SPDD o AIDD a un módulo según sus seis dimensiones de riesgo.
args: "[<módulo>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# methodology

## Propósito

Asigna el modo metodológico de un módulo (VIBE/IDD/SDD/SPDD/AIDD) con reglas deterministas por dimensión, para que la ceremonia de cada parte del ADS sea proporcional a su riesgo.

## Cuándo usarlo

- Al planificar un módulo nuevo.
- Cuando `drift` detecta que el modo asignado ya no encaja.

## Entradas

- Descripción del módulo.
- `methodology-map.md` existente.
- `integrations/decision/thresholds.yaml`.

## Pasos

1. [verde] Ejecuta `./abm methodology classify` con las seis dimensiones (incertidumbre, criticidad, horizonte, tamaño de equipo, brownfield, autonomía) o con texto libre.
2. [amarillo] Si es texto libre, la capa System One infiere las dimensiones; lo de confianza baja va a la cola con `./abm pending add`.
3. [verde] Aplica los disparadores de escalamiento (pagos, auth, datos personales o de salud, regulación) → fuerzan SDD con revisión humana.
4. [verde] Aplica el desescalamiento cuando corresponda (prototipo desechable, herramienta interna de bajo riesgo).
5. [verde] Registra el modo, la justificación y el nivel de revisión en `methodology-map.md`.

## Salidas

- `methodology-map.md` actualizado.

## Gates

Todo módulo tiene un modo asignado y justificado antes de construirse.

## Fallback

Aplica a mano la tabla de reglas de `methodology/router.md`.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm methodology classify` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm methodology classify --json`; MCP `abm_methodology_classify`.
