---
name: frontend-builder
description: Construye o modifica una interfaz de usuario (componentes, páginas, formularios) aplicando el estándar de frontend de ABM — design system y tokens, accesibilidad WCAG 2.2 AA, responsive, Core Web Vitals, i18n/SEO y estados vacíos/error. Úsala en cualquier FU/DU de UI, antes de dar por hecho un componente o pantalla.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# frontend-builder

## Pasos
1. Lee `standards/frontend/standard.md` (rango relevante a la tarea) antes de escribir código.
2. Revisa si el componente ya existe en el design system del ADS; compón antes de crear uno nuevo.
3. Define los tokens de diseño a usar (color, tipografía, espaciado); nunca hardcodees un valor de
   estilo fuera de ellos.
4. Implementa los cuatro estados de toda vista con datos: carga, vacío, error, contenido — antes de
   considerar el componente terminado.
5. Verifica accesibilidad contra `standards/a11y/README.md`: teclado, foco visible, contraste,
   nombre accesible en cada control.
6. Verifica responsive mobile-first (viewport más chico primero) y que no haya scroll horizontal.
7. Mide o estima Core Web Vitals de la ruta afectada contra los umbrales de
   `standards/frontend/standard.md` (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, p75).
8. Si hay formulario: valida en cliente y en servidor, mensajes asociados al campo, el valor
   ingresado no se pierde ante un error.
9. Externaliza todo texto (i18n); si la página es indexable, agrega metadatos únicos y encabezados
   jerárquicos.
10. Escribe o actualiza tests según `standards/frontend/testing.md` (unitario, componente, E2E si
    toca ruta crítica).
11. Corre `standards/frontend/checklist-dod.md` completo antes de reportar la unidad como hecha.

## Criterios de salida
- Todas las casillas de `standards/frontend/checklist-dod.md` marcadas o justificadas como
  `no-verificado` en el reporte.
- Tests de `standards/frontend/testing.md` en verde.
- Si la acción también es agéntica, el contrato coincide con `standards/backend/standard.md`.
- Reporte final según `standards/communication.md` (≤ 12 líneas).
