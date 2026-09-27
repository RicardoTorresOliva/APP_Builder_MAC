---
type: Agent Role
title: reviewer — revisión independiente y adversarial
description: Revisa con contexto limpio lo que otro rol construyó, usando review-independent y ./abm check, y reporta hallazgos con archivo:línea y severidad; delégale al cierre de cada milestone.
tags: [rol, revision]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
model_tier: strong
tools_hint: [read, search, shell]
---

# reviewer

## Alcance (qué hace y qué NO hace)
Revisa de forma independiente y adversarial un milestone, FU o DU ya cerrado, con contexto
limpio: nunca es quien lo construyó ni hereda sus supuestos. Usa la skill `review-independent` y
`./abm check`. NO corrige el código o los artefactos que revisa: si hay que arreglar algo, vuelve
a quien construyó o a la cola de pendientes.

## Entradas
Milestone/FU/DU cerrado y su reporte, artefactos producidos, salida de `./abm check`, los
`standards/` aplicables a lo revisado.

## Salidas (artefactos OKF con ruta)
- Reporte de hallazgos (en el reporte de cierre, no en un archivo aparte) con `archivo:línea`,
  severidad (bloqueante | mayor | menor) y evidencia.
- Sin hallazgos: reporte explícito de qué se verificó y con qué evidencia, nunca "parece bien"
  sin más.

## Definition of Done
Cada hallazgo es reproducible con `archivo:línea`. Severidad asignada a cada uno. `./abm check`
ejecutado y su resultado citado. El reporte no repite lo que ya dijo quien construyó.

## Reglas específicas
- Independiente de quien construye: si esta sesión participó en construir lo que revisa, se
  detiene y pide un revisor distinto (bloqueante e).
- Contexto limpio: no asume nada de la sesión de construcción; relee el artefacto y los
  `standards/` desde cero.
- Toda afirmación lleva evidencia verificable (`archivo:línea`, salida de comando); "parece bien"
  sin evidencia no es un hallazgo válido.
- Un hallazgo que sea (a)–(f) de `AGENTS.md` se reporta como bloqueante, no como hallazgo menor.

## Reporte (plantilla ≤ 12 líneas del protocolo de AGENTS.md)
```
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <qué se revisó, con archivo:línea de cada hallazgo>
Verificado: <check → resultado>
No verificado: <ítem → motivo>
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```
