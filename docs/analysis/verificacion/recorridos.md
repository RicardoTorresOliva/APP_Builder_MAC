---
type: Review
title: Recorridos de los 6 encargos simulados
description: Recorrido de punta a punta, como vibe coder, de seis encargos con la documentación y el CLI de ABM v5; huecos encontrados.
tags: [verificacion, fase-4, recorridos]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:06:28Z }
---

# Recorridos de los 6 encargos simulados

Verificador: solo documentación del repo (`README.md`, `QUICKSTART.md`, `docs/manual/**`, `AGENTS.md`,
`commands/*.md`, `skills/`, `templates/`, `methodology/`, `stacks/`, `integrations/`) y el CLI `./abm`,
como lo usaría un vibe coder. Esqueletos ADS creados en
`/tmp/claude-0/-home-user-APP-Builder-MAC/1fe7b2e6-756c-5a30-a025-d618c49e6219/scratchpad/recorridos/{a..f}`
con `./abm new-ads`; no se tocó nada del repo salvo este informe.

## (a) Landing con formulario de contacto

**Clasificación** (`./abm methodology classify --text "Landing con formulario de contacto para captar leads de una pyme" --json`): proyecto **IDD** (desescalamiento `landing-content`); módulo `general`: IDD. Razonable: sin pagos/auth/datos personales — modo único, sin mezcla esperable.

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Encargo | (editar) | — | `START_PROJECT.md` | `docs/manual/primeros-15-minutos.md` | OK |
| Perfil+ceremonia+stack+plan | `init-project` | methodology-router, stack-advisor | `templates/plan.md` | `docs/manual/comandos/init-project.md` | OK |
| Elegir stack | `stack` | stack-advisor | — | `stacks/cases/landing-marketing.md` | OK |
| Construir FU/DU | `start-execution` → `ui` | frontend-builder | — | `docs/manual/comandos/ui.md` | OK |
| Endpoint del formulario | `api` | api-builder | — | `docs/manual/comandos/api.md` | OK |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Accesibilidad/seguridad | `a11y`, `security` | a11y-audit, security-hardening | — | `docs/manual/comandos/{a11y,security}.md` | OK |
| Medir tokens | `tokens report/dashboard` | token-ledger | `TOKENS.md` | `docs/manual/tokens.md` | OK |
| Publicar | `deploy` → `release` | — | `templates/handoff.md` | `docs/manual/comandos/{deploy,release}.md` | OK |

**Perfil/stack:** `software-app`; `stacks/cases/landing-marketing.md` (Astro+Vercel vibe coder, sin DB ni auth). Cobertura completa, sin inventar.

**Esqueleto ADS:** `./abm new-ads .../a --id landing-contacto --name "Landing con formulario de contacto" --profile software-app --ceremony mvp`. `ads-check`: 0 errores (2 warnings esperables en un esqueleto recién creado: dashboard de tokens aún no generado, placeholders `<...>` en `ads.yaml` pendientes de `init-project`). `agent-conformance`: 12/12 pasos OK.

## (b) Dashboard con auth, base de datos y gráficos

**Clasificación** (`--text "Dashboard interno con autenticación, base de datos y gráficos para ventas"`): proyecto **SDD** (escalamiento `auth`); módulo `general`: SDD. Razonable dado que auth escala sin excepción.

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Perfil+metodología+stack+plan | `init-project` | methodology-router, stack-advisor | `templates/plan.md`, `templates/methodology-map.md` | `docs/manual/comandos/init-project.md` | OK |
| Esquema de datos | `db` | db-builder | — | `docs/manual/comandos/db.md` | OK |
| Identidad (FU) | `start-execution` (auth) | api-builder | `templates/spec/*` | `docs/manual/comandos/{spec,api}.md` | OK |
| API + gráficos | `api`, `ui` | api-builder, frontend-builder | — | `docs/manual/comandos/{api,ui}.md` | OK |
| Semáforo de riesgo de cada acción | `decide --preset risk` | system-one | `integrations/decision/presets/risk.yaml` | `docs/manual/comandos/decide.md` | OK (ver abajo) |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Seguridad/tests de rutas críticas | `security`, `test` | security-hardening, test-strategy | — | `docs/manual/comandos/{security,test}.md` | OK |
| Revisión independiente | `review` | review-independent | — | `docs/manual/comandos/review.md` | OK |
| Tokens | `tokens record/report/dashboard/attest` | token-ledger | `TOKENS.md` | `docs/manual/tokens.md` | OK |
| Publicar | `deploy` → `release` | — | `templates/handoff.md` | `docs/manual/comandos/{deploy,release}.md` | OK |

