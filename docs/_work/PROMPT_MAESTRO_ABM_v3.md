---
type: Prompt
title: Prompt maestro — análisis y repotenciación de ABM (v3)
description: Instrucciones para que un agente analice y repotencie APP_Builder_MAC y los ADS que produce.
tags: [abm, ads, prompt, repotenciacion]
status: draft
generated: { by: claude-code/web, at: 2026-09-27T23:07:20Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format (OKF) v0.2
  - id: typesafe-docs
    resource: https://docs.typesafe.ai/llms.txt
    title: TypeSafe AI documentation index
  - id: hermes-docs
    resource: https://hermes-agent.nousresearch.com/docs/
    title: Hermes Agent documentation
---

# PROMPT MAESTRO — Análisis y repotenciación de APP_Builder_MAC (ABM) · v3

## 0. Parámetros (editar antes de enviar)
- **REPO:** `RicardoTorresOliva/APP_Builder_MAC` (en adelante, **ABM**). Si no está en la sesión, añádelo con `add_repo` y clónalo.
- **RAMA:** la que la sesión designe para este repo. Si no hay ninguna, `feat/abm-v3`. Nunca `main`.
- **MODO:** `TURBO` (por defecto: avanzas sin detenerte salvo ante un bloqueante; ver R12) | `CHECKPOINT` (igual que TURBO, pero además te detienes al final de la Fase 2 a pedir mi aprobación).
- **IDIOMA:** español neutro en todo lo que lee el usuario. Los términos técnicos estándar van en inglés. Los nombres de archivos y comandos van en inglés kebab-case, con alias en español si aportan.
- **OKF:** Open Knowledge Format de Google Cloud. Especificación oficial: `GoogleCloudPlatform/knowledge-catalog/okf/SPEC.md` (v0.2 al 2026-09-27; Anexo D). Es norma obligatoria (R15). `knowledge/README.md` del repo es el perfil de productor de ABM: puede ser más estricto que la especificación, nunca contradecirla. Mantén la interoperabilidad con la capa `conocimiento/` de AGE_Builder.
- **CREDENCIALES OPCIONALES** (solo por variable de entorno, nunca en el repo): `TYPESAFE_API_KEY` (Jev) y claves de proveedores LLM para pruebas. Si faltan, usa el fallback o un mock, marca el resultado `no-verificado` y sigue.
- **ORQUESTACIÓN:** usa subagentes en paralelo para el análisis, la investigación y la revisión. [Opcional: "Autorizo usar un workflow multi-agente en las Fases 1 y 4."]

## 0.1 Glosario vinculante
| Término | Definición |
|---|---|
| **ABM** | APP_Builder_MAC: la fábrica. Este repo. |
| **ADS** | **Activo Digital SLG**: todo lo que produce ABM (app web o móvil, API, dashboard, ERP, automatización, app con IA, informe, producto de datos, producto de inteligencia o un híbrido). ABM produce ADS. |
| **OKF** | Open Knowledge Format: especificación abierta de Google Cloud para conocimiento legible por humanos y agentes (Markdown + frontmatter YAML). Formato obligatorio de todo documento (R15, Anexo D). |
| **Perfil de ADS** | El actual Asset Profile (`profiles/`): fija la completitud, los gates y la ceremonia de cada tipo de ADS. |
| **FU / DU** | Foundation Unit / Deliverable Unit: las unidades con que ABM construye un ADS (ya definidas en `AGENTS.md`). |
| **WU** | Unidad de trabajo de ESTA repotenciación de ABM. No confundir con FU/DU. |
| **Contrato ADS** | Requisitos que cumple todo ADS, y ABM mismo, verificados por `ads-check` (§4.7). |
| **Superficie agéntica** | Interfaces por las que un agente externo (tipo Hermes) descubre, opera y audita un ADS (§4.8). |
| **Capa System One** | Modelo de decisión tipada con confianza calibrada; Jev, de TypeSafe AI, es el primer adaptador (§4.9). |
| **Espacio de tokens** | Ledger más dashboard de consumo de tokens y costo de un ADS o de ABM (§4.12). |
| **Cola de pendientes** | `docs/_work/PENDIENTES.md`: decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado (§4.16). |
| **Bloqueante** | Lo único que detiene el trabajo (R12). |

## 1. Rol y misión
Actúas como Principal Engineer, arquitecto de plataformas de desarrollo agent-native y Tech Writer. La misión tiene dos tiempos, en este orden estricto:
1) **Análisis completo** de ABM tal como está hoy (solo lectura).
2) **Repotenciación completa** basada en ese análisis. El resultado debe ser un mega-repo que:
   - no dependa de una herramienta ni de un modelo concretos;
   - guíe a agentes de IA para producir cualquier ADS, tanto greenfield como sobre stacks corporativos existentes, legacy incluido;
   - haga que todo ADS sea **agent-native y conectable**: operable sin fricción ("seamless") por agentes tipo Hermes;
   - dé a todo ADS un **espacio de control de tokens**;
   - trabaje en **modo turbo** y con **comunicación concreta, sin conversación**;
   - pueda usarlo una persona con conocimientos medios ("vibe coder", no programador) y también un equipo corporativo.

**ABM es su propio primer ADS.** Todo requisito que se exige a un ADS se exige también a ABM, y se verifica con las mismas herramientas.

## 2. Reglas innegociables
1. No se modifica nada hasta terminar y documentar el análisis (Fase 1).
2. Cero invención. Verifica contra la documentación oficial vigente (WebSearch/WebFetch), a la fecha de ejecución: rutas de configuración, formatos, capacidades de cada herramienta, APIs, versiones, precios y afirmaciones metodológicas. Registra fuente y fecha (como `sources` OKF, R15). Lo que no puedas verificar lleva la marca `no-verificado` y no se presenta como hecho. Las afirmaciones comerciales de un proveedor (velocidad, costo, "no alucina") se citan como afirmación del proveedor hasta que las midas.
3. Fuente única de verdad: ningún contenido se copia a mano entre adaptadores; todos se generan.
4. Conserva lo que funciona. Todo lo que se renombre, mueva o elimine va a `MIGRATION.md` con su equivalente y con alias de compatibilidad cuando corresponda. Los proyectos existentes no deben romperse.
5. Seguridad por defecto:
   - nunca secretos en el repo; usa `.env.example`;
   - mínimo privilegio en MCP, APIs y agentes;
   - confirmación humana antes de cualquier acción destructiva, de producción, de pago o externa.
6. Git: un commit atómico por WU, con Conventional Commits. Push solo a la RAMA. No abras un PR salvo que yo lo pida.
7. Reporte fiel: separa siempre lo verificado, lo no verificado y lo pendiente. Si un check falla, muestra la salida recortada a las líneas relevantes.
8. Disciplina de tokens en esta misma tarea:
   - grep antes de leer, y lectura por rangos;
   - los subagentes devuelven conclusiones con evidencia (archivo:línea), no volcados de archivos;
   - no se vuelve a leer lo ya establecido.
9. Continuidad: mantén `docs/_work/PROGRESS.md` (en OKF) con la fase actual, las decisiones, las WU hechas y pendientes, el consumo de tokens y el próximo paso. Actualízalo al cerrar cada WU para que el trabajo sobreviva a la compactación de contexto.
10. La gobernanza actual de ABM (`AGENTS.md` y sus reglas 1–8, perfiles, comandos) es **objeto de análisis**. Respeta sus reglas de seguridad, pero justifica con un ADR cualquier cambio de gobernanza.
11. **Protocolo de salida (anti-verbosidad).** Aplica a ti durante esta tarea, a todo agente que opere ABM y a todo agente que construya un ADS:
    - informa acciones hechas, resultados verificables y medidas concretas; nada más;
    - prohibido: saludos, elogios, disculpas de relleno, repetir la instrucción, anunciar lo que vas a hacer en lugar de hacerlo, preguntas retóricas, resúmenes duplicados, imitar una conversación humana y emojis decorativos;
    - cada línea aporta un hecho, una evidencia, una decisión o un siguiente paso;
    - formato fijo en §6.
