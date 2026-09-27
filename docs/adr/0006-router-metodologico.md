---
type: ADR
title: "ADR 0006 — Router metodológico"
description: Cómo elige y mezcla ABM Vibe, IDD, SDD, SPDD y AIDD por encargo y por módulo.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0006 — Router metodológico

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
No hay una metodología óptima para todo (Anexo A). ABM hoy solo tiene SDD implícito.

## Decisión
- **Seis dimensiones** puntuadas 0–2: incertidumbre, criticidad/riesgo, horizonte, tamaño del equipo, brownfield, autonomía deseada.
- **Reglas deterministas** (`methodology/router.md`) asignan un modo por módulo; **disparadores de escalamiento** (dinero, auth, datos personales o de salud, regulación) fuerzan SDD con revisión humana; **desescalamiento** para prototipos desechables y herramientas internas de bajo riesgo.
- **Mezcla por módulo** en `methodology-map.md` (modo + justificación + nivel de revisión).
- **Niveles de ceremonia** (Prototipo, MVP, Producto, Enterprise-Regulado) fijan modo por defecto, gates, nivel del Contrato ADS y nivel del dashboard de tokens.
- `abm methodology classify` aplica las reglas; si la entrada es texto libre, infiere las dimensiones con la capa System One (ADR 0011) y manda a la cola lo que tenga confianza baja.

## Consecuencias
- El modo es explícito y auditable por módulo; `/drift` vigila la sincronía intención/spec/contratos/código.

## Alternativas descartadas
- Un modo único por proyecto: sobre-ceremonia en módulos triviales y sub-ceremonia en los críticos.
