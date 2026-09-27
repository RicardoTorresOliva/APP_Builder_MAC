---
type: Template
title: intent.md — árbol de intención (IDD)
description: Minimum Viable Spec de IDD — Propósito → Usuario → Medios, restricciones, criterios de éxito y no-objetivos.
tags: [template, idd, intent]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Intención: `<módulo o ADS>`

Modo: IDD (`/methodology/idd.md`). No describe el "cómo": eso lo decide el agente y lo registra en
`adr.md`. Si aparece un disparador de escalamiento (pagos, auth, datos personales/salud, regulación),
reclasifica a SDD (`/methodology/router.md`) antes de continuar.

## Árbol de intención

### Propósito
`<por qué existe este módulo; qué problema real resuelve, en una frase>`

### Usuario
- Para quién: `<rol o persona concreta, no "todos"`
- Situación en la que lo necesita: `<contexto de uso>`

### Medios
- `<qué capacidad concreta lo logra — no la implementación, la capacidad>`
- `<otra capacidad, si aplica>`

## Restricciones
- `<técnica, de negocio o de plazo que el agente no puede cruzar>`

## Criterios de éxito (medibles)
- `<criterio verificable, no "funciona bien" — p. ej. "el usuario completa X en menos de Y pasos">`

## No-objetivos
- `<algo que explícitamente NO se construye ahora, para evitar alcance implícito>`

## Estado

| Campo | Valor |
|---|---|
| Clasificado por | `<abm methodology classify \| humano>` |
| Confianza | `<1.0 si determinista; valor de decide si inferido>` |
| ADRs ligeros de esta unidad | `<enlaces a adr.md creados durante la construcción>` |

Al cerrar: `/templates/closeout.md` confirma que el código cumple esta intención o la actualiza.
