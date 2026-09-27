---
type: Playbook
title: intent — captura la intención
description: Registra el qué y el por qué de una unidad antes de especificarla o construirla.
args: "[<unidad>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# intent

## Propósito
Fija la intención de una unidad —problema, usuario, resultado esperado, no-objetivos— antes de convertirla en spec o en código, sobre todo en VIBE/IDD.

## Cuándo usarlo
- Al iniciar una FU/DU nueva, especialmente en modo VIBE o IDD.

## Entradas
- Pedido del usuario.
- `templates/intent.md`.

## Pasos
1. [verde] Redacta la intención en `templates/intent.md`: problema, usuario, resultado esperado, no-objetivos.
2. [verde] Distingue explícito, implícito y asumido en cada punto.
3. [amarillo] Si algo asumido es irreversible o caro de deshacer, conviértelo en pregunta bloqueante en vez de asumirlo.
4. [verde] Enlaza la intención a la FU/DU en `implementation/user_units.md`.

## Salidas
- `docs/intent/<unidad>.md` (desde `templates/intent.md`).

## Gates
Toda DU tiene una intención registrada antes de tener spec.

## Fallback
Escribe la intención en una nota de una página con los mismos 4 campos.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate docs/intent` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
"lee y ejecuta este playbook"; sin orden CLI dedicada.
