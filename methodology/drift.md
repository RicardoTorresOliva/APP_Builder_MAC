---
type: Methodology
title: Control de deriva (drift)
description: Qué compara `drift`, cuándo corre y cómo propone actualizar intención, spec, contratos y código.
tags: [metodologia, drift, sincronia]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Control de deriva

Todo modo metodológico corre el riesgo de que el artefacto de intención se separe del código real
(*technical drift*, señalado para `IDD` en el Anexo A). `/drift` es el mecanismo que lo detecta y
propone la corrección; el `closeout` de cada FU/DU lo obliga.

## Qué compara

| Modo | Compara | Contra |
|---|---|---|
| IDD | `intent.md` (Propósito/Usuario/Medios, restricciones, criterios de éxito, no-objetivos) | El código y sus ADRs ligeros |
| SDD | `requirements.md` / `design.md` / `tasks.md` | El código y la matriz `TASK↔REQ↔TEST` |
| SPDD | `prompt-contract.md` (entradas, salidas, invariantes) | Los archivos vinculados y sus tests de aceptación |
| AIDD | El artefacto que produjo `consolidate` (intención o spec) | El código construido en la fase de revisión humana |

VIBE no se compara: su salida es `explore-log.md`, no un artefacto que deba mantenerse sincronizado.

## Cuándo corre

- **Obligatorio** en el `closeout.md` de cada FU/DU (regla 6 de `AGENTS.md`): no se cierra una unidad
  con intención/spec/contrato y código en desacuerdo.
- **Bajo demanda**, vía el comando `drift`, en cualquier punto (por ejemplo antes de una revisión o de
  un `handoff.md`).
- **Tras un `iterate`**: un cambio post-entrega puede introducir drift si no actualiza el artefacto de
  origen; `drift` lo señala antes de considerar la iteración terminada.

## Cómo propone actualizaciones

1. Extrae del código las señales observables (endpoints, campos, invariantes reales) y las contrasta
   con lo declarado en el artefacto de intención/spec/contrato.
2. Por cada discrepancia, propone **una de dos direcciones**, nunca ambas en silencio:
   - actualizar el artefacto para reflejar una decisión de diseño legítima tomada durante la construcción, o
   - señalar el código como una desviación no autorizada de la intención/spec, para corregirlo.
3. Las discrepancias de confianza baja (texto libre, sin un `REQ`/invariante explícito que comparar) van
   a `abm pending add` para que un humano decida la dirección.
4. El resultado queda registrado en `docs/work_log.md` de la unidad, nunca se aplica en silencio.

## Qué bloquea el closeout

- SDD: cualquier `REQ` sin `TASK`/`TEST` que lo cubra, o cualquier `TASK` sin `REQ`.
- SPDD: cualquier invariante del contrato roto por el código, o una versión de contrato sin subir tras
  un cambio incompatible.
- IDD/AIDD: un criterio de éxito de `intent.md` que el código no cumple, sin que se haya actualizado
  `intent.md` para reflejar el cambio de alcance.

## Ver también

`/methodology/idd.md` · `/methodology/sdd.md` · `/methodology/spdd.md` · `/methodology/aidd.md` ·
`/templates/closeout.md` · `/docs/adr/0006-router-metodologico.md`
