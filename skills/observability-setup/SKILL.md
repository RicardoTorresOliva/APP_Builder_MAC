---
name: observability-setup
description: Instrumenta logs estructurados, trazas y métricas OpenTelemetry en un servicio, y conecta el ledger de tokens/costo, siguiendo standards/observability/ y standards/finops/. Úsala al construir un servicio nuevo o al agregar una integración con un modelo de lenguaje.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# observability-setup

## Pasos

1. Lee `standards/observability/README.md` antes de instrumentar.
2. Agrega logs estructurados (JSON) con id de correlación por solicitud, propagado a cada servicio
   que la solicitud toque; confirma que ningún dato sensible quede en texto plano.
3. Instrumenta trazas OpenTelemetry de punta a punta para la ruta crítica declarada; un salto entre
   servicios es un span hijo de la traza padre, no una traza nueva desconectada.
4. Define métricas de latencia (p50/p95/p99), tasa de error y throughput por endpoint crítico;
   conecta cada SLO de `standards/backend/standard.md` a una alerta con acción definida.
5. Si el servicio invoca un modelo de lenguaje, emite el evento de tokens/costo según
   `standards/finops/README.md` (fase, fuente, tokens, modelo, unidad, funcionalidad, tenant); si no
   hay telemetría del proveedor, usa estimación y márcala `estimado` explícitamente.
6. Conecta el evento al ledger (`abm tokens record` o `estimate`) y confirma que el nivel de
   dashboard (N1/N2/N3) corresponda al perfil activo.
7. Verifica que un incumplimiento de SLO o un tope duro de presupuesto dispare la alerta o el
   bloqueante correspondiente (AGENTS.md §Bloqueantes, ítem f).

## Criterios de salida

- Logs, trazas y métricas presentes en la ruta crítica del servicio, verificables en un recorrido real.
- Evento de tokens emitido (medido o `estimado`) si el servicio invoca un modelo de lenguaje.
- Alertas de SLO y de presupuesto con acción definida, no solo configuradas.
- Reporte final según `standards/communication.md` (≤ 12 líneas).
