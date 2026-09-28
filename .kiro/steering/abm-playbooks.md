---
inclusion: manual
---
<!-- GENERADO por abm sync desde commands/*.md. No editar. -->
# Playbooks de ABM

La gobernanza está en `AGENTS.md`. Cada fila es un playbook neutral en `commands/<nombre>.md`: léelo solo cuando toque (no los precargues).

Flujo: `session-start` siempre primero → sin plan publicado, `init-project` → `start-execution` por unidad → `review` por milestone → `closeout` → `iterate`.

| Playbook | Para qué |
|---|---|
| `a11y` | Verifica accesibilidad WCAG 2.2 AA de la capa de interfaz antes de entregar. |
| `ads-check` | Verifica que el ADS cumple su nivel del Contrato ADS, estático y dinámico. |
| `api` | Construye la capa de API/servicio de una unidad con contrato de errores y quality gate. |
| `assess` | Inventaría un stack existente y propone el patrón de integración más simple que funcione. |
| `bootstrap` | Detecta la plataforma, corre doctor y sync, y confirma que el repo está listo para trabajar. |
| `closeout` | Sincroniza intención, spec, contrato y código, registra tokens y actualiza la memoria del proyecto. |
| `connect` | Da al ADS su superficie agéntica (ads.yaml, skill, MCP, API) para que otro agente lo opere. |
| `consolidate` | Convierte los aprendizajes de un explore en spec y diseño definitivos (IDD/SDD). |
| `db` | Modela y migra el esquema de datos de una unidad con migraciones reversibles. |
| `decide` | Resuelve una decisión tipada (choice/score/boolean) con la capa de decisión y su routing por confianza. |
| `deploy` | Publica el ADS en su entorno de destino tras pasar la checklist previa y con rollback listo. |
| `doctor` | Diagnostica el entorno (Python, git, estructura, config) en lenguaje simple y sugiere arreglos. |
| `drift` | Detecta y resuelve la deriva entre intención, spec, contrato de prompt y código real. |
| `explore` | Prueba y descarta en una rama sandbox con tiempo acotado para resolver una incertidumbre. |
| `fix` | Reproduce el bug, escribe el test que falla, aplica el cambio mínimo y verifica sin regresión. |
| `help` | Muestra el catálogo de comandos por fase y resuelve alias en español. |
| `init-project` | Elige perfil y ceremonia, clasifica la metodología, explora el stack con el humano y publica el plan. |
| `integrate` | Conecta el ADS con un tercero por la vía más segura disponible, de MCP a SQL de mínimo privilegio. |
| `intent` | Registra el qué y el por qué de una unidad antes de especificarla o construirla. |
| `iterate` | Aplica un cambio, mejora o corrección tras la entrega, con spec-delta antes de tocar código. |
| `methodology` | Asigna VIBE, IDD, SDD, SPDD o AIDD a un módulo según sus seis dimensiones de riesgo. |
| `pending` | Lista, agrega y resuelve en lote las decisiones y defaults que turbo dejó en cola. |
| `perf` | Verifica rendimiento, escalabilidad básica y costo por unidad antes de entregar. |
| `plan` | Ordena FU y DU en el tracker, redacta el plan y lo publica para su aprobación o cola. |
| `prompt-contract` | Fija entradas, salidas, límites y HITL de un prompt o agente antes de construirlo. |
| `refactor` | Reestructura código manteniendo la suite de tests en verde antes y después, sin cambiar comportamiento. |
| `release` | Cierra una versión del ADS con semver, changelog y verificación previa completa. |
| `review` | Lanza un revisor con contexto limpio que verifica la última unidad o milestone completado. |
| `security` | Audita la unidad o el ADS contra OWASP y verifica que no haya secretos expuestos. |
| `session-start` | Lee la memoria del proyecto y la cola de pendientes, y dice por dónde retomar el trabajo. |
| `spec` | Convierte la intención en requirements, design y tasks verificables (formato EARS). |
| `stack` | Explora 2-3 opciones de stack con trade-offs y espera la elección del humano (HITL). |
| `start-execution` | Verifica que el plan esté listo y ejecuta las FU y DU aprobadas hasta la entrega. |
| `test` | Verifica la unidad con la pirámide de pruebas del perfil, priorizando rutas críticas. |
| `tokens` | Registra, reporta y verifica el consumo y presupuesto de tokens de cada unidad. |
| `ui` | Construye la capa de interfaz de una unidad siguiendo el standard de frontend y su quality gate. |

CLI para agentes: `./abm <orden> --json` (Windows: `abm.cmd`). Servidor MCP: `python3 scripts/abm.py mcp`.
