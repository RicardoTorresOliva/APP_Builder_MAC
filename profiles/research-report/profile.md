---
type: Asset Profile
title: research-report
description: Documento que se lee: conocimiento sintetizado y argumentado desde fuentes citadas.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: minimo
---

# Perfil: research-report

ADS que se **lee**: análisis de mercado, due diligence, white paper de estrategia, revisión de literatura.

## design_docs

- outline: estructura del argumento por sección — [HIGH]
- thesis: tesis central y qué la probaría o refutaría — [HIGH]
- source_map: catálogo de fuentes con notas de credibilidad (`sources` OKF) — [MEDIUM]
- evidence_table: afirmación → fuente(s) → fuerza — [MEDIUM]
- style_guide: voz, formato de citas, convenciones — [LIGHT]

## foundation_unit_examples

- Encuadrar la pregunta de investigación y el alcance
- Reunir y validar fuentes; construir la base de evidencia
- Esqueleto del argumento (outline + tesis)

## deliverable_unit_completeness

Un DU (sección o capítulo) está hecho solo si:

- se lee con coherencia de principio a fin;
- toda afirmación tiene fuente (nota al pie ligada a `sources`), sin afirmaciones huérfanas;
- está contrastado con las fuentes y encaja con la tesis;
- las preguntas abiertas están señaladas, no ocultas;
- el documento es OKF y lo puede navegar un agente (índice + `llms.txt`).

## quality_gate

- Integridad de citas: cada afirmación trazable a una fuente real
- Credibilidad de fuentes: sin fuentes circulares o de baja calidad
- Cero invención: ni datos, ni citas, ni estadísticas inventadas
- Balance: contraposiciones relevantes representadas
- Exactitud de cifras y nombres; consistencia interna

## deliverable_format

- Documento (markdown / procesador de texto / PDF) en OKF; opcionalmente un resumen ejecutivo

## publication_step

- Exportar al formato elegido + pasada de revisión editorial

## stack_candidates

- autoría: [markdown primero | procesador de texto primero]
- citas: [en línea | notas al pie | gestor de referencias]
- render: [generador de documentos]
- Catálogo: `stacks/cases/intelligence-product.md`

## tooling_candidates

- servidor MCP de búsqueda/investigación web
- skill de citas y verificación de hechos
- skill de generación de documentos

## knowledge_bundles

- editorial-standards/<estilo-de-la-casa>
- domain-context/<tema>
