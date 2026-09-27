---
name: test-strategy
description: Decide qué tests escribir y en qué nivel de la pirámide (unitario, integración/componente, E2E/contrato) para una FU/DU, siguiendo standards/testing/. Úsala al planificar la cobertura de una unidad antes de construirla, o al auditar por qué una unidad no tiene evidencia suficiente.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# test-strategy

## Pasos
1. Lee `standards/testing/README.md` y el `testing.md` de la(s) capa(s) que toca la unidad
   (`standards/frontend/testing.md`, `standards/backend/testing.md`, `standards/database/testing.md`).
2. Identifica qué de la unidad es lógica pura (candidata a unitario), qué es integración entre
   componentes/servicios reales (candidata a integración) y qué es una ruta crítica de negocio de
   punta a punta (candidata a E2E).
3. Ubica cada test en el nivel más bajo que pueda probarlo; si algo solo se prueba vía E2E hoy,
   regístralo como pendiente de bajar de nivel, no lo dejes así por comodidad.
4. Si la unidad expone o cambia un contrato (API, schema), agrega o actualiza el test de contrato
   correspondiente.
5. Si la unidad es idempotente o multi-tenant, agrega el caso de reintento o de aislamiento entre
   tenants explícitamente; no asumas que el test funcional ya lo cubre.
6. Verifica que los datos de prueba sean realistas y no contengan datos sensibles reales.
7. Corre los tres niveles; un test en rojo bloquea el cierre de la unidad salvo que quede en
   `abm pending add` con motivo y fecha de retoma.
8. Registra el resultado por nivel (verde/rojo, cuántos) en el reporte de cierre.

## Criterios de salida
- Cobertura de lógica crítica dentro del mínimo que el perfil activo exige.
- Ningún nivel de la pirámide vacío si la unidad tiene lógica, integración y ruta crítica que lo
  ameriten.
- Reporte final según `standards/communication.md` (≤ 12 líneas), con el resultado por nivel.