12. **Modo turbo por defecto.** Actúa sin pedir permiso en todo lo reversible. Paraleliza: tool calls independientes en un mismo turno y subagentes en paralelo. No esperes confirmación para lo que puedas decidir con un default razonable. Solo te detienes ante un **bloqueante**:
    - a) acción destructiva o irreversible fuera de la RAMA (borrar datos, force-push, reescribir historia ajena);
    - b) producción, pagos, publicación o envío a terceros;
    - c) credencial ausente sin fallback posible;
    - d) cambio de permisos o de seguridad con impacto fuera del repo;
    - e) ambigüedad en la que un default equivocado sea irreversible o cueste más que detenerse.

    Todo lo demás: aplica el default, regístralo en la cola de pendientes (§4.16) y sigue.
13. **Categorías en el núcleo, productos en catálogos.** Se mantiene la regla 7 actual de `AGENTS.md` (sin lock-in). El núcleo nombra categorías ("modelo de decisión tipada", "gateway LLM", "nube"). Los productos (Jev, Hermes, AWS, Azure, etc.) viven solo en `adapters/`, `integrations/`, `stacks/` y `examples/`, cada uno con su fecha de revisión.
14. **Precedencia ante conflicto:** seguridad (R5) > reglas de este prompt > `AGENTS.md` actual > defaults. Todo conflicto resuelto queda registrado en un ADR.
15. **OKF obligatorio (Open Knowledge Format de Google Cloud).** Todo documento que produzcan ABM y cada ADS es un concepto OKF conforme a la especificación oficial vigente (v0.2 al 2026-09-27; Anexo D) y al perfil ABM. Incluye PROGRESS, PENDIENTES, ADRs, análisis, manual, playbooks, fichas de stack y la matriz de compatibilidad. Exige:
    - frontmatter YAML con `type` (obligatorio), `title`, `description` y `tags`;
    - `generated: { by, at }` con la convención de actores de la spec (`<herramienta>/<versión>`, `human:<id>`, `process:<id>`) y fechas ISO 8601 con zona UTC; `timestamp` queda obsoleto;
    - `verified` solo cuando hubo una verificación real; un concepto sin `verified` es `no-verificado` (R2);
    - `sources` con `id` y una nota al pie por cada afirmación verificada: así se cumple "fuente y fecha" (R2);
    - `status` (`draft` | `stable` | `deprecated`) y `stale_after` en todo lo que caduca: precios, versiones, stacks, compat-matrix e insumos de proveedores;
    - `index.md` y `log.md` en cada bundle (el perfil ABM los exige; la spec los deja opcionales) y `okf_version` en el `index.md` raíz;
    - enlaces entre conceptos en la forma que fije el ADR 4 (la spec recomienda `/ruta.md`, relativa a la raíz del bundle);
    - `Attested Computation` para cifras que deben calcularse de forma sancionada (costos del espacio de tokens, métricas de productos de datos).

    El perfil ABM puede ser más estricto que la especificación, nunca contradecirla.

## 3. Fases

