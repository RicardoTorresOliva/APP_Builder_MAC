---
type: Reference
title: Ejemplo completo de documento OKF v0.2 + perfil ABM
description: Un documento ficticio con sources, notas al pie, stale_after y verified resueltos de punta a punta, para copiar la forma.
tags: [referencia, okf, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Ejemplo completo

Un `Stack Sheet` real (exige `stale_after` por tipo) con todo resuelto:

```markdown
---
type: Stack Sheet
title: "Stack: automatización low-cost"
description: Combinación de categorías para una automatización de bajo costo con HITL.
tags: [stack, low-cost, automatizacion]
status: stable
stale_after: 2026-12-27T00:00:00Z
sources:
  - { id: precios-cola, resource: "https://ejemplo.invalid/pricing", title: "Precios del proveedor de colas" }
  - { id: benchmark-2026, resource: "https://ejemplo.invalid/bench", title: "Benchmark de proveedores 2026" }
generated: { by: claude-code/web, at: 2026-09-27T18:00:00Z }
verified: { by: human:ricardo, at: 2026-09-27T19:10:00Z }
---

# Stack: automatización low-cost

El costo mensual del proveedor de colas evaluado es de USD 9 en el plan de entrada[^precios-cola].
Frente a las tres alternativas del benchmark, esta combinación tuvo el menor costo total de
propiedad a 12 meses[^benchmark-2026].

[^precios-cola]: Precios del proveedor de colas
[^benchmark-2026]: Benchmark de proveedores 2026
```

## Qué valida `abm okf validate` en este ejemplo
- `type`, `title`, `description`, `status`, `generated` presentes → pasa `abm.required`.
- `stale_after` presente porque `Stack Sheet` está en `okf.stale_required_types` → pasa
  `abm.stale_after`.
- `generated.by: claude-code/web` matchea `[^\s:/]+/[^\s]+` → pasa `okf.actor`.
- `verified.by: human:ricardo` matchea `human:[^\s]+` → pasa `okf.actor`.
- Cada `[^id]` referenciado en el cuerpo (`precios-cola`, `benchmark-2026`) tiene su definición al
  final y coincide con un `id` de `sources` → pasa `abm.footnote` (error y warning).
- `stale_after` es ISO 8601 con zona y aún no venció (a la fecha de este ejemplo) → sin
  `abm.stale`.

## Errores comunes que esto evita
- Olvidar `stale_after` en un tipo que lo exige → `abm.stale_after`.
- Citar `[^id]` sin definirlo al final → `abm.footnote` (error).
- Definir un `id` en `sources` y no citarlo, o citar un `id` que no está en `sources` →
  `abm.footnote` (warning, no bloquea).
- Usar `timestamp` en vez de `generated.at` (herencia v0.1) → `abm.legacy`.
