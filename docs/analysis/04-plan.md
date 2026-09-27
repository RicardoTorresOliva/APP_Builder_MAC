---
type: Plan
title: Plan de repotenciación ABM v5
description: Arquitectura objetivo, plan de migración y roadmap de WU con criterios de aceptación y verificación.
tags: [plan, roadmap, migracion]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:24:13Z }
---

# Plan de repotenciación ABM v5

Base: [diagnóstico](/docs/analysis/01-diagnostico.md), [benchmark](/docs/analysis/02-benchmark.md), [investigación agéntica](/docs/analysis/03-investigacion-agentica.md) y los ADR 0001–0016 en [docs/adr/](/docs/adr/0001-nomenclatura-abm-ads.md).

## Resumen de una pantalla
- **Diagnóstico:** 1,75/5. Núcleo de gobernanza sólido; faltan contrato y superficie agéntica de los ADS, espacio de tokens, generador de adaptadores, metodologías, paridad FE/BE/DB, catálogo, turbo y CI.
- **Decisiones clave:** ABM v5.0.0 produce ADS con `ads.yaml` (ADR 0009); tooling Python stdlib con `--json` (ADR 0003); adaptadores generados para 9 herramientas (ADR 0002); OKF v0.2 en todo (ADR 0004); MCP 2025-11-25 y servidor MCP propio (ADR 0010); capa System One con Jev → LLM → reglas (ADR 0011); turbo por defecto con cola de pendientes (ADR 0014); núcleo sin productos, verificado por lint (ADR 0016).
- **Roadmap:** 16 WU; núcleo y contrato primero, contenido en paralelo, verificación al final.

## Arquitectura objetivo
```
AGENTS.md                 # canónico (≤ 150 líneas): identidad, reglas, turbo, protocolo de salida, punteros
abm.yaml                  # configuración de ABM/ADS: modo, OKF, presupuestos, lint, decisión
ads.yaml                  # manifiesto del Contrato ADS de ABM (perfil api-service, nivel extendido)
llms.txt                  # índice para agentes
index.md · log.md         # raíz del bundle OKF (index generado = mapa de contexto)
abm · abm.cmd             # lanzadores del CLI (macOS/Linux · Windows)
okf/                      # PROFILE.md (perfil ABM sobre OKF v0.2) · schema.json
contract/                 # README (niveles) · ads.schema.json · token-event.schema.json
profiles/                 # (existe) + api-service, automation-integration; ads_contract_level y ceremonia
commands/                 # 36 playbooks neutrales (Propósito…Reporte…Invocación por agentes)
skills/<name>/SKILL.md    # Agent Skills: capacidades que el agente activa por descripción
agents/                   # 13 roles con alcance, entradas, salidas y DoD
methodology/              # router, vibe, idd, sdd, spdd, aidd, mezcla, ceremonia, deriva
standards/                # frontend/ backend/ database/ security/ testing/ observability/ a11y/
                          # agentic/ finops/ communication.md
stacks/                   # catálogo (≥ 14 casos) + clouds.md, llm-providers.md, legacy.md
integrations/             # mcp/ api/ webhooks/ auth/ agents/ decision/ llm-gateway/ observability/
templates/                # plantillas OKF de artefactos + agentic/ (manifiesto, skill, servidor MCP, llms.txt)
docs/                     # manual/ guides/ glossary faq troubleshooting compat-matrix adr/ analysis/ _work/
                          # + espacio del proyecto: project_memory, decision_log, work_log
examples/                 # golden paths (nunca referenciados por el núcleo)
scripts/                  # abm.py + abmkit/ (CLI) · shims .sh de compatibilidad
.github/workflows/        # CI de ABM: abm check + markdownlint + secret scan
ops/tokens/               # ledger JSONL, dashboard N2
planning/ implementation/ design_docs/ deliverables/ knowledge/   # espacio de trabajo del ADS (existe)
# Salidas generadas por abm sync: CLAUDE.md, .claude/, .agents/, .codex/, .agent/, GEMINI.md, .gemini/,
# .github/ (Copilot), .cursor/, .windsurf/, .kiro/ … (según docs/compat-matrix.md)
```

