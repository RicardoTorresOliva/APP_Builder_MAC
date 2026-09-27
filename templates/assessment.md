---
type: Template
title: assessment.md — inventario brownfield
description: Inventario que produce assess antes de intervenir un sistema existente.
tags: [template, assess, brownfield]
status: draft
generated: { by: human:tu-id, at: 2026-01-01T00:00:00Z }
---

# Assessment brownfield: `<sistema>`

Dimensión brownfield del router (`/methodology/router.md`): `<0 greenfield | 1 parcial | 2 estricto>`

## Lenguajes y frameworks

| Capa | Lenguaje/framework | Versión | Notas |
|---|---|---|---|
| Backend | `<...>` | `<...>` | `<...>` |
| Frontend | `<...>` | `<...>` | `<...>` |

## Base de datos y middleware

- BD: `<motor, versión>` — `<multi-tenant? migraciones versionadas?>`
- Middleware/colas/caché: `<...>`

## Identidad

- Proveedor de identidad (IdP): `<interno | delegado, cuál>`
- Modelo de auth actual: `<...>`

## CI/CD y nube

- Pipeline: `<...>`
- Proveedor de nube o on-prem: `<...>`
- Entornos: `<dev/staging/prod, cómo se promueve>`

## Políticas y restricciones

- Restricciones de red: `<qué está bloqueado, qué requiere excepción>`
- Políticas de datos/seguridad que aplican: `<...>`
- Stack corporativo fijo (no negociable): `<...>`

## Integraciones existentes

| Sistema | Tipo de integración | Riesgo si se rompe |
|---|---|---|
| `<...>` | `<API\|archivo\|evento\|BD compartida>` | `<...>` |

## Patrones propuestos

`<qué patrón de integración se propone para no romper lo existente, y por qué>`

## Clasificación resultante

`<módulo(s) afectados y su modo, con /docs/adr/0006-router-metodologico.md y methodology-map.md>`
