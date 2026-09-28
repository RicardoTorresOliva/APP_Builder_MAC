---
okf_version: "0.2"
---

<!-- Generado por `abm okf index`. No editar a mano. -->

# (raíz)

* [AGENTS.md — gobernanza de ABM v5](/AGENTS.md) - Fuente única de gobernanza de APP_Builder_MAC y de todo ADS que produce; neutral de herramienta y de modelo.
* [Changelog de ABM](/CHANGELOG.md) - Cambios por versión de APP_Builder_MAC según versionado semántico.
* [Cómo contribuir a ABM](/CONTRIBUTING.md) - Flujo de cambios, reglas de estilo y verificaciones obligatorias antes de proponer un cambio a ABM.
* [Migración de ABM v4.1 a v5](/MIGRATION.md) - Equivalencias de todo lo renombrado, movido o eliminado, con alias de compatibilidad.
* [Quickstart de ABM v5](/QUICKSTART.md) - Procedimiento corto para preparar ABM una vez y producir un ADS nuevo.
* [APP_Builder_MAC (ABM) v5](/README.md) - Fábrica agent-native de Activos Digitales SLG (ADS), neutral de herramienta y de modelo; punto de entrada del repo.
* [Política de seguridad de ABM](/SECURITY.md) - Cómo reportar vulnerabilidades y qué controles de seguridad aplica ABM por defecto.
* [Encargo del ADS](/START_PROJECT.md) - Descripción inicial del ADS que lee init-project; reemplaza los textos entre corchetes.
* [Reporte de tokens](/TOKENS.md) - Consumo de tokens y costo del ADS (construcción y operación), generado desde el ledger.

# docs

