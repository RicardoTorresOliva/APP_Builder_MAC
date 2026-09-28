---
type: Analysis
title: Diagnóstico de ABM v4.1
description: Estado de APP_Builder_MAC antes de la repotenciación, con scorecard por dimensión y evidencia archivo:línea.
tags: [analisis, diagnostico, abm]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:13:33Z }
verified: { by: process:abm-analysis, at: 2026-09-27T23:13:33Z }
---

# Diagnóstico de ABM v4.1

## Resumen ejecutivo

- ABM v4.1 es una base sólida de **gobernanza neutral**: una sola fuente (`AGENTS.md`, 169 líneas), perfiles de activo componibles, unidades FU/DU, selección de stack con humano en el bucle y regla de "categorías, no productos".
- Cubre bien el **qué** (gobierno del proceso) y poco el **cómo** (estándares técnicos, metodologías, catálogo de stacks, integraciones).
- **Brechas críticas** frente al objetivo:
  1. sin superficie agéntica ni contrato para los activos producidos (D12);
  2. sin espacio de tokens: solo una tabla manual (D14);
  3. adaptadores copiados a mano, 4 herramientas, sin Codex, Copilot, Gemini CLI, Windsurf ni Kiro (D3);
  4. sin motor metodológico ni paridad FE/BE/DB (D4, D5);
  5. el flujo empuja a detenerse y preguntar; no hay modo turbo ni protocolo de salida (D15);
  6. OKF aplicado parcialmente y según v0.1 (D10);
  7. sin CI activa, sin licencia y scripts solo bash (D11).
- **Deuda puntual:** un bug en `scripts/check_doc_sync.sh:24` (busca `design/`, la carpeta es `design_docs/`), texto obsoleto en los wrappers de Claude Code y un error de formato en `adapters/README.md:32`.
- **Estrategia:** conservar el núcleo y los perfiles; añadir encima el Contrato ADS, la superficie agéntica, el espacio de tokens, el motor metodológico, los estándares, el catálogo y el generador de adaptadores; migrar OKF a v0.2 y el tooling a Python multiplataforma.

## Scorecard (0–5)

| # | Dimensión | Nota | Evidencia |
|---|---|---|---|
| D1 | Inventario y mapa | 3 | Flujo idea → entrega en `QUICKSTART.md:31-56` y 6 playbooks; termina en "Delivered" (`commands/start-execution.md:44`); no existe la fase "operando". |
| D2 | Gobernanza y flujo | 4 | Fuente única (`AGENTS.md:7`), FU/DU (`AGENTS.md:37-42`), perfiles (`AGENTS.md:44-58`). Frenos al turbo: "Quality over speed, always" (`AGENTS.md:30`), "ask the user" (`AGENTS.md:32`), lista de paradas (`commands/start-execution.md:18-24`), cortar sesión al leer 8 archivos (`AGENTS.md:111-115`). |
| D3 | Multi-herramienta | 2 | 4 herramientas (`adapters/README.md`); copias manuales idénticas `adapters/claude-code/.claude` ↔ `.claude`; Hermes ausente en `install-adapter.sh:7-17`; `scripts/detect_platform.sh` solo distingue 3. |
| D4 | Metodologías | 1 | Solo SDD implícito (`scripts/check_doc_sync.sh:3`) y spec-delta en `commands/iterate.md:12-20`. Sin router ni Vibe/IDD/SPDD/AIDD ni mezcla por módulo. |
| D5 | Paridad FE/BE/DB | 1 | Solo la checklist de seguridad de `profiles/software-app/profile.md` (quality_gate) y 3 design docs. Sin estándares, skills, a11y, rendimiento, migraciones ni pirámide de tests. |
| D6 | Stacks y plantillas | 1 | Solo categorías (`profiles/*/profile.md` stack_candidates), por diseño (`AGENTS.md:21`). Sin catálogo, vigencia, costos ni recetas. |
| D7 | Integraciones y seguridad | 2 | Regla de secretos (`AGENTS.md:16`), gitleaks de ejemplo (`ci/app-builder-gates.yml:32`), `mcps/inventory.md` vacío. Sin `.env.example`, sin defensa contra prompt injection, sin guía MCP/API. |
| D8 | Eficiencia de tokens | 3 | Divulgación progresiva (`AGENTS.md:104`), modelo por tarea (`AGENTS.md:107`). Siempre cargado ≈ 3 697 tokens. Sin medición automática ni presupuestos. |
| D9 | UX vibe coder | 2 | `QUICKSTART.md` claro, pero mezcla idiomas (núcleo en inglés, guía en español formal) y da la terminal por sabida (`QUICKSTART.md:18-22`). Sin manual, glosario, FAQ ni guía para deshacer. |
| D10 | Calidad documental | 2 | 18 de 53 `.md` sin frontmatter; `status: stub` fuera del enum OKF (`knowledge/index.md:4`); `index.md`/`log.md` con frontmatter, contra la spec; `log.md` en tabla; texto obsoleto "milestone M1" (`.claude/commands/init-project.md:8`). |
| D11 | Calidad del repo | 1 | Sin `.github/workflows`, sin tests de scripts, sin LICENSE/CHANGELOG/CONTRIBUTING/SECURITY; scripts solo bash (no Windows nativo); bug `scripts/check_doc_sync.sh:24`. |
| D12 | Superficie agéntica | 1 | Skill de Hermes (`adapters/hermes/SKILL.md`) y `AGENTS.md` nativo. Sin manifiesto, MCP, CLI `--json` ni `llms.txt`; los activos producidos no tienen contrato agéntico. |
| D13 | Portabilidad corporativa | 2 | Sin lock-in (`AGENTS.md:21`), abstracción LLM mencionada (`profiles/software-app/profile.md` stack_candidates.llm). Sin flujo brownfield/legacy, matriz de nubes ni gateway LLM. |
| D14 | Tokens y costo | 1 | Registro manual por milestone (`AGENTS.md:89`, `docs/run_metadata.md`). Sin ledger, sin consumo en operación, sin dashboard ni alertas. |
| D15 | Velocidad y verbosidad | 2 | Salidas concisas en `commands/bootstrap.md:29-36` y `commands/session-start.md:9-15`. Sin protocolo de salida general, sin paralelismo, sin configuración turbo por herramienta. |
| D16 | Capa System One | 0 | Inexistente. |

