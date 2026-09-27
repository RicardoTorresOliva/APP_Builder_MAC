---
type: Reference
title: Servidor MCP de ABM — inventario de tools
description: Mapeo 1:1 entre órdenes del CLI abm y las tools abm_* del servidor MCP, con hints y un flujo de ejemplo.
tags: [referencia, mcp, operate-abm]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Servidor MCP de ABM

`./abm mcp` expone un servidor MCP stdio (protocolo base `2025-11-25`, ADR 0010) con una tool por
orden del CLI. El nombre sustituye espacios/subcomandos por guiones bajos: `abm <a> <b>` →
`abm_<a>_<b>`.

## Tools de lectura (`readOnlyHint: true`)

| Tool | Orden equivalente | Notas |
|---|---|---|
| `abm_okf_validate` | `okf validate [paths]` | Acepta rutas; sin rutas valida todo el bundle. |
| `abm_links` | `links` | Enlaces internos rotos. |
| `abm_token_budget` | `token-budget` | Tokens estimados vs presupuesto por archivo. |
| `abm_lint` | `lint core\|playbooks\|manual` | `kind` obligatorio. |
| `abm_check` | `check` | Auditoría agregada de solo lectura. |
| `abm_doctor` | `doctor` | Diagnóstico del entorno. |
| `abm_ads_check` | `ads-check` | Estático, contra `ads.yaml`. |
| `abm_tokens_report` | `tokens report` | Genera/lee `TOKENS.md` (N1). |
| `abm_tokens_dashboard` | `tokens dashboard` | N2, HTML estático. |
| `abm_tokens_budget` | `tokens budget` | Falla si hay tope duro superado. |
| `abm_pending_list` | `pending list` | Cola de pendientes actual. |
| `abm_methodology_classify` | `methodology classify` | Clasifica encargo/módulo. |
| `abm_decide` | `decide` | Capa System One; ver skill `system-one`. |

## Tools de escritura (`destructiveHint` según corresponda, `dry_run=true` por defecto)

| Tool | Orden equivalente | Qué escribe |
|---|---|---|
| `abm_okf_index` | `okf index` | `index.md` raíz. |
| `abm_sync` | `sync [--apply-turbo]` | Adaptadores por herramienta. |
| `abm_pending_add` | `pending add` | Nueva fila en la cola. |
| `abm_pending_resolve` | `pending resolve` | Cierra un pendiente. |
| `abm_tokens_record` | `tokens record` | Evento en el ledger JSONL. |
| `abm_tokens_estimate` | `tokens estimate` | Evento estimado en el ledger. |
| `abm_tokens_attest` | `tokens attest` | `Attested Computation`, determinista. |
| `abm_new_ads` | `new-ads` | Scaffolding de un ADS nuevo. |
| `abm_agent_conformance` | `agent-conformance` | Corre el guion dinámico; no persiste nada salvo log. |
| `abm_secrets` | `secrets` | Reporta hallazgos; no modifica archivos. |

`destructiveHint: true` solo en tools que puedan sobrescribir o borrar contenido existente
(`abm_sync`, `abm_new_ads`); el resto son `destructiveHint: false` porque solo añaden filas o
regeneran contenido derivado.

## Recurso

`abm://tokens/summary` — resumen de consumo de solo lectura, sin credenciales de escritura,
pensado para que un agente orquestador externo lea presupuesto restante sin invocar una tool.

## Flujo de ejemplo (agente externo operando un ADS hecho con ABM)

1. Descubrir: listar tools del servidor MCP del ADS (no de ABM).
2. Listar: `abm_pending_list` / equivalente del ADS para ver qué falta.
3. Leer: `abm_okf_validate` o el recurso de tokens, sin escribir nada.
4. `--dry-run`: cualquier tool de escritura con `dry_run=true` para ver el efecto antes de aplicar.
5. Tokens: leer `abm://tokens/summary` antes de decidir si hay presupuesto para seguir.

Esto es exactamente lo que ejecuta `abm agent-conformance` de forma automática y determinista.
