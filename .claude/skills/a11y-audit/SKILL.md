---
name: a11y-audit
description: Audita una interfaz existente contra el checklist WCAG 2.2 AA de standards/a11y/README.md — contraste, teclado, foco, nombres accesibles, zoom. Úsala antes de un release de UI o cuando se reporta un problema de accesibilidad.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# a11y-audit

## Pasos
1. Lee `standards/a11y/README.md` y recorre su checklist ítem por ítem sobre la(s) pantalla(s) en
   alcance.
2. Navega la ruta crítica 100 % por teclado: verifica orden de tabulación, foco visible y ausencia
   de trampas de foco.
3. Verifica contraste de texto y de controles interactivos con una herramienta de medición, no a
   ojo.
4. Verifica que cada control tenga nombre accesible real (label asociado), no solo un placeholder.
5. Prueba con al menos un lector de pantalla la ruta crítica; confirma que el contenido dinámico
   (toasts, modales, mensajes de error) se anuncia sin robar el foco de forma inesperada.
6. Verifica la interfaz a 200 % de zoom: sin pérdida de contenido ni de funcionalidad.
7. Para cada ítem que falla, registra severidad usando `standards/frontend/review-criteria.md`
   (bloqueante si rompe la ruta crítica o el contraste AA; mayor/menor según impacto).
8. Si el hallazgo bloquea, se detiene el release de esa pantalla hasta mitigarlo; si es menor, va a
   `abm pending add`.

## Criterios de salida
- Checklist de `standards/a11y/README.md` completo, con evidencia por ítem (captura, grabación o
  resultado de herramienta).
- Cero hallazgos bloqueantes sin mitigar.
- Resultado incorporado a `standards/frontend/checklist-dod.md` de la unidad auditada.
- Reporte final según `standards/communication.md` (≤ 12 líneas).
