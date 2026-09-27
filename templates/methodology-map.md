---
type: Template
title: methodology-map.md — mezcla metodológica por módulo
description: Tabla módulo | modo | justificación | revisión | disparadores, salida de abm methodology classify.
tags: [template, methodology-map, router]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Mapa metodológico: `<ADS>`

Salida de `abm methodology classify` por módulo (`/methodology/router.md`). Un módulo reclasifica si
durante la construcción aparece un disparador de escalamiento o si `/drift` señala que ya no aplica.

| Módulo | Modo | Justificación | Revisión | Disparadores |
|---|---|---|---|---|
| `<módulo>` | `VIBE\|IDD\|SDD\|SPDD\|AIDD` | `<regla o disparador que ganó, de router.yaml>` | `<opcional\|recomendada\|humana obligatoria>` | `<ninguno\|payments\|auth\|personal-data\|health\|regulated>` |

<!-- Una fila por módulo. Ver el ejemplo del mini-ERP en /methodology/mixing.md. -->

## Clasificación

| Campo | Valor |
|---|---|
| Ceremonia del ADS | `<prototipo\|mvp\|producto\|enterprise-regulado>` (`/methodology/ceremony.md`) |
| Clasificado por | `<abm methodology classify --json \| humano>` |
| Confianza (si inferido de texto libre) | `<valor de decide; <0.60 → abm pending add>` |
| Fecha | `<ISO 8601>` |

## Reclasificaciones

| Módulo | De | A | Motivo | Fecha |
|---|---|---|---|---|
| `<módulo>` | `<modo anterior>` | `<modo nuevo>` | `<disparador o cambio de dimensión>` | `<ISO 8601>` |