### Fase 0 — Preparación
- Asegura el acceso al repo y la rama. Revisa el árbol a 2–3 niveles, el tamaño de los archivos y `README.md`, `QUICKSTART.md`, `START_PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, `adapters/` (incluido `adapters/hermes/SKILL.md`), `profiles/`, `commands/`, `scripts/` y `ci/`.
- **Adopta OKF** (R15):
  - verifica la versión vigente de la especificación oficial y su changelog (Anexo D). Si no puedes acceder a ella, usa el Anexo D, márcalo `no-verificado` y sigue;
  - contrasta `knowledge/README.md` y los documentos existentes con esa versión (brechas iniciales en el Anexo D);
  - esboza el perfil ABM: valores de `type` por documento (intent, spec, ADR, informe, manual…) y campos obligatorios por tipo. Se formaliza en el ADR 4;
  - registra en la cola de pendientes la alineación de `conocimiento/` de AGE_Builder, que está fuera de este repo;
  - desde este momento, todo documento que crees nace conforme (PROGRESS y PENDIENTES incluidos).
- Crea `docs/_work/PROGRESS.md` y `docs/_work/PENDIENTES.md`.
- **Línea base** para el antes/después: tokens que se cargan siempre (≈ caracteres/4), número de comandos, herramientas soportadas, checks de CI y capacidades agénticas existentes.

### Fase 1 — Análisis completo (solo lectura)
Analiza con evidencia las siguientes dimensiones, en paralelo con subagentes:

| # | Dimensión | Preguntas clave |
|---|---|---|
| D1 | Inventario y mapa | ¿Qué existe? ¿Para qué sirve cada pieza? ¿Cómo pasa un usuario de "idea" a "ADS entregado y operando"? |
| D2 | Gobernanza y flujo | Perfiles, FU/DU, comandos, memoria, gates de revisión: ¿qué funciona, qué sobra, qué falta? ¿Qué reglas frenan el modo turbo sin aportar seguridad? |
| D3 | Compatibilidad multi-herramienta | ¿Qué herramientas soporta hoy (Hermes incluido) y con qué fidelidad? |
| D4 | Metodologías | ¿Qué soporta frente a Vibe / IDD / SDD / SPDD / AIDD híbrido (Anexo A)? ¿Puede mezclarlas por encargo y por módulo? |
| D5 | Paridad FE/BE/DB | ¿Tienen las tres capas la misma profundidad (estándares, skills, checklists, revisión, tests)? |
| D6 | Stacks y plantillas | ¿Qué opciones ofrece por tipo de ADS? ¿Siguen vigentes? |
| D7 | Integraciones y seguridad | MCP, APIs, webhooks, secretos, permisos, riesgo de prompt injection. |
| D8 | Eficiencia de tokens | Tokens (≈ caracteres/4) de lo que se carga siempre frente a lo que se carga bajo demanda; duplicación; verbosidad. |
| D9 | UX para vibe coder | Onboarding, claridad, lenguaje, manual, recuperación ante errores. |
| D10 | Calidad documental | Consistencia, duplicados, enlaces rotos, obsolescencia, cumplimiento de OKF. |
| D11 | Calidad del propio repo | CI, validadores, tests, licencias, versionado, changelog, portabilidad de los scripts (hoy `.sh`). |
| D12 | Superficie agéntica y conectividad | ¿Puede un agente externo (Hermes u otro) descubrir, operar y auditar ABM y los ADS que produce? ¿Qué protocolos expone (MCP, API, CLI, A2A, skills)? |
| D13 | Portabilidad corporativa | ¿Soporta brownfield y legacy, varios lenguajes de programación, varios proveedores LLM, varias nubes y escalamiento? |
| D14 | Observabilidad de tokens y costo | ¿Se mide lo que cuesta construir un ADS y lo que cuesta operarlo? ¿Hay presupuestos, alertas, dashboard? |
| D15 | Velocidad y verbosidad | Pasos seriales evitables, confirmaciones innecesarias, playbooks que inducen verbosidad, ausencia de formato de salida. |
| D16 | Capa de decisión System One | ¿Dónde aportaría Jev (TypeSafe AI) en ABM y en los ADS? ¿Con qué riesgos y qué fallback? (Anexo B) |

Haz además un **benchmark** frente a estos referentes, verificando que siguen vigentes: GitHub Spec Kit, AWS Kiro (specs/steering), BMAD Method, Agent OS, el estándar AGENTS.md, Agent Skills (SKILL.md / agentskills.io), las reglas de Cursor y Copilot, los repos de skills de Anthropic y OpenAI, **Hermes Agent** (Nous Research), la especificación MCP vigente, el protocolo A2A, `llms.txt`, las convenciones semánticas GenAI de OpenTelemetry, los gateways LLM (como categoría) y **TypeSafe AI / Jev**. Toma ideas, no copies, y respeta las licencias.

**Investigación dirigida** (obligatoria, con fuente y fecha):
- **Hermes:** cómo carga el contexto (`AGENTS.md`, skills), configuración MCP (`mcp_servers`), delegación, gateway de mensajería y límites. Qué necesita un ADS para que Hermes lo opere sin fricción. (Insumo: Anexo C.)
- **Jev:** API, SDKs, tipos de pregunta, confianza, patrones oficiales, agent skill oficial, limitaciones conocidas, disponibilidad, precios, términos de datos y si existe o no un servidor MCP. Diseña al menos 3 puntos de integración en ABM y 5 recetas para ADS, cada uno con su fallback. (Insumo: Anexo B.)
- **Telemetría de uso:** qué consumo de tokens expone cada herramienta y cada proveedor (OpenTelemetry, logs de sesión, APIs de uso).

Entregables (en OKF):
- `docs/analysis/01-diagnostico.md`, con:
  - resumen ejecutivo de una página como máximo;
  - scorecard de 0 a 5 por dimensión, con evidencia;
  - fortalezas que hay que conservar;
  - brechas, riesgos y deuda;
  - quick wins.
- `docs/analysis/02-benchmark.md`.
- `docs/analysis/03-investigacion-agentica.md`: Hermes, Jev, protocolos de conectividad y telemetría de uso por herramienta.

### Fase 2 — Diseño objetivo y roadmap
- Arquitectura objetivo (árbol comentado) según la sección 4.
- ADRs en `docs/adr/NNNN-titulo.md`, como mínimo sobre:
  1. nomenclatura ABM/ADS y glosario;
  2. fuente única y generador de adaptadores;
  3. lenguaje de los scripts (multiplataforma Windows/macOS/Linux, con cero o mínimas dependencias);
  4. OKF: adopción de la especificación oficial vigente, perfil ABM (tipos, campos obligatorios, forma de los enlaces), migración de la convención actual y compatibilidad con AGE_Builder;
  5. estándar de skills;
  6. router metodológico;
  7. nomenclatura de comandos;
  8. idioma;
  9. Contrato ADS y sus niveles por perfil;
  10. superficie agéntica: protocolos por perfil, y si ABM expone su propio servidor MCP o le bastan skill + CLI;
  11. capa System One: interfaz, adaptador Jev, umbrales de confianza y fallback;
  12. portabilidad: gateway LLM, matriz multinube y estrategia legacy;
  13. espacio de tokens: esquema del ledger, fuentes de telemetría, niveles de dashboard y presupuestos;
  14. modo turbo y cola de pendientes, y su encaje con las reglas 1 (Planning Gate) y 4 (alcance) de `AGENTS.md`;
  15. protocolo de salida y cómo se hace cumplir;
  16. reconciliación "categorías en el núcleo / productos en catálogos" (regla 7).
- Plan de migración y roadmap de WU priorizadas por impacto/esfuerzo. Cada WU indica: objetivo, archivos, criterio de aceptación y cómo se verifica.
- `docs/analysis/04-plan.md` (OKF).
- **GATE:** publica un resumen de una pantalla (diagnóstico, decisiones clave, roadmap).
  - `TURBO`: registra "Aprobar plan" en la cola de pendientes y continúa. Todo está en la RAMA y es reversible.
  - `CHECKPOINT`: detente y espera mi aprobación.

### Fase 3 — Implementación por WU
Orden sugerido; ajústalo según el diagnóstico:
- WU1 Núcleo: glosario ABM/ADS; OKF (perfil ABM, JSON Schema, validador y migración de `knowledge/` y `docs/` a la versión vigente); `AGENTS.md` canónico mínimo con protocolo de salida y turbo; estructura base.
- WU2 Generador de adaptadores (`sync`), con modo `--check` para CI. Incluye Hermes.
- WU3 Contrato ADS y verificador `ads-check`. Desde aquí se aplica también a ABM.
- WU4 Motor metodológico y plantillas.
- WU5 Comandos, skills y agentes-rol.
- WU6 Paridad FE/BE/DB.
- WU7 Superficie agéntica: plantillas (manifiesto, SKILL.md del ADS, servidor MCP, OpenAPI, CLI `--json`, `llms.txt`, A2A cuando aplique) y prueba de conformidad con Hermes.
- WU8 Capa System One: interfaz, adaptador Jev, fallback LLM, uso en el router y en el semáforo de ABM, recetas para ADS.
- WU9 Portabilidad corporativa: gateway LLM, matriz multinube, recetas legacy, escalabilidad.
- WU10 Catálogo de stacks y recetas.
- WU11 Integraciones MCP/API y seguridad.
- WU12 Tokens: espacio de control (ledger, CLI `tokens`, dashboards por nivel) y optimización (medición y presupuestos en CI).
- WU13 Turbo y protocolo de salida: configuración turbo por herramienta, cola de pendientes y comando `pending`, lint de playbooks.
- WU14 Manual de comandos, onboarding, glosario, FAQ y troubleshooting.
- WU15 Ejemplos golden-path y CI completo.
- WU16 README, CHANGELOG, MIGRATION, CONTRIBUTING, SECURITY, LICENSE.

Ciclo de cada WU: implementar → autoverificar → registrar el consumo de la WU en el ledger de ABM → actualizar PROGRESS y PENDIENTES → commit → push.

### Fase 4 — Verificación
- Ejecuta todos los validadores: OKF, markdownlint, enlaces, `sync --check`, presupuesto de tokens, secret scan, `ads-check` (sobre ABM y sobre cada ejemplo) y lint de playbooks (plantilla de salida presente y dentro de presupuesto).
- Recorre como un vibe coder, de principio a fin, seis encargos simulados usando solo la documentación y los comandos:
  - (a) landing con formulario;
  - (b) dashboard con auth, base de datos y gráficos;
  - (c) app móvil con backend;
  - (d) mini-ERP con inventario, ventas, facturación y roles;
  - (e) producto de inteligencia para un cliente de consultoría (informe + dataset o dashboard);
  - (f) brownfield corporativo: módulo nuevo sobre un ERP legacy on-prem (SQL Server + servicios SOAP), desplegado en Azure, con proveedor LLM intercambiable por configuración (p. ej., Azure OpenAI ↔ AWS Bedrock) sin tocar el código.

  En cada uno comprueba:
  - que el router elige un modo razonable (y uno mixto en d y f);
  - que cada paso tiene su comando, skill o plantilla, y que no quedan huecos;
  - que el ADS resultante cumple el Contrato ADS: un agente externo lo descubre, lista sus capacidades, ejecuta una operación de lectura y otra con `--dry-run`, y consulta su espacio de tokens. Usa Hermes si se puede instalar; si no, un cliente MCP genérico, y decláralo;
  - que la capa System One decide al menos un punto del flujo en (b) o (f): Jev real si hay clave; si no, el fallback, marcado `no-verificado`;
  - que se genera el dashboard de tokens del nivel que corresponde al perfil.

  Si el entorno lo permite, genera y ejecuta al menos el (b), con build y tests.
- Mide velocidad y brevedad: tiempo y tokens por encargo; longitud de los reportes frente al formato de §6.
- Lanza una revisión independiente y adversarial del diff completo con un subagente revisor, y corrige lo que encuentre.
- Contrasta cada adaptador con la documentación oficial de su herramienta.

### Fase 5 — Cierre
- `docs/analysis/05-informe-final.md` (OKF), con:
  - qué cambió y por qué;
  - métricas antes/después: tokens siempre cargados, herramientas soportadas, comandos documentados, cobertura FE/BE/DB, checks en CI, requisitos del Contrato ADS que cumple ABM, y tokens y costo de esta repotenciación (según el ledger);
  - qué está verificado y qué no;
  - pendientes y próximos pasos, con la cola de pendientes consolidada.
- En el chat: reporte en el formato de §6, con enlaces a los archivos. Ofrece abrir un PR, pero no lo abras sin permiso.

## 4. Especificación del ABM objetivo

### 4.0 ABM → ADS
- ABM es la fábrica. Cada ADS es un activo con identidad propia: manifiesto, versión, perfil y dueño.
- Tipos de ADS = perfiles. Parte de los actuales (`software-app`, `research-report`, `data-product`, `intelligence-product`) y añade los que justifique el diagnóstico (p. ej., automatización/integración o app con IA/agéntica).
- Todo ADS cumple el Contrato ADS (§4.7). ABM también.
- Frontera con AGE_Builder (la fábrica de arneses de agentes de SLG): ABM no duplica su alcance. Si un encargo es un arnés de agente, ABM lo detecta, lo indica e interopera vía OKF. Verifica esta frontera con lo que dice el repo sobre AGE_Builder.

### 4.1 Principios
- Independiente de la herramienta y del modelo.
- Agent-native: todo ADS es operable por agentes; la conectividad es un requisito, no un extra.
- Portable: se adapta al stack corporativo existente, legacy incluido; multi-lenguaje, multi-LLM, multinube y escalable.
- Observable: el consumo de tokens y el costo son visibles en todo ADS y en ABM.
- Rápido y conciso: turbo por defecto y comunicación concreta.
- Fuente única y adaptadores generados.
- Divulgación progresiva: se carga solo lo necesario.
- Seguro por defecto, con un humano en el bucle donde importa.
- Frontend, backend y base de datos con el mismo peso.
- Todo documento en OKF.
- Accesible para no programadores sin renunciar al rigor profesional.

### 4.2 Estructura (propuesta; parte de lo existente y se valida en la Fase 2)
```
AGENTS.md                 # canónico y corto: identidad, reglas, protocolo de salida, turbo, punteros
okf/                      # SPEC.md (extiende knowledge/README.md), schema.json, templates/
knowledge/                # (existe) bundles OKF del ADS activo
profiles/                 # (existe) perfiles de ADS: completitud, gates, ceremonia, nivel del contrato
contract/                 # Contrato ADS: requisitos, niveles por perfil, ads.schema.json (manifiesto)
commands/                 # (existe) playbooks neutrales (1 archivo = 1 comando)
skills/<name>/SKILL.md    # estándar Agent Skills + references/ bajo demanda
agents/                   # roles: orchestrator, architect, frontend, backend, data, security, qa,
                          #        reviewer, devops, docs, integrations, agentic, finops
