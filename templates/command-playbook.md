---
type: Template
title: Plantilla de playbook de comando
description: Esqueleto OKF que sigue todo commands/<name>.md; lo exige `./abm lint playbooks`.
tags: [template, comando]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# Plantilla de playbook de comando

## Propósito
Esqueleto que copian `init-project` y cualquier nuevo comando en `commands/`. Fija el frontmatter
OKF y las nueve secciones que exige `./abm lint playbooks` (ADR 0015).

## Cuándo usarlo
- Al crear un comando nuevo en `commands/`.
- Al revisar que un comando existente conserva el formato.

## Uso
Copia el bloque siguiente a `commands/<name>.md`, sustituye los valores entre `< >` y borra
esta nota. `<name>` es el nombre exacto del comando (ADR 0007); `<fase>` es una de: arranque,
descubrir, construir, asegurar, medir, entregar.

```markdown
---
type: Playbook
title: <name> — <frase corta>
description: <una línea, ≤ 120 caracteres, en español>
args: "<pista de argumentos o vacío>"
tags: [comando, <fase>]
status: stable
generated: { by: claude-code/web, at: <UTC ISO actual> }
---
# <name>

## Propósito
<qué resuelve este comando y por qué existe>

## Cuándo usarlo
- <situación 1>
- <situación 2>

## Entradas
- <archivo o dato que lee>

## Pasos
1. [verde|amarillo|rojo] <paso concreto>
2. [verde|amarillo|rojo] <paso concreto>

## Salidas
- <artefacto producido, con ruta>

## Gates
<qué debe cumplirse para cerrar; qué es bloqueante; qué va a `abm pending add`>

## Fallback
<cómo ejecutarlo sin subagentes/hooks/skills/MCP: pasos secuenciales en lenguaje natural>

## Reporte
\`\`\`text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: <check → resultado>
No verificado: <ítem → motivo>
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
\`\`\`

## Invocación por agentes
<CLI `./abm <orden> --json` y/o MCP `abm_<orden>`; si no hay orden, "lee y ejecuta este playbook">
```

## Reglas del esqueleto
- Cada paso numerado lleva exactamente una etiqueta de semáforo entre corchetes.
- El bloque de `## Reporte` es un único fenced code block de ≤ 12 líneas.
- Las nueve secciones (`Propósito` … `Invocación por agentes`) son obligatorias y en este orden.
- Rutas a archivos que aún no existen van en `código`, nunca en enlace `[texto](ruta)`.
- Sin nombres de producto (regla 7): solo categorías; el stack real vive en `stacks/`/`integrations/`.
