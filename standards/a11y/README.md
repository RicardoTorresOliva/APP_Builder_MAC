---
type: Reference
title: Estándar de accesibilidad — índice
description: Checklist WCAG 2.2 AA aplicable a cualquier interfaz con usuario humano.
tags: [a11y, wcag, accesibilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Accesibilidad — índice

Piso mínimo: **WCAG 2.2 nivel AA**, en toda interfaz con usuario humano (web, dashboard, app móvil
con framework de componentes).

## Checklist

- [ ] Contraste de texto normal ≥ 4.5:1; texto grande (≥ 18pt o 14pt negrita) ≥ 3:1.
- [ ] Todo control interactivo es operable por teclado, sin trampas de foco; orden de tabulación
      sigue el orden visual.
- [ ] Foco visible en todo elemento que lo recibe.
- [ ] Toda imagen informativa tiene alternativa textual; la decorativa se marca como tal.
- [ ] Todo control tiene nombre accesible (label asociado, no solo placeholder).
- [ ] Estructura semántica: encabezados jerárquicos, landmarks (nav, main, etc.), listas como listas.
- [ ] Mensajes de error de formulario asociados a su campo y anunciados a tecnología asistiva.
- [ ] Objetivos táctiles ≥ 24×24px CSS, con espacio suficiente entre controles adyacentes.
- [ ] Nada de contenido parpadeante que pueda inducir convulsiones; animación pausable.
- [ ] El contenido dinámico (toasts, modales) es anunciado sin robar el foco de forma inesperada.
- [ ] La interfaz funciona a 200 % de zoom sin pérdida de contenido o funcionalidad.
- [ ] Verificado con al menos un lector de pantalla y navegación 100 % por teclado en la ruta crítica.

## Verificación

`skills/a11y-audit/SKILL.md` recorre este checklist; el resultado (ítem → pasa/falla → evidencia) va
en `standards/frontend/checklist-dod.md` de la unidad auditada.