## Plan de migración
| Antes (v4.1) | Después (v5) | Compatibilidad |
|---|---|---|
| `scripts/*.sh` | `abm <orden>` (Python) | los `.sh` quedan como shims |
| `install-adapter.sh` | `abm sync [--tool X]` | shim |
| `adapters/<tool>/` (copias) | `adapters/tools.yaml` + salidas generadas | punteros en la raíz se regeneran |
| `mcps/inventory.md`, `skills/inventory.md` | `docs/tooling/mcp-inventory.md`, `docs/tooling/skills-inventory.md` | alias en MIGRATION |
| `docs/run_metadata.md` | ledger + `TOKENS.md` | la tabla se conserva como histórico |
| `timestamp`, `status: stub` | `generated.at`, `status: draft` + etiqueta | `abm okf validate` guía la migración |
| `QUICKSTART.md` | `QUICKSTART.md` reescrito + `docs/manual/` | misma ruta |
| 6 comandos | 36 comandos | los 6 conservan nombre |

## Roadmap de WU
| WU | Objetivo | Archivos | Aceptación | Verificación |
|---|---|---|---|---|
| WU1 | Núcleo | `AGENTS.md`, `abm.yaml`, `okf/`, `scripts/abmkit/`, `abm`, `abm.cmd`, `docs/glossary.md`, `index.md`, `log.md`, frontmatter de todo `.md` | `AGENTS.md` ≤ 150 líneas; todo `.md` conforme | `abm okf validate`, `abm token-budget` |
| WU2 | Generador de adaptadores | `scripts/abmkit/sync.py`, `adapters/tools.yaml`, salidas | 9 herramientas + fallback | `abm sync --check` |
| WU3 | Contrato ADS | `contract/`, `ads.yaml`, perfiles | ABM nivel extendido | `abm ads-check` |
| WU4 | Motor metodológico | `methodology/`, `templates/`, `scripts/abmkit/methodology.py` | 5 modos, mezcla, escalamiento, `/drift` | `abm methodology classify` en los 6 encargos |
| WU5 | Comandos, skills y roles | `commands/`, `skills/`, `agents/` | 36 playbooks, 13 roles | `abm lint playbooks` |
| WU6 | Paridad FE/BE/DB | `standards/`, skills de capa | misma estructura en las 3 capas | revisión + OKF |
| WU7 | Superficie agéntica | `scripts/abmkit/mcp_server.py`, `conformance.py`, `templates/agentic/`, `llms.txt` | ABM operable por MCP | `abm agent-conformance` |
| WU8 | Capa System One | `scripts/abmkit/decide.py`, `integrations/decision/` | Jev + LLM + reglas; umbrales | pruebas unitarias; Jev real `no-verificado` sin clave |
| WU9 | Portabilidad | `stacks/clouds.md`, `stacks/llm-providers.md`, `stacks/legacy.md`, `commands/assess.md` | encargo (f) sin huecos | recorrido Fase 4 |
| WU10 | Catálogo de stacks | `stacks/` | ≥ 14 casos con matriz completa | OKF (`stale_after`) |
| WU11 | Integraciones | `integrations/` | MCP/API/otras vías + seguridad | OKF + lint core |
| WU12 | Tokens | `scripts/abmkit/tokens.py`, `dashboard.py`, `contract/token-event.schema.json`, pricing | N1/N2 + presupuestos | `abm tokens report/dashboard/budget` |
| WU13 | Turbo y protocolo | salidas turbo en `sync`, `scripts/abmkit/pending.py`, `standards/communication.md` | configuración por herramienta | `abm sync --check`, `abm pending` |
| WU14 | Manual | `docs/manual/`, glosario, FAQ, troubleshooting | 100 % de comandos | `abm lint manual` |
| WU15 | Ejemplos y CI | `examples/`, `.github/workflows/` | (b) ejecutado con build y tests | CI local + `abm check` |
| WU16 | Documentos de proyecto | README, CHANGELOG, MIGRATION, CONTRIBUTING, SECURITY, LICENSE | completos | OKF + enlaces |

## Paralelización
- Secuencial: WU1 → WU3 (el contenido depende del perfil OKF y del contrato).
- En paralelo con subagentes (rutas disjuntas): WU4, WU5, WU6, WU10+WU9, WU11; el orquestador hace WU2, WU7, WU8, WU12, WU13.
- Después: WU14 (depende de WU5), WU15, WU16, Fase 4.