methodology/              # router + vibe, idd, sdd, spdd, aidd + reglas de mezcla/escalamiento
standards/                # frontend/ backend/ database/ security/ testing/ observability/ a11y/
                          # agentic/ (diseño agent-friendly) finops/ (tokens y costo)
stacks/                   # catálogo + matrices + recetas; legacy/ clouds/ llm-providers/
integrations/             # mcp/ api/ webhooks/ auth/ agents/ (hermes, a2a) decision/ (typesafe-jev)
                          # llm-gateway/ observability/
templates/                # intent, spec, plan, tasks, prompt-contract, methodology-map, adr, closeout,
                          # handoff, ads-manifest, agent-skill, mcp-server, token-dashboard, pending-queue
docs/                     # manual/, guides/, glossary, faq, troubleshooting, compat-matrix,
                          # adr/, analysis/, _work/
examples/                 # (existe) golden paths; el núcleo nunca los referencia
scripts/                  # sync, doctor, validate-okf, token-budget, ads-check, agent-conformance,
                          # tokens, pending, new-ads
ci/ + .github/workflows/  # CI del propio repo
adapters/                 # (existe) fuentes de los adaptadores. Salida generada (rutas exactas a verificar
                          # en la Fase 2): CLAUDE.md, .claude/ · Codex (.codex/ o .agents/) · Antigravity
                          # (.agent/) · GEMINI.md, .gemini/ · .github/ (Copilot) · .cursor/ · .windsurf/
                          # · .kiro/ · Hermes (skill + plantilla mcp_servers) · .clinerules · .junie/ …
