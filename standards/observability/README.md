---
type: Reference
title: Estándar de observabilidad — índice
description: Logs, trazas y métricas mínimas de cualquier ADS.
tags: [observabilidad, opentelemetry, logs]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Observabilidad — índice

## Qué se instrumenta
- **Logs estructurados** (JSON): un evento por línea, con id de correlación por solicitud propagado
  entre servicios, nivel (`error`/`warn`/`info`/`debug`) y sin datos sensibles en texto plano.
- **Trazas**: una traza por solicitud de punta a punta, con los saltos entre servicios como spans
  hijos; permite ver dónde se fue el tiempo o dónde falló.
- **Métricas**: latencia (p50/p95/p99), tasa de error y throughput por endpoint crítico, más las
  métricas de negocio que el ADS declare.

## Estándar de instrumentación
OpenTelemetry (categoría: convención abierta de trazas/métricas/logs) como formato común, exportable
a la pila de observabilidad que el stack del ADS elija (`stacks/`). Si el ADS invoca un modelo de
lenguaje, los eventos de token/costo siguen el esquema de `standards/finops/README.md`, alineado a
las convenciones semánticas GenAI de OpenTelemetry (verificar su estado antes de asumirlas estables).

## Alertas
Todo SLO declarado en `standards/backend/standard.md` tiene una alerta asociada cuando se incumple;
una alerta sin acción definida (a quién despierta, qué hacer) no cuenta como cubierta.

## Verificación
`skills/observability-setup/SKILL.md` aplica este estándar al instrumentar un servicio nuevo.