**Promedio:** 1,75 / 5.

## Fortalezas que hay que conservar

- Gobernanza en un solo archivo neutral, con adaptadores que solo apuntan (`AGENTS.md:7-11`).
- Asset Profiles con composición (`profiles/_contract.md:82-117`): n perfiles producen hasta 2ⁿ híbridos sin duplicar.
- FU/DU con completitud end-to-end definida por perfil (`AGENTS.md:37-42`).
- Stack elegido con humano en el bucle y regla de categorías (`AGENTS.md:121-126`).
- Verificación mecánica delegada a scripts (`AGENTS.md:35`).
- Revisión independiente con contexto limpio (`commands/review.md:3`).
- Spec-delta antes de cambiar (`commands/iterate.md:12-20`).
- Adopción temprana de OKF y de Hermes.

## Brechas, riesgos y deuda

| # | Brecha o riesgo | Severidad | Tratamiento (WU) |
|---|---|---|---|
| B1 | Los ADS no son operables por agentes externos | alta | Contrato ADS + superficie agéntica (WU3, WU7) |
| B2 | Sin espacio de tokens ni costo en operación | alta | Ledger + dashboards (WU12) |
| B3 | Adaptadores manuales; 5 herramientas mínimas sin soporte | alta | Generador `sync` (WU2) |
| B4 | Sin metodologías ni mezcla por módulo | alta | Motor metodológico (WU4) |
| B5 | FE/BE/DB sin estándares ni skills | alta | Paridad (WU6) |
| B6 | Reglas que frenan el turbo sin aportar seguridad | media | ADR 14 + `AGENTS.md` nuevo (WU1, WU13) |
| B7 | OKF v0.1 parcial | media | Perfil OKF v0.2 + validador (WU1) |
| B8 | Tooling solo bash; sin CI | media | CLI Python multiplataforma + CI (WU1, WU15) |
| B9 | Sin catálogo de stacks ni ruta legacy | media | WU9, WU10 |
| B10 | Sin guía de integraciones ni defensa ante prompt injection | media | WU11 |
| B11 | Sin capa de decisión tipada | baja | WU8 |
| B12 | Documentos legales y de proyecto ausentes | baja | WU16 |

## Quick wins

1. Corregir `scripts/check_doc_sync.sh:24` (`design` → `design_docs`).
2. Quitar el texto "milestone M1" de los wrappers de Claude Code.
3. Arreglar la tabla de `adapters/README.md` (fila de Hermes fuera de lugar).
4. Añadir Hermes a `install-adapter.sh` (luego lo reemplaza `sync`).
5. Frontmatter OKF en los 18 `.md` que no lo tienen.
6. Instalar la CI de ejemplo en `.github/workflows/`.
