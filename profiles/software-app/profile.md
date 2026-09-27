---
type: Asset Profile
title: software-app
description: Perfil de referencia para software con interfaz de usuario: web, móvil, escritorio, dashboard o ERP.
tags: [perfil, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:34:39Z }
ads_contract_level: extendido
---

# Perfil: software-app

Software que una persona **usa** a través de una interfaz. Categorías, sin productos ni stack por defecto: el stack se elige con `stack` (catálogo en `stacks/`).

## design_docs
- data_model: entidades, campos, relaciones, índices (ERD) — [HIGH]
- api_contracts: endpoints, métodos, esquemas, auth, errores problem+json — [HIGH]
- ui_wireframes: navegación, pantallas clave, flujos, estados vacíos y de error — [MEDIUM]
- architecture: componentes, comunicación, integraciones, superficie agéntica — [MEDIUM]
- style_guide: design system, tokens, tipografía, componentes — [LIGHT]

## foundation_unit_examples
- Scaffolding (backend + frontend + contenedores) con CLIs de scaffolding
- Capa de datos (modelos, migraciones reversibles, seeds)
- Identidad (según la categoría elegida)
- Servicios compartidos que varios DU necesitan
- Superficie agéntica base (`ads.yaml`, skill `operate-<id>`, servidor MCP) y ledger de tokens

## deliverable_unit_completeness
Un DU está hecho solo si:
- el backend soporta la funcionalidad y el frontend la expone;
- el consumidor completa la acción de punta a punta, con estados vacíos y de error;
- las capacidades nuevas están en `ads.yaml` y son operables por agentes (MCP o CLI `--json`);
- pasan el quality gate y los tests de rutas críticas (auth, pagos, mutaciones de datos, integraciones);
- el consumo de tokens de la unidad está en el ledger.

## quality_gate
- Estándares y checklists de `standards/frontend/`, `standards/backend/` y `standards/database/`
- Seguridad: `standards/security/` (OWASP web, LLM y agéntico); sin secretos ni datos sensibles en código, logs, errores o UI
- Validación de entradas, authN/authZ en rutas protegidas, consultas parametrizadas, escape de contenido
- Errores sin detalles internos (`application/problem+json`)
- Accesibilidad WCAG 2.2 AA y Core Web Vitals en objetivo
- `./abm ads-check` y `./abm agent-conformance` en verde

## deliverable_format
- Repositorio desplegable de forma independiente, con `ads.yaml`, `AGENTS.md` y adaptadores generados

## publication_step
- Build en contenedores y despliegue en la plataforma elegida en planificación (categoría)

## stack_candidates
- backend: [lenguaje + framework web + acceso a datos + herramienta de migraciones]
- frontend: [framework + lenguaje + design system + gestión de estado]
- database: [relacional | documental | otra — según el modelo de datos]
- auth: [identidad gestionada por la app | proveedor de identidad delegado]
- llm: [proveedor detrás de un gateway intercambiable] + capa System One opcional
- deploy: [contenedores + plataforma de despliegue]
- Catálogo: `stacks/cases/` (saas-web-app, internal-dashboard-bi, e-commerce, mobile-app, desktop-app, erp-crm-backoffice)

## tooling_candidates
- skill de diseño de esquema: validar el modelo de datos antes de implementar
- skill de design system: acelerar la UI
- servidor MCP de base de datos (solo lectura por defecto)
- servidor MCP de navegador para verificación visual

## knowledge_bundles
- stack-patterns/<stack-elegido> (se crea por proyecto y se reutiliza)

## profile-specific rule
- Superficie de administración/operación (logs, credenciales, ciclo de vida) **cuando los usuarios del ADS la necesitan**, no por defecto.
