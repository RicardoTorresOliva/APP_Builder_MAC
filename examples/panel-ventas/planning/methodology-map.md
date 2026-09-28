---
type: Methodology Map
title: Mapa metodológico — panel-ventas
description: Modo metodológico por módulo del ADS, con justificación, revisión y disparadores.
tags: [metodologia, plan]
status: draft
generated: { by: process:abm-methodology, at: 2026-09-27T23:52:55Z }
---

# Mapa metodológico — panel-ventas

Ceremonia: **producto** · modo del proyecto: **SDD** · clasificación: rules.

| Módulo | Modo | Justificación | Revisión | Disparadores |
|---|---|---|---|---|
| auth | SDD | escalamiento: auth | human | auth |
| ventas | SDD | Riesgo alto (dinero, datos personales o de salud, seguridad): exige trazabilidad requisito-tarea-test y revisión humana. | humana | — |
| dashboard | SDD | Riesgo alto (dinero, datos personales o de salud, seguridad): exige trazabilidad requisito-tarea-test y revisión humana. | humana | — |

## Dimensiones

| Dimensión | Nivel (0–2) | Confianza | Fuente |
|---|---|---|---|
| uncertainty | 1 | 0.0 | rules |
| criticality | 2 | 1.0 | rules |
| horizon | 1 | 0.0 | rules |
| team | 0 | 0.0 | rules |
| brownfield | 0 | 0.0 | rules |
| autonomy | 1 | 0.0 | rules |

## Clasificación

| Campo | Valor |
|---|---|
| Comando | `./abm methodology classify --text "<encargo>" --module "auth=login y roles" --module "ventas=registro de ventas" --module "dashboard=gráficos de ventas" --json` (desde la raíz de ABM, con `--write` hacia este archivo) |
| Ceremonia del ADS | `producto` → contrato `extendido`, tokens `N2`, revisión obligatoria en críticos |
| Regla ganadora | criticidad = 2 (regla 1) y disparador `auth` en el módulo auth |
| Confianza | 1.0 en criticidad; 0.0 en las otras cinco dimensiones (sin proveedor de `decide`: reglas) |
| Pendiente | P-001: confirmar las cinco dimensiones de baja confianza (defaults aplicados) |

## Consecuencias aplicadas

- Los tres módulos van en SDD: requisitos EARS con id, trazabilidad requisito → unidad → test en [requisitos](requirements.md).
- `auth` exige revisión humana: queda en cola como P-003 (el ejemplo no la sustituye).
- Tests de rutas críticas obligatorios: auth, permisos por rol, CSRF, mutaciones y migraciones.
