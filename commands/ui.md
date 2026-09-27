---
type: Playbook
title: ui — construye la interfaz
description: Construye la capa de interfaz de una unidad siguiendo el standard de frontend y su quality gate.
args: "[<unidad>]"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# ui

## Propósito

Construye la capa de interfaz de una unidad con paridad frente a backend y datos, siguiendo el standard de frontend del núcleo.

## Cuándo usarlo

- La unidad tiene una superficie de interacción: pantalla, formulario, componente.

## Entradas

- Design doc de la unidad.
- `standards/frontend/{standard,checklist-dod,review-criteria,testing}.md`.
- Skill `frontend-builder`; rol `agents/frontend.md`.

## Pasos

1. [verde] Lee el design doc y `standards/frontend/standard.md` antes de construir.
2. [verde] Implementa siguiendo el standard; usa la skill `frontend-builder` si está activa.
3. [verde] Cubre estados vacíos, de carga y de error — no solo el camino feliz.
4. [amarillo] Verifica accesibilidad básica (contraste, foco, etiquetas) antes de marcar la unidad como hecha.
5. [verde] Aplica `standards/frontend/checklist-dod.md` como quality gate.
6. [verde] Verifica de punta a punta con el consumidor real (persona o agente) antes de cerrar.

## Salidas

- Interfaz de la unidad.
- Evidencia del checklist-dod en `work_log.md`.

## Gates

`standards/frontend/checklist-dod.md` cumplido; sin datos ficticios visibles en la entrega final.

## Fallback

Sin skill dedicada, sigue `standards/frontend/standard.md` paso a paso.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `standards/frontend/checklist-dod.md` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm tokens estimate --unit ui-<id> <archivos> --json`; skill `frontend-builder` si la herramienta la soporta.
