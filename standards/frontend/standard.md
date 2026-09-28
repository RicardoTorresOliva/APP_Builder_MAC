---
type: Standard
title: Estándar de frontend
description: Qué construye y cómo cualquier interfaz de usuario producida por ABM.
tags: [frontend, estandares, ui]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Estándar de frontend

## Design system y tokens

- Tokens de diseño (color, tipografía, espaciado, radios, sombras, breakpoints) como fuente única;
  ningún valor de estilo se hardcodea fuera de los tokens.
- Librería de componentes propia del ADS: cada componente documenta variantes, props, y estados
  (default, hover/focus, disabled, loading, error).
- Un componente nuevo se justifica frente a componer los existentes.

## Accesibilidad

- WCAG 2.2 AA como piso; ver `standards/a11y/README.md` para el checklist completo.
- Todo control interactivo tiene nombre accesible, rol correcto y es operable por teclado.

## Responsive y mobile-first

- El layout se diseña primero para el viewport más chico y escala hacia arriba.
- Objetivos táctiles ≥ 24×24px CSS; sin scroll horizontal no intencional.

## Rendimiento (Core Web Vitals, percentil 75)

| Métrica | Umbral "bueno" |
|---|---|
| LCP (Largest Contentful Paint) | ≤ 2.5 s |
| INP (Interaction to Next Paint) | ≤ 200 ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 |

Medido en la(s) ruta(s) crítica(s) de negocio, no solo en el home. Presupuesto de peso de JS/CSS
inicial declarado por el ADS.

## Estado, formularios y validación

- Estado de servidor y estado de UI se manejan por separado; sin duplicar fuente de verdad.
- Validación en cliente (feedback inmediato) y en servidor (autoridad); ambas usan los mismos
  mensajes de error, asociados a su campo (`aria-describedby` o equivalente).
- Formularios preservan el valor ingresado ante un error; nunca limpian el campo.

## i18n y SEO

- Textos externalizados (sin concatenar cadenas traducidas); fechas, números y monedas se formatean
  según la configuración regional del usuario.
- Metadatos por página (title, description) únicos; encabezados jerárquicos (un solo `h1`); URLs
  legibles; datos estructurados cuando la página lo amerita (contenido indexable).

## Estados vacíos y de error

- Toda vista con datos declara su estado vacío (primer uso, sin resultados de filtro) y su estado
  de error (falla de red, falla del servidor), cada uno con una acción de salida clara.
- Estado de carga visible a partir de ~300 ms para evitar parpadeo en respuestas rápidas.

## Superficie agéntica

Si la UI expone acciones que un agente externo también puede invocar, esas acciones se diseñan
junto con la API (`standards/backend/standard.md` → superficie agéntica) para que el mismo caso de
uso tenga una vía humana y una vía programática coherentes.

## Tests

Ver `standards/frontend/testing.md`: unitarios (lógica), de componente (render, interacción y
accesibilidad) y E2E (ruta crítica).
