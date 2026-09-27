---
type: Specification
title: Perfil ABM sobre OKF v0.2
description: Reglas de productor de ABM sobre el Open Knowledge Format (OKF) v0.2; más estrictas que la spec, nunca contrarias.
tags: [okf, perfil, especificacion]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:31:52Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format (OKF) v0.2
  - id: okf-blog-v02
    resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
    title: OKF v0.2 adds trust signals
---

# Perfil ABM sobre OKF v0.2

Norma base: OKF v0.2[^okf-spec]. Este perfil añade requisitos; no contradice la spec. Decisión: `/docs/adr/0004-okf.md`. Validación: `./abm okf validate` (nivel spec con `--spec-only`).

## Bundle

- La raíz del repo es la raíz del bundle. `index.md` raíz lo genera `./abm okf index` (lleva `okf_version: "0.2"`) y es el mapa de contexto del repo.
- `log.md` raíz: encabezados `## YYYY-MM-DD`, entradas más recientes primero, sin frontmatter.
- `knowledge/` es un sub-bundle montable con su propio `index.md` y `log.md`.
- **Fuera del bundle** (`abm.yaml → okf.exclude`): salidas generadas de adaptadores (`.claude/`, `.agents/`, `.github/`, `CLAUDE.md`…) y los `SKILL.md` (el estándar Agent Skills no admite claves extra de primer nivel; su tipo va en `metadata.okf_type`).

## Frontmatter

| Campo | Spec | Perfil ABM |
|---|---|---|
| `type` | obligatorio | obligatorio (Title Case: `Playbook`, `Standard`, `ADR`…) |
| `title`, `description` | recomendados | obligatorios |
| `tags` | opcional | recomendado |
| `status` | opcional (`draft`/`stable`/`deprecated`) | obligatorio |
| `generated: { by, at }` | opcional | obligatorio; `by` con convención de actores |
| `verified` | opcional | solo si hubo verificación real; sin él, el concepto es `no-verificado` |
| `sources` | opcional | obligatorio si hay afirmaciones externas; cada afirmación con nota al pie `[^id]` |
| `stale_after` | opcional | obligatorio en `Compat Matrix`, `Stack Sheet`, `Research`, `Pricing` |
| `timestamp` | obsoleto (v0.1) | prohibido: usa `generated.at` |

- **Actores:** `<herramienta>/<versión>` para agentes y herramientas, `human:<id>` para personas, `process:<id>` para procesos. Lo escrito o confirmado por una persona lleva `human:`.
- **Fechas:** ISO 8601 con zona (`2026-09-28T00:00:00Z`).
- **Enlaces:** `/ruta.md` (relativa a la raíz del bundle = raíz del repo; también resuelve en la web del repo). Relativos permitidos.
- **Caducidad:** `./abm okf validate` avisa si `now >= stale_after`; falla en los tipos de `okf.critical_stale_types`.
- **Cifras sancionadas:** concepto `type: Attested Computation` (spec §10) con `runtime`, `parameters`, `executor` y `attester` deterministas (p. ej. costos de tokens: `./abm tokens attest`).

## Subconjunto YAML

El CLI usa un parser sin dependencias (`scripts/abmkit/yamlmini.py`): mapas y listas por indentación, listas `[a, b]` y mapas `{k: v}` en línea, escalares con o sin comillas, bloques `|` y `>`, comentarios. Las fechas se leen como texto. No uses anclas, etiquetas ni varios documentos.

## Migración desde la convención v4.1

- `timestamp` → `generated.at` · `status: stub` → `status: draft` + etiqueta `stub` · lista de citas → `sources` + notas al pie.
- Interoperabilidad con `conocimiento/` de AGE_Builder: un consumidor v0.2 acepta bundles v0.1[^okf-blog-v02].

[^okf-spec]: Open Knowledge Format (OKF) v0.2
[^okf-blog-v02]: OKF v0.2 adds trust signals