**Perfil/stack:** `software-app`; `stacks/cases/internal-dashboard-bi.md` (o `saas-web-app.md` si es multi-cliente). **Evidencia real:** `examples/panel-ventas/` (auth PBKDF2 ≥600k iteraciones, SQLite, gráficos SVG propios, CSRF, `problem+json`). Este ADS de ejemplo se completó *durante* este recorrido (otra sesión lo seguía construyendo en paralelo sobre el mismo checkout): al corte final, `./abm ads-check examples/panel-ventas` → 0 errores, `./abm agent-conformance examples/panel-ventas` → 12/12 OK, y su suite (`python3 -m unittest discover` en `tests/`) → 45/45 en verde.

**Decisión System One** (`./abm decide --preset risk --use risk --state "Publicar en producción el dashboard de ventas y dar permisos de borrado a los administradores" --json`, ejecutado dentro del esqueleto `b/`): `risk=rojo`, confianza 1.0, `route=act`, **`provider: rules`** (sin `TYPESAFE_API_KEY` ni `ABM_LLM_*` → cae al fallback determinista; Jev real = **no-verificado**).

**Hallazgo sobre la evidencia (aún reproducible al corte final):** una vez que `examples/panel-ventas/` generó su propio `index.md` (con `okf index`, como lo haría cualquier ADS que sigue el quickstart), `./abm okf validate` desde la raíz del repo host **falla**: `ERROR examples/panel-ventas/index.md: index.md no admite frontmatter (salvo okf_version en la raíz) [okf.index]`; y `./abm links` reporta 6 enlaces rotos, todos en ese mismo `index.md` (p. ej. `/planning/methodology-map.md`, `/docs/manual/operacion.md`), porque esos enlaces `/ruta.md` son correctos *relativos a la raíz del propio ADS de ejemplo* pero el validador del repo host los resuelve contra la raíz del repo ABM (bundle único). Es el mismo choque estructural que ya se había observado, y corregido en vivo, para `skills/**/SKILL.md` (ver H3).

**Tokens** (esqueleto `b/`): `tokens record --phase build --input 18000 --output 3200 --unit DU1-dashboard-ventas` → `tokens report` (TOKENS.md, 1 evento, 21 200 tokens) → `tokens dashboard` (`ops/tokens/dashboard.html` generado) → `tokens attest` → **"Atestación: OK — las cifras del reporte salen del ledger"**.

## (c) App móvil con backend

**Clasificación** (`--text "App móvil con backend para pedidos de comida"`): proyecto **IDD**; módulo `general`: IDD. Razonable (sin pagos/auth mencionados explícitamente en el texto).

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Perfil+stack+plan | `init-project` → `stack` | stack-advisor | `templates/plan.md` | `stacks/cases/mobile-app.md` | OK |
| Esquema de datos | `db` | db-builder | — | `docs/manual/comandos/db.md` | OK |
| Backend (API) | `api` | api-builder | — | `docs/manual/comandos/api.md` | OK |
| UI móvil | `ui` | frontend-builder | — | `docs/manual/comandos/ui.md` | OK |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Tests rutas críticas (pedido, pago si aplica) | `test` | test-strategy | — | `docs/manual/comandos/test.md` | OK |
| Accesibilidad móvil | `a11y` | a11y-audit | — | `docs/manual/comandos/a11y.md` | OK |
| Tokens | `tokens report/dashboard` | token-ledger | `TOKENS.md` | `docs/manual/tokens.md` | OK |
| Publicar en tiendas | `deploy` → `release` | — | `templates/handoff.md` | `docs/manual/comandos/{deploy,release}.md` | OK — `deploy`/`release` no distinguen build EAS/App Store de un deploy web; cubierto solo indirectamente por `stacks/cases/mobile-app.md` (build/distribución) |

**Perfil/stack:** `software-app`; `stacks/cases/mobile-app.md` (Expo+Supabase vibe coder). Si "pedidos" implica cobro, el propio módulo escala a `payments`/SDD en `closeout` (regla de `methodology/mixing.md`, "reclasifica antes de seguir") — correcto y sin hueco.