```

### 4.3 Compatibilidad multi-herramienta
- Herramientas mínimas: Claude Code, OpenAI Codex (CLI/IDE/cloud), Google Antigravity, VS Code con GitHub Copilot, Cursor, Gemini CLI, Windsurf, Kiro y **Hermes Agent**. Cualquier otra (Zed, JetBrains/Junie, Cline/Roo, Aider, OpenCode, Amp…) queda cubierta por `AGENTS.md` como fallback universal.
- En `docs/compat-matrix.md` documenta y verifica, para cada herramienta: archivo de instrucciones, reglas por ruta, comandos/prompts/workflows, skills, subagentes, hooks, configuración MCP, archivos ignore, límites, **configuración turbo** (modos de permisos, auto-aprobación y allowlists seguras vigentes) y **telemetría de uso disponible** (para el espacio de tokens). Cada celda lleva fuente y fecha.
- El generador construye cada adaptador a partir de `commands/`, `skills/`, `agents/` y `standards/`.
- Degradación elegante: si una herramienta no soporta subagentes, hooks o skills, el playbook trae un fallback secuencial en lenguaje natural ("ejecuta el playbook `commands/x.md`").
- `scripts/doctor` detecta la herramienta, el sistema operativo y las dependencias, y explica en lenguaje simple qué falta.

### 4.4 Motor metodológico (integra el Anexo A)
Principio: no existe una metodología mejor para todo. ABM elige y **mezcla** según el encargo y **por módulo**.

**Clasificación del encargo** (con `/methodology` o dentro de `/init-project`):
- incertidumbre;
- criticidad y riesgo: dinero, datos personales, salud, regulación;
- horizonte: prototipo desechable / MVP / producto / sistema crítico;
- tamaño del equipo;
- greenfield o brownfield, y restricciones del stack corporativo existente;
- autonomía deseada para el agente.

La clasificación puede apoyarse en la capa System One (preguntas Choice/Score con confianza). Con confianza baja, cae al LLM o entra en la cola de pendientes. La decisión y su confianza quedan en el `methodology-map.md`.

**Modos:**
- `VIBE`: exploración rápida en una rama sandbox, con tiempo acotado y desechable. Salida obligatoria: aprendizajes que se pasan a `/consolidate`.
- `IDD` (Minimum Viable Spec): `intent.md` organizado como árbol Propósito → Usuario → Medios, más restricciones, criterios de éxito y no-objetivos. El agente decide el "cómo" y lo registra en ADRs ligeros.
- `SDD`: requirements → design → tasks, con trazabilidad requisito ↔ tarea ↔ test. Compatible con los formatos de Spec Kit y Kiro (verificar).
- `SPDD`: contratos de prompt versionados (`prompt-contract.md`: versión, intención, entradas, salidas, invariantes, tests de aceptación y archivos vinculados), sincronizados en ambos sentidos con el código.
- `AIDD` híbrido: explorar con Vibe → consolidar en IDD o SDD → construir con revisión humana obligatoria → closeout.

**Mezcla:**
- Cada ADS tiene un `methodology-map.md` que asigna a cada módulo un modo y una justificación.
- Reglas de escalamiento automático. Por ejemplo: pagos, auth, datos personales o de salud → SDD con revisión humana; una landing → IDD; un experimento → VIBE.
- Reglas de desescalamiento equivalentes.

**Control de deriva:** `/drift` compara la intención, la spec y los contratos con el código y propone actualizaciones. El closeout de cada FU/DU obliga a sincronizarlos.

**Capa de gobernanza** opcional para el perfil regulado: trazabilidad alineada con ISO/IEC 42001, NIST AI RMF y EU AI Act. Es orientativa, no asesoría legal.

**Niveles de ceremonia** (por ejemplo Prototipo / MVP / Producto / Enterprise-Regulado): cada uno fija un modo por defecto, sus gates, su nivel de Contrato ADS y su nivel de dashboard de tokens. Se integran con los perfiles de ADS existentes; la forma exacta se decide por ADR.

### 4.5 Paridad Frontend / Backend / Database
Las tres capas reciben la misma estructura: estándar, checklist de DoD, skill(s), agente-rol, comando, plantillas, tests y criterios de revisión.

- **Frontend:**
  - design system y tokens, componentes;
  - accesibilidad WCAG 2.2 AA, responsive y mobile-first;
  - rendimiento (Core Web Vitals);
  - estado, formularios y validación;
  - i18n y SEO;
  - tests unitarios, de componente y E2E.
- **Backend:**
  - diseño de API: REST con OpenAPI, GraphQL, tRPC o RPC; la superficie agéntica (§4.8) forma parte del diseño;
  - validación y manejo de errores;
  - authN/authZ y rate limiting;
  - jobs, colas y caché;
  - observabilidad: logs estructurados y OpenTelemetry;
  - idempotencia;
  - tests unitarios, de integración y de contrato.
- **Database:**
  - modelado con ERD en Mermaid; normalización frente a desnormalización;
  - migraciones versionadas y reversibles, y seeds;
  - índices, integridad y rendimiento de las consultas;
  - RLS y permisos, auditoría;
  - backups y restauración;
  - multi-tenant;
  - tipos generados;
  - privacidad y retención de datos.
- **Transversal:** pirámide de tests, CI/CD, entornos (dev/staging/prod), feature flags, costos y FinOps (incluidos tokens).

### 4.6 Catálogo de stacks
`stacks/` contiene una matriz por caso: landing/marketing, web app SaaS, dashboard/BI interno, e-commerce, app móvil, desktop, API/backend puro, ERP/CRM/backoffice, apps con IA (RAG/agentes), tiempo real, automatizaciones/integraciones, CLI/extensiones, **integración sobre legacy corporativo** y **producto de inteligencia/consultoría**.

Cada caso incluye:
- la opción **recomendada para vibe coder**;
- una alternativa **pro/escalable**;
- una alternativa **low-cost/self-hosted**;
- una variante **corporativa/legacy** y sus equivalencias por nube (AWS / Azure / GCP / on-prem);
- cuándo NO usar cada opción;
- costo aproximado, curva de aprendizaje y hosting;
- FE, BE, DB, auth, pagos y deploy como un paquete coherente;
- proveedor LLM y capa System One cuando el caso usa IA;
- nivel de superficie agéntica y de dashboard de tokens por defecto;
- "comprar vs construir" (por ejemplo, ERP: Odoo/ERPNext frente a uno a medida).

Las versiones y precios se verifican a la fecha, y cada ficha lleva `sources` y `stale_after` (OKF). `/stack` hace preguntas simples, recomienda y explica el porqué.

### 4.7 Contrato ADS
Todo ADS, y ABM, declara un manifiesto `ads.yaml` validado por `contract/ads.schema.json` y cumple los requisitos según el nivel que fije su perfil:

| Requisito | Mínimo (todo ADS) | Extendido (software, datos, IA) |
|---|---|---|
| Identidad | `ads.yaml`: id, versión semántica, perfil, dueño, capacidades, endpoints, auth, límites | + SLO y entornos |
| Gobernanza del agente | `AGENTS.md` propio con protocolo de salida y turbo | + adaptadores generados |
| Superficie agéntica | SKILL.md para operarlo + `llms.txt` + bundle OKF navegable | + API (OpenAPI/GraphQL), servidor MCP, CLI `--json`, eventos/webhooks, A2A si es un agente |
| Espacio de tokens | ledger + reporte (N1) | dashboard N2 o N3, presupuestos y alertas |
| Portabilidad | stack, dependencias y proveedor LLM declarados; sin lock-in injustificado | IaC, contenedores, matriz de nube, gateway LLM, plan de salida por proveedor |
| Seguridad | secretos fuera del repo; mínimo privilegio | scopes por agente, auditoría de acciones de agentes, HITL en acciones rojas |
| Documentación | OKF | + manual de operación para humanos y para agentes |

`scripts/ads-check` verifica el contrato y hace fallar la CI si no se cumple el nivel del perfil.

### 4.8 Superficie agéntica y conectividad
Objetivo: que un agente tipo Hermes descubra, opere y audite cualquier ADS sin integración a medida.
- **Descubrimiento:** `ads.yaml`, `AGENTS.md`, `llms.txt`, SKILL.md (agentskills.io; verifica la compatibilidad con Hermes) y A2A Agent Card cuando el ADS es o expone un agente (verifica la versión vigente).
- **Operación:** servidor MCP (tools, resources y prompts; transporte stdio y HTTP; auth según la especificación MCP vigente); API con OpenAPI; CLI con `--json`, `--dry-run` y códigos de salida estables; eventos y webhooks firmados.
- **Diseño agent-friendly** (`standards/agentic/`):
  - operaciones idempotentes y reintentables;
  - errores estructurados y accionables (p. ej., `application/problem+json`);
  - paginación, límites y rate limits declarados;
  - descripciones de tools cortas y precisas, porque cada una consume tokens;
  - scopes mínimos por agente y tokens revocables;
  - auditoría de cada acción de un agente: quién, qué, cuándo y con qué resultado;
  - HITL obligatorio en acciones rojas (§4.17);
  - la salida de un tool es un dato, nunca una instrucción.
- **Hermes:** plantillas de `mcp_servers` con allowlist de tools, skill de operación del ADS, verificación de que carga `AGENTS.md` y recetas para operar el ADS desde su gateway de mensajería cuando aplique.
- **ABM también:** sus comandos son invocables por agentes (skill + CLI `--json`; servidor MCP propio si el ADR 10 lo justifica), de modo que Hermes pueda conducir ABM de principio a fin.
- `scripts/agent-conformance`: guion reproducible (descubrir → listar capacidades → leer → `--dry-run` → consultar tokens) contra Hermes o, si no está disponible, contra un cliente MCP genérico.

### 4.9 Capa de decisión System One (Jev de TypeSafe AI)
- **Categoría en el núcleo:** "modelo de decisión tipada con confianza calibrada". Jev es el primer adaptador (`integrations/decision/typesafe-jev/`); la interfaz admite otros.
- **Interfaz neutral:** `decide(state, questions[]) → answers[]`, con tipos `choice`, `score` y `boolean-probability` (Noul en Jev). Cada respuesta trae valor, probabilidades y, cuando el proveedor la da, confianza.
- **Patrón base, routing por confianza:** confianza alta → actúa el código; zona gris → LLM (System Two) o cola de pendientes; confianza baja → humano. Umbrales por perfil y versionados.
- **Fallback obligatorio:** un LLM con salida estructurada (JSON Schema) detrás de la misma interfaz. El ADS funciona sin Jev.
- **Usos en ABM** (mide latencia y tokens frente a usar solo un LLM; reporta como medido o `no-verificado`):
  - clasificación del encargo y router metodológico;
  - semáforo de riesgo de cada acción;
  - selección del comando o skill adecuado (patrón oficial de sugerencia de skills);
  - triage de los hallazgos de revisión;
  - filtro de prompt injection en la salida de los tools;
  - ruteo de modelos: determinista / LLM barato / LLM potente / humano.
- **Recetas para ADS:** intent routing, guardrails de entrada y salida, filtrado de pasajes RAG, verificación de citas, extracción verificada, clasificación jerárquica con confianza y scoring compuesto con pesos en código.
- **Seguridad y datos:** el `state` puede contener datos personales, así que pasa por el gate de gobernanza de datos del perfil. La clave va solo por entorno. Las decisiones quedan registradas y son auditables; su consumo va al ledger.
- **Verifica antes de implementar:** estado de acceso (early access o GA), precios, SDKs, versión del modelo, limitaciones conocidas, términos de datos y licencia del agent skill oficial.

### 4.10 Portabilidad corporativa
- **Brownfield/legacy:** un comando `assess` (nombre final por ADR) inventaría el stack existente —lenguajes, frameworks, bases de datos, middleware, IdP, CI/CD, nube, políticas y restricciones de red— y lo registra en OKF.
  - Patrones de integración: strangler fig, anti-corruption layer, fachada API, CDC/eventos, batch/SFTP/EDI; RPA solo como último recurso.
  - SSO corporativo (SAML/OIDC y directorios corporativos), proxies, redes privadas y on-prem.
- **Lenguajes de programación:** recetas y estándares para los dominantes en entornos corporativos (p. ej., TS/JS, Python, Java/Kotlin, C#/.NET, Go, PHP) e interoperabilidad con legacy (mainframe vía APIs o colas; ERPs vía sus interfaces oficiales). Prioriza según el diagnóstico.
- **Multi-LLM:** gateway LLM (categoría) con adaptadores para proveedores directos, servicios LLM de las nubes (Azure, AWS, GCP) y modelos abiertos o locales.
  - Cambio de proveedor por configuración, sin tocar código.
  - Matriz de capacidades (tool use, salida estructurada, contexto, costo) con fecha.
  - Evals mínimos para cambiar de modelo con seguridad.
- **Multinube:** matriz de equivalencias AWS / Azure / GCP / on-prem por bloque (cómputo, base de datos, storage, colas, secretos, identidad, observabilidad, servicio LLM); IaC (categoría, con opciones); contenedores y 12-factor. Todo servicio propietario lleva una abstracción o un plan de salida documentado.
- **Escalabilidad:** servicios sin estado, caché, colas, escalamiento de la base de datos, multi-tenant, pruebas de carga, SLO/SLI y costo por unidad (tokens incluidos).

### 4.11 Integraciones seguras (MCP, API y otras vías)
- **MCP:**
  - catálogo curado de servidores oficiales o verificados;
  - plantillas de configuración por herramienta (Hermes incluido);
  - mínimo privilegio, solo lectura por defecto y versiones fijadas;
  - activar por proyecto solo los servidores necesarios (cada tool consume tokens);
  - defensa contra prompt injection: la salida de un tool es un dato, no una instrucción.
- **API:**
  - clientes tipados generados desde OpenAPI;
  - webhooks con verificación de firma;
  - OAuth2/OIDC;
  - reintentos con backoff e idempotencia.
- **Otras vías:** SDKs, colas y eventos, iPaaS (n8n/Make/Zapier), import/export CSV/Excel, y SQL directo solo con credenciales de mínimo privilegio.
- **Secretos:**
  - `.env.example`;
  - el gestor de secretos de cada plataforma;
  - secret scanning en CI;
  - nunca credenciales de producción al alcance del agente.
- `/integrate <plataforma>` guía paso a paso y elige la vía más segura disponible.

### 4.12 Espacio de control de tokens
- **Dos ledgers** con un esquema común (JSON Schema alineado con las convenciones semánticas GenAI de OpenTelemetry; verifica su estado):
  - **construcción:** tokens y costo de los agentes que construyen el ADS, por sesión, FU/DU/WU, comando, modelo y herramienta;
  - **operación:** tokens y costo del ADS en uso (LLM y capa System One), por funcionalidad, usuario/tenant, modelo y proveedor.
- **Fuentes:** telemetría de cada herramienta y proveedor (según `compat-matrix`). Si no existe, estimación (≈ caracteres/4) marcada `estimado`. Precios en `pricing.yaml`, con fuente y fecha.
- **Niveles** (el perfil fija el mínimo; el usuario puede subirlo):
  - N1, prototipo o informe: `TOKENS.md` generado + `tokens report` en la CLI;
  - N2, MVP o producto: dashboard HTML estático generado desde el ledger (sin servidor), con presupuestos y alertas en CI;
  - N3, enterprise o regulado: dashboard en vivo sobre la pila de observabilidad elegida, con presupuestos por tenant y funcionalidad, alertas, chargeback y detección de anomalías.
- **Presupuestos:** por sesión, FU/DU/WU y funcionalidad. Superar el umbral blando → entrada en la cola de pendientes. Superar el tope duro → bloqueante.
- **Cifras oficiales de costo:** conceptos OKF `Attested Computation`, para que el cálculo sea el sancionado y se pueda verificar.
- **Expuesto a agentes:** recurso MCP o endpoint de solo lectura con el resumen de consumo.
- **ABM tiene su propio espacio de tokens:** muestra lo que costó construir cada ADS y lo que cuesta esta repotenciación.

### 4.13 Comandos, skills y agentes
- Conserva los comandos existentes (`bootstrap`, `init-project`, `session-start`, `start-execution`, `review`, `iterate`), o crea alias para ellos. Semilla por ciclo de vida (los nombres finales se fijan por ADR):
  - Arranque: `bootstrap`, `doctor`, `session-start`, `help`, `pending`
  - Descubrir y definir: `init-project` (wizard), `assess`, `methodology`, `intent`, `spec`, `prompt-contract`, `plan`, `stack`, `explore`, `consolidate`
  - Construir: `start-execution`, `ui`, `api`, `db`, `connect` (superficie agéntica), `decide` (capa System One), `integrate`, `test`
  - Asegurar: `review`, `security`, `drift`, `perf`, `a11y`, `ads-check`
  - Medir: `tokens`
  - Entregar e iterar: `deploy`, `release`, `closeout`, `iterate`, `fix`, `refactor`
- Cada comando es un playbook neutral con: propósito, cuándo usarlo, entradas, pasos clasificados en verde/amarillo/rojo, salidas (en OKF), gates, fallback, plantilla de salida (§6 y §4.17) e invocación por agentes (CLI/MCP).
- Las skills llevan un frontmatter corto y preciso, para que se disparen de forma fiable; el cuerpo y las references se cargan bajo demanda.
- Cada agente-rol define alcance, entradas, salidas y DoD. El revisor siempre es independiente de quien construye.

### 4.14 Manual de comandos (`docs/manual/`)
Pensado para no programadores:
- índice y cheatsheet de una página;
- por cada comando:
  - qué hace y cuándo usarlo;
  - qué escribes (ejemplo literal);
  - qué hará el agente y qué obtienes;
  - errores comunes y cómo salir de ellos;
  - una tabla con cómo invocarlo en cada herramienta, y cómo lo invoca un agente;
- "Tus primeros 15 minutos", glosario, FAQ y troubleshooting;
- cómo leer la cola de pendientes y el dashboard de tokens;
- "cómo deshacer": los checkpoints de git explicados sin jerga.

CI comprueba que cada comando tiene su entrada en el manual y viceversa.

### 4.15 Optimización de tokens (de ABM y de los ADS que produce)
- Lo que se carga siempre es mínimo (objetivo: `AGENTS.md` de unas 150 líneas como máximo) y apunta al resto. Todo lo demás se carga bajo demanda: skills, references y standards por ruta.
- CI mide un presupuesto por archivo (`scripts/token-budget`).
- Un repo map / context map generado evita escanear todo el repo.
- Archivos ignore para cada herramienta (verifica los nombres vigentes).
- Memoria de proyecto compacta (STATE/HANDOFF en OKF), actualizada al cerrar cada FU/DU.
- Subagentes de exploración que devuelven conclusiones.
- Ruteo de modelos: uno rápido y barato para búsqueda y formato; uno potente para arquitectura y revisión; la capa System One para decisiones cortas y tipadas cuando la medición lo justifique.
- Prefijos estables para favorecer el prompt caching.
- Diffs en lugar de reescrituras completas; grep antes de leer; lectura por rangos.
- Plantillas y CLIs de scaffolding en lugar de generar boilerplate.
- MCP mínimo en cada proyecto y descripciones de tools cortas.
- Salidas breves por protocolo (§4.17): menos tokens de salida.
- Guía `docs/guides/token-discipline.md` con reglas y ejemplos.

### 4.16 Modo turbo y cola de pendientes
- Turbo es el default de ABM y de todo ADS.
- **Velocidad:** tool calls independientes en paralelo; subagentes en paralelo para exploración y revisión; lecturas por lote; modelo rápido para tareas mecánicas; scaffolding con CLIs; sin verificaciones redundantes, pero nunca sin la verificación del gate.
- **Configuración turbo por herramienta**, generada por `sync` a partir de los modos de permisos y allowlists vigentes (verificados): la lectura y los comandos seguros se aprueban solos; lo destructivo, la producción, los pagos y la red externa piden siempre confirmación.
- **Cola de pendientes** (`docs/_work/PENDIENTES.md`, OKF). Una entrada por ítem: ID · tipo (decisión / aprobación / credencial / revisión / propuesta de alcance) · contexto en una línea · default aplicado · alternativa · impacto si no se responde · estado. El comando `pending` la muestra agrupada y aplica las respuestas en lote.
- **Encaje con la gobernanza:** el ADR 14 redefine las reglas 1 (Planning Gate) y 4 (alcance) de `AGENTS.md` para turbo. Dirección propuesta:
  - el plan se publica y la ejecución reversible sigue con aprobación acumulada;
  - el gate sigue siendo bloqueante en el perfil Enterprise-Regulado y ante acciones irreversibles;
  - lo que "parece útil" pero está fuera de alcance entra en la cola como propuesta; no se construye.

### 4.17 Protocolo de comunicación del agente
- Aplica a ABM y a todo ADS en construcción. En tiempo de ejecución, los agentes de un ADS heredan la brevedad, salvo que el caso de uso (p. ej., atención al cliente) exija otro tono; esa decisión queda registrada en el brief.
- **Acción verde:** sin anuncio; aparece en el reporte agrupado.
- **Acción amarilla:** una línea antes: qué, por qué y cómo se deshace.
- **Acción roja:** bloqueante; tres líneas como máximo: qué, riesgo y qué necesita del humano.
- **Errores:** causa en una línea + pasos concretos para salir. Nunca se da por sabido el uso de la terminal: se indica el comando exacto.
- Cada playbook incluye su plantilla de salida; CI verifica que exista y que respete el presupuesto de líneas.

### 4.18 Experiencia vibe coder
- Wizard con preguntas en lenguaje simple.
- Comunicación según §4.17: concreta, sin conversación.
- Semáforo de riesgo (verde/amarillo/rojo) en cada acción.
- Defaults seguros y checkpoints para deshacer.
- Cola de pendientes en lugar de interrupciones constantes.
- Cada error se traduce en pasos concretos.

### 4.19 Calidad, seguridad y gobernanza
- OWASP Top 10 y ASVS; OWASP Top 10 para LLM y la guía OWASP vigente para aplicaciones agénticas (verifica nombre y versión).
- Seguridad MCP y auditoría de las acciones de los agentes.
- Cadena de suministro: lockfiles, Renovate/Dependabot, SBOM.
- Secret scanning y control de licencias.
- Versionado semántico de ABM y de cada ADS, con CHANGELOG.
- CODEOWNERS opcional.

### 4.20 Formato OKF
- **Norma:** la especificación oficial de Google Cloud (R15, Anexo D) más el perfil ABM, que reemplaza o extiende `knowledge/README.md` según el ADR 4.
- **Entregables:**
  - `okf/PROFILE.md`: reglas del perfil ABM y referencia a la versión de la spec que adopta;
  - `okf/schema.json`: JSON Schema del frontmatter por `type`;
  - plantillas por tipo de documento, que ya nacen conformes;
  - validador en CI con dos niveles: conformidad de la spec (§11 de la spec) y perfil ABM (campos por tipo, `generated`, `status`, `stale_after` donde aplique, `index.md`/`log.md`, `okf_version`).
- **Tipos de documento** (`type`), por ejemplo: Intent, Spec, Plan, ADR, Playbook, Stack Sheet, Compat Matrix, Analysis, Progress, Pending Queue, Manual Page. Los fija el ADR 4.
- **Caducidad en CI:** aviso si `now >= stale_after`; fallo en los documentos que el perfil marque como críticos.
- **Migración de la convención actual:** `timestamp` → `generated.at`; citas en el cuerpo → `sources`. Queda registrada en `MIGRATION.md`.
- **Alcance:** TODO documento de ABM y de cada ADS. El conocimiento de un ADS se entrega como bundle OKF y forma parte de su superficie agéntica (§4.8): Hermes y otros agentes lo consumen sin conversión.
- **Interoperabilidad** con `conocimiento/` de AGE_Builder: se mantiene (un consumidor v0.2 acepta bundles v0.1).

## 5. Criterios de aceptación (DoD global)
- [ ] Diagnóstico, benchmark, investigación agéntica, plan e informe final existen y pasan el validador OKF.
- [ ] Todo documento del repo es conforme a OKF (versión oficial vigente) y al perfil ABM, validado en CI; `okf_version` declarado; convención heredada migrada.
- [ ] Glosario ABM/ADS aplicado en todo el repo, sin términos huérfanos.
- [ ] `AGENTS.md` canónico dentro de presupuesto, con protocolo de salida y turbo; presupuesto de tokens comprobado en CI; métrica antes/después reportada.
- [ ] `sync --check` en verde; adaptadores para las 9 herramientas mínimas más el fallback universal; matriz de compatibilidad con fuente y fecha, incluidas la configuración turbo y la telemetría de uso.
- [ ] Contrato ADS con schema, niveles por perfil y `ads-check` en CI. **ABM lo cumple.**
- [ ] Superficie agéntica: plantillas completas y `agent-conformance` en verde contra Hermes (o contra un cliente MCP genérico, declarado) en ABM y en los ejemplos.
- [ ] Capa System One: interfaz, adaptador Jev, fallback LLM y umbrales; usada en el router de ABM; al menos 5 recetas para ADS; mediciones reportadas o marcadas `no-verificado`.
- [ ] Portabilidad: gateway LLM, matriz multinube, recetas legacy y de escalabilidad; el encargo (f) se recorre sin huecos.
- [ ] Espacio de tokens: ledger con esquema, CLI `tokens`, plantillas de dashboard N1–N3 y presupuestos en CI; ABM muestra el consumo de esta repotenciación.
- [ ] Turbo: configuración por herramienta, cola de pendientes y comando `pending`; ADR sobre el Planning Gate.
- [ ] Protocolo de salida presente en `AGENTS.md` y en cada playbook, y verificado por CI.
- [ ] Motor metodológico con 5 modos, mezcla por módulo, escalamiento y `/drift`; una plantilla para cada artefacto.
- [ ] FE, BE y DB con la misma estructura completa (estándar, checklist, skill, agente, comando, tests).
- [ ] Catálogo con al menos 14 casos y la matriz completa, incluidas la variante corporativa/legacy y las equivalencias por nube.
- [ ] Guía de integraciones MCP, API y otras vías, con configuración por herramienta y controles de seguridad.
- [ ] 100 % de los comandos en el manual (comprobado por CI), más onboarding, glosario, FAQ y troubleshooting.
- [ ] CI del repo en verde: OKF, markdownlint, enlaces, sync, token budget, secret scan, `ads-check` y lint de playbooks.
- [ ] Los 6 encargos simulados recorridos sin huecos; al menos uno ejecutado si el entorno lo permite.
- [ ] README renovado, CHANGELOG, MIGRATION con alias, CONTRIBUTING, SECURITY y LICENSE.

## 6. Cómo comunicarte conmigo
- Reporta solo al cerrar una fase o una WU, con este formato y 12 líneas como máximo:
  ```
  [Fase N | WU-x] HECHO | BLOQUEADO
  Acciones: <una línea por acción, con archivo o commit>
  Verificado: <check → resultado>
  No verificado: <ítem → motivo>
  Pendientes: <+n nuevos en PENDIENTES.md; total n>
  Tokens: <consumo de la fase o WU; fuente o "estimado">
  Siguiente: <acción concreta>
  ```
- Sin volcados de archivos y sin texto fuera del formato.
- Pregunta solo ante un bloqueante (R12): tres líneas como máximo, con la opción recomendada. En lo demás, decide, aplica el default, regístralo (ADR o cola de pendientes) y sigue.

## Anexo A — Nota sobre metodologías (insumo: verificar las fuentes)
- Premisa: ningún enfoque "mata" a SDD. En 2026, lo más avanzado es el desarrollo guiado por intención y contratos vivos, integrado en flujos agent-native con validación automática.
- **IDD/IDSD.** Se definen intención, expectativas, contexto y restricciones, y el agente decide el "cómo".
  - Ventajas: menos ceremonia, se adapta a requisitos cambiantes, se alinea con resultados de negocio.
  - Ideal para: greenfield, MVPs, alta incertidumbre, equipos pequeños o medianos.
  - Riesgo: *technical drift* si la intención no se mantiene al día.
- **SPDD.** La spec vive como prompts o contratos versionados, sincronizados en ambos sentidos con el código: un contrato vivo entre humano y agente. Ideal cuando las specs de SDD se desincronizan del código.
- **AIDD híbrido.** Vibe coding para explorar y SDD/IDD para producción, con revisión humana obligatoria. Da productividad sin caos ni burocracia.
- **Agent-native.**
  - Herramientas: Spec Kit, Kiro, skills de Claude Code.
  - Intent tree (Propósito / Usuario / Medios) → issues → specs → código → review/closeout.
  - Validación automática, trazabilidad y gobernanza (ISO 42001, NIST AI RMF, EU AI Act).
- **Tabla de decisión:**
  - MVP o alta incertidumbre → IDD.
  - Sistemas críticos, regulados o equipos grandes → SDD maduro con revisión humana.
  - Specs que quedan obsoletas → SPDD.
  - Productividad sin caos → AIDD híbrido.
- **Requisito del usuario:** ABM debe integrar enfoques mixtos según el encargo.
- Fuentes:
  - https://www.codysandahl.com/2026/07/14/kill-the-ceremony-intent-driven-development-and-the-minimum-viable-spec/
  - https://www.linkedin.com/pulse/intent-driven-development-idd-spec-driven-sdd-bhupendra-4t1we
  - https://www.webreactiva.com/blog/spdd
  - https://pasqualepillitteri.it/es/news/3384/aidd-vs-vibe-coding-spec-driven-development-2026-es
  - https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2
  - https://www.intent-driven-development.com/landscape
  - https://intent-driven.dev/knowledge/intent-driven-development/

## Anexo B — Jev de TypeSafe AI (insumo consultado el 2026-09-27; volver a verificar)
- **Qué es:** el modelo insignia de TypeSafe AI y su primer modelo "System One". No genera texto: evalúa preguntas tipadas contra un `state` y devuelve valores tipados con probabilidades, que el código usa directamente, sin parsing.
- **Primitivas:**
  - Choice: elige una opción de una lista; devuelve `choice`, `probabilities` y `confidence`.
  - Score: puntúa el `state` según una rúbrica de niveles; devuelve `score`, `probabilities` y `confidence`.
  - Noul: probabilidad (0–1) de que un enunciado sea verdadero.
  - Se pueden mezclar en una sola llamada; cada pregunta se evalúa en paralelo y de forma aislada frente al mismo `state`.
- **Guía del proveedor:** preguntas atómicas compuestas en código. Patrones: speculative fan-out, confidence-gated routing, composite scoring, intent routing.
- **Recetas oficiales relevantes:** guardrails para LLMs, clasificación de pasajes RAG, verificación de citas, function calling, sugerencia de skills sobre el catálogo de Hermes, cascada de extracción de datos.
- **Integración:** API HTTP; SDKs de Python y JavaScript (las respuestas incluyen uso de tokens); agent skill para Claude Code, Codex y otros; página "Jev with coding agents" (qué es y qué no es); integración con LangChain (`langchain_typesafe`, según el blog de LangChain). Índice de la documentación: `https://docs.typesafe.ai/llms.txt`.
- **Estado:** early access desde mediados de septiembre de 2026 (fuente secundaria). Versión documentada: `jev-1.13`, con una página de limitaciones conocidas ("jaggedness").
- **Afirmaciones del proveedor, NO verificadas:** 40–200× más rápido que los LLMs frontera; costo de entrada muy bajo y salida gratuita; latencias de 70–500 ms; no produce errores de tipo.
- Fuentes:
  - https://docs.typesafe.ai/introduction
  - https://docs.typesafe.ai/llms.txt
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://www.langchain.com/blog/building-a-harness-with-jev
  - https://beam.ai/agentic-insights/jev-typesafe-ai-agents

