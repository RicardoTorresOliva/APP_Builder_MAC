---
type: Template
title: explore-log.md — aprendizajes de VIBE
description: Registro de una exploración desechable y la recomendación de modo siguiente para consolidate.
tags: [template, vibe, explore-log]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Log de exploración: `<pregunta que se quería responder>`

Modo: VIBE (`/methodology/vibe.md`) · Rama sandbox: `<nombre>` · Tiempo acotado: `<duración>`

## Qué se probó

`<qué se construyó o intentó, sin ceremonia>`

## Qué se aprendió

- `<aprendizaje concreto, aunque sea "esto no funciona porque...">`

## Qué se descarta

`<qué parte del código de exploración no se lleva a la rama principal>`

## Disparadores de escalamiento detectados durante la exploración

`<ninguno | payments | auth | personal-data | health | regulated>` — si hay alguno, `consolidate` debe
producir SDD, no IDD (`/methodology/router.md`).

## Recomendación para consolidate

| Campo | Valor |
|---|---|
| Modo siguiente recomendado | `IDD \| SDD` |
| Por qué | `<...>` |
| Artefacto a crear | `intent.md \| requirements.md + design.md + tasks.md` |