**Esqueleto ADS:** `./abm new-ads .../c --id pedidos-movil --profile software-app --ceremony mvp`. `ads-check`: 0 errores. `agent-conformance`: 12/12 OK.

## (d) Mini-ERP con inventario, ventas, facturación y roles

**Clasificación**, dos formas de pedirlo:

1. Como lo escribiría literalmente un vibe coder — el texto general del encargo (`--text "Mini-ERP con inventario, ventas, facturación y roles"`) más los módulos textuales de `methodology/mixing.md` (`Inventario`, `Ventas`, `Facturación`, `Roles y autenticación`, `Reportes`) → **project_mode SDD y los 5 módulos SDD** (todos, incluidos `Inventario`/`Ventas`/`Reportes`, que el propio manual documenta como IDD). **No sale mixto** — ver H1.
2. Reformulando el texto general sin la palabra "facturación" (dejándola solo en la descripción del módulo) → `inventario`/`ventas` **IDD**, `facturacion` **SDD** (`escalamiento: payments`), `roles` **SDD** (`escalamiento: auth`) — **mixto**, y coincide con el ejemplo de `methodology/mixing.md`.

Con (2) el modo por proyecto y por módulo es razonable y mixto, tal como exige la metodología; con (1) —la forma natural de redactar el encargo— **no lo es**, por H1.

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Perfil+ceremonia+stack+plan | `init-project` | methodology-router, stack-advisor | `templates/plan.md` | `docs/manual/comandos/init-project.md` | OK |
| Metodología por módulo | `methodology classify --module ...` | methodology-router | `templates/methodology-map.md` | `methodology/mixing.md`, `methodology/router.md` | **HUECO** (H1) |
| Esquema de datos (inventario/ventas/facturación) | `db` ×3 | db-builder | — | `docs/manual/comandos/db.md` | OK |
| API por módulo | `api` ×4 | api-builder | — | `docs/manual/comandos/api.md` | OK |
| UI por módulo | `ui` | frontend-builder | — | `docs/manual/comandos/ui.md` | OK |
| Roles/permisos | `start-execution` (auth) + `security` | security-hardening | `templates/spec/*` | `standards/security/` | OK |
| Facturación (spec formal) | `spec` | test-strategy (para tests fiscales) | `templates/spec/{requirements,design,tasks}.md` | `docs/manual/comandos/spec.md` | OK |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Revisión + tokens | `review`, `tokens` | review-independent, token-ledger | `TOKENS.md` | `docs/manual/comandos/review.md` | OK |
| Publicar | `deploy` → `release` | — | `templates/handoff.md` | `docs/manual/comandos/{deploy,release}.md` | OK |

**Perfil/stack:** `software-app`; `stacks/cases/erp-crm-backoffice.md` (usuarios internos, `ads_contract_level: extendido`, comprar Odoo/ERPNext vs. construir ya contemplado).

**Esqueleto ADS:** `./abm new-ads .../d --id mini-erp --profile software-app --ceremony producto`. `ads-check`: 0 errores. `agent-conformance`: 12/12 OK.

## (e) Producto de inteligencia para un cliente de consultoría

**Clasificación** (`--text "Producto de inteligencia para consultoría: informe, dataset y dashboard para un cliente"`): proyecto **IDD**; módulo `general`: IDD. Razonable (sin pagos/auth/datos sensibles en el texto; si las fuentes son datos personales o de salud del cliente, `init-project` debe reclasificar a SDD por disparador).

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Perfil (compuesto)+stack+plan | `init-project` | methodology-router, stack-advisor | `templates/plan.md` | `profiles/intelligence-product/profile.md` | OK |
| Elegir stack | `stack` | stack-advisor | — | `stacks/cases/intelligence-product.md` | OK |
| Pipeline de datos | `db` (o script de ingesta) | db-builder | — | `docs/manual/comandos/db.md` | OK |
| Contrato del asistente de redacción con IA | `prompt-contract` | system-one (para el semáforo de confianza) | `templates/prompt-contract.md` | `docs/manual/comandos/prompt-contract.md` | OK |
| Dataset/dashboard | `db`, `ui` | db-builder, frontend-builder | — | `stacks/cases/internal-dashboard-bi.md` | OK |
| Informe (documento OKF citado) | `start-execution` | okf-author | `templates/spec/*` | `okf/PROFILE.md` | OK |
| Observabilidad de cada llamada LLM | `integrate` (Langfuse u otro) | observability-setup | — | `integrations/observability/README.md` | OK |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Revisión + tokens | `review`, `tokens` | review-independent, token-ledger | `TOKENS.md` | `docs/manual/comandos/review.md` | OK |
| Entrega | `release` | — | `templates/handoff.md` | `docs/manual/comandos/release.md` | OK |

