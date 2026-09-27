---
type: Playbook
title: help — índice de comandos
description: Muestra el catálogo de comandos por fase y resuelve alias en español.
args: "[<tema o alias>]"
tags: [comando, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# help

## Propósito
Orienta a quien no sabe qué comando usar: catálogo por fase y alias en español para no memorizar nombres en inglés.

## Cuándo usarlo
- No sabes qué comando corresponde a lo que quieres hacer.
- Quieres ver el catálogo completo agrupado por fase.

## Entradas
- Ninguna, u opcionalmente una palabra o alias en español.

## Pasos
1. [verde] Muestra el catálogo agrupado por fase: arranque, descubrir, construir, asegurar, medir, entregar.
2. [verde] Resuelve alias en español: pendientes→pending, diagnostico→doctor, iniciar→init-project, ejecutar→start-execution, revisar→review, iterar→iterate, corregir→fix, refactorizar→refactor, desplegar→deploy, publicar→release, cerrar→closeout, seguridad→security, pruebas→test, conectar→connect, decidir→decide, integrar→integrate, explorar→explore, evaluar→assess, pila→stack.
3. [verde] Si la persona describe una necesidad en vez de nombrar un comando, sugiere el que mejor encaja.
4. [verde] Apunta a `docs/manual/` para la explicación paso a paso de cada comando.

## Salidas
- Ninguno (comando de lectura).

## Gates
Ninguno.

## Fallback
Lee la tabla "Comandos" en `AGENTS.md` y el índice de `docs/manual/`.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: AGENTS.md → sección Comandos → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
"lee y ejecuta este playbook"; el índice vive en el manual, sin orden CLI dedicada.
