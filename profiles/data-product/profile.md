---
type: Asset Profile
title: data-product
description: Datos que se consultan: dataset validado, pipeline, capa de métricas o dashboard.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: extendido
---

# Perfil: data-product

ADS que se **consulta**: datos refinados y consultables (dataset validado, pipeline, dashboard, capa de métricas).

## design_docs

- data_sources: origen, método de acceso, frecuencia de refresco — [HIGH]
- schema: tablas, campos, tipos (diccionario de datos) — [HIGH]
- lineage: cómo cada salida se traza a sus fuentes — [HIGH]
- transformation_logic: limpieza, joins, derivaciones, definición de métricas (Attested Computation OKF para cifras sancionadas) — [MEDIUM]
- exposure_contract: cómo se consulta (vistas, API, dashboard, MCP) — [MEDIUM]

## foundation_unit_examples

- Ingesta desde fuentes
- Esquema y almacenamiento
- Pipeline de limpieza y transformación
- Capa de acceso (vistas, API, servidor MCP de solo lectura)

## deliverable_unit_completeness

Un DU (dataset, vista o dashboard) está hecho solo si:

- los datos están validados (nulos, duplicados, rangos, integridad);
- el esquema está documentado y el linaje es trazable;
- no hay fuga de datos personales; se cumple la gobernanza de datos;
- el consumidor (persona o agente) lo consulta de punta a punta;
- es reproducible: re-ejecutar el pipeline da el mismo resultado.

## quality_gate

- Corrección de esquema y calidad de datos
- Datos personales y cumplimiento: campos sensibles enmascarados según política
- Procedencia intacta; pipeline determinista y documentado
- Cada métrica definida sin ambigüedad (una sola fuente de verdad)
- `standards/database/` y `./abm ads-check`

## deliverable_format

- Dataset + dashboard o notebook + diccionario de datos + acceso para agentes

## publication_step

- Carga en un almacén de datos + controles de acceso

## stack_candidates

- almacenamiento: [data warehouse relacional | lakehouse | documental]
- pipeline: [batch | streaming | guiado por notebooks]
- exposición: [vistas SQL | API | dashboard de BI | notebook | servidor MCP]
- Catálogo: `stacks/cases/internal-dashboard-bi.md`

## tooling_candidates

- servidor MCP de base de datos o warehouse (solo lectura)
- skill de perfilado de datos
- skill de visualización

## knowledge_bundles

- data-governance/<política> · metric-definitions/<dominio> · schema-conventions/<estilo>
