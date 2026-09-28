---
type: Playbook
title: assess — inventario de brownfield/legacy
description: Inventaría un stack existente y propone el patrón de integración más simple que funcione.
args: "[<sistema a evaluar>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# assess

## Propósito

Inventaría, antes de intervenir, el stack corporativo ya en producción con el que el ADS convivirá o al que reemplaza, y propone el patrón de integración de menor riesgo.

## Cuándo usarlo

- El ADS se integra con, o reemplaza, sistemas ya en producción (brownfield/legacy).

## Entradas

- Acceso de solo lectura al sistema existente (código, infraestructura, documentación).
- `stacks/legacy.md`.

## Pasos

1. [verde] Inventaría lenguajes, frameworks, bases de datos, middleware, IdP, CI/CD, nube y restricciones de red; regístralo en OKF con `templates/assessment.md`.
2. [verde] Identifica SSO corporativo (SAML/OIDC), proxies, redes privadas y políticas de acceso.
3. [amarillo] Propón el patrón de integración desde `stacks/legacy.md` (strangler fig, anti-corruption layer, fachada API, CDC/eventos, batch/SFTP/EDI; RPA solo como último recurso) y justifica por qué no uno más simple.
4. [verde] Documenta restricciones que limitan el stack nuevo (versión mínima, protocolo obligatorio, ventana de mantenimiento).
5. [rojo] Si el diagnóstico exige credenciales de producción o acceso de escritura, detente: es bloqueante (c/d).

## Salidas

- `docs/assessment.md` (o la ruta del ADS), consumido por `stack` y `planning/risks.md`.

## Gates

Ningún patrón elegido sin justificar por qué se descartaron los más simples; RPA solo tras descartar el resto.

## Fallback

Entrevista a los dueños del sistema existente y completa `templates/assessment.md` a mano.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate docs/assessment.md` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

Sin orden CLI dedicada aún — "lee y ejecuta este playbook"; registra tokens con `./abm tokens estimate --unit assess <archivos>`.
