---
type: Reference
title: Tools y recursos del servidor MCP de ABM
description: Inventario generado desde scripts/abmkit/mcp_server.py; no editar a mano.
tags: [mcp, referencia, generado]
status: stable
generated: { by: process:abm-sync, at: 2026-01-01T00:00:00Z }
---

# Tools y recursos del servidor MCP de ABM

<!-- GENERADO por abm sync desde scripts/abmkit/mcp_server.py. No editar. -->
Servidor: `python3 scripts/abm.py mcp` · protocolo 2025-11-25 · ABM 5.0.0. `*` = argumento obligatorio.
Escritura: `dry_run=true` por defecto. Destructiva: además `confirm=true` con confirmación humana.

| Tool | Tipo | Argumentos | Descripción |
|---|---|---|---|
| `abm_doctor` | lectura | — | Diagnóstico del entorno: herramienta, SO y dependencias. |
| `abm_check` | lectura | only | Ejecuta los validadores de ABM (OKF, enlaces, presupuesto, secretos, sync, contrato, lints). |
| `abm_okf_validate` | lectura | paths | Valida OKF v0.2 + perfil ABM en rutas o en todo el repo. |
| `abm_ads_check` | lectura | path | Verifica el Contrato ADS (ads.yaml) de este repo o de una ruta. |
| `abm_links` | lectura | — | Verifica enlaces internos de markdown. |
| `abm_token_budget` | lectura | — | Mide tokens por archivo contra el presupuesto. |
| `abm_lint` | lectura | kind* | Lints: core (sin productos), playbooks, manual o skills. |
| `abm_methodology_classify` | lectura | text, file | Clasifica un encargo y propone modo metodológico por módulo. |
| `abm_decide` | escritura | state*, questions*, provider | Decisión tipada (choice/score/boolean) con confianza; capa System One con fallback. |
| `abm_pending_list` | lectura | all | Lista la cola de pendientes. |
| `abm_pending_add` | escritura | type*, context*, default*, alternative, impact, dry_run | Añade un pendiente con su default aplicado. |
| `abm_tokens_summary` | lectura | — | Resumen del espacio de tokens (sin escribir). |
| `abm_tokens_report` | escritura | dry_run | Genera el reporte N1 (TOKENS.md) desde el ledger. |
| `abm_tokens_record` | escritura | phase, source, input*, output*, model, provider, unit, feature, dry_run | Registra un evento de consumo de tokens en el ledger. |
| `abm_sync` | destructiva | check, dry_run, confirm | Genera o verifica los adaptadores; puede borrar salidas huérfanas (destructiva: dry_run y confirm). |

| Recurso | Contenido |
|---|---|
| `abm://tokens/summary` | Resumen del consumo de tokens y presupuestos |
| `abm://pending` | Cola de pendientes abiertos |
| `abm://ads` | Manifiesto del Contrato ADS (ads.yaml) |
