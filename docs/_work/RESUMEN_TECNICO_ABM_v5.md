---
type: Summary
title: Resumen técnico — ABM v4.1 → v5.0
description: Estado inicial frente a estado final de la repotenciación de ABM, correcciones de CI, cola de pendientes y lo no verificado.
tags: [abm, resumen, v5]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T01:20:00Z }
---

# Resumen técnico: ABM v4.1 → v5.0

Tres PR fusionados en `main`: [#1](https://github.com/RicardoTorresOliva/APP_Builder_MAC/pull/1) (`dd6b9a3`), [#2](https://github.com/RicardoTorresOliva/APP_Builder_MAC/pull/2) (`b86d121`) y [#3](https://github.com/RicardoTorresOliva/APP_Builder_MAC/pull/3) (`08f2398`). CI en verde en los tres. Detalle completo: `/docs/analysis/05-informe-final.md`.

## Estado inicial vs final

| Dimensión | Inicial | Final |
|---|---|---|
| `AGENTS.md` | 169 líneas, ≈2 482 tokens | ≈2 050 tokens (−17 %); 14 reglas, 6 bloqueantes, protocolo de salida |
| Contexto siempre cargado | ≈3 697 tokens | ≈3 305 tokens (−11 %) |
| Metadatos de comandos, skills y roles | no medido | ≈2 814 tokens sin perfil activo; con perfil: `research-report` −707, `api-service` y `automation-integration` −230 |
| Herramientas con adaptador | 4 (1 inoperante), copias a mano | 9 generadas con `abm sync` más `AGENTS.md` como respaldo; `sync --check` en CI |
| Comandos / manual | 6 / 0 | 36 / 36 |
| CLI | ninguno | `abm`: Python sin dependencias, 20 órdenes, `--json` y `--dry-run` |
| Superficie agéntica | solo una skill de Hermes | servidor MCP (15 tools, 3 recursos), `ads.yaml`, `llms.txt`, skill `operate-abm`, plantillas para ADS nuevos |
| Contrato ADS | no existía | `ads.yaml` en dos niveles; ABM cumple el extendido (`ads-check` OK, conformidad 12/12) |
| Documentos OKF conformes | 35 de 53 | 282 de 282, validador `abm okf validate` |
| Espacio de tokens | tabla manual | ledger JSONL, reporte N1, dashboard N2, guía N3 (OTel), presupuestos blando/duro, atestación |
| Metodología | ninguna | VIBE/IDD/SDD/SPDD/AIDD por módulo con 4 niveles de ceremonia |
| Capa de decisión | ninguna | `abm decide`: proveedores Jev → LLM → reglas, con umbrales de confianza |
| Estándares y stacks | 0 | FE/BE/DB completos, 14 casos de stack, nubes, 9 precios de LLM verificados, legacy |
| Checks de CI | 0 activos | 15 validadores en 3 SO × Python 3.9/3.13, 21 tests del CLI, 45 del ejemplo, markdownlint, gitleaks |
| Modo de trabajo | conversacional | turbo por defecto, cola de pendientes (`abm pending`), permisos turbo aplicados |
| Licencia | provisional | propietaria SLG definitiva |

## Correcciones de CI (PR #1)

- Windows: los programas hijos escribían en cp1252 → stdio UTF-8 en el ejemplo y en la plantilla MCP.
- `secret-scan`: error 403 → permiso `pull-requests: read`.
- `secret-scan`: 10 falsos positivos en `adapters/.generated.json` → `.gitleaks.toml` con allowlist solo para ese registro.

## Cola de pendientes

- Resueltos: P-001 (plan), P-002 (tarea en `RicardoTorresOliva/AGE_Builder_MAC#1`), P-003 (licencia), P-007 (turbo), P-008 a P-011 (presupuestos).
- Abiertos: P-005 (Hermes) y P-006 (Jev). Faltan credenciales: `TYPESAFE_API_KEY` y las del LLM de Hermes, en la configuración del entorno.

## Otros ajustes

- Ledger de tokens: el identificador de modelo pasó a `no-declarado`. Consecuencia: el costo ya no se calcula, solo los tokens.
- `.claude/settings.local.json` salió del repo y quedó en `.gitignore`.

## No verificado

- Jev y Hermes en vivo: sin credenciales.
- Workflows de Antigravity y claves MCP de Hermes: las fuentes oficiales se contradicen.

## Residuales

- `yamlmini` acepta en silencio algo de YAML inválido fuera del subconjunto que soporta.
- No hay presupuesto de tokens por sesión (sí por unidad, por funcionalidad y total).
