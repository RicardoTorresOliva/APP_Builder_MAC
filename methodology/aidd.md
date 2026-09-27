---
type: Methodology
title: "AIDD — híbrido explorar/consolidar/construir"
description: Explorar en VIBE, consolidar en IDD o SDD, construir con revisión humana obligatoria, cerrar.
tags: [metodologia, aidd, hibrido]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# AIDD (híbrido)

## Qué es
Combina los otros modos en secuencia: **explorar** con `VIBE` → **consolidar** en `IDD` o `SDD` →
**construir** con revisión humana obligatoria → `closeout`. Da la velocidad de explorar sin la
improvisación de quedarse en modo exploratorio, y sin la burocracia de escribir una spec formal antes
de saber qué se está construyendo.

## Cuándo sí / cuándo no
- **Sí:** incertidumbre alta sobre qué construir, pero con intención de llegar a algo que se usa de
  verdad (no un descarte), y autonomía alta del agente durante la fase de exploración.
- **No:** si ya hay claridad sobre la solución (usa `IDD` o `SDD` directo, saltarse la fase de exploración
  ahorra tiempo); o si un disparador de escalamiento está presente desde el inicio (la fase de
  exploración también debe respetar `review: human` si toca datos sensibles o dinero, o se hace en un
  entorno completamente aislado sin datos reales).

## Artefactos
Los de cada fase, en orden: `/templates/explore-log.md` (explorar) → `/templates/intent.md` o
`/templates/spec/requirements.md` + `design.md` + `tasks.md` (consolidar, según lo que decida
`consolidate`) → `/templates/adr.md` durante la construcción → `/templates/closeout.md` al final.

## Flujo paso a paso
1. **Explorar (VIBE):** rama sandbox, tiempo acotado, `explore-log.md` con los aprendizajes.
2. **Consolidar:** `/consolidate` decide si el aprendizaje se formaliza en `intent.md` (IDD) o en
   `requirements.md`/`design.md`/`tasks.md` (SDD), según si apareció un disparador de escalamiento o el
   riesgo subió durante la exploración.
3. **Construir con revisión humana obligatoria:** el agente implementa siguiendo el artefacto consolidado;
   a diferencia de IDD/SDD normales, aquí la revisión humana **no es opcional**, sea cual sea la ceremonia.
4. **Cerrar:** `closeout.md` confirma la sincronía intención/spec↔código y registra qué se aprendió en
   la fase de exploración que cambió el resultado final.

## Gates y nivel de revisión
- Revisión humana **obligatoria** en la fase de construcción, sin excepción de ceremonia (es la única
  diferencia dura frente a usar IDD o SDD "puro").
- Gate de transición: no se pasa a "construir" sin que `consolidate` haya producido el artefacto formal
  (no se construye directo sobre el código de exploración).

## Salida obligatoria
`explore-log.md` + el artefacto de consolidación (`intent.md` o spec completa) + `closeout.md` con la
revisión humana registrada.

## Riesgos y cómo se controlan
- **Se salta la consolidación y se construye sobre el código de exploración:** el gate de transición lo
  bloquea; sin `intent.md` o spec formal no hay `plan.md` que autorice `start-execution`.
- **La revisión humana se trata como opcional "porque el proyecto es turbo":** AIDD la fija como
  obligatoria en el propio modo, no depende de `abm.yaml → mode`.
- **Caos por mezclar fases sin orden:** el flujo es lineal (explorar → consolidar → construir → cerrar);
  saltarse un paso es tratado como drift y lo detecta `/methodology/drift.md`.