* [Cola de pendientes](/docs/_work/PENDIENTES.md) - Decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado.
* [Progreso de la repotenciación de ABM](/docs/_work/PROGRESS.md) - Estado vivo de la ejecución del prompt maestro v3 (modo TURBO) para sobrevivir a la compactación de contexto.
* [Prompt maestro — análisis y repotenciación de ABM (v3)](/docs/_work/PROMPT_MAESTRO_ABM_v3.md) - Instrucciones para que un agente analice y repotencie APP_Builder_MAC y los ADS que produce.
* [ADR 0001 — Nomenclatura ABM/ADS y glosario](/docs/adr/0001-nomenclatura-abm-ads.md) - Cómo se nombran la fábrica, lo que produce y sus unidades de trabajo.
* [ADR 0002 — Fuente única y generador de adaptadores](/docs/adr/0002-fuente-unica-generador-adaptadores.md) - Los adaptadores por herramienta se generan desde fuentes neutrales con `abm sync`.
* [ADR 0003 — Lenguaje de los scripts](/docs/adr/0003-lenguaje-de-scripts.md) - El tooling de ABM se escribe en Python 3.9+ solo con biblioteca estándar.
* [ADR 0004 — OKF v0.2 y perfil ABM](/docs/adr/0004-okf.md) - Adopción de la especificación OKF de Google Cloud y del perfil de productor de ABM.
* [ADR 0005 — Estándar de skills](/docs/adr/0005-estandar-de-skills.md) - Las skills siguen Agent Skills (agentskills.io) y se distribuyen a cada herramienta por generación.
* [ADR 0006 — Router metodológico](/docs/adr/0006-router-metodologico.md) - Cómo elige y mezcla ABM Vibe, IDD, SDD, SPDD y AIDD por encargo y por módulo.
* [ADR 0007 — Nomenclatura de comandos](/docs/adr/0007-nomenclatura-de-comandos.md) - Nombres de comandos y política de alias.
* [ADR 0008 — Idioma](/docs/adr/0008-idioma.md) - Idioma de la documentación, los playbooks y los identificadores.
* [ADR 0009 — Contrato ADS](/docs/adr/0009-contrato-ads.md) - Requisitos verificables que cumple todo ADS y ABM mismo.
* [ADR 0010 — Superficie agéntica](/docs/adr/0010-superficie-agentica.md) - Protocolos por los que un agente externo descubre y opera un ADS.
* [ADR 0011 — Capa System One (Jev)](/docs/adr/0011-capa-system-one.md) - Interfaz de decisión tipada con confianza, primer adaptador Jev y fallback obligatorio.
* [ADR 0012 — Portabilidad corporativa](/docs/adr/0012-portabilidad.md) - Gateway LLM, matriz multinube y estrategia legacy.
* [ADR 0013 — Espacio de control de tokens](/docs/adr/0013-espacio-de-tokens.md) - Ledger, fuentes, niveles de dashboard y presupuestos.
* [ADR 0014 — Modo turbo, cola de pendientes y Planning Gate](/docs/adr/0014-turbo-y-pendientes.md) - Cómo se reconcilia la velocidad con las reglas 1 y 4 de AGENTS.md.
* [ADR 0015 — Protocolo de salida](/docs/adr/0015-protocolo-de-salida.md) - Comunicación concreta y verificable de todo agente que opere ABM o construya un ADS.
* [ADR 0016 — Categorías en el núcleo, productos en catálogos](/docs/adr/0016-categorias-y-productos.md) - Reconciliación de la regla 7 con los productos que el prompt exige (Jev, Hermes, nubes, stacks).
* [Diagnóstico de ABM v4.1](/docs/analysis/01-diagnostico.md) - Estado de APP_Builder_MAC antes de la repotenciación, con scorecard por dimensión y evidencia archivo:línea.
* [Benchmark de referentes](/docs/analysis/02-benchmark.md) - Referentes de desarrollo agent-native verificados a la fecha y las ideas que ABM adopta de cada uno.
* [Investigación agéntica — Hermes, Jev, protocolos y telemetría](/docs/analysis/03-investigacion-agentica.md) - Hechos verificados para diseñar la superficie agéntica, la capa System One y el espacio de tokens de ABM y sus ADS.
* [Plan de repotenciación ABM v5](/docs/analysis/04-plan.md) - Arquitectura objetivo, plan de migración y roadmap de WU con criterios de aceptación y verificación.
* [Informe final de la repotenciación de ABM v5](/docs/analysis/05-informe-final.md) - Qué cambió y por qué, métricas antes/después, verificación, criterios de aceptación, pendientes y próximos pasos.
* [Verificación de adaptadores contra la documentación oficial](/docs/analysis/verificacion/adaptadores.md) - Contraste de cada salida de abm sync con la documentación oficial vigente de su herramienta.
* [Recorridos de los 6 encargos simulados](/docs/analysis/verificacion/recorridos.md) - Recorrido de punta a punta, como vibe coder, de seis encargos con la documentación y el CLI de ABM v5; huecos encontrados.
* [Revisión adversarial independiente de ABM v5](/docs/analysis/verificacion/revision-adversarial.md) - Hallazgos de un revisor independiente sobre el diff completo de la repotenciación, con evidencia y severidad.
* [Matriz de compatibilidad multi-herramienta](/docs/compat-matrix.md) - Cómo consume cada herramienta de IA las instrucciones, reglas, comandos, skills, subagentes, hooks, MCP, ignore, turbo y telemetría.
* [Registro de decisiones](/docs/decision_log.md) - Decisiones significativas del ADS durante la planificación y la ejecución.
* [Preguntas frecuentes sobre ABM](/docs/faq.md) - Respuestas cortas a las dudas más comunes de alguien que usa ABM sin saber programar.
* [Totales de tokens del ADS](/docs/finops/token-totals.md) - Cálculo sancionado de los totales de tokens y costo a partir del ledger; verificable con un atestador determinista.
* [Glosario de ABM](/docs/glossary.md) - Definiciones canónicas de ABM; ningún otro archivo redefine estos términos.
* [Disciplina de tokens](/docs/guides/token-discipline.md) - Reglas y ejemplos concretos para que un agente use el mínimo de tokens necesario, en ABM y en cualquier ADS que produce.
* [Manual de ABM](/docs/manual/README.md) - Índice del manual para no programadores y cómo usarlo según lo que necesites hacer.
* [Cheatsheet de comandos de ABM](/docs/manual/cheatsheet.md) - Los 36 comandos de ABM en una sola página, agrupados por fase, con su alias en español.
* [a11y — accesibilidad WCAG 2.2 AA](/docs/manual/comandos/a11y.md) - Verifica accesibilidad WCAG 2.2 AA de la capa de interfaz antes de entregar.
* [ads-check — verifica el Contrato ADS](/docs/manual/comandos/ads-check.md) - Verifica que el ADS cumple su nivel del Contrato ADS, estático y dinámico.
* [api — construye el servicio](/docs/manual/comandos/api.md) - Construye la capa de API/servicio de una unidad con contrato de errores y quality gate.
* [assess — inventario de brownfield/legacy](/docs/manual/comandos/assess.md) - Inventaría un stack existente y propone el patrón de integración más simple que funcione.
* [bootstrap — chequeo único de plataforma](/docs/manual/comandos/bootstrap.md) - Detecta la plataforma, corre doctor y sync, y confirma que el repo está listo para trabajar.
* [closeout — cierra una unidad](/docs/manual/comandos/closeout.md) - Sincroniza intención, spec, contrato y código, registra tokens y actualiza la memoria del proyecto.
* [connect — superficie agéntica del ADS](/docs/manual/comandos/connect.md) - Da al ADS su superficie agéntica (ads.yaml, skill, MCP, API) para que otro agente lo opere.
* [consolidate — lleva lo aprendido a diseño real](/docs/manual/comandos/consolidate.md) - Convierte los aprendizajes de un explore en spec y diseño definitivos (IDD/SDD).
* [db — construye el modelo de datos](/docs/manual/comandos/db.md) - Modela y migra el esquema de datos de una unidad con migraciones reversibles.
* [decide — capa System One](/docs/manual/comandos/decide.md) - Resuelve una decisión tipada (choice/score/boolean) con la capa de decisión y su routing por confianza.
* [deploy — publica el ADS](/docs/manual/comandos/deploy.md) - Publica el ADS en su entorno de destino tras pasar la checklist previa y con rollback listo.
* [doctor — diagnóstico del entorno](/docs/manual/comandos/doctor.md) - Diagnostica el entorno (Python, git, estructura, config) en lenguaje simple y sugiere arreglos.
* [drift — deriva intención/spec/código](/docs/manual/comandos/drift.md) - Detecta y resuelve la deriva entre intención, spec, contrato de prompt y código real.
* [explore — spike acotado en sandbox](/docs/manual/comandos/explore.md) - Prueba y descarta en una rama sandbox con tiempo acotado para resolver una incertidumbre.
* [fix — corrige un bug](/docs/manual/comandos/fix.md) - Reproduce el bug, escribe el test que falla, aplica el cambio mínimo y verifica sin regresión.
* [help — índice de comandos](/docs/manual/comandos/help.md) - Muestra el catálogo de comandos por fase y resuelve alias en español.
* [init-project — planifica un proyecto nuevo](/docs/manual/comandos/init-project.md) - Elige perfil y ceremonia, clasifica la metodología, explora el stack con el humano y publica el plan.
* [integrate — integra una plataforma externa](/docs/manual/comandos/integrate.md) - Conecta el ADS con un tercero por la vía más segura disponible, de MCP a SQL de mínimo privilegio.
* [intent — captura la intención](/docs/manual/comandos/intent.md) - Registra el qué y el por qué de una unidad antes de especificarla o construirla.
* [iterate — cambios post-entrega](/docs/manual/comandos/iterate.md) - Aplica un cambio, mejora o corrección tras la entrega, con spec-delta antes de tocar código.
* [methodology — clasifica el modo metodológico](/docs/manual/comandos/methodology.md) - Asigna VIBE, IDD, SDD, SPDD o AIDD a un módulo según sus seis dimensiones de riesgo.
* [pending — cola de pendientes](/docs/manual/comandos/pending.md) - Lista, agrega y resuelve en lote las decisiones y defaults que turbo dejó en cola.
* [perf — rendimiento y escalabilidad](/docs/manual/comandos/perf.md) - Verifica rendimiento, escalabilidad básica y costo por unidad antes de entregar.
* [plan — publica el plan de ejecución](/docs/manual/comandos/plan.md) - Ordena FU y DU en el tracker, redacta el plan y lo publica para su aprobación o cola.
* [prompt-contract — contrato de un agente o prompt](/docs/manual/comandos/prompt-contract.md) - Fija entradas, salidas, límites y HITL de un prompt o agente antes de construirlo.
* [refactor — mejora la estructura sin cambiar comportamiento](/docs/manual/comandos/refactor.md) - Reestructura código manteniendo la suite de tests en verde antes y después, sin cambiar comportamiento.
* [release — cierra una versión](/docs/manual/comandos/release.md) - Cierra una versión del ADS con semver, changelog y verificación previa completa.
* [review — revisión independiente](/docs/manual/comandos/review.md) - Lanza una revisión independiente, con contexto limpio, de la última unidad o milestone completado.
* [security — auditoría de seguridad](/docs/manual/comandos/security.md) - Audita la unidad o el ADS contra OWASP y verifica que no haya secretos expuestos.
* [session-start — inicio de sesión](/docs/manual/comandos/session-start.md) - Lee la memoria del proyecto y la cola de pendientes, y dice por dónde retomar el trabajo.
* [spec — especificación verificable](/docs/manual/comandos/spec.md) - Convierte la intención en requirements, design y tasks verificables (formato EARS).
* [stack — elige el stack con el humano](/docs/manual/comandos/stack.md) - Explora 2-3 opciones de stack con trade-offs y espera la elección del humano (HITL).
* [start-execution — ejecución autónoma](/docs/manual/comandos/start-execution.md) - Verifica que el plan esté listo y ejecuta las FU y DU aprobadas hasta la entrega.
* [test — pirámide de pruebas](/docs/manual/comandos/test.md) - Verifica la unidad con la pirámide de pruebas del perfil, priorizando rutas críticas.
* [tokens — espacio de control de tokens](/docs/manual/comandos/tokens.md) - Registra, reporta y verifica el consumo y presupuesto de tokens de cada unidad.
* [ui — construye la interfaz](/docs/manual/comandos/ui.md) - Construye la capa de interfaz de una unidad siguiendo el standard de frontend y su quality gate.
* [Cómo deshacer un cambio](/docs/manual/como-deshacer.md) - Los checkpoints de git explicados sin jerga, y los comandos exactos para volver atrás de forma segura.
* [Herramientas de IA compatibles con ABM](/docs/manual/herramientas.md) - Tabla maestra de cómo invocar comandos en cada herramienta, qué genera "./abm sync" para cada una, y qué no se puede generar.
* [Modo turbo y cola de pendientes](/docs/manual/modo-turbo.md) - Qué es turbo frente a checkpoint, los bloqueantes, la cola de pendientes, el semáforo de riesgo, y cómo activar turbo en cada herramienta.
* [Tus primeros 15 minutos con ABM](/docs/manual/primeros-15-minutos.md) - Onboarding paso a paso, sin dar por sabido nada de programación, desde abrir el repo hasta ver el plan de tu proyecto.
* [Cómo leer TOKENS.md y el dashboard](/docs/manual/tokens.md) - Qué es un token, cómo leer el reporte TOKENS.md y el dashboard de tokens, qué es un presupuesto blando o duro, y qué hacer si se supera.
* [Memoria del proyecto](/docs/project_memory.md) - Estado actual del ADS y punto de reanudación entre sesiones.
* [Metadatos de ejecución (histórico)](/docs/run_metadata.md) - Tabla manual de tokens por milestone de v4.1; reemplazada por el ledger y TOKENS.md.
* [Inventario de servidores MCP](/docs/tooling/mcp-inventory.md) - Servidores MCP evaluados para el ADS, con selecciones y rechazos en una línea.
* [Inventario de skills](/docs/tooling/skills-inventory.md) - Skills evaluadas para el ADS, con selecciones y rechazos en una línea.
* [Solución de problemas de ABM](/docs/troubleshooting.md) - Errores típicos de ABM con su causa en una línea y los pasos exactos para resolverlos.
* [Registro de trabajo](/docs/work_log.md) - Registro cronológico por unidad: qué se produjo, qué se verificó, hallazgos y riesgos.

