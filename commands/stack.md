---
type: Playbook
title: stack — elige el stack con el humano
description: Explora 2-3 opciones de stack con trade-offs y espera la elección del humano (HITL).
args: "[<categoría>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# stack

## Propósito
Explora el stack técnico y lo elige junto con el humano, nunca por defecto: presenta opciones con trade-offs y respeta la regla 7 (sin lock-in en el núcleo).

## Cuándo usarlo
- En `init-project`.
- Al introducir una pieza nueva del stack durante la construcción.

## Entradas
- `stack_candidates` del perfil activo.
- `stacks/README.md`, `stacks/cases/*.md`.

## Pasos
1. [verde] Parte de las categorías sugeridas por el perfil (`stack_candidates`), nunca de un producto fijo.
2. [verde] Busca opciones bien ajustadas a este ADS en `stacks/cases/*.md`.
3. [verde] Presenta 2–3 opciones con trade-offs: costo, madurez, encaje, portabilidad, y cuándo NO usar cada una.
4. [rojo] Espera la elección del humano — es bloqueante (e), salvo ceremonia prototipo o mvp: aplica la recomendada y encola "confirmar stack".
5. [verde] Registra la elección en `docs/decision_log.md`; nunca nombres un producto que el humano no eligió.

## Salidas
- `docs/decision_log.md` actualizado.
- Stack confirmado, o encolado en prototipo/mvp.

## Gates
Ningún producto aparece en `commands/`, `methodology/`, `standards/` ni `profiles/` (regla 7); el elegido queda documentado en `stacks/`, `integrations/` o `docs/`.

## Fallback
Presenta las opciones en una conversación normal y anota la respuesta en `docs/decision_log.md`.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm lint core` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
`./abm pending add --type scope --json` para encolar en prototipo/mvp; "lee y ejecuta este playbook" para explorar.
