---
type: Methodology
title: Niveles de ceremonia
description: Prototipo, MVP, Producto y Enterprise-Regulado — modo por defecto, gates, Contrato ADS y dashboard de tokens.
tags: [metodologia, ceremonia, ads-contract, tokens]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Niveles de ceremonia

La ceremonia (`abm.yaml → ceremony`) fija cuánto rigor aplica un ADS por defecto: el modo metodológico
de partida, el nivel del Contrato ADS (`/docs/adr/0009-contrato-ads.md`), el nivel del dashboard de
tokens (`/docs/adr/0013-espacio-de-tokens.md`) y si el Planning Gate se acumula en la cola o bloquea
(`/docs/adr/0014-turbo-y-pendientes.md`). El router (`/methodology/router.md`) puede escalar un módulo
puntual por encima de este default; nunca por debajo de un disparador de escalamiento.

## Los cuatro niveles

| Nivel | Modo por defecto | Contrato ADS | Dashboard de tokens | Revisión | Planning Gate |
|---|---|---|---|---|---|
| **Prototipo** | VIBE | mínimo | N1 (`TOKENS.md`) | opcional | acumulado |
| **MVP** | IDD | mínimo | N1 (`TOKENS.md`) | recomendada | acumulado |
| **Producto** | IDD | extendido | N2 (dashboard HTML) | obligatoria en módulos críticos | acumulado |
| **Enterprise-Regulado** | SDD | extendido | N3 (pipeline OTel) | humana obligatoria | bloqueante |

Valores exactos (identificadores que consume el CLI): `/methodology/router.yaml → ceremony`.

## Por qué el default de Producto sigue siendo IDD

Un ADS en ceremonia `producto` no fuerza `SDD` en todos sus módulos: la mayoría de la lógica de negocio
sigue siendo mejor servida por `IDD` (menos ceremonia, se adapta a requisitos cambiantes). Lo que sube
es el **nivel de contrato y de observabilidad de tokens** del ADS completo, y los módulos que activan un
disparador de escalamiento (`/methodology/router.md`) sí pasan a `SDD` con revisión humana. Ver el
ejemplo del mini-ERP en `/methodology/mixing.md`.

## Por qué Enterprise-Regulado sí fuerza SDD por defecto

En este nivel se asume que casi cualquier módulo puede tocar un dominio regulado, así que el default es
el más riguroso; un módulo puede desescalar explícitamente solo si el router confirma que ningún
disparador aplica. Además, el Planning Gate es **bloqueante** (no se acumula en la cola: el humano
aprueba antes de construir) y la capa de gobernanza opcional aplica (`/methodology/governance-regulated.md`).

## Gates comunes a los cuatro niveles

- Quality gate del perfil activo tras cada FU/DU (regla 3 de `AGENTS.md`).
- `closeout.md` de cada unidad sincroniza intención/spec/contrato/código (`/methodology/drift.md`).
- `abm ads-check` verifica que el ADS cumple el nivel de Contrato ADS de su ceremonia.

## Ver también

`/methodology/router.md` · `/methodology/router.yaml` · `/methodology/mixing.md` ·
`/docs/adr/0006-router-metodologico.md` · `/docs/adr/0009-contrato-ads.md` ·
`/docs/adr/0013-espacio-de-tokens.md` · `/docs/adr/0014-turbo-y-pendientes.md`
