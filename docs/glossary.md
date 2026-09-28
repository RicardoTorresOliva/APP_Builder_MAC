---
type: Glossary
title: Glosario de ABM
description: Definiciones canónicas de ABM; ningún otro archivo redefine estos términos.
tags: [glosario, referencia]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:32:18Z }
---

# Glosario de ABM

| Término | Definición |
|---|---|
| **ABM** | APP_Builder_MAC: la fábrica. Este repo y su CLI `abm`. |
| **ADS** | Activo Digital SLG: todo lo que produce ABM (app, API, dashboard, ERP, automatización, app con IA, informe, producto de datos o de inteligencia, híbrido). |
| **Perfil** | Tipo de ADS (`profiles/<name>/profile.md`): completitud, quality gate, design docs, nivel del Contrato ADS. Los perfiles se componen. |
| **Ceremonia** | Nivel de formalidad (`abm.yaml → ceremony`): prototipo, mvp, producto, enterprise-regulado. Fija modo por defecto, gates y niveles. |
| **FU** | Foundation Unit: trabajo base sin salida consumible directa. Va primero. |
| **DU** | Deliverable Unit: algo que un consumidor usa de punta a punta. |
| **WU** | Unidad de trabajo de la evolución de ABM (no de un ADS). |
| **Contrato ADS** | Requisitos verificables de todo ADS, declarados en `ads.yaml` (`contract/README.md`). Niveles `minimo` y `extendido`. |
| **Superficie agéntica** | Interfaces por las que un agente externo descubre, opera y audita un ADS: `AGENTS.md`, skill de operación, `llms.txt`, MCP, CLI `--json`, API. |
| **Capa System One** | Modelo de decisión tipada (choice, score, boolean) con confianza; decide pasos cortos en lugar de un LLM (`decide`). |
| **Espacio de tokens** | Ledger de consumo (construcción y operación) + reporte (N1) o dashboard (N2/N3) + presupuestos. |
| **Ledger** | Archivo JSONL con un evento por consumo de tokens (`contract/token-event.schema.json`). |
| **Presupuesto** | Límite de tokens por sesión, unidad o funcionalidad: umbral blando → cola; tope duro → bloqueante. |
| **Modo turbo** | Modo por defecto: se actúa sin pedir permiso en lo reversible; solo detienen los bloqueantes. |
| **Modo checkpoint** | Como turbo, pero el plan requiere aprobación explícita antes de producir. |
| **Bloqueante** | Una de las causas a–f de `AGENTS.md`; lo único que detiene el trabajo. |
| **Cola de pendientes** | `docs/_work/PENDIENTES.md`: decisiones no bloqueantes con su default ya aplicado (`abm pending`). |
| **Semáforo** | Clasificación de cada acción: `[verde]` reversible, `[amarillo]` recuperable, `[rojo]` bloqueante. |
| **Protocolo de salida** | Forma de comunicar del agente: acciones, evidencias y siguientes pasos, sin conversación (`standards/communication.md`). |
| **Playbook** | Procedimiento neutral de un comando (`commands/<name>.md`). |
| **Skill** | Capacidad que el agente activa por su descripción (`skills/<name>/SKILL.md`, estándar Agent Skills). |
| **Rol** | Agente especializado con alcance y DoD (`agents/<rol>.md`); el revisor nunca es quien construye. |
| **Adaptador** | Archivo que una herramienta concreta lee para encontrar la gobernanza; se genera con `abm sync`. |
| **OKF** | Open Knowledge Format (Google Cloud) v0.2: Markdown + frontmatter YAML; formato de todo documento (`okf/PROFILE.md`). |
| **Modos metodológicos** | VIBE (exploración desechable), IDD (intención mínima viable), SDD (spec → diseño → tareas), SPDD (contratos de prompt versionados), AIDD (explorar → consolidar → construir con revisión humana). |
| **Methodology map** | Tabla módulo → modo → justificación → revisión de un ADS. |
| **Deriva (drift)** | Desincronía entre intención, spec, contratos y código; se controla con `drift` y `closeout`. |
| **Brownfield** | Trabajo sobre un sistema o stack existente; se inventaría con `assess`. |
| **HITL** | Humano en el bucle: decisión o revisión que exige a una persona. |
