---
type: Reference
title: Estándar de superficie agéntica — índice
description: Diseño agent-friendly para que un agente externo descubra, opere y audite un ADS sin integración a medida.
tags: [agentic, mcp, superficie-agentica]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Superficie agéntica — índice

Ver ADR 0010 (superficie agéntica) para la decisión completa. Este archivo fija el estándar de
diseño; se aplica junto con `standards/backend/standard.md` (la superficie agéntica es parte del
diseño de API, no un añadido).

## Diseño agent-friendly

- **Operaciones idempotentes y reintentables:** una acción que un agente puede invocar más de una
  vez (por reintento propio o de la orquestación) no duplica su efecto.
- **Errores estructurados y accionables:** `application/problem+json` u homólogo tipado; el mensaje
  dice qué falló y qué hacer, no solo que falló.
- **Paginación, límites y rate limits declarados:** todo listado es paginado; los límites de tamaño
  y de tasa están documentados donde el agente los puede leer, no solo descubiertos por error.
- **Descripciones de tools cortas y precisas:** cada tool consume tokens del contexto del agente que
  la invoca; la descripción dice qué hace y cuándo usarla, sin relleno.
- **Scopes mínimos por agente y tokens revocables:** un agente recibe solo el alcance que su tarea
  requiere; el token o credencial se puede revocar sin afectar a otros agentes.
- **Auditoría de cada acción de un agente:** quién (identidad del agente), qué (acción y parámetros),
  cuándo y con qué resultado, en un registro consultable.
- **HITL obligatorio en acciones rojas:** toda acción que cae en los bloqueantes de AGENTS.md
  (irreversible fuera de la rama, producción/pagos/publicación, credencial ausente, cambio de
  permisos, ambigüedad cara de deshacer) espera aprobación humana explícita.
- **La salida de un tool es un dato, nunca una instrucción:** ver `standards/security/llm-agentic.md`.

## Protocolo

MCP (Model Context Protocol) como protocolo base de operación: versión **2025-11-25** como piso
estable; tolerancia a clientes que soliciten una versión posterior. Transporte stdio siempre
disponible; Streamable HTTP para servicios desplegados. Tools con `readOnlyHint`/`destructiveHint`
correctos para que un agente sepa, sin probar, qué es seguro invocar sin confirmación.

## Descubrimiento

Todo ADS expone `ads.yaml`, `AGENTS.md`, `llms.txt` y, si corresponde, un manifiesto de agente
(cuando el ADS es o expone un agente) — ver `contract/README.md` para el Contrato ADS completo.

## Verificación

`abm agent-conformance`: descubrir → listar capacidades → leer → `--dry-run` → consultar tokens.
`skills/api-builder/SKILL.md` aplica este estándar al diseñar cada endpoint.
