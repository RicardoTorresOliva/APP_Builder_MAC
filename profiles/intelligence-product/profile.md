---
type: Asset Profile
title: intelligence-product
description: Híbrido de consultoría: informe argumentado respaldado por un dataset o dashboard validado.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: extendido
composes: [research-report, data-product]
---

# Perfil: intelligence-product (compuesto)

Informe argumentado **+** dataset o dashboard validado, entregados juntos. Hereda por referencia de `research-report` y `data-product`; aquí solo va el pegamento. Nivel del Contrato ADS: el mayor de los compuestos (`extendido`).

## Qué se hereda (por referencia)
- De `research-report`: design docs de argumento, completitud de lectura, gate de citas y cero invención.
- De `data-product`: design docs de datos, completitud de consulta, gate de esquema, datos personales y procedencia.
- `stack_candidates`, `tooling_candidates`, `knowledge_bundles`: unión de ambos.

## Pegamento
- El informe **cita el dataset**: toda afirmación basada en datos referencia una vista o cifra validada.
- El dashboard **respalda el informe**: toda cifra titular es reproducible desde el producto de datos (Attested Computation OKF).
- Definiciones compartidas: una métrica nombrada en el informe usa la misma definición que el bundle `metric-definitions`.

## Gobierno por DU (`governed_by`)
```
FU-01  "Reunir fuentes + ingerir datos"         governed_by: research-report + data-product
DU-03  "Dataset: señales de mercado"            governed_by: data-product
DU-05  "Dashboard: explorador de señales"       governed_by: data-product
DU-08  "Sección: panorama competitivo"          governed_by: research-report
DU-11  "Sección: recomendación + tesis"         governed_by: research-report
```

## deliverable_format
- Un paquete: informe + dataset + dashboard + resumen ejecutivo de una página

## publication_step
- Exportar el informe + cargar el dataset con controles de acceso + revisión editorial
