---
type: Standard
title: Transversales — entornos, CI/CD, feature flags y costo
description: Lo que aplica a todo ADS sin importar la capa: entornos, integración continua, flags y costo.
tags: [cross-cutting, ci-cd, entornos, feature-flags]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Transversales

## Entornos

- **dev:** datos de ejemplo, sin secretos reales, cambios rápidos; el agente opera libre dentro del
  modo turbo.
- **staging:** espejo de producción en configuración; datos sintéticos o anonimizados, nunca datos
  personales reales sin anonimizar; es donde se prueba la migración y la carga antes de producción.
- **prod:** credenciales de producción nunca al alcance del agente (AGENTS.md regla 2); todo cambio
  llega por el mismo pipeline de CI/CD que staging, sin pasos manuales que staging no tuvo.

## CI/CD

- Pipeline único por ambiente creciente (dev → staging → prod), sin bifurcaciones manuales.
- Gate de CI por unidad: OKF válido, lint de núcleo sin hallazgos, presupuesto de tokens dentro de
  rango, tests de los tres niveles en verde, secret scanning limpio.
- Un cambio que no pasa el gate no avanza de ambiente, sin excepción manual silenciosa.

## Feature flags

- Toda funcionalidad riesgosa o incompleta se lanza detrás de un flag, no detrás de una rama de larga
  vida.
- Un flag tiene dueño y fecha de retiro; un flag "permanente" sin revisión es deuda técnica y va a la
  cola de pendientes.

## Costo

- Costo de infraestructura y costo de tokens (`standards/finops/README.md`) se miden por ambiente;
  staging y prod no comparten presupuesto sin distinguirlo.
- Un pico de costo inesperado en cualquier ambiente entra a la cola de pendientes si es blando, o es
  bloqueante si supera el tope duro (AGENTS.md §Bloqueantes, ítem f).

## Verificación

El perfil activo fija cuáles de estos controles son obligatorios según su ceremonia
(`abm.yaml → ceremony`); `standards/backend/checklist-dod.md` y `standards/database/checklist-dod.md`
referencian este archivo para lo que les aplica.