# commands

* [a11y — accesibilidad WCAG 2.2 AA](/commands/a11y.md) - Verifica accesibilidad WCAG 2.2 AA de la capa de interfaz antes de entregar.
* [ads-check — verifica el Contrato ADS](/commands/ads-check.md) - Verifica que el ADS cumple su nivel del Contrato ADS, estático y dinámico.
* [api — construye el servicio](/commands/api.md) - Construye la capa de API/servicio de una unidad con contrato de errores y quality gate.
* [assess — inventario de brownfield/legacy](/commands/assess.md) - Inventaría un stack existente y propone el patrón de integración más simple que funcione.
* [bootstrap — chequeo único de plataforma](/commands/bootstrap.md) - Detecta la plataforma, corre doctor y sync, y confirma que el repo está listo para trabajar.
* [closeout — cierra una unidad](/commands/closeout.md) - Sincroniza intención, spec, contrato y código, registra tokens y actualiza la memoria del proyecto.
* [connect — superficie agéntica del ADS](/commands/connect.md) - Da al ADS su superficie agéntica (ads.yaml, skill, MCP, API) para que otro agente lo opere.
* [consolidate — lleva lo aprendido a diseño real](/commands/consolidate.md) - Convierte los aprendizajes de un explore en spec y diseño definitivos (IDD/SDD).
* [db — construye el modelo de datos](/commands/db.md) - Modela y migra el esquema de datos de una unidad con migraciones reversibles.
* [decide — capa System One](/commands/decide.md) - Resuelve una decisión tipada (choice/score/boolean) con la capa de decisión y su routing por confianza.
* [deploy — publica el ADS](/commands/deploy.md) - Publica el ADS en su entorno de destino tras pasar la checklist previa y con rollback listo.
* [doctor — diagnóstico del entorno](/commands/doctor.md) - Diagnostica el entorno (Python, git, estructura, config) en lenguaje simple y sugiere arreglos.
* [drift — deriva intención/spec/código](/commands/drift.md) - Detecta y resuelve la deriva entre intención, spec, contrato de prompt y código real.
* [explore — spike acotado en sandbox](/commands/explore.md) - Prueba y descarta en una rama sandbox con tiempo acotado para resolver una incertidumbre.
* [fix — corrige un bug](/commands/fix.md) - Reproduce el bug, escribe el test que falla, aplica el cambio mínimo y verifica sin regresión.
* [help — índice de comandos](/commands/help.md) - Muestra el catálogo de comandos por fase y resuelve alias en español.
* [init-project — planifica un proyecto nuevo](/commands/init-project.md) - Elige perfil y ceremonia, clasifica la metodología, explora el stack con el humano y publica el plan.
* [integrate — integra una plataforma externa](/commands/integrate.md) - Conecta el ADS con un tercero por la vía más segura disponible, de MCP a SQL de mínimo privilegio.
* [intent — captura la intención](/commands/intent.md) - Registra el qué y el por qué de una unidad antes de especificarla o construirla.
* [iterate — cambios post-entrega](/commands/iterate.md) - Aplica un cambio, mejora o corrección tras la entrega, con spec-delta antes de tocar código.
* [methodology — clasifica el modo metodológico](/commands/methodology.md) - Asigna VIBE, IDD, SDD, SPDD o AIDD a un módulo según sus seis dimensiones de riesgo.
* [pending — cola de pendientes](/commands/pending.md) - Lista, agrega y resuelve en lote las decisiones y defaults que turbo dejó en cola.
* [perf — rendimiento y escalabilidad](/commands/perf.md) - Verifica rendimiento, escalabilidad básica y costo por unidad antes de entregar.
* [plan — publica el plan de ejecución](/commands/plan.md) - Ordena FU y DU en el tracker, redacta el plan y lo publica para su aprobación o cola.
* [prompt-contract — contrato de un agente o prompt](/commands/prompt-contract.md) - Fija entradas, salidas, límites y HITL de un prompt o agente antes de construirlo.
* [refactor — mejora la estructura sin cambiar comportamiento](/commands/refactor.md) - Reestructura código manteniendo la suite de tests en verde antes y después, sin cambiar comportamiento.
* [release — cierra una versión](/commands/release.md) - Cierra una versión del ADS con semver, changelog y verificación previa completa.
* [review — revisión independiente](/commands/review.md) - Lanza un revisor con contexto limpio que verifica la última unidad o milestone completado.
* [security — auditoría de seguridad](/commands/security.md) - Audita la unidad o el ADS contra OWASP y verifica que no haya secretos expuestos.
* [session-start — inicio de sesión](/commands/session-start.md) - Lee la memoria del proyecto y la cola de pendientes, y dice por dónde retomar el trabajo.
* [spec — especificación verificable](/commands/spec.md) - Convierte la intención en requirements, design y tasks verificables (formato EARS).
* [stack — elige el stack con el humano](/commands/stack.md) - Explora 2-3 opciones de stack con trade-offs y espera la elección del humano (HITL).
* [start-execution — ejecución autónoma](/commands/start-execution.md) - Verifica que el plan esté listo y ejecuta las FU y DU aprobadas hasta la entrega.
* [test — pirámide de pruebas](/commands/test.md) - Verifica la unidad con la pirámide de pruebas del perfil, priorizando rutas críticas.
* [tokens — espacio de control de tokens](/commands/tokens.md) - Registra, reporta y verifica el consumo y presupuesto de tokens de cada unidad.
* [ui — construye la interfaz](/commands/ui.md) - Construye la capa de interfaz de una unidad siguiendo el standard de frontend y su quality gate.

