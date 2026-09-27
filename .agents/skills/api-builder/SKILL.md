---
name: api-builder
description: Diseña o modifica un endpoint de API (REST/OpenAPI, GraphQL o RPC tipado) aplicando el estándar de backend de ABM — contrato primero, errores problem+json, authN/authZ, idempotencia, observabilidad y superficie agéntica. Úsala en cualquier FU/DU que agregue o cambie una API.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# api-builder

## Pasos
1. Lee `standards/backend/standard.md` (rango relevante) antes de escribir el endpoint.
2. Escribe o actualiza el contrato (OpenAPI/schema) primero; la implementación sigue al contrato,
   no al revés.
3. Diseña la respuesta de error en `application/problem+json` (`type`, `title`, `status`, `detail`)
   para cada caso de falla esperado, no solo el camino feliz.
4. Define autenticación y autorización explícitas para el endpoint; sin acceso implícito.
5. Si la operación muta estado, hazla idempotente (llave de idempotencia o upsert semántico) y
   pruébalo con un reintento real.
6. Declara rate limiting si el endpoint es público o de alto costo (respuesta 429 + `Retry-After`).
7. Diseña la superficie agéntica del endpoint junto con la API, siguiendo
   `standards/agentic/README.md`: paginación, límites declarados, descripción corta y precisa si se
   expone como tool.
8. Instrumenta logs estructurados con id de correlación y trazas OpenTelemetry
   (`standards/observability/README.md`).
9. Si invoca un modelo de lenguaje, estima o mide el costo por unidad de negocio
   (`standards/finops/README.md`).
10. Revisa el endpoint contra `standards/security/web-api.md` (OWASP Top 10 + ASVS del nivel del perfil).
11. Escribe o actualiza tests según `standards/backend/testing.md` (unitario, integración, contrato).
12. Corre `standards/backend/checklist-dod.md` completo antes de reportar la unidad como hecha.

## Criterios de salida
- Contrato publicado coincide con la implementación; tests de contrato en verde.
- Todas las casillas de `standards/backend/checklist-dod.md` marcadas o justificadas.
- Sin secreto ni dato sensible en logs, errores o respuestas.
- Reporte final según `standards/communication.md` (≤ 12 líneas).
