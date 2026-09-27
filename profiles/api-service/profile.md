---
type: Asset Profile
title: api-service
description: Servicio o herramienta consumida por programas o agentes (API, CLI o servidor MCP) sin UI propia.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: extendido
---

# Perfil: api-service

ADS cuyo consumidor es **un programa o un agente**: API HTTP, CLI, servidor MCP, SDK o worker. Sin interfaz de usuario propia. ABM mismo usa este perfil.

## design_docs
- api_contracts: OpenAPI / esquema de tools MCP / sintaxis de CLI, errores problem+json, versionado — [HIGH]
- data_model: si persiste datos — [HIGH]
- architecture: componentes, dependencias, límites, idempotencia — [MEDIUM]
- operations: SLO/SLI, rate limits, observabilidad, costos por llamada (incl. tokens) — [MEDIUM]

## foundation_unit_examples
- Scaffolding del servicio y del contrato (OpenAPI o esquema MCP primero)
- Capa de datos, autenticación de clientes y agentes (scopes mínimos)
- Observabilidad y ledger de tokens

## deliverable_unit_completeness
Un DU (endpoint, tool MCP u orden de CLI) está hecho solo si:
- está en el contrato (OpenAPI / `tools/list` / `--help`) y en `ads.yaml → capabilities`;
- un cliente real lo invoca de punta a punta (test de contrato o `./abm agent-conformance`);
- valida entradas, es idempotente donde aplica y devuelve errores estructurados;
- las operaciones destructivas exigen confirmación humana (`hitl_actions`) y quedan auditadas;
- tiene tests unitarios, de integración y de contrato.

## quality_gate
- `standards/backend/`, `standards/agentic/`, `standards/security/`
- Descripciones de tools cortas y `readOnlyHint`/`destructiveHint` correctos
- Rate limits y límites de payload declarados
- `./abm ads-check` y `./abm agent-conformance` en verde

## deliverable_format
- Repositorio desplegable o paquete distribuible + contrato publicado + skill `operate-<id>`

## publication_step
- Publicación del paquete o despliegue del servicio (categoría elegida en planificación)

## stack_candidates
- lenguaje + framework de API o de CLI · almacenamiento si aplica · despliegue (contenedores, serverless o paquete)
- Catálogo: `stacks/cases/api-backend.md`, `stacks/cases/cli-extensions.md`

## tooling_candidates
- generador de clientes desde OpenAPI · servidor MCP de pruebas · skill `api-builder`

## knowledge_bundles
- api-conventions/<estilo> (nombres, paginación, errores, versionado)