# skills

* [Checklist de superficie agéntica por nivel de Contrato ADS](/skills/agentic-surface/references/checklist.md) - Checklist archivo por archivo para el nivel mínimo y extendido del Contrato ADS, con la ruta exacta esperada.
* [Vías de integración por categoría](/skills/integrate-safely/references/vias.md) - Comparación de vías de integración (API directa, webhook, MCP, cola de eventos, automatización de navegador) con su superficie de riesgo, sin nombrar productos.
* [Modos metodológicos — criterios y matriz de escalamiento](/skills/methodology-router/references/modos.md) - Señales de clasificación por modo, matriz de escalamiento y un methodology-map.md de ejemplo.
* [Ejemplo completo de documento OKF v0.2 + perfil ABM](/skills/okf-author/references/ejemplo-completo.md) - Un documento ficticio con sources, notas al pie, stale_after y verified resueltos de punta a punta, para copiar la forma.
* [Tools y recursos del servidor MCP de ABM](/skills/operate-abm/references/mcp-server.md) - Inventario generado desde scripts/abmkit/mcp_server.py; no editar a mano.
* [Severidad de hallazgos en revisión independiente](/skills/review-independent/references/severidades.md) - Taxonomía de severidad, ejemplos de hallazgo bien y mal formulado, y la plantilla de reporte de una revisión.
* [Criterios de los cuatro perfiles de stack](/skills/stack-advisor/references/perfiles-stack.md) - Señales para decidir qué perfil de stacks/ (vibe coder, pro, low-cost, corporativo) calza con un proyecto, en categorías, sin nombrar productos.
* [Patrones de la capa System One para un ADS](/skills/system-one/references/patrones.md) - Siete recetas reutilizables de decisión tipada con su fallback, para usar dentro de cualquier ADS construido con ABM.
* [Esquema del evento de tokens y reglas del ledger](/skills/token-ledger/references/ledger-schema.md) - Campos del evento (contract/token-event.schema.json), ruta por defecto del ledger, niveles N1/N2/N3 y la regla de costo "n/d".

# agents

