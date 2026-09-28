---
type: Project Brief
title: Encargo — panel de ventas
description: Encargo original del ADS panel-ventas tal como lo escribió la persona, antes de init-project.
tags: [encargo, ejemplo, software-app]
status: stable
generated: { by: human:encargo-simulado, at: 2026-09-27T23:50:00Z }
---

# Encargo

> Quiero un panel web para ver las ventas de mi equipo. Cada vendedor entra con usuario y contraseña y
> registra sus ventas; yo, como administradora, veo todo y puedo corregir errores. Necesito gráficos de
> ventas por mes y por vendedor, y una tabla con el detalle. Tiene que correr en mi computador sin
> instalar nada. Me gustaría que un asistente de IA pueda consultar el resumen o cargar ventas por mí.

## Lectura de ABM (init-project, paso 2)

| Campo | Valor |
|---|---|
| Perfil | `software-app` (interfaz que una persona usa) — nivel de Contrato ADS `extendido` |
| Ceremonia | `producto` (valor de `abm.yaml`; datos de negocio y auth con horizonte más allá de un prototipo) |
| Módulos | `auth` (login y roles), `ventas` (registro), `dashboard` (gráficos) |
| Restricción explícita | "sin instalar nada" → sin dependencias externas ni servicios |
| Consumidores | personas (web) y agentes (MCP y CLI) |

Siguiente artefacto: [requisitos](planning/requirements.md) y [mapa metodológico](planning/methodology-map.md).
