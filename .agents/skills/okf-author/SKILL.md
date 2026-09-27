---
name: okf-author
description: Cómo escribir un documento Markdown conforme a OKF v0.2 + perfil ABM — frontmatter, sources y notas al pie, stale_after, la convención generated/verified, index.md y log.md. Actívala cada vez que vayas a crear o editar un .md fuera de un SKILL.md (que sigue Agent Skills, no OKF).
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# okf-author

Todo `.md` de ABM (menos `skills/*/SKILL.md`) es un concepto OKF v0.2 con el perfil ABM. Frontmatter
mínimo:

```yaml
---
type: <Playbook | Standard | Checklist | Methodology | Template | Agent Role | Stack Sheet |
       Integration Guide | Reference | ...>
title: <título>
description: <una frase>
tags: [<etiquetas>]
status: stable   # o draft
generated: { by: <actor>, at: <ISO 8601 UTC> }
---
```

## Convención de actor (`generated.by`, `verified.by`)
Uno de: `human:<id>` (una persona), `process:<id>` (un pipeline), o `<herramienta>/<contexto>`
(p. ej. `claude-code/web`). `at` siempre ISO 8601 con zona (`Z` o `±HH:MM`).

## Cuándo añadir más
- **Caduca** (versiones, precios, productos, APIs de terceros): añade `stale_after: <ISO UTC, ~3
  meses>` y `sources: [{id, resource: <URL>, title}]`. Cita cada afirmación derivada de una fuente
  con `[^id]`, definida al final como `[^id]: <título>`. Los tipos **Stack Sheet, Research,
  Pricing y Compat Matrix EXIGEN** `stale_after`.
- **Verificado por otro actor además de quien lo generó**: añade `verified: {by, at}` (o una lista).

## Reglas duras
- `type` es obligatorio y no vacío. `status` ∈ {draft, stable, deprecated}. Nunca `timestamp`
  (v0.1): usa `generated.at`.
- Toda nota al pie referenciada (`[^id]`) necesita su definición; si citas una fuente, el `id`
  debe existir en `sources`.
- Enlaces internos con forma `/ruta/archivo.md` relativa a la raíz del repo; solo enlaza lo que
  existe o lo que tú vas a crear en la misma unidad.
- `index.md` no lleva frontmatter (salvo `okf_version` en el de la raíz); `log.md` no lleva
  frontmatter y sus encabezados `##` son fechas `YYYY-MM-DD`.
- Lo no verificable en la fuente oficial se marca `no-verificado` en el cuerpo, nunca se inventa
  (regla 14 de `AGENTS.md`).

## Comandos
- `./abm okf validate [rutas]` — 0 errores antes de cerrar. `--spec-only` para solo la spec sin el
  perfil ABM.
- `./abm okf index` — regenera el `index.md` raíz (mapa de contexto); `--check` para verificar sin
  escribir.

## Excepción: SKILL.md
`skills/<name>/SKILL.md` sigue el estándar Agent Skills, no OKF: frontmatter **solo** `name`
(= carpeta), `description`, `license`, `metadata`. El detalle OKF completo va en
`skills/<name>/references/*.md`.

## Detalle extra
`references/ejemplo-completo.md`: un documento con `sources`, notas al pie y `stale_after`
resueltos de punta a punta.