* [agentic — hace el ADS operable por agentes](/agents/agentic.md) - Construye la superficie agéntica del ADS (ads.yaml, MCP, CLI --json, llms.txt) con agentic-surface y la verifica con agent-conformance; delégale al cerrar el Contrato ADS de cualquier ADS.
* [architect — diseña la arquitectura del ADS](/agents/architect.md) - Define arquitectura, contratos entre capas, nivel de Contrato ADS y methodology-map; delégale al iniciar un ADS o ante un cambio estructural que afecte a varios roles.
* [backend — construye la lógica de servidor del ADS](/agents/backend.md) - Implementa API y lógica de servidor según standards/backend/, con contratos estables para frontend e integrations; delégale cualquier FU/DU de lógica de negocio o exposición de datos.
* [data — modela y gobierna los datos del ADS](/agents/data.md) - Diseña esquema, migraciones y calidad de datos según standards/database/, y aplica el gate de datos del perfil; delégale cualquier FU/DU de modelo de datos, migración o dataset.
* [devops — build, deploy y portabilidad del ADS](/agents/devops.md) - Configura CI/CD, despliegue y portabilidad por proveedor; delégale cualquier FU/DU de pipeline, entorno o publicación (con aprobación si es producción).
* [docs — documenta el ADS y el trabajo de ABM](/agents/docs.md) - Escribe y mantiene documentos OKF, el manual y la memoria del proyecto según okf-author y standards/communication.md; delégale al cerrar cualquier unidad o fase que deba quedar documentada.
* [finops — controla el espacio de tokens del ADS](/agents/finops.md) - Registra consumo de tokens, reporta N1/N2 y vigila presupuestos con token-ledger; delégale al cierre de cada FU/DU o cuando un presupuesto de ads.yaml esté cerca del tope.
* [frontend — construye la interfaz del ADS](/agents/frontend.md) - Implementa UI/UX según standards/frontend/ y el design system elegido, con estados vacíos y de error; delégale cualquier FU/DU cuya salida sea una interfaz consumible.
* [integrations — conecta el ADS con servicios externos](/agents/integrations.md) - Elige la vía de integración más segura y de mínimo privilegio usando integrate-safely; delégale cualquier FU/DU que conecte el ADS con una API, webhook o servicio de terceros.
* [orchestrator — coordina el encargo sin construir](/agents/orchestrator.md) - Clasifica el encargo, arma el plan por FU/DU, paraleliza lo independiente y delega con especificación completa; delégale cuando empieza un encargo o hay que repartir trabajo entre roles.
* [qa — prueba de punta a punta cada DU](/agents/qa.md) - Prueba rutas críticas, estados vacíos y de error según standards/testing/ y la completitud del perfil; delégale la verificación de cualquier DU antes de darlo por entregado.
* [reviewer — revisión independiente y adversarial](/agents/reviewer.md) - Revisa con contexto limpio lo que otro rol construyó, usando review-independent y ./abm check, y reporta hallazgos con archivo:línea y severidad; delégale al cierre de cada milestone.
* [security — aplica seguridad y gobierno de secretos](/agents/security.md) - Implementa controles OWASP, gestión de secretos y defensa contra prompt injection según standards/security/; delégale cualquier FU/DU con auth, datos sensibles, pagos o superficie agéntica.

# methodology

* [Metodologías de ABM — índice](/methodology/README.md) - Qué modo metodológico usar, cuándo, cómo se mezclan y dónde está cada pieza del motor.
* [AIDD — híbrido explorar/consolidar/construir](/methodology/aidd.md) - Explorar en VIBE, consolidar en IDD o SDD, construir con revisión humana obligatoria, cerrar.
* [Niveles de ceremonia](/methodology/ceremony.md) - Prototipo, MVP, Producto y Enterprise-Regulado — modo por defecto, gates, Contrato ADS y dashboard de tokens.
* [Control de deriva (drift)](/methodology/drift.md) - Qué compara `drift`, cuándo corre y cómo propone actualizar intención, spec, contratos y código.
* [Gobernanza para Enterprise-Regulado](/methodology/governance-regulated.md) - Capa opcional de trazabilidad alineada con ISO/IEC 42001, NIST AI RMF y el Reglamento europeo de IA.
* [IDD — Intent-Driven Development](/methodology/idd.md) - Minimum Viable Spec, intent tree Propósito→Usuario→Medios, y control del drift de intención.
* [Mezcla de metodologías por módulo](/methodology/mixing.md) - Cómo un mismo ADS combina VIBE, IDD, SDD, SPDD y AIDD por módulo, con reglas y un ejemplo.
* [Router metodológico](/methodology/router.md) - Seis dimensiones, reglas de decisión, disparadores de escalamiento/desescalamiento y cómo lo ejecuta `abm methodology classify`.
* [SDD — Spec-Driven Development](/methodology/sdd.md) - Requirements (EARS) → design → tasks con trazabilidad requisito↔tarea↔test y revisión humana.
* [SPDD — Spec-as-Prompt-Contract Development](/methodology/spdd.md) - Contrato de prompt versionado, sincronizado en ambos sentidos con el código.
* [VIBE — exploración desechable](/methodology/vibe.md) - Cuándo y cómo usar VIBE, su flujo, gates y salida obligatoria hacia consolidate.

# standards

