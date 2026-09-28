---
type: Checklist
title: Definition of Done — backend
description: Casillas verificables para cerrar una FU/DU de API.
tags: [backend, dod, checklist]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# DoD — backend

- [ ] Contrato de API (OpenAPI, schema GraphQL o equivalente) publicado y coincide con la
      implementación.
- [ ] Errores responden `application/problem+json` con `type`, `title`, `status`, `detail`.
- [ ] Todo endpoint declara su requisito de autenticación y autorización; ninguno queda abierto por
      omisión.
- [ ] Rate limiting definido para endpoints públicos o de alto costo.
- [ ] Operaciones mutantes son idempotentes (llave de idempotencia o upsert semántico) y probadas
      con reintento.
- [ ] Jobs asíncronos tienen reintento con backoff y una cola de fallidos visible.
- [ ] Caché tiene invalidación explícita documentada.
- [ ] Logs estructurados con id de correlación; trazas OpenTelemetry en los endpoints críticos.
- [ ] SLO de disponibilidad y latencia declarado para cada endpoint crítico.
- [ ] Si consume un modelo de lenguaje, el costo por unidad de negocio está estimado o medido
      (`standards/finops/README.md`).
- [ ] Si expone superficie agéntica, cumple `standards/agentic/README.md` (idempotencia, errores
      estructurados, paginación, scopes mínimos).
- [ ] Tests unitarios, de integración y de contrato en verde.
