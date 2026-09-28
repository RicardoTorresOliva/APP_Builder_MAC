---
type: Playbook
title: tokens — espacio de control de tokens
description: Registra, reporta y verifica el consumo y presupuesto de tokens de cada unidad.
args: "record | estimate | report | dashboard | budget | attest"
tags: [comando, medir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# tokens

## Propósito

Gestiona el espacio de control de tokens: ledger, reporte, dashboard y presupuestos, para saber qué cuesta construir y operar el ADS.

## Cuándo usarlo

- Al cerrar cada unidad, para registrar su consumo.
- Al revisar el costo del proyecto o del ADS en operación.

## Entradas

- `ads.yaml → tokens.ledger`.
- `integrations/observability/pricing.yaml`.

## Pasos

1. [verde] Registra el consumo de cada unidad: medido con `./abm tokens record` si hay telemetría, o estimado con `./abm tokens estimate --unit <id> <archivos>` (≈ caracteres/4).
2. [verde] Genera el reporte N1: `./abm tokens report`.
3. [amarillo] Si el perfil exige N2 (MVP o producto), genera el dashboard estático: `./abm tokens dashboard`.
4. [verde] Verifica presupuestos: `./abm tokens budget` — el umbral blando entra en la cola; el tope duro es bloqueante (f).
5. [rojo] El tope duro superado detiene la unidad hasta que el humano decida: ampliar presupuesto o recortar alcance.
6. [verde] Para cifras oficiales de costo, usa `./abm tokens attest`.

## Salidas

- Entradas en el ledger JSONL.
- `TOKENS.md` (N1).
- Dashboard HTML (N2, si aplica).

## Gates

Toda unidad registra su consumo antes de `closeout`; ningún tope duro queda superado sin resolución.

## Fallback

Sin CLI, estima a mano (caracteres del contenido producido / 4) y anótalo en `docs/work_log.md` como `estimado`.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm tokens budget` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm tokens record|estimate|report|dashboard|budget|attest --json`; recurso MCP `abm://tokens/summary`.