* [Estándares de ABM — índice](/standards/README.md) - Mapa de standards/ — qué contiene, cuándo se carga cada archivo y quién lo usa.
* [Estándar de accesibilidad — índice](/standards/a11y/README.md) - Checklist WCAG 2.2 AA aplicable a cualquier interfaz con usuario humano.
* [Estándar de superficie agéntica — índice](/standards/agentic/README.md) - Diseño agent-friendly para que un agente externo descubra, opere y audite un ADS sin integración a medida.
* [Estándar de backend — índice](/standards/backend/README.md) - Alcance del estándar de backend y cómo se relaciona con sus archivos hermanos.
* [Definition of Done — backend](/standards/backend/checklist-dod.md) - Casillas verificables para cerrar una FU/DU de API.
* [Criterios de revisión — backend](/standards/backend/review-criteria.md) - Qué mira el revisor independiente de API y con qué severidad.
* [Estándar de backend](/standards/backend/standard.md) - Qué construye y cómo cualquier superficie de API producida por ABM.
* [Tests de backend](/standards/backend/testing.md) - Qué tests se escriben, qué cubren y en qué momento corren.
* [Protocolo de comunicación del agente](/standards/communication.md) - Cómo informa un agente que construye u opera un ADS — semáforo, formato de reporte y ejemplos.
* [Transversales — entornos, CI/CD, feature flags y costo](/standards/cross-cutting.md) - Lo que aplica a todo ADS sin importar la capa: entornos, integración continua, flags y costo.
* [Estándar de database — índice](/standards/database/README.md) - Alcance del estándar de base de datos y cómo se relaciona con sus archivos hermanos.
* [Definition of Done — database](/standards/database/checklist-dod.md) - Casillas verificables para cerrar una FU/DU de datos.
* [Criterios de revisión — database](/standards/database/review-criteria.md) - Qué mira el revisor independiente de datos y con qué severidad.
* [Estándar de database](/standards/database/standard.md) - Qué construye y cómo cualquier almacén de datos producido por ABM.
* [Tests de database](/standards/database/testing.md) - Qué tests se escriben, qué cubren y en qué momento corren.
* [Estándar de FinOps y tokens — índice](/standards/finops/README.md) - Ledger, niveles de dashboard, presupuestos blando/duro y costo por unidad, incluidos tokens.
* [Estándar de frontend — índice](/standards/frontend/README.md) - Alcance del estándar de frontend y cómo se relaciona con sus archivos hermanos.
* [Definition of Done — frontend](/standards/frontend/checklist-dod.md) - Casillas verificables para cerrar una FU/DU de interfaz de usuario.
* [Criterios de revisión — frontend](/standards/frontend/review-criteria.md) - Qué mira el revisor independiente de UI y con qué severidad.
* [Estándar de frontend](/standards/frontend/standard.md) - Qué construye y cómo cualquier interfaz de usuario producida por ABM.
* [Tests de frontend](/standards/frontend/testing.md) - Qué tests se escriben, qué cubren y en qué momento corren.
* [Estándar de observabilidad — índice](/standards/observability/README.md) - Logs, trazas y métricas mínimas de cualquier ADS.
* [Estándares de seguridad — índice](/standards/security/README.md) - Alcance de standards/security/ y cuándo se carga cada archivo.
* [Seguridad de LLM y agentes](/standards/security/llm-agentic.md) - OWASP Top 10 para LLM y OWASP Top 10 para aplicaciones agénticas, y defensa contra prompt injection.
* [Seguridad de la cadena de suministro](/standards/security/supply-chain.md) - Lockfiles, actualización de dependencias, SBOM, licencias y secret scanning.
* [Seguridad web y de API](/standards/security/web-api.md) - OWASP Top 10 y OWASP ASVS aplicados al frontend y al backend de un ADS.
* [Estándar de tests — índice](/standards/testing/README.md) - Pirámide de tests y su verificación en CI para cualquier ADS.

# stacks

* [Catálogo de stacks](/stacks/README.md) - Índice de los 14 casos de stack, cómo los usa el comando stack, leyenda de columnas y política de revisión.
* [Caso: apps con IA (RAG/agentes)](/stacks/cases/ai-app-rag-agents.md) - Opciones de stack para aplicaciones con recuperación aumentada y agentes, con gateway LLM, vector DB y observabilidad.
* [Caso: API/backend puro](/stacks/cases/api-backend.md) - Paquetes para un servicio API sin UI propia, consumido por programas o agentes, con equivalencias por nube.
* [Caso: automatizaciones e integraciones](/stacks/cases/automation-integrations.md) - Opciones de stack para flujos de automatización e iPaaS, de un flujo simple en n8n/Zapier a integración corporativa.
* [Caso: CLI y extensiones](/stacks/cases/cli-extensions.md) - Opciones de stack para herramientas de línea de comandos y extensiones de editor/navegador, con foco en distribución y portabilidad de runtime.
* [Caso: App de escritorio](/stacks/cases/desktop-app.md) - Paquetes desktop (Tauri/Electron) con backend opcional de sincronización y equivalencias por nube.
* [Caso: E-commerce](/stacks/cases/e-commerce.md) - Paquetes de tienda en línea (SaaS vs headless self-hosted vs corporativo), comprar vs construir y equivalencias por nube.
* [Caso: ERP/CRM/backoffice](/stacks/cases/erp-crm-backoffice.md) - Opciones de stack para un backoffice interno (ERP, CRM u operaciones), y cuándo comprar Odoo/ERPNext en vez de construir.
* [Caso: producto de inteligencia/consultoría](/stacks/cases/intelligence-product.md) - Opciones de stack para el perfil intelligence-product (informe argumentado + dataset o dashboard validado entregados juntos).
* [Caso: Dashboard/BI interno](/stacks/cases/internal-dashboard-bi.md) - Paquetes para un panel de inteligencia de negocio de uso interno, comprar vs construir y equivalencias por nube.
* [Caso: Landing / sitio de marketing](/stacks/cases/landing-marketing.md) - Paquetes FE+hosting+CMS+pagos para un sitio de marketing o landing, con equivalencias por nube.
* [Caso: integración sobre legacy corporativo](/stacks/cases/legacy-integration.md) - Opciones de stack cuando el ADS es, en sí mismo, una capa de modernización o integración sobre sistemas corporativos existentes.
* [Caso: App móvil](/stacks/cases/mobile-app.md) - Paquetes multiplataforma (Expo/RN, Flutter) con backend, tiendas y equivalencias por nube.
* [Caso: aplicaciones en tiempo real](/stacks/cases/realtime.md) - Opciones de stack para chat, notificaciones en vivo, dashboards colaborativos y streaming de eventos.
* [Caso: Web app SaaS](/stacks/cases/saas-web-app.md) - Paquetes FE+BE+DB+auth+pagos+deploy para una aplicación SaaS multi-tenant, con equivalencias por nube.
* [Equivalencias multinube](/stacks/clouds.md) - Matriz AWS / Azure / GCP / on-prem por bloque de infraestructura, IaC multinube y la regla de abstracción o plan de salida.
* [Lenguajes dominantes en entornos corporativos](/stacks/languages.md) - Versiones LTS vigentes, frameworks típicos por capa e interoperabilidad con legacy para TS/JS, Python, Java/Kotlin, C#/.NET, Go y PHP.
* [Patrones de integración con legacy corporativo](/stacks/legacy.md) - Catálogo de patrones de integración, conectores típicos, SSO corporativo y redes privadas, y su uso desde el comando assess.
* [Proveedores LLM y capa System One](/stacks/llm-providers.md) - Gateway LLM como categoría, matriz de capacidades y precios con fecha, y la capa de decisión tipada System One.

