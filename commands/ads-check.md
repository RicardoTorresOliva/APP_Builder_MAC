---
type: Playbook
title: ads-check — verifica el Contrato ADS
description: Verifica que el ADS cumple su nivel del Contrato ADS, estático y dinámico.
args: ""
tags: [comando, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# ads-check

## Propósito
Verifica que el ADS cumple el nivel del Contrato ADS que fija su perfil, con una prueba estática y una dinámica.

## Cuándo usarlo
- En `connect`.
- Siempre antes de `release`.

## Entradas
- `ads.yaml`.
- `contract/README.md`.

## Pasos
1. [verde] Ejecuta `./abm ads-check` — verifica identidad, capacidades, `AGENTS.md`, skill de operación, `llms.txt`, índice OKF, ledger de tokens y portabilidad (nivel mínimo).
2. [verde] Si el nivel es extendido, verifica además servidor MCP, CLI/API, dashboard de tokens, log de auditoría y HITL en capacidades destructivas.
3. [verde] Ejecuta `./abm agent-conformance` — prueba dinámica: descubrir → listar → leer → dry-run → tokens.
4. [amarillo] Corrige cualquier hallazgo antes de continuar; los de nivel extendido no bajan el nivel declarado en el perfil.
5. [rojo] Un ADS que declara nivel extendido y no lo cumple no se libera — es bloqueante hasta corregir.

## Salidas
- Reporte de `ads-check` y `agent-conformance`.

## Gates
0 errores en ambos comandos antes de `release`.

## Fallback
Recorre `contract/README.md` como checklist manual, nivel por nivel.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm ads-check` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
`./abm ads-check --json`, `./abm agent-conformance --json`.
