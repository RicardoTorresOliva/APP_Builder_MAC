---
type: Reference
title: Estándar de tests — índice
description: Pirámide de tests y su verificación en CI para cualquier ADS.
tags: [testing, ci, pirueta-de-tests]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Testing — índice

## Pirámide
```
        E2E (pocos, caros, rutas críticas de negocio)
      Integración / contrato (moderados, contra dependencias reales)
   Unitarios (muchos, baratos, lógica pura)
```
Cada capa tiene su detalle en `standards/frontend/testing.md`, `standards/backend/testing.md` y
`standards/database/testing.md`. Este archivo fija lo común.

## Regla de oro
Un test se ubica en el nivel más bajo que pueda probar lo que necesita probar. Duplicar cobertura en
un nivel superior (p. ej. probar una regla de negocio solo vía E2E) se recorta.

## CI
- Los tres niveles corren en cada PR; el nivel de carga (si el perfil lo exige) corre antes de un
  hito de escalamiento o release mayor.
- Un test en rojo bloquea el merge; no se omite ("skip") sin un pendiente (`abm pending add`) que
  explique por qué y cuándo se retoma.
- Datos de prueba realistas, nunca placeholders vacíos; sin datos sensibles reales en fixtures.

## Cobertura
El perfil activo fija el mínimo de cobertura de lógica crítica; perseguir el 100 % sin relación con
el riesgo real del código no es el objetivo.

## Verificación
El resultado de los tests (verde/rojo por nivel) forma parte del reporte de cierre de cada FU/DU
(AGENTS.md §Protocolo de salida).