# integrations

* [Integraciones seguras — mapa de vías](/integrations/README.md) - Orden de preferencia y matriz de riesgo/esfuerzo para conectar un ADS a sistemas externos.
* [Agentes externos — Hermes y A2A](/integrations/agents/README.md) - Cómo un agente externo descubre, opera y, si aplica, conversa con un ADS de ABM.
* [A2A (Agent2Agent) — cuándo y cómo](/integrations/agents/a2a.md) - Cuándo publicar un Agent Card A2A, sus campos obligatorios y la relación con MCP.
* [Hermes Agent — integración con ABM](/integrations/agents/hermes.md) - Instalación, carga de AGENTS.md, plantilla mcp_servers, modo one-shot para CI y límites conocidos.
* [Integraciones vía API — clientes tipados](/integrations/api/README.md) - Clientes generados desde OpenAPI, reintentos con jitter, idempotencia, timeouts y errores problem+json.
* [Auth para integraciones — OAuth2/OIDC](/integrations/auth/README.md) - Flujos, PKCE, client credentials y scopes mínimos por agente para integraciones externas.
* [Capa de decisión System One](/integrations/decision/README.md) - Interfaz neutral decide(state, questions), cadena de proveedores y routing por confianza.
* [Jev (TypeSafe AI) — primer adaptador de System One](/integrations/decision/typesafe-jev.md) - Endpoint, forma de request/response, precios y límites, SDKs, limitaciones y recetas de Jev.
* [Gateway LLM — categoría](/integrations/llm-gateway/README.md) - Interfaz de chat compatible como lingua franca, variables de configuración y evals mínimos para cambiar de proveedor.
* [MCP en ABM — principios](/integrations/mcp/README.md) - Cómo ABM y sus ADS consumen servidores MCP con mínimo privilegio y disciplina de tokens.
* [Catálogo de servidores MCP verificados](/integrations/mcp/catalog.md) - Servidores MCP oficiales o verificados por categoría, con transporte, auth y modo recomendado.
* [Configuración MCP por herramienta](/integrations/mcp/config-by-tool.md) - Plantilla del servidor MCP de ABM y de un servidor de terceros para cada herramienta agéntica soportada.
* [Seguridad de servidores MCP](/integrations/mcp/security.md) - Prompt injection, tool poisoning, allowlists y auth para servidores MCP en ABM.
* [Observabilidad — espacio de tokens en producción (N3)](/integrations/observability/README.md) - Backends posibles, presupuestos y alertas por tenant/funcionalidad, chargeback y qué no capturar por PII.
* [N3 — exportar el ledger a OpenTelemetry](/integrations/observability/n3-otel.md) - Mapeo de atributos gen_ai.*, la métrica de tokens y el pipeline OTel del nivel N3.
* [Otras vías de integración](/integrations/other-ways.md) - SDKs, colas y eventos, iPaaS, CSV/Excel y SQL de mínimo privilegio, y cuándo usar cada una.
* [Gestión de secretos](/integrations/secrets.md) - .env.example, gestor de secretos por plataforma, secret scanning en CI y rotación.
* [Webhooks — recepción segura de eventos](/integrations/webhooks/README.md) - Verificación de firma HMAC, timestamp y replay, idempotencia y cola de procesamiento.

# templates

* [Plantillas de ABM — índice](/templates/README.md) - Qué plantilla usar según el modo metodológico y el momento del ciclo de vida.
* [adr.md — decisión ligera](/templates/adr.md) - ADR ligero para decisiones de diseño que el agente toma en IDD/SDD/AIDD y registra sin ceremonia formal.
* [assessment.md — inventario brownfield](/templates/assessment.md) - Inventario que produce assess antes de intervenir un sistema existente.
* [closeout.md — cierre de unidad](/templates/closeout.md) - Qué se hizo, sincronía intención/spec/contrato/código, tokens de la unidad y pendientes.
* [Plantilla de playbook de comando](/templates/command-playbook.md) - Esqueleto OKF que sigue todo commands/<name>.md; lo exige `./abm lint playbooks`.
* [explore-log.md — aprendizajes de VIBE](/templates/explore-log.md) - Registro de una exploración desechable y la recomendación de modo siguiente para consolidate.
* [handoff.md — traspaso entre agentes o sesiones](/templates/handoff.md) - Contexto mínimo para que otro agente o una sesión nueva retome el trabajo sin releer todo.
* [intent.md — árbol de intención (IDD)](/templates/intent.md) - Minimum Viable Spec de IDD — Propósito → Usuario → Medios, restricciones, criterios de éxito y no-objetivos.
* [methodology-map.md — mezcla metodológica por módulo](/templates/methodology-map.md) - Tabla módulo | modo | justificación | revisión | disparadores, salida de abm methodology classify.
* [plan.md — plan de construcción](/templates/plan.md) - FU/DU por milestone con criterios de aceptación; base del Planning Gate y de start-execution.
* [prompt-contract.md — contrato de prompt versionado (SPDD)](/templates/prompt-contract.md) - Versión, intención, entradas/salidas, invariantes, tests de aceptación y archivos vinculados.
* [design.md — diseño técnico (SDD)](/templates/spec/design.md) - Diseño que satisface los requisitos de requirements.md, referenciando cada REQ-NNN.
* [requirements.md — requisitos EARS (SDD)](/templates/spec/requirements.md) - Requisitos en formato EARS con ID único, usados por SDD para trazar TASK↔REQ↔TEST.
* [tasks.md — tareas trazables (SDD)](/templates/spec/tasks.md) - Tabla TASK ↔ REQ ↔ TEST que descompone design.md en trabajo verificable.
* [state.md — memoria compacta del proyecto](/templates/state.md) - Estado mínimo para retomar un ADS sin releer todo su historial; se actualiza al cerrar sesión.

# profiles

