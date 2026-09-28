---
type: Analysis
title: Informe final de la repotenciación de ABM v5
description: Qué cambió y por qué, métricas antes/después, verificación, criterios de aceptación, pendientes y próximos pasos.
tags: [informe, cierre, fase-5]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:20:41Z }
verified:
  - { by: process:abm-check, at: 2026-09-28T00:20:41Z }
---

# Informe final — repotenciación de ABM v5

## Resumen

- ABM pasó de plantilla de gobernanza (v4.1, promedio 1,75/5 en el [diagnóstico](/docs/analysis/01-diagnostico.md)) a **fábrica agent-native de ADS** (v5.0.0), ejecutada en modo TURBO en 26 commits sobre la rama de trabajo.
- Todo ADS —y ABM mismo— cumple un **Contrato ADS** verificable: manifiesto `ads.yaml`, superficie agéntica (MCP, CLI `--json`, skill, `llms.txt`), espacio de tokens, portabilidad y seguridad.
- **9 herramientas** con adaptadores generados desde una sola fuente, **36 comandos** con manual, **5 metodologías** con mezcla por módulo, **paridad FE/BE/DB**, **14 casos de stack**, **capa System One** (Jev → LLM → reglas), **OKF v0.2** en 282 conceptos.
- Verificación: `abm check` 15/15 en Python 3.9, 3.11 y 3.13; 19 tests del CLI; ejemplo ejecutado (45 tests + E2E); 6 encargos recorridos; revisión adversarial con 35 hallazgos corregidos o documentados.

## Qué cambió y por qué

| Área | Antes (v4.1) | Después (v5) | Decisión |
|---|---|---|---|
| Identidad | "digital assets" | ABM produce ADS; ABM es su propio primer ADS | ADR 0001 |
| Adaptadores | copias manuales, 4 herramientas (Cursor roto) | `abm sync`: 353 salidas para 9 herramientas, `--check` en CI | ADR 0002 |
| Tooling | bash (sin Windows) | CLI Python stdlib, `--json`/`--dry-run`, 20 órdenes | ADR 0003 |
| Documentos | OKF parcial tipo v0.1 | OKF v0.2 + perfil ABM, validador de 2 niveles | ADR 0004 |
| Skills y roles | 1 skill (Hermes) | 18 skills (Agent Skills) + 13 roles | ADR 0005 |
| Metodología | SDD implícito | router de 6 dimensiones, 5 modos, mezcla por módulo, ceremonia, deriva | ADR 0006 |
| Comandos | 6 | 36, con semáforo por paso y plantilla de reporte | ADR 0007 |
| Idioma | inglés + español formal | español neutro con tuteo | ADR 0008 |
| Contrato ADS | — | `ads.yaml`, niveles mínimo/extendido, `ads-check` + `agent-conformance` | ADR 0009 |
| Superficie agéntica | — | servidor MCP de ABM (15 tools, 3 recursos), plantillas para ADS, `new-ads` | ADR 0010 |
| Capa System One | — | `abm decide`, umbrales por ceremonia, presets de riesgo e inyección | ADR 0011 |
| Portabilidad | categorías | gateway LLM, matriz multinube, patrones legacy, lenguajes corporativos | ADR 0012 |
| Tokens | tabla manual | ledger JSONL, N1/N2/N3, presupuestos, atestación, import | ADR 0013 |
| Velocidad | "pregunta ante la duda" | turbo + 6 bloqueantes + cola de pendientes | ADR 0014 |
| Comunicación | — | protocolo de salida verificado por lint | ADR 0015 |
| Productos | prohibidos | solo en catálogos; `lint core` en CI | ADR 0016 |

## Métricas antes/después

| Métrica | Antes | Después |
|---|---|---|
| `AGENTS.md` | 169 líneas · ≈ 2 482 tokens | ≈ 2 050 tokens (−17 %) |
| Siempre cargado, núcleo (mismos archivos) | ≈ 3 697 tokens | ≈ 3 305 tokens (−11 %); ≈ 3 999 con la cola de pendientes |
| Metadatos de skills, roles y comandos (herramientas que listan descripciones) | — | ≈ 3 000 tokens (nuevo costo; ver pendientes) |
| Herramientas con adaptador | 4 (1 inoperante) | 9 + fallback `AGENTS.md` (6 lectores verificados) |
| Comandos / páginas de manual | 6 / 0 | 36 / 36 (paridad en CI) |
| Cobertura FE/BE/DB | 0 estándares | 3 capas × 5 artefactos + skill + rol + comando |
| Casos de stack | 0 | 14 + nubes, LLMs (9 precios verificados), legacy, lenguajes |
| Checks de CI activos | 0 | 15 validadores en 3 SO × 2 versiones de Python + 19 tests CLI + 45 tests del ejemplo + markdownlint + escaneo de secretos |
| Conceptos OKF conformes | 35 de 53 | 282 de 282 (0 errores) |
| Contrato ADS de ABM | — | nivel extendido: `ads-check` OK, conformidad 12/12 |

## Criterios de aceptación (§5 del prompt)

