---
type: Reference
title: Criterios de revisión — frontend
description: Qué mira el revisor independiente de UI y con qué severidad.
tags: [frontend, revision, severidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Criterios de revisión — frontend

El revisor usa un contexto limpio (nunca quien construyó, AGENTS.md §Unidades de trabajo).

## Bloqueante
- Ruta crítica inoperable por teclado, o con trampa de foco.
- Contraste por debajo del umbral AA en texto o control crítico.
- CWV muy por debajo del umbral en la ruta crítica (p. ej. LCP > 4 s).
- Dato sensible visible en el DOM, en la URL o en un log de cliente.
- Formulario que pierde el valor ingresado o no valida en servidor.

## Mayor
- Falta el estado vacío o el estado de error de una vista con datos.
- Texto hardcodeado sin pasar por i18n.
- Componente nuevo que duplica uno existente del design system sin justificación.
- Test E2E de la ruta crítica ausente o en rojo.

## Menor
- Inconsistencia visual respecto a los tokens del design system sin impacto funcional.
- Nombre de test poco descriptivo.
- Metadato SEO ausente en una página no crítica para indexación.

## Evidencia esperada
Captura o grabación del estado antes/después, resultado de Lighthouse o equivalente para CWV, y
salida de los tests (unitarios, componente, E2E) referenciados por archivo.
