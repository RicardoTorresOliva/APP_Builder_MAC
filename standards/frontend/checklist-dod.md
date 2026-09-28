---
type: Checklist
title: Definition of Done — frontend
description: Casillas verificables para cerrar una FU/DU de interfaz de usuario.
tags: [frontend, dod, checklist]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# DoD — frontend

- [ ] Usa tokens del design system; cero valores de estilo hardcodeados fuera de ellos.
- [ ] Todo control interactivo es accesible por teclado y tiene nombre/rol accesible.
- [ ] Contraste de texto normal ≥ 4.5:1 y de texto grande ≥ 3:1, verificado.
- [ ] Sin trampas de foco; el orden de tabulación sigue el orden visual.
- [ ] Responsive verificado en mobile, tablet y desktop; sin scroll horizontal no intencional.
- [ ] LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (p75) en la ruta crítica medida.
- [ ] Formulario valida en cliente y en servidor; errores asociados a su campo; el valor ingresado
      no se pierde ante un error.
- [ ] Estado vacío, de carga y de error definidos para toda vista con datos.
- [ ] Textos externalizados (i18n); fechas/números/monedas localizados.
- [ ] `title`/`meta description` únicos y encabezados jerárquicos (un solo `h1`) en páginas indexables.
- [ ] Tests unitarios de la lógica, tests de componente de la interacción y E2E de la ruta crítica
      en verde.
- [ ] Sin errores ni warnings de consola en el flujo normal.
- [ ] Si la acción también es agéntica, el contrato de datos coincide con el de la API
      (`standards/backend/checklist-dod.md`).
