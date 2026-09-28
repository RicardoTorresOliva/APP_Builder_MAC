---
type: Playbook
title: pending — cola de pendientes
description: Lista, agrega y resuelve en lote las decisiones y defaults que turbo dejó en cola.
args: "list | add | resolve <id...>"
tags: [comando, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# pending

## Propósito

Administra la cola de pendientes de turbo (ADR 0014): lo reversible avanza con un default aplicado, y el humano responde en lote en vez de por interrupciones.

## Cuándo usarlo

- Al cerrar una unidad, al iniciar sesión, o cuando el humano quiere revisar decisiones acumuladas.

## Entradas

- `docs/_work/PENDIENTES.md`

## Pasos

1. [verde] Lista la cola agrupada por tipo: `./abm pending list`.
2. [verde] Por cada default aplicado en turbo, agrégalo: `./abm pending add --type <tipo> --context <ctx> --default <d> --alternative <a> --impact <i>`.
3. [amarillo] Presenta la cola al humano para respuesta en lote — una pasada, no una interrupción por ítem.
4. [verde] Aplica las respuestas: `./abm pending resolve <ids> --answer <texto>`.
5. [rojo] Si un pendiente resulta ser en realidad un bloqueante (a–f de AGENTS.md) mal clasificado, escálalo de inmediato — no lo dejes en cola.

## Salidas

- `docs/_work/PENDIENTES.md` actualizado.

## Gates

Ningún pendiente de tipo credencial o que sea en realidad bloqueante queda abierto al cerrar una unidad.

## Fallback

Edita `docs/_work/PENDIENTES.md` a mano: una fila por ítem (ID, tipo, contexto, default, alternativa, impacto, estado).

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm pending list` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm pending list --json`, `./abm pending add --json ...`, `./abm pending resolve <id> --json`.
