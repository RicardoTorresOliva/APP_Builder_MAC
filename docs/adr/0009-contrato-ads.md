---
type: ADR
title: "ADR 0009 — Contrato ADS"
description: Requisitos verificables que cumple todo ADS y ABM mismo.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0009 — Contrato ADS

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto
Los ADS producidos no tenían identidad, superficie agéntica ni control de tokens exigibles.

## Decisión
- Manifiesto **`ads.yaml`** en la raíz de cada ADS; su forma se documenta en `contract/ads.schema.json` y `contract/README.md`.
- **Niveles:** `minimo` (todo ADS) y `extendido` (software, datos, IA). Cada perfil declara `ads_contract_level`; el manifiesto puede subirlo, nunca bajarlo.
- **Mínimo:** identidad (id, semver, perfil, dueño, capacidades con modo read/write/destructive), `AGENTS.md`, skill de operación, `llms.txt`, índice OKF, ledger + reporte de tokens (N1), portabilidad declarada, secretos fuera del repo.
- **Extendido:** + servidor MCP, CLI `--json` o API OpenAPI, dashboard N2/N3 con presupuestos, log de auditoría de acciones de agentes, HITL en capacidades destructivas, plan de salida por proveedor.
- **`abm ads-check`** (estático) + **`abm agent-conformance`** (dinámico) en CI.

## Consecuencias
- ABM mismo cumple el nivel `extendido`: si no lo cumple, su CI falla.

## Alternativas descartadas
- Checklist en prosa: no es verificable por máquina.
