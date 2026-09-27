---
name: perf-audit
description: Mide rendimiento contra los umbrales de standards/ — Core Web Vitals en frontend, SLO/latencia en backend, plan de consultas en database. Úsala antes de un release o cuando se sospecha una regresión de rendimiento.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# perf-audit

## Pasos
1. Identifica la(s) ruta(s) crítica(s) de negocio en alcance (la unidad lo declara, o el perfil la fija).
2. **Frontend:** mide LCP, INP y CLS en p75 de esa ruta contra los umbrales de
   `standards/frontend/standard.md` (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1); revisa peso de JS/CSS
   inicial contra el presupuesto declarado del ADS.
3. **Backend:** mide latencia p95/p99 y tasa de error del endpoint contra el SLO declarado en
   `standards/backend/standard.md`; confirma que el servicio siga sin estado bajo carga.
4. **Database:** revisa el plan de ejecución (`EXPLAIN` o equivalente) de las consultas de la ruta
   crítica; confirma índices presentes en filtros/joins/orden frecuentes
   (`standards/database/standard.md`).
5. Si el flujo invoca un modelo de lenguaje, mide latencia y costo por unidad de negocio
   (`standards/finops/README.md`); confirma límites de tokens/llamadas para evitar consumo sin techo.
6. Compara contra la medición previa (si existe) para distinguir regresión de línea base nueva.
7. Todo umbral incumplido se registra con severidad (`standards/frontend/review-criteria.md` o
   `standards/backend/review-criteria.md` según la capa) y su plan de mitigación.

## Criterios de salida
- Métricas medidas (no estimadas) en la ruta crítica declarada, con su fuente.
- Ningún umbral "bueno" incumplido sin mitigación o entrada en `abm pending add`.
- Reporte final según `standards/communication.md` (≤ 12 líneas), con las métricas clave.
