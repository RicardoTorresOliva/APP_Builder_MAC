---
type: Profile Contract
title: Contrato de perfiles de ADS
description: Esquema que todo perfil de ADS debe seguir y reglas de composición de perfiles híbridos.
tags: [perfil, contrato]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:52:17Z }
version: "2.0"
---

# Contrato de perfiles de ADS

Un **perfil** le dice al núcleo de ABM cómo producir un *tipo* de ADS. El núcleo (`AGENTS.md`) es constante; el perfil trae todo lo específico del tipo. Cada ADS elige un perfil (o uno compuesto) en `init-project` y lo registra en `abm.yaml → active_profile`.

## Reglas de todo perfil
1. **Sin nombres de productos comerciales**: solo categorías (regla 7; lo verifica `abm lint core`). Los productos aparecen en `stacks/` durante la exploración de stack.
2. **`stack_candidates` son sugerencias, nunca defaults**: la elección es humana (`stack`).
3. **`tooling_candidates` se evalúan por costo**: una herramienta se instala solo si ahorra más contexto/tokens del que cuesta.
4. **`knowledge_bundles` se montan, no se incrustan**: bundles OKF en `knowledge/` o ejemplos etiquetados.
5. **El perfil declara comportamiento; no repite reglas de `AGENTS.md`.**

## Campos obligatorios
```markdown
---
type: Asset Profile
title: <nombre-del-perfil>
description: <una frase>
tags: [perfil, ads]
status: stable
generated: { by: <actor>, at: <ISO 8601 UTC> }
ads_contract_level: minimo | extendido     # nivel mínimo del Contrato ADS (contract/README.md)
---
# Perfil: <nombre>

## design_docs              # documentos de diseño y nivel de detalle [HIGH | MEDIUM | LIGHT]
## foundation_unit_examples # FU típicas
## deliverable_unit_completeness  # qué es "hecho" para un DU: de punta a punta, incluida la operación por agentes
## quality_gate             # checklist por unidad y auditoría final (o referencia a standards/)
## deliverable_format       # qué se entrega
## publication_step         # CATEGORÍA, nunca producto
## stack_candidates         # categorías a explorar + casos de stacks/cases/
## tooling_candidates       # skills/MCP a evaluar por costo
## knowledge_bundles        # bundles OKF a montar
```

## Cómo consume el núcleo un perfil
- `init-project` lo elige, explora el stack desde `stack_candidates` y crea `ads.yaml` con el nivel de contrato del perfil.
- `review` aplica `quality_gate` y `deliverable_unit_completeness`.
- `abm ads-check` exige que `ads.yaml → contract_level` no sea menor que `ads_contract_level`.
- Cambiar de perfil es una decisión de diseño: regístrala en `docs/decision_log.md`.

## Composición (híbridos)
Un híbrido no copia campos: **compone** perfiles atómicos y aporta solo el pegamento.

```markdown
---
type: Asset Profile
title: intelligence-product
ads_contract_level: extendido               # el mayor de los perfiles compuestos
composes: [research-report, data-product]   # referencias, nunca copias
---
```

Cada DU declara qué capacidad lo gobierna con `governed_by:` (p. ej. `DU-04 governed_by: research-report`).

**Resolución:**
- `design_docs`, `foundation_unit_examples`, `stack_candidates`, `tooling_candidates`, `knowledge_bundles` → **unión** de los compuestos.
- `deliverable_unit_completeness` y `quality_gate` → **por DU**, según su `governed_by`.
- `deliverable_format`, `publication_step` → los declara el pegamento.
- `ads_contract_level` → el **mayor** de los compuestos.

## Perfiles incluidos
| Perfil | Tipo de ADS | Nivel de contrato |
|---|---|---|
| `software-app` | Software con interfaz (web, móvil, escritorio, dashboard, ERP) | extendido |
| `api-service` | API, CLI o servidor MCP consumido por programas o agentes | extendido |
| `data-product` | Dataset, pipeline, capa de métricas o dashboard que se consulta | extendido |
| `automation-integration` | Flujos entre sistemas, automatizaciones, agentes de proceso | extendido |
| `research-report` | Documento que se lee, argumentado con fuentes | minimo |
| `intelligence-product` | Compuesto: informe + dataset/dashboard (consultoría) | extendido |
