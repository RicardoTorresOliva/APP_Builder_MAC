---
type: Methodology
title: "SPDD — Spec-as-Prompt-Contract Development"
description: Contrato de prompt versionado, sincronizado en ambos sentidos con el código.
tags: [metodologia, spdd, prompt-contract]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# SPDD (Spec-as-Prompt-Contract Development)

## Qué es

La spec vive como un **contrato de prompt versionado** (`prompt-contract.md`): versión, intención,
entradas, salidas, invariantes, tests de aceptación y archivos vinculados. Es un contrato vivo entre
humano y agente, sincronizado en **ambos sentidos** con el código: si el código cambia, el contrato se
actualiza; si el contrato cambia, el código se regenera o ajusta.

## Cuándo sí / cuándo no

- **Sí:** módulos con mucha autonomía del agente que van a seguir cambiando (no son un prototipo
  desechable) y donde una spec tipo `SDD` se desactualizaría rápido — típicamente lógica agéntica,
  prompts de producto, flujos que el agente reconfigura seguido.
- **No:** módulo con disparador de escalamiento (usa `SDD` con revisión humana), o exploración puntual
  sin continuidad (usa `VIBE`).

## Artefactos

- `/templates/prompt-contract.md` — versión, intención, entradas/salidas, invariantes, tests de
  aceptación, archivos vinculados.
- `/templates/adr.md` para decisiones que cambian el contrato de forma incompatible.

## Flujo paso a paso

1. Completar `prompt-contract.md` v1: intención, entradas/salidas esperadas, invariantes que nunca
   deben romperse, tests de aceptación y qué archivos de código implementan el contrato.
2. Implementar el código que cumple el contrato; enlazarlo en `archivos vinculados`.
3. Cada cambio de código que afecte entradas, salidas o invariantes sube la versión del contrato.
4. Cada cambio de intención en el contrato dispara una revisión del código enlazado antes de cerrar.
5. `/drift` compara contrato vs. código en cada unidad; un desacuerdo bloquea el `closeout` hasta
   resolverse en un sentido o el otro (no se permite que queden desincronizados).

## Gates y nivel de revisión

- Gate de sincronía bidireccional: no se cierra una unidad SPDD con el contrato y el código en
  desacuerdo (`/methodology/drift.md`).
- Revisión según ceremonia; si el módulo escala por un disparador durante el ciclo, pasa a `SDD`
  con revisión humana obligatoria.

## Salida obligatoria

`prompt-contract.md` actualizado a la versión vigente, con sus tests de aceptación pasando, y
`closeout.md` confirmando la sincronía contrato↔código.

## Riesgos y cómo se controlan

- **El contrato queda "de adorno" y el código se desvía:** el gate de sincronía en el `closeout` es
  obligatorio, no opcional; `/drift` lo verifica antes de dar por cerrada la unidad.
- **Versión de contrato sin subir tras un cambio incompatible:** cada test de aceptación roto exige
  subir versión o revertir el cambio, nunca dejarlo silencioso.
- **Se usa SPDD para evitar la revisión humana de un módulo crítico:** los disparadores de escalamiento
  de `/methodology/router.md` tienen prioridad sobre SPDD; no son evitables por elección de modo.