| Criterio | Estado | Evidencia |
|---|---|---|
| Diagnóstico, benchmark, plan e informe en OKF | cumple | `docs/analysis/01…05`, `abm okf validate` |
| `AGENTS.md` en presupuesto, tokens en CI, antes/después | cumple | tabla de métricas; `abm token-budget` |
| `sync --check` verde, 9 herramientas + fallback, matriz con fuente y fecha | cumple (con límites documentados) | `/docs/compat-matrix.md`, `/docs/analysis/verificacion/adaptadores.md` |
| Motor metodológico: 5 modos, mezcla, escalamiento, `/drift` | cumple | `methodology/`, recorridos (d) y (f) mixtos |
| FE/BE/DB con la misma estructura | cumple | `standards/{frontend,backend,database}/` |
| Catálogo ≥ 14 casos | cumple | `stacks/README.md` |
| Integraciones MCP/API/otras vías con seguridad | cumple | `integrations/` (13 servidores MCP verificados) |
| 100 % de comandos en el manual | cumple | `abm lint manual` |
| CI en verde | cumple localmente; ejecución en la plataforma de CI sin evidencia | `abm check` 15/15 en 3.9/3.11/3.13 y cp1252 |
| 6 encargos sin huecos; uno ejecutado | cumple (huecos H1–H5 corregidos) | `/docs/analysis/verificacion/recorridos.md`, `examples/panel-ventas/` |
| README, CHANGELOG, MIGRATION, CONTRIBUTING, SECURITY, LICENSE | cumple (licencia provisional, P-003) | raíz del repo |
| Contrato ADS, superficie agéntica, System One, portabilidad, tokens, turbo, protocolo (criterios del prompt v3) | cumple; Jev y Hermes en vivo sin verificar | `ads.yaml`, `abm agent-conformance`, `abm decide`, `TOKENS.md` |

## Verificación (Fase 4)

- **Revisión adversarial** (`/docs/analysis/verificacion/revision-adversarial.md`): 2 críticos, 10 altos, 15 medios y 8 bajos. Corregidos: todos los críticos y altos (bucle infinito del parser, Python 3.9, servidor MCP tumbable, borrado fuera del repo en `sync`, turbo que sobrescribía archivos del usuario y saltaba la denegación de lectura de secretos, falsos negativos del router, inyección que pasaba como "limpia", skill con tools inexistentes, codificación en Windows) y los medios salvo los parciales de abajo. Pruebas de regresión añadidas.
- **Adaptadores vs documentación oficial**: 5 discrepancias. Corregidas: skills en `.github/skills` (Copilot Agent Host), nota de confianza de Codex, alcance Cascade de Windsurf. Documentadas como `no-verificado`: workflows de Antigravity y claves MCP/carga de `AGENTS.md` de Hermes (fuentes contradictorias).
- **Recorridos**: 6 encargos con esqueleto ADS, `ads-check` y conformidad OK; (d) y (f) salen mixtos; 5 huecos corregidos.
- **Evidencia en vivo**: la propia sesión de Claude Code cargó las 18 skills, los 36 comandos y los 13 roles generados por `abm sync`.

## Qué NO está verificado

- Jev real (sin `TYPESAFE_API_KEY`): la capa System One funcionó con el proveedor de reglas (P-006).
- Hermes en vivo (sin credenciales de LLM): conformidad con cliente MCP genérico (P-005).
- Ejecución en Windows y macOS reales y en la plataforma de CI (probado: Python 3.9/3.11/3.13 y salida cp1252 en Linux).
- Antigravity `.agents/workflows/` y claves MCP de Hermes (fuentes contradictorias).
- Calidad de la clasificación con texto libre sin proveedor de decisión (reglas de palabras clave).

## Residuales conocidos

- `yamlmini` acepta en silencio algunos YAML inválidos fuera del subconjunto (B1); `lint core` distingue mayúsculas por diseño (B4); marcas `generated.at` aproximadas en conceptos creados por subagentes (B7).
- Los esquemas `ads.schema.json` y `okf/schema.json` documentan; los validadores ejecutables son `ads-check` y `okf validate` (M12).
- Presupuesto por sesión no implementado (hay por unidad, funcionalidad y total).
- Costo de metadatos (~3 000 tokens) en herramientas que listan todas las descripciones.

## Consumo de esta repotenciación

Ledger `ops/tokens/ledger.jsonl` → `/TOKENS.md` y dashboard N2: subagentes y orquestador, fuente `telemetry` (totales reportados por la sesión, sin desglose entrada/salida: el costo es cota inferior). `abm tokens attest` OK. Umbrales blandos superados en Fase 1, WU5 y Fase 4 (encolados); ningún tope duro.

## Pendientes y próximos pasos

Cola: `/docs/_work/PENDIENTES.md` (P-001 a P-010). Próximos pasos recomendados:

1. Aprobar el plan (P-001) y decidir la licencia (P-003).
2. Verificar Jev con clave (P-006) y Hermes con credenciales (P-005): `./abm decide --provider typesafe-jev`, `./abm agent-conformance --hermes`.
3. Ejecutar la CI en la plataforma y corregir lo que falle en Windows/macOS reales.
4. Decidir si se activa turbo en las herramientas (P-007): `./abm sync --apply-turbo`.
5. Reducir metadatos: filtrar comandos o skills por perfil en `adapters/tools.yaml`.
