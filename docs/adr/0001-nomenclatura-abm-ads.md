---
type: ADR
title: "ADR 0001 — Nomenclatura ABM/ADS y glosario"
description: Cómo se nombran la fábrica, lo que produce y sus unidades de trabajo.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0001 — Nomenclatura ABM/ADS y glosario

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto

El repo se llamaba "APP_Builder v4.1" y hablaba de "digital assets". El prompt maestro fija: ABM produce ADS (Activo Digital SLG). Coexisten FU/DU (unidades con que se construye un ADS) y WU (unidades de esta repotenciación).

## Decisión

- **ABM** (APP_Builder_MAC) es la fábrica; versión **5.0.0** (semver; hay cambios incompatibles: rutas de scripts y OKF v0.2).
- **ADS** es todo lo que produce ABM. Cada ADS tiene identidad propia: `ads.yaml` (ADR 0009).
- **Tipo de ADS = perfil** (`profiles/`). Se añaden dos perfiles atómicos que el diagnóstico exige: `api-service` (API, CLI o servidor MCP consumido por programas o agentes, sin UI propia) y `automation-integration` (flujos entre sistemas).
- **FU/DU** se conservan para construir un ADS. **WU** se reserva para la evolución de ABM.
- `docs/glossary.md` es el glosario canónico; ningún otro archivo redefine términos.
- **Frontera con AGE_Builder** (fábrica de arneses de agentes de SLG): si el encargo es un arnés de agente, `init-project` lo indica y remite; la interoperabilidad es vía OKF.
- ABM es su propio primer ADS: `ads.yaml` en la raíz, perfil `api-service`, nivel `extendido`.

## Consecuencias

- Todo texto de ABM usa ADS en lugar de "activo digital" o "app".
- `QUICKSTART.md` y `README.md` se reescriben con la nueva nomenclatura.

## Alternativas descartadas

- Mantener "digital asset": no distingue los activos de SLG ni ata el Contrato ADS.
