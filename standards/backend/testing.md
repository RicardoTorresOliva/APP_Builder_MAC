---
type: Standard
title: Tests de backend
description: Qué tests se escriben, qué cubren y en qué momento corren.
tags: [backend, tests]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Tests de backend

Ver la pirámide general en `standards/testing/README.md`. Aquí, lo específico de API.

| Nivel | Cubre | Cuándo corre |
|---|---|---|
| Unitario | lógica de dominio pura, sin red ni base de datos: reglas de negocio, cálculos, validadores | en cada commit, local y en CI |
| Integración | el endpoint contra sus dependencias reales o equivalentes (base de datos de prueba, cola, caché); incluye el camino feliz y los errores esperados | en cada PR que toque el endpoint |
| Contrato | el esquema publicado (OpenAPI/GraphQL) no rompe a los consumidores existentes; se corre contra el contrato, no contra la implementación interna | en cada cambio al contrato y antes de release |
| Carga (según perfil) | comportamiento bajo el SLO declarado (latencia, throughput) en los endpoints críticos | antes de un hito de escalamiento o release mayor |

## Reglas
- Un test de integración que solo repite lo que ya cubre el unitario se recorta; el objetivo es
  cubrir el punto de integración, no duplicar cobertura.
- Idempotencia se prueba explícitamente: la misma solicitud, dos veces, produce el mismo efecto.
- Los tests de contrato corren contra ejemplos reales de `application/problem+json`, no contra un
  mock que asuma siempre el camino feliz.
- Superficie agéntica (si existe) se prueba con el mismo guion que `abm agent-conformance`:
  descubrir → listar → leer → `--dry-run`.
