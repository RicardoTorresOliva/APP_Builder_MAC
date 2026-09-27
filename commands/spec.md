---
type: Playbook
title: spec — especificación verificable
description: Convierte la intención en requirements, design y tasks verificables (formato EARS).
args: "[<unidad>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# spec

## Propósito

Convierte la intención en una especificación verificable: requisitos en formato EARS, decisiones de diseño y tareas trazables, para los módulos en modo SDD/SPDD.

## Cuándo usarlo

- Tras `intent`, antes de `plan` o `start-execution`, en módulos SDD/SPDD.

## Entradas

- `docs/intent/<unidad>.md`.
- `templates/spec/{requirements,design,tasks}.md`.

## Pasos

1. [verde] Redacta `requirements.md` en formato EARS (Given/When/Then) desde `templates/spec/requirements.md`.
2. [verde] Redacta `design.md` con las decisiones técnicas necesarias para cumplir los requisitos.
3. [verde] Redacta `tasks.md` descomponiendo en pasos verificables, atados a FU/DU.
4. [amarillo] Marca cada requisito explícito/implícito/asumido; los asumidos irreversibles van a la cola o al humano.
5. [verde] Enlaza la spec a `implementation/user_units.md` y a `knowledge/index.md`.

## Salidas

- `docs/spec/<unidad>/{requirements,design,tasks}.md`.

## Gates

Todo requisito es trazable a una FU/DU; `drift` puede comparar spec contra código en cualquier momento.

## Fallback

Usa las tres plantillas como checklist en un documento único si no hay carpetas separadas.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate docs/spec/<unidad>` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook"; verifica con `./abm okf validate docs/spec/<unidad>`.
