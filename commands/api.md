---
type: Playbook
title: api — construye el servicio
description: Construye la capa de API/servicio de una unidad con contrato de errores y quality gate.
args: "[<unidad>]"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# api

## Propósito

Construye la capa de servicio o API de una unidad, con contrato explícito y errores estructurados, siguiendo el standard de backend del núcleo.

## Cuándo usarlo

- La unidad expone o consume una interfaz de servicio.

## Entradas

- Design doc de la unidad.
- `standards/backend/{standard,checklist-dod,review-criteria,testing}.md`.
- Skill `api-builder`; rol `agents/backend.md`.

## Pasos

1. [verde] Define el contrato de la API (rutas, esquema, errores) antes de implementar.
2. [verde] Implementa siguiendo `standards/backend/standard.md`; usa la skill `api-builder` si está activa.
3. [verde] Usa errores estructurados y accionables (formato `problem+json`, RFC 9457) y operaciones idempotentes donde aplique.
4. [amarillo] Verifica autenticación y autorización mínimas antes de exponer la API fuera de la rama.
5. [verde] Aplica `standards/backend/checklist-dod.md`; incluye tests de rutas críticas si el perfil lo exige.
6. [rojo] Exponer la API fuera del entorno de desarrollo (dominio público, credenciales reales) es bloqueante (b).

## Salidas

- API de la unidad.
- Contrato documentado.
- Evidencia del checklist-dod.

## Gates

`standards/backend/checklist-dod.md` cumplido; contrato de errores consistente en toda la unidad.

## Fallback

Sin skill dedicada, sigue `standards/backend/standard.md` paso a paso.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `standards/backend/checklist-dod.md` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm tokens estimate --unit api-<id> <archivos> --json`; skill `api-builder` si la herramienta la soporta.
