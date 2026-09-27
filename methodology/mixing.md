---
type: Methodology
title: Mezcla de metodologías por módulo
description: Cómo un mismo ADS combina VIBE, IDD, SDD, SPDD y AIDD por módulo, con reglas y un ejemplo.
tags: [metodologia, mezcla, methodology-map]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Mezcla por módulo

Un ADS no tiene un solo modo metodológico: cada módulo se clasifica por separado con
`/methodology/router.md` y el resultado se fija en `methodology-map.md`
(`/templates/methodology-map.md`), con modo, justificación, nivel de revisión y disparadores que
podrían reclasificarlo.

## Reglas de escalamiento

Si el módulo toca pagos, autenticación, datos personales, salud o cae bajo regulación → escala a `SDD`
con revisión humana obligatoria, sin importar qué digan las dimensiones (`router.yaml → triggers.escalate`).
El escalamiento se revisa en cada `closeout`: si un módulo `IDD` empieza a tocar uno de estos dominios,
reclasifica antes de seguir.

## Reglas de desescalamiento

- Prototipo desechable, sin continuidad prevista → `VIBE`.
- Landing o contenido informativo/estático → `IDD` (no necesita EARS ni trazabilidad formal).
- Herramienta interna de bajo riesgo (uso del propio equipo, sin datos sensibles) → `IDD`.

El desescalamiento nunca se aplica si hay un disparador de escalamiento activo: el escalamiento gana
siempre (`/methodology/router.md → algoritmo de clasificación`).

## Ejemplo: mini-ERP

| Módulo | Modo | Justificación | Revisión | Disparadores |
|---|---|---|---|---|
| Inventario | IDD | Reglas de negocio claras, riesgo bajo si hay un error puntual, iteración frecuente | Recomendada | Ninguno activo |
| Ventas | IDD | Flujo conocido, incertidumbre media en la UX, sin manejo directo de dinero | Recomendada | Si integra cobro directo, escala a SDD |
| Facturación | SDD | Genera documentos fiscales y montos: disparador `payments`/`regulated` | Humana obligatoria | `payments`, `regulated` |
| Roles y autenticación | SDD | Control de acceso: disparador `auth` | Humana obligatoria | `auth` |
| Reportes | IDD | Solo lectura, sin riesgo de escritura ni datos sensibles nuevos | Recomendada | Ninguno activo |

Este es el contenido que produciría `abm methodology classify` para cada módulo del mini-ERP, y es la
forma esperada de `methodology-map.md` para cualquier ADS con módulos de riesgo mixto.

## Ver también

`/methodology/router.md` · `/methodology/router.yaml` · `/templates/methodology-map.md` ·
`/methodology/ceremony.md`