**Perfil/stack:** `intelligence-product` (compone `research-report` + `data-product`, `ads_contract_level: extendido`); `stacks/cases/intelligence-product.md`. Cobertura completa: gateway LLM para redacción asistida con verificación humana antes de publicar, ya indicado en la ficha.

**Esqueleto ADS:** `./abm new-ads .../e --id inteligencia-cliente --profile intelligence-product --ceremony producto`. `ads-check`: 0 errores, nivel `extendido` (coincide con `ads_contract_level` del perfil). `agent-conformance`: 12/12 OK.

## (f) Brownfield corporativo: módulo nuevo sobre ERP legacy (SQL Server + SOAP), Azure, LLM intercambiable

**Clasificación** (`--text` del encargo + módulos `integracion-erp`, `aprobaciones-compra`, `sso-corporativo`, `asistente-llm`): proyecto **IDD**; `sso-corporativo` → **SDD** (`escalamiento: auth`); `integracion-erp`, `aprobaciones-compra`, `asistente-llm` → **IDD**. **Mixto**, como exige el enunciado — pero ver H5: `aprobaciones-compra` maneja montos y aprobación de compras y no dispara ningún trigger (el diccionario de `payments` solo cubre vocabulario de checkout/e-commerce, no de backoffice/compras).

| Paso | Comando | Skill | Plantilla | Manual | Estado |
|---|---|---|---|---|---|
| Arranque | `bootstrap` | abm-playbooks | — | `docs/manual/primeros-15-minutos.md` | OK |
| Inventario del legacy | `assess` | — | `templates/assessment.md` | `commands/assess.md`, `stacks/legacy.md` | OK |
| Perfil+ceremonia+metodología+stack+plan | `init-project` | methodology-router, stack-advisor | `templates/plan.md` | `docs/manual/comandos/init-project.md` | OK |
| Patrón de integración (fachada API sobre SQL Server/SOAP) | `stack` (categoría) + `stacks/legacy.md` | stack-advisor | — | `stacks/cases/legacy-integration.md` | OK |
| Equivalencia de nube (Azure) | `stack` | stack-advisor | — | `stacks/clouds.md` | OK |
| Gateway LLM intercambiable | `integrate` | integrate-safely | `.env.example` | `integrations/llm-gateway/README.md`, `stacks/llm-providers.md` | **HUECO** (H2) |
| Conector legacy (mínimo privilegio) | `integrate` | integrate-safely | — | `commands/integrate.md` | OK |
| Nuevo flujo de aprobaciones | `api`, `db` | api-builder, db-builder | `templates/spec/*` | `docs/manual/comandos/{api,db}.md` | OK |
| SSO corporativo | `start-execution` (auth) + `security` | security-hardening | — | `standards/security/`, `stacks/legacy.md` (SSO/redes) | OK |
| Semáforo de riesgo de cada acción | `decide --preset risk` | system-one | `integrations/decision/presets/risk.yaml` | `docs/manual/comandos/decide.md` | OK (ver abajo) |
| Superficie agéntica | `connect` | agentic-surface | `templates/agentic/*` | `docs/manual/comandos/connect.md` | OK |
| Revisión humana obligatoria + tokens | `review`, `tokens` | review-independent, token-ledger | `TOKENS.md` | `methodology/governance-regulated.md` | OK |
| Despliegue en Azure | `deploy` | — | `templates/handoff.md` | `stacks/clouds.md` | OK |

**Perfil/stack:** `software-app`; `stacks/cases/legacy-integration.md` (fachada API/ACL, `assess` primero) + `stacks/legacy.md` (conectores SQL Server/SOAP, SSO, RPA como último recurso) + `stacks/clouds.md` (equivalencias Azure) + `stacks/llm-providers.md`/`integrations/llm-gateway/README.md` (gateway intercambiable). **No bastan sin reconciliar una contradicción**: `stacks/llm-providers.md` documenta variables de entorno (`LLM_PROVIDER`, `LLM_MODEL`, `LLM_BASE_URL`, `<PROVIDER>_API_KEY`) distintas de las que usan `integrations/llm-gateway/README.md`, `.env.example`, `abm.yaml` y el código real (`ABM_LLM_BASE_URL`, `ABM_LLM_API_KEY`, `ABM_LLM_MODEL`) — ver H2. Un vibe coder que solo lea `stacks/llm-providers.md` configurará variables que el CLI no lee.