## Anexo C — Hermes Agent (insumo consultado el 2026-09-27; volver a verificar)
- **Qué es:** agente open-source y self-hosted de Nous Research. Memoria persistente, skills que crea y mejora con el uso, y gateway de mensajería (Telegram, entre otros); corre en terminal, app de escritorio, plataformas de mensajería e IDEs.
- **Skills:** compatible con el estándar abierto agentskills.io; skills instaladas en `$HERMES_HOME/skills/`.
- **MCP (como cliente):** `~/.hermes/config.yaml` → `mcp_servers`. Admite stdio o HTTP, OAuth 2.1, mTLS y filtros `tools.include` / `tools.exclude`, `resources` y `prompts`. Los tools se nombran `mcp__<server>__<tool>`.
- **Seguridad:** secretos en `~/.hermes/.env`; `security.redact_secrets` activo por defecto.
- **Según el adaptador existente del repo (`adapters/hermes/SKILL.md`, verificar):** Hermes inyecta automáticamente el `AGENTS.md` del directorio de trabajo; delega con `delegate_task` a subagentes que no ven la conversación; el modelo se fija por invocación.
- Fuentes:
  - https://hermes-agent.nousresearch.com/docs/
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
  - https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
  - https://github.com/nousresearch/hermes-agent

## Anexo D — OKF, Open Knowledge Format de Google Cloud (insumo consultado el 2026-09-27; volver a verificar)
- **Qué es:** especificación abierta de Google Cloud que formaliza el patrón "LLM wiki". El conocimiento es un directorio de archivos Markdown con frontmatter YAML: legible por humanos y agentes sin SDK, versionable en git y portable entre herramientas. La v0.1 se publicó en junio de 2026; la v0.2 es la vigente y añade provenance, trust, lifecycle y attestation. Knowledge Catalog de Google Cloud ingiere OKF.
- **Conformidad v0.2 (§11 de la spec):**
  - todo `.md` no reservado tiene un frontmatter YAML parseable con `type` no vacío;
  - `index.md` y `log.md`, si existen, siguen su estructura;
  - un consumidor no rechaza un bundle por campos opcionales faltantes, tipos desconocidos, claves extra, enlaces rotos o falta de `index.md`.
