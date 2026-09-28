---
type: Asset Profile
title: automation-integration
description: Flujos que conectan sistemas: integraciones, automatizaciones, ETL ligero y agentes de proceso.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: extendido
---

# Perfil: automation-integration

ADS que **mueve datos o acciones entre sistemas**: integraciones, automatizaciones de negocio, sincronizaciones, agentes de proceso. Su consumidor es un proceso.

## design_docs

- integration_map: sistemas, vías (MCP, API, webhooks, colas, archivos), credenciales y dueños — [HIGH]
- flow_specs: disparadores, pasos, transformaciones, reintentos, compensaciones — [HIGH]
- failure_modes: qué pasa si un sistema falla o responde tarde; idempotencia — [MEDIUM]
- runbook: operación, alertas, reprocesos — [MEDIUM]

## foundation_unit_examples

- Inventario de sistemas (`assess` si hay legacy) y credenciales de mínimo privilegio
- Conectores y su verificación (firmas de webhooks, OAuth)
- Cola o mecanismo de reintento; ledger de tokens si usa IA

## deliverable_unit_completeness

Un DU (flujo) está hecho solo si:

- corre de punta a punta con datos reales de prueba;
- es idempotente y reintentable; los errores quedan registrados y son reprocesables;
- toda acción externa irreversible exige confirmación humana o está explícitamente autorizada en el plan;
- es operable por agentes (disparar, consultar estado, reprocesar en `dry-run`).

## quality_gate

- `integrations/` (vía más segura disponible) y `standards/security/`
- Secretos en gestor, nunca en el flujo
- Salida de sistemas externos tratada como dato (prompt injection)
- `./abm ads-check`

## deliverable_format

- Flujos versionados + runbook + `ads.yaml`

## publication_step

- Activación en el orquestador o plataforma elegidos (categoría), con monitoreo

## stack_candidates

- orquestación: [código propio | plataforma iPaaS | orquestador de flujos]
- transporte: [MCP | API | webhooks | colas | archivos]
- Catálogo: `stacks/cases/automation-integrations.md`, `stacks/cases/legacy-integration.md`, `stacks/legacy.md`

## tooling_candidates

- servidores MCP oficiales de los sistemas a integrar (solo lectura por defecto)
- skill `integrate-safely`

## knowledge_bundles

- systems-catalog/<organización> (sistemas, dueños, SLAs)