**Esqueleto ADS:** `./abm new-ads .../f --id modulo-aprobaciones --profile software-app --ceremony enterprise-regulado`. `ads-check`: 0 errores, nivel `extendido`. `agent-conformance`: 12/12 OK.

**Decisión System One** (`./abm decide --preset risk --use risk --state "Cambiar en producción el proveedor LLM de Azure OpenAI a AWS Bedrock sin correr los evals de regresión, tocando las credenciales del ERP legacy" --json`, esqueleto `f/`): `risk=rojo`, confianza 0.667 (< umbral `act` 0.90 y < `gray` 0.70) → `route=human` — el propio sistema de umbrales (`integrations/decision/thresholds.yaml`) obliga a escalar a un humano, correcto para un cambio de proveedor LLM en producción sin evals. `provider: rules` (mismo motivo que en (b): **no-verificado** para Jev real).

## Brevedad del reporte (todos los encargos)

`AGENTS.md` (§Protocolo de salida) y `standards/communication.md` fijan el reporte de cierre en ≤ 12 líneas, con semáforo por acción y una lista explícita de "frases prohibidas" (saludos, disculpas de relleno, preguntas retóricas, cierres de cortesía). `standards/communication.md` incluye un ejemplo etiquetado **"mal"** con una frase conversacional ("Cualquier cosa avisame y lo vemos juntos") — está marcado como antipatrón, no como invitación real. `./abm lint playbooks` (0 hallazgos), `./abm lint core` (0), `./abm lint manual` (0) y `./abm lint skills` (0) verifican mecánicamente que los 36 `commands/*.md` traen semáforo por paso y una plantilla de reporte en bloque de código ≤ 12 líneas. No se encontró texto en `commands/`, `skills/` o el manual que invite a conversar en el reporte del agente; el tono más explicativo de `docs/manual/*` es correcto porque esas páginas hablan al humano, no son el reporte de cierre del agente.

## Tabla consolidada de HUECOS

