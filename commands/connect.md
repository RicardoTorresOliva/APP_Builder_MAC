---
type: Playbook
title: connect — superficie agéntica del ADS
description: Da al ADS su superficie agéntica (ads.yaml, skill, MCP, API) para que otro agente lo opere.
args: ""
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# connect

## Propósito

Da al ADS la superficie agéntica completa que exige su nivel del Contrato ADS, para que otro agente lo descubra y opere sin integración a medida.

## Cuándo usarlo

- Al cerrar la primera DU operativa del ADS.
- Cada vez que su superficie agéntica cambia.

## Entradas

- `ads.yaml`, `AGENTS.md` del ADS.
- `templates/agentic/` (manifiesto, skill, servidor MCP, `llms.txt`).

## Pasos

1. [verde] Confirma que existen `ads.yaml`, `AGENTS.md`, `llms.txt` e índice OKF (mínimo del Contrato ADS).
2. [verde] Genera o actualiza la skill `operate-<id>` desde `templates/agentic/` para que un agente externo sepa operar el ADS.
3. [amarillo] Si el nivel es extendido: añade servidor MCP (stdio; Streamable HTTP si está desplegado), CLI `--json`/`--dry-run`, y OpenAPI si expone HTTP; errores en formato `problem+json`.
4. [verde] Revisa que las tools tengan descripciones cortas, indicadores de solo-lectura/destructivo correctos y HITL en las destructivas.
5. [rojo] Ninguna acción destructiva o de producción queda ejecutable por un agente externo sin confirmación explícita.
6. [verde] Verifica con `./abm ads-check` y `./abm agent-conformance` (descubrir → listar → leer → dry-run → tokens).

## Salidas

- `ads.yaml`, skill `operate-<id>`, servidor MCP o API según nivel, `llms.txt`.

## Gates

`./abm ads-check` y `./abm agent-conformance` sin errores antes de cerrar.

## Fallback

Arma el manifiesto y la skill a mano copiando `templates/agentic/`; documenta en `integrations/agents/hermes.md` cómo un gateway de mensajería lo operaría.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm ads-check` y `./abm agent-conformance` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm ads-check --json`, `./abm agent-conformance --json`.