* [Contrato de perfiles de ADS](/profiles/_contract.md) - Esquema que todo perfil de ADS debe seguir y reglas de composición de perfiles híbridos.
* [api-service](/profiles/api-service/profile.md) - Servicio o herramienta consumida por programas o agentes (API, CLI o servidor MCP) sin UI propia.
* [automation-integration](/profiles/automation-integration/profile.md) - Flujos que conectan sistemas: integraciones, automatizaciones, ETL ligero y agentes de proceso.
* [data-product](/profiles/data-product/profile.md) - Datos que se consultan: dataset validado, pipeline, capa de métricas o dashboard.
* [intelligence-product](/profiles/intelligence-product/profile.md) - Híbrido de consultoría: informe argumentado respaldado por un dataset o dashboard validado.
* [research-report](/profiles/research-report/profile.md) - Documento que se lee: conocimiento sintetizado y argumentado desde fuentes citadas.
* [software-app](/profiles/software-app/profile.md) - Perfil de referencia para software con interfaz de usuario: web, móvil, escritorio, dashboard o ERP.

# contract

* [Contrato ADS](/contract/README.md) - Requisitos verificables que cumple todo ADS (y ABM), por nivel, declarados en ads.yaml.

# okf

* [Perfil ABM sobre OKF v0.2](/okf/PROFILE.md) - Reglas de productor de ABM sobre el Open Knowledge Format (OKF) v0.2; más estrictas que la spec, nunca contrarias.

# knowledge

* [knowledge/ — sub-bundle OKF del ADS](/knowledge/README.md) - Conocimiento de diseño del ADS activo, en OKF v0.2, navegado desde knowledge/index.md.

# examples

* [examples/](/examples/README.md) - Ejemplos de referencia; el núcleo nunca depende de ellos.
* [AGENTS.md — panel de ventas](/examples/panel-ventas/AGENTS.md) - Reglas para agentes que operan o modifican el ADS panel-ventas; la gobernanza completa es la de ABM.
* [Ejemplo golden path — panel de ventas](/examples/panel-ventas/README.md) - ADS completo y ejecutable (dashboard con auth, base de datos y gráficos) recorrido con ABM de encargo a entrega, con build, tests y Contrato ADS en verde.
* [Encargo — panel de ventas](/examples/panel-ventas/START_PROJECT.md) - Encargo original del ADS panel-ventas tal como lo escribió la persona, antes de init-project.
* [Reporte de tokens](/examples/panel-ventas/TOKENS.md) - Consumo de tokens y costo del ADS (construcción y operación), generado desde el ledger.
* [Contratos de API — panel de ventas](/examples/panel-ventas/design_docs/api-contracts.md) - Endpoints, autenticación, autorización por rol y errores problem+json del panel de ventas (design doc HIGH).
* [Modelo de datos — panel de ventas](/examples/panel-ventas/design_docs/data-model.md) - ERD, restricciones, índices y migraciones del panel de ventas (design doc HIGH del perfil software-app).
* [Interfaz y arquitectura — panel de ventas](/examples/panel-ventas/design_docs/ui-architecture.md) - Pantallas, estados, guía de estilo y componentes del panel de ventas (design docs MEDIUM/LIGHT).
* [Cola de pendientes](/examples/panel-ventas/docs/_work/PENDIENTES.md) - Decisiones no bloqueantes acumuladas para el humano, cada una con su default ya aplicado.
* [Registro de decisiones — panel de ventas](/examples/panel-ventas/docs/decision_log.md) - Decisiones de stack, datos, identidad y superficie agéntica del panel de ventas, con alternativas y reversibilidad.
* [Plan de salida — panel de ventas](/examples/panel-ventas/docs/exit-plan.md) - Cómo migrar el panel de ventas fuera del stack de demo sin reescribir reglas ni contratos.
* [Manual de operación — panel de ventas](/examples/panel-ventas/docs/manual/operacion.md) - Cómo arrancar, sembrar, migrar, respaldar y operar el panel de ventas, para personas y agentes.
* [Memoria del proyecto — panel de ventas](/examples/panel-ventas/docs/project_memory.md) - Estado vigente del ADS panel-ventas para retomar el trabajo en una sesión nueva (session-start).
* [Registro de trabajo — panel de ventas](/examples/panel-ventas/docs/work_log.md) - Registro por unidad del panel de ventas con lo producido, el quality gate aplicado, la evidencia y los riesgos residuales.
* [Task tracker — panel de ventas](/examples/panel-ventas/implementation/task_tracker.md) - Estado de las FU y DU del panel de ventas por milestone (start-execution).
* [Unidades de trabajo — panel de ventas](/examples/panel-ventas/implementation/user_units.md) - FU y DU del panel de ventas con criterio de aceptación atado a la regla de completitud de software-app.
* [Mapa metodológico — panel-ventas](/examples/panel-ventas/planning/methodology-map.md) - Modo metodológico por módulo del ADS, con justificación, revisión y disparadores.
* [Requisitos — panel de ventas](/examples/panel-ventas/planning/requirements.md) - Requisitos EARS del panel de ventas con trazabilidad a unidades y tests, alcance y riesgos (init-project, paso 6).

# adapters

* [adapters/ — generador de adaptadores por herramienta](/adapters/README.md) - Cómo abm sync genera, desde fuentes neutrales, lo que cada herramienta de IA necesita leer; plantillas turbo.

# design_docs

* [design_docs/](/design_docs/README.md) - Documentos de diseño que exige el perfil activo, con su nivel de detalle.

# implementation

* [Seguimiento de tareas](/implementation/task_tracker.md) - Todas las FU/DU del ADS agrupadas por milestone, con su estado.
* [Unidades de trabajo (FU/DU)](/implementation/user_units.md) - Definición de FU y DU con criterios de aceptación ligados a la completitud del perfil.

# planning

* [Preguntas](/planning/questions.md) - Preguntas de planificación: bloqueantes y supuestos encolados.
* [Requisitos](/planning/requirements.md) - Requisitos funcionales y no funcionales, cada uno explícito, implícito o supuesto.
* [Riesgos](/planning/risks.md) - Riesgos con probabilidad, impacto y mitigación.
* [Alcance](/planning/scope.md) - Qué entra, qué no entra y qué queda para el futuro.
