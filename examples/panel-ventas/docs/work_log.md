---
type: Work Log
title: Registro de trabajo — panel de ventas
description: Registro por unidad del panel de ventas con lo producido, el quality gate aplicado, la evidencia y los riesgos residuales.
tags: [work-log, quality-gate, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:10:47Z }
---

# Work log

Quality gate del perfil `software-app`: DoD de `standards/frontend`, `standards/backend` y `standards/database` de ABM,
seguridad OWASP, problem+json, WCAG 2.2 AA y `ads-check` + `agent-conformance`. Tokens: estimados (caracteres/4) en
`ops/tokens/ledger.jsonl`; totales en [TOKENS.md](../TOKENS.md).

## PLAN — init-project

- Producido: [encargo](../START_PROJECT.md), [requisitos EARS](../planning/requirements.md), [mapa metodológico](../planning/methodology-map.md)
  (`./abm methodology classify`: SDD en los 3 módulos), design docs, [unidades](../implementation/user_units.md), [decisiones](decision_log.md), `ads.yaml`.
- Gate: cada REQ mapea a una FU/DU y a un test; stack encolado (P-002) por ser elección HITL; `ads.yaml` al nivel del perfil.
- Tokens: out ≈ 6 952 · in ≈ 20 856 (estimado).

## FU-01 — capa de datos

- Producido: `app/db.py` (migraciones 1–2 up/down, seeds idempotentes, reglas de negocio), `tests/test_db.py`.
- Gate DoD database: ERD Mermaid ✔ · migración reversible probada up/down/up ✔ · seeds idempotentes ✔ · FK, UNIQUE y CHECK ✔ ·
  índices en filtros del resumen ✔ · auditoría de altas y bajas ✔ · lecturas en modo solo lectura ✔ · tests 11/11 ✔.
  No aplica: RLS y multi-tenant (una base por equipo). Pendiente: backup/restauración probados (solo documentado).
- Tokens: out ≈ 7 691 · in ≈ 23 073.

## FU-02 — identidad y servidor

- Producido: `app/server.py` (PBKDF2 600 000 it. con sal por usuario, sesión opaca HttpOnly + SameSite=Strict, CSRF, `Origin`,
  límite 5 intentos/15 min, CSP estricta, problem+json), `tests/test_auth.py`.
- Gate DoD backend: contrato OpenAPI ✔ · problem+json con `type/title/status/detail` ✔ · auth/authz declarada por ruta ✔ ·
  rate limit en login ✔ · mutación idempotente con `Idempotency-Key` ✔ · logs JSON con id de petición ✔. No aplica: jobs asíncronos,
  caché. No verificado: trazas OpenTelemetry (fuera del alcance sin dependencias).
- Hallazgo corregido: con `Referrer-Policy: no-referrer` el navegador envía `Origin: null` y el login fallaba (403); pasa a `same-origin`.
- Tokens: out ≈ 5 853 · in ≈ 17 559.

## FU-03 — superficie agéntica base

- Producido: `ads.yaml` (extendido), `AGENTS.md`, skill `operate-panel-ventas`, `ops/mcp_server.py` (desde la plantilla de ABM), `abm.yaml`, `.env.example`.
- Gate: `./abm ads-check` → 0 errores.
- Tokens: out ≈ 4 160 · in ≈ 12 480.

## DU-01 — registrar, listar y borrar ventas

- Uso de punta a punta: vendedor registra desde el formulario y la venta aparece primera en la tabla; admin borra con confirmación.
- Gate: permisos por rol, CSRF, `Origin`, 415/413/400/422/404, idempotencia, inyección SQL tratada como dato, borrado auditado → `tests/test_api.py` 20/20 ✔.
- Tokens: out ≈ 2 678 · in ≈ 8 034.

## DU-02 — dashboard

- Producido: `app/static/app.js` y `app.css`: KPIs, columnas por mes, barras por vendedor, tooltip por puntero y teclado, tabla, tema oscuro, estados.
- Gate DoD frontend (verificado en navegador sin interfaz): sin errores de consola ✔ · claro y oscuro ✔ · estado vacío ✔ · validación en
  cliente y servidor con error por campo sin perder valores ✔ · 390 px sin scroll horizontal ✔ (hallazgo corregido: `.sr-only` desbordaba) ·
  textos de datos con `textContent` ✔. No verificado: Core Web Vitals medidos e i18n externalizada (textos en español en el código).
- Tokens: out ≈ 5 461 · in ≈ 16 383.

## DU-03 — operación por agentes

- Producido: `app/cli.py` (`--json`, `--dry-run`, `--confirm`), tools MCP `status`, `ventas_resumen`, `crear_venta`, `borrar_venta`, manual de operación, `ops/smoke_e2e.py`, `run_checks.sh`.
- Gate: `tests/test_mcp.py` 6/6 ✔ · `./abm agent-conformance` OK ✔ · borrar sin confirmación → 428 sin efecto ✔.
- Tokens: out ≈ 4 135 · in ≈ 12 405.

## Riesgos residuales

- Servidor de la biblioteca estándar: apto para uso local; exponerlo requiere TLS y el [plan de salida](exit-plan.md).
- Revisión humana de auth (P-003) y review independiente (P-004) pendientes.
- `agent-conformance` no ejecuta un dry-run real: las tools de escritura exigen argumentos; el dry-run está cubierto por `test_mcp`.