- **Nombres reservados:**
  - `index.md`: listado para divulgación progresiva; sin frontmatter, salvo `okf_version` en la raíz del bundle;
  - `log.md`: entradas agrupadas bajo `## YYYY-MM-DD`, las más recientes primero.
- **Campos recomendados:** `title`, `description`, `resource`, `tags`.
- **Familias opcionales:**
  - provenance: `sources` (`id`, `resource`, `title`, `author`, `usage_count`, `last_modified`) y `usage_window`;
  - trust: `generated { by, at }` y `verified`. Los niveles de confianza (unverified, machine-confirmed, human-reviewed) se derivan de `verified`;
  - lifecycle: `status` (`draft` | `stable` | `deprecated`) y `stale_after`;
  - tipo `Attested Computation`: `runtime`, `parameters`, `computation`, `executor` y `attester` (código determinista, sin LLM).
- **Actores:** `<producer>/<version>` para agentes y herramientas, `human:<id>` para personas, `process:<id>` para procesos.
- **Cambios incompatibles de v0.1 a v0.2:** `timestamp` → `generated.at`; la lista `# Citations` del cuerpo → `sources`.
- **Brechas iniciales de `knowledge/README.md` frente a v0.2** (se confirman en la Fase 0):
  - no cita la especificación de Google ni su versión, y no declara `okf_version`;
  - recomienda `timestamp` (v0.1) con fecha sin hora; v0.2 usa `generated.at` en ISO 8601 con zona UTC;
  - no contempla `sources`, `generated`, `verified`, `status` ni `stale_after`;
  - usa enlaces relativos; la spec recomienda `/ruta.md`, relativa a la raíz del bundle;
  - exige `index.md` y `log.md` (la spec los deja opcionales): válido como perfil más estricto;
  - limita OKF a `knowledge/`; debe extenderse a todo documento.
- Fuentes:
  - https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
  - https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
  - https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
