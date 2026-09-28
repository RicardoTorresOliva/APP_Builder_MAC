---
type: Template
title: design.md — diseño técnico (SDD)
description: Diseño que satisface los requisitos de requirements.md, referenciando cada REQ-NNN.
tags: [template, sdd, design]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Diseño: `<módulo>`

Modo: SDD (`/methodology/sdd.md`). Responde a `requirements.md`; cada decisión referencia el `REQ-NNN`
que satisface. Decisiones de arquitectura no triviales van a `/templates/adr.md`.

## Resumen de la solución

`<2-3 frases: qué se construye y cómo satisface los requisitos, sin detalle de implementación>`

## Componentes

| Componente | Responsabilidad | REQ que satisface |
|---|---|---|
| `<componente>` | `<qué hace>` | `REQ-001, REQ-002` |

## Datos

`<modelo de datos relevante, o referencia a un ERD si existe en design_docs del perfil>`

## Interfaces

`<contratos de entrada/salida entre componentes o hacia afuera — endpoints, eventos, colas>`

## Casos límite y errores

- `<caso límite>` → `<comportamiento esperado>` (`REQ-NNN`)

## Decisiones registradas

- `<decisión no trivial>` → `/templates/adr.md#<slug>`

## Trazabilidad

Todo `REQ-NNN` de `requirements.md` debe aparecer aquí al menos una vez. Lo que este diseño cubre pasa
a `tasks.md` como tareas concretas.
