---
type: Specification
title: Contrato ADS
description: Requisitos verificables que cumple todo ADS (y ABM), por nivel, declarados en ads.yaml.
tags: [contrato, ads, agentes, tokens]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:33:33Z }
---

# Contrato ADS

Todo ADS declara un manifiesto `ads.yaml` en su raíz (plantilla: `templates/agentic/ads.yaml`; forma: `/contract/ads.schema.json`). Decisión: `/docs/adr/0009-contrato-ads.md`.

## Niveles

El perfil fija el mínimo (`ads_contract_level` en su frontmatter); `ads.yaml → contract_level` puede subirlo, nunca bajarlo.

| Requisito | `minimo` (todo ADS) | `extendido` (software, datos, IA) |
|---|---|---|
| Identidad | `id` kebab-case, `version` semver, `profile`, `owner`, `description`, `capabilities` (modo read/write/destructive) | + SLO y entornos si aplica |
| Gobernanza del agente | `AGENTS.md` del ADS con turbo y protocolo de salida | + adaptadores generados (`abm sync`) |
| Superficie agéntica | skill `operate-<id>`, `llms.txt`, índice OKF | + servidor MCP (`endpoints.mcp`), CLI `--json` o API OpenAPI, errores `application/problem+json`, A2A solo si es agente |
| Espacio de tokens | ledger + reporte N1 (`TOKENS.md`) | dashboard N2 o N3 + `tokens.budgets` |
| Portabilidad | lenguajes y proveedores LLM declarados | + gateway LLM, IaC, matriz de nube, `exit_plan` |
| Seguridad | secretos por entorno o gestor | + `agent_audit_log`; toda capacidad `destructive` en `hitl_actions` |
| Documentación | OKF | + manual de operación para personas y agentes |

## Verificación

- `./abm ads-check [ruta]`: estático; valida `ads.yaml`, niveles y que existan los archivos declarados.
- `./abm agent-conformance [--server "<cmd>"]`: dinámico; un cliente MCP descubre, lista capacidades, ejecuta una lectura y un `dry-run` y consulta `abm://tokens/summary` o equivalente.
- Ambos corren en `./abm check` y en CI.

## Eventos de tokens

Esquema: `/contract/token-event.schema.json`. Mapeo a OpenTelemetry GenAI (estado Development): `input_tokens` → `gen_ai.usage.input_tokens`, `output_tokens` → `gen_ai.usage.output_tokens`, `cache_read_tokens` → `gen_ai.usage.cache_read.input_tokens`, `provider` → `gen_ai.provider.name`, `model` → `gen_ai.request.model`, `command` → `gen_ai.operation.name`.
