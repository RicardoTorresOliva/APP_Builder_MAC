---
type: Reference
title: Severidad de hallazgos en revisión independiente
description: Taxonomía de severidad, ejemplos de hallazgo bien y mal formulado, y la plantilla de reporte de una revisión.
tags: [referencia, revision, calidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Severidad de hallazgos

| Severidad | Criterio | Acción |
|---|---|---|
| Bloqueante | Corresponde a una causa a–f de `AGENTS.md`, o el DU no cumple `deliverable_unit_completeness` del perfil | Se detiene la entrega; se informa en ≤ 3 líneas con la opción recomendada |
| Mayor | Compromete seguridad, expone datos, o rompe un contrato que otro módulo/ADS ya consume | Vuelve a quien construyó antes de cerrar el milestone |
| Menor | Mejora legítima, deuda técnica o estilo que no afecta la entrega actual | Va a la cola de pendientes con su default |

## Hallazgo bien formulado
```
[mayor] api/checkout.py:142 — el endpoint devuelve el stack trace completo en el cuerpo del
error 500, incluida la cadena de conexión a la base de datos. Viola standards/security/
(no exponer detalles internos en errores). Reproducible: POST /checkout con body inválido.
```

## Hallazgo mal formulado (evitar)
```
El manejo de errores del checkout parece un poco frágil, convendría revisarlo.
```
Sin archivo:línea, sin severidad, sin cómo reproducirlo — no es accionable ni verificable por
quien lo reciba.

## "Sin hallazgos" bien formulado
```
Sin hallazgos bloqueantes ni mayores. Revisado: api/checkout.py, standards/security/,
standards/testing/. Verificado con `./abm check` (OK) y ejecutando los 4 casos de
deliverable_unit_completeness del perfil software-app — los 4 pasan con evidencia en
docs/work_log.md#2026-09-28.
```
Nombra qué se revisó, con qué se verificó y dónde queda la evidencia — no es un "parece bien"
vacío, aunque la conclusión sea la misma (no hay problemas).

## Plantilla de reporte de la revisión
Usa el mismo formato de cierre de `AGENTS.md` (protocolo de salida); en `Acciones` lista cada
hallazgo con su `archivo:línea` y severidad, uno por línea, en vez de una sola línea genérica de
"revisión completada".
