---
type: Example
title: Ejemplo golden path — panel de ventas
description: ADS completo y ejecutable (dashboard con auth, base de datos y gráficos) recorrido con ABM de encargo a entrega, con build, tests y Contrato ADS en verde.
tags: [ejemplo, golden-path, software-app, ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:12:08Z }
---

# Ejemplo golden path — panel de ventas

Encargo simulado: *"dashboard con auth, base de datos y gráficos"* ([START_PROJECT.md](START_PROJECT.md)). Muestra cómo un vibe coder
recorre ABM con los playbooks `init-project` y `start-execution` y obtiene un ADS real: web con login por roles, registro de ventas,
gráficos por mes y por vendedor, y una superficie agéntica (MCP + CLI) que un agente externo puede operar.

Stack (decisión [D-001](docs/decision_log.md)): Python 3.9+ solo biblioteca estándar + SQLite + HTML/CSS/SVG. Cero dependencias.

## Ejecutar en 3 comandos

```sh
cd examples/panel-ventas
python3 app/server.py --port 8765      # migra, siembra y muestra las contraseñas demo SOLO en consola → http://127.0.0.1:8765
./run_checks.sh                        # build + 45 tests + e2e + Contrato ADS + OKF + presupuestos + secretos
```

Usuarios demo: `ana` (admin), `bruno`, `carla`, `diego` (vendedores). La contraseña se genera al sembrar; para fijarla en una
sesión: `PANEL_VENTAS_DEMO_PASSWORD=<la-tuya> python3 app/server.py` (no la guardes en archivos).
Para agentes: `python3 ops/mcp_server.py` (MCP stdio) o `python3 app/cli.py status --json`.

## Qué demuestra

| Pieza | Dónde | Estándar aplicado |
|---|---|---|
| Auth: PBKDF2-SHA256 600 000 it. + sal por usuario, sesión HttpOnly + SameSite=Strict, CSRF, límite de intentos | `app/db.py`, `app/server.py` | OWASP, `standards/backend` |
| Datos: migraciones versionadas up/down (`schema_migrations`), CHECK/FK/UNIQUE, auditoría, seeds idempotentes | `app/db.py` | `standards/database` |
| API JSON con errores `application/problem+json` y contrato OpenAPI 3.1 | `app/server.py`, `api/openapi.yaml` | RFC 9457 |
| Dashboard: KPIs, barras SVG por mes y por vendedor, tooltips por puntero y teclado, tabla, modo oscuro, estados vacío/carga/error | `app/static/` | `standards/frontend`, WCAG 2.2 AA |
| Superficie agéntica: MCP (lectura, dry-run, destructiva con `confirm`), CLI `--json/--dry-run`, skill, `llms.txt` | `ops/mcp_server.py`, `app/cli.py`, `skills/` | Contrato ADS `extendido` |
| Espacio de tokens N2: ledger, reporte y dashboard con presupuestos | `ops/tokens/`, `TOKENS.md` | `contract/token-event.schema.json` |

## Qué comando de ABM produjo cada artefacto

| Paso | Comando o playbook | Artefacto |
|---|---|---|
| Encargo | — (persona) | [START_PROJECT.md](START_PROJECT.md) |
| Perfil y ceremonia | `init-project` pasos 2–3 | [memoria](docs/project_memory.md), `abm.yaml` |
| Metodología | `./abm methodology classify --text … --module auth=… --module ventas=… --module dashboard=… --write …` | [methodology-map.md](planning/methodology-map.md) |
| Requisitos, alcance, riesgos | `init-project` paso 6 (`spec`, EARS) | [requirements.md](planning/requirements.md) |
| Stack | `init-project` paso 7 (`stack`, HITL) | [decision_log.md](docs/decision_log.md) + P-002 en cola |
| Design docs | `init-project` paso 8 | [datos](design_docs/data-model.md), [API](design_docs/api-contracts.md), [UI](design_docs/ui-architecture.md) |
| Unidades y milestones | `init-project` paso 9 | [user_units.md](implementation/user_units.md), [task_tracker.md](implementation/task_tracker.md) |
| Contrato ADS | `init-project` paso 10 (plantilla `templates/agentic/ads.yaml`) | `ads.yaml`, [AGENTS.md](AGENTS.md), skill, `ops/mcp_server.py` |
| Knowledge | `init-project` paso 11 | [knowledge/index.md](knowledge/index.md) |
| Cola turbo | `./abm pending add` | [PENDIENTES.md](docs/_work/PENDIENTES.md) |
| Construcción FU → DU | `start-execution` | `app/`, `ops/`, `tests/` |
| Registro por unidad | `start-execution` paso 4 + `./abm tokens estimate --unit <id> <archivos>` | [work_log.md](docs/work_log.md), `ops/tokens/ledger.jsonl` |
| Reporte y dashboard de tokens | `./abm tokens report`, `./abm tokens dashboard` | [TOKENS.md](TOKENS.md), `ops/tokens/dashboard.html` |
| Índice OKF y llms.txt | `./abm okf index` | `index.md`, `llms.txt` |
| Verificación | `./abm ads-check`, `./abm agent-conformance`, `./abm okf validate` | salida abajo |

Aquí `./abm` es un atajo a la CLI de ABM con este ejemplo como raíz (`scripts/abm.py`); equivale a `python3 ../../scripts/abm.py --root .`.
Un ADS real se crea fuera de ABM con `./abm new-ads <carpeta> --id … --profile software-app` y trae su propia copia de la CLI.

## Resultados de verificación

Salida real de `./run_checks.sh` (2026-09-28, Python 3.11, Linux):

| Paso | Resultado |
|---|---|
| `python3 -m compileall -q app ops tests` | OK |
| `python3 -m unittest discover -s tests` | 45 tests OK (auth 8, api 20, db 11, mcp + cli 6) |
| `python3 ops/smoke_e2e.py` | login `ana` → 303 `/dashboard` 200 → `/api/resumen`: 175 ventas, 13 meses, 3 vendedores |
| `./abm ads-check` | Contrato ADS (panel-ventas, nivel extendido): 0 errores → OK |
| `./abm agent-conformance` | 12 pasos · 0 fallan → OK (dry-run: no aplica; las tools de escritura exigen argumentos y el dry-run lo cubre `test_mcp`) |
| `./abm okf index` / `okf validate` | index.md y llms.txt generados; OKF perfil ABM 0 errores |
| `./abm tokens budget` | todos los alcances bajo el umbral blando |
| `./abm secrets` | 0 hallazgos |

Verificación visual (navegador sin interfaz): claro, oscuro, estado vacío y móvil de 390 px sin errores de consola.
Pendientes honestos en la cola: revisión humana de auth (P-003) y review independiente (P-004).