| ID | Encargo | Severidad | Descripción | Archivo afectado | Corrección propuesta exacta |
|---|---|---|---|---|---|
| H1 | (d), (f) | alta | `abm methodology classify` con `--module` no aísla el texto: si la descripción **general** del encargo contiene una palabra clave de dimensión (p. ej. "facturación", que es keyword de `criticality:2`), el `base_mode` que heredan los módulos sin disparador propio se calcula sobre esa descripción general, no sobre la del módulo. Con el texto literal del encargo (d) y los módulos tal como los describe `methodology/mixing.md`, el resultado es **todo SDD**, no el mixto que ese mismo documento muestra como ejemplo esperado. | `scripts/abmkit/methodology.py` (función `classify`, cálculo de `base_vals`/`base_mode` a partir de `text` completo, ~L80-108) | En `classify()`, cuando un módulo no tiene disparador propio (`esc`/`de` vacíos en `triggers_for(desc, router)`), calcular su modo llamando a `infer_dimensions(ctx, router, desc)` sobre la descripción **propia** del módulo en vez de reutilizar `base_mode` del proyecto completo; alternativamente, documentar en `methodology/router.md` que el texto general actúa como piso de riesgo de todos los módulos y corregir el ejemplo de `methodology/mixing.md` para que coincida con ese comportamiento. |
| H2 | (f) | alta | Contradicción de nombres de variables de entorno para el proveedor LLM intercambiable: `stacks/llm-providers.md` documenta `LLM_PROVIDER`, `LLM_MODEL`, `LLM_BASE_URL`, `<PROVIDER>_API_KEY`; el código real (`decide()`), `.env.example` y `abm.yaml` usan `ABM_LLM_BASE_URL`, `ABM_LLM_API_KEY`, `ABM_LLM_MODEL` (sin `LLM_PROVIDER`). | `stacks/llm-providers.md` (sección "Cambio de proveedor por configuración"); confirmado contra `scripts/abmkit/decide.py:93`, `.env.example:5-7`, `abm.yaml:60` | En `stacks/llm-providers.md`, reemplazar "`LLM_PROVIDER`, `LLM_MODEL`, `LLM_BASE_URL` y `<PROVIDER>_API_KEY`" por "`ABM_LLM_BASE_URL`, `ABM_LLM_API_KEY`, `ABM_LLM_MODEL` (ver `integrations/llm-gateway/README.md`); el proveedor se determina por el valor de `ABM_LLM_BASE_URL`, no por una variable `LLM_PROVIDER` separada". |
| H3 | (b) | alta | Un ADS de ejemplo anidado bajo `examples/<id>/` que sigue el quickstart genera sus propios artefactos OKF (`index.md` con frontmatter completo, enlaces `/ruta.md` relativos a su propia raíz) tal como lo haría cualquier ADS — pero `./abm okf validate`/`./abm links` corridos desde la raíz del repo host tratan todo el árbol como un único bundle: `examples/panel-ventas/index.md` falla con `index.md no admite frontmatter (salvo okf_version en la raíz) [okf.index]` y sus enlaces `/planning/...`, `/design_docs/...`, `/docs/...` salen "ROTO" porque se resuelven contra la raíz del repo ABM, no la del ejemplo. (Un síntoma hermano de la misma causa, ya observado y corregido en vivo durante este recorrido: `abm.yaml → okf.exclude` no cubría `examples/**/skills/**/SKILL.md`, y al momento de este corte ya usa el patrón general `**/SKILL.md`.) | `okf/PROFILE.md` (no define `examples/<id>/` como sub-bundle, a diferencia de `knowledge/`); `abm.yaml → okf.exclude`; `scripts/abmkit/okf.py`, `scripts/abmkit/links.py` | Declarar cada `examples/<id>/` como sub-bundle montable (igual que `knowledge/`, documentado en `okf/PROFILE.md → Bundle`) y hacer que `abm okf validate`/`abm links` detecten un `abm.yaml` propio en un subdirectorio y lo validen como bundle aparte en vez de resolver sus enlaces `/...` e `index.md` contra la raíz del repo host; mientras tanto, añadir `examples/*/` a `abm.yaml → okf.exclude`. |
| H4 | (d) | baja | Los disparadores de escalamiento hacen coincidencia de palabra/frase completa, no por lema: el trigger `auth` incluye "roles" (plural) y "rol de usuario" (frase) pero no "rol" (singular suelto); una descripción de módulo como "control de acceso por rol" no dispara `auth` por sí sola (confirmado con el código y `methodology/router.yaml` vigentes al corte de este recorrido). | `methodology/router.yaml` (trigger `auth`, lista `keywords`) | Añadir `rol` como keyword suelta de `auth` en `methodology/router.yaml` (p. ej. `rol*` si el motor soporta comodín de prefijo, junto a `roles`, `rol de usuario`). |
| H5 | (f), (d) | media | El diccionario de palabras clave de `criticality:2`/trigger `payments` cubre vocabulario de e-commerce/checkout (`pag*`, `factur*`, `cobr*`, `tarjeta*`, `suscrip*`, `billing`, `invoice*`...) pero no de backoffice/compras corporativas ("orden de compra", "monto", "aprobación de compra", "presupuesto"): un módulo de aprobación de compras con montos (típico de un ERP/brownfield corporativo) no escala a SDD por sí solo (confirmado con el `router.yaml` vigente al corte). | `methodology/router.yaml` (dimensión `criticality`, keywords nivel 2; trigger `payments`, lista `keywords`) | Agregar a `methodology/router.yaml` las keywords `orden de compra`, `monto`, `aprobaci* de compra`, `presupuesto` a la dimensión `criticality` nivel 2 y/o al trigger `payments`. |

## Modo por proyecto y por módulo (resumen)

| Encargo | Modo del proyecto | Módulos | ¿Mixto esperado? |
|---|---|---|---|
| (a) landing | IDD | general: IDD | No — cumple |
| (b) dashboard | SDD | general: SDD | No — cumple |
| (c) app móvil | IDD | general: IDD | No — cumple |
| (d) mini-ERP | SDD (texto literal, H1) / IDD (texto reformulado) | Con módulos bien acotados: inventario IDD, ventas IDD, facturación SDD, roles SDD | Sí, pero solo si se evita la palabra de riesgo en el texto general (H1) |
| (e) inteligencia | IDD | general: IDD | No — cumple |
| (f) brownfield | IDD | integracion-erp IDD, aprobaciones-compra IDD (H5), sso-corporativo SDD, asistente-llm IDD | Sí — cumple |
