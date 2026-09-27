---
type: Playbook
title: db — construye el modelo de datos
description: Modela y migra el esquema de datos de una unidad con migraciones reversibles.
args: "[<unidad>]"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# db

## Propósito

Modela o evoluciona el esquema de datos de una unidad, con migraciones reversibles y el gate de gobernanza de datos del perfil.

## Cuándo usarlo

- La unidad crea, modifica o consume el modelo de datos.

## Entradas

- Design doc de la unidad.
- `standards/database/{standard,checklist-dod,review-criteria,testing}.md`.
- Skill `db-builder`; rol `agents/data.md`.

## Pasos

1. [verde] Modela el esquema desde el design doc; documenta relaciones y restricciones.
2. [amarillo] Toda migración se escribe con su reversa (subir/bajar) antes de aplicarla.
3. [verde] Aplica el gate de gobernanza de datos del perfil (clasificación de datos sensibles) antes de sembrar datos de ejemplo.
4. [verde] Usa la skill `db-builder` si está activa; sigue `standards/database/standard.md`.
5. [rojo] Aplicar una migración irreversible o borrar datos fuera de la rama de trabajo es bloqueante (a).
6. [verde] Aplica `standards/database/checklist-dod.md`; verifica escalabilidad básica (índices, N+1) si el perfil lo exige.

## Salidas

- Esquema y migraciones de la unidad.
- Evidencia del checklist-dod.

## Gates

Toda migración es reversible, o queda documentada como no reversible con aprobación explícita; datos sensibles nunca en el repo.

## Fallback

Sin skill dedicada, sigue `standards/database/standard.md` y escribe las migraciones a mano.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `standards/database/checklist-dod.md` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm tokens estimate --unit db-<id> <archivos> --json`; skill `db-builder` si la herramienta la soporta.
