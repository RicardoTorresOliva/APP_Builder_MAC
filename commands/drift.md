---
type: Playbook
title: drift — deriva intención/spec/código
description: Detecta y resuelve la deriva entre intención, spec, contrato de prompt y código real.
args: "[<unidad>]"
tags: [comando, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# drift

## Propósito

Detecta deriva entre intención, spec, contrato de prompt y el código real de la unidad, y decide de forma explícita cómo resolverla.

## Cuándo usarlo

- Periódicamente durante `start-execution`.
- Siempre antes de `closeout`.

## Entradas

- `docs/intent/`, `docs/spec/`, `docs/prompt-contracts/`.
- Código de la unidad.

## Pasos

1. [verde] Compara la spec (`requirements.md`) contra el comportamiento real de la unidad.
2. [verde] Compara el contrato de prompt, si existe, contra el comportamiento del agente o flujo con IA.
3. [amarillo] Si hay deriva, decide: actualizar la spec (el código tenía razón) o corregir el código (la spec tenía razón); documenta cuál y por qué.
4. [verde] Registra la deriva y su resolución en `docs/work_log.md`.
5. [rojo] Deriva en una unidad que toca pagos, autenticación o datos personales exige revisión humana antes de resolver.

## Salidas

- Entrada de deriva en `docs/work_log.md`.
- Spec o código actualizados.

## Gates

Ninguna unidad cierra con deriva sin resolver o sin justificar por qué se acepta.

## Fallback

Compara a mano spec contra código, unidad por unidad, usando la lista de requisitos como checklist.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `docs/work_log.md` → sección Deriva → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook"; sin orden CLI dedicada.
