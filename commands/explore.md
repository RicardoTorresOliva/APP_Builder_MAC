---
type: Playbook
title: explore — spike acotado en sandbox
description: Prueba y descarta en una rama sandbox con tiempo acotado para resolver una incertidumbre.
args: "[<pregunta>] [--tiempo <minutos>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# explore

## Propósito
Reduce incertidumbre alta con un spike en modo VIBE, acotado en tiempo y aislado en una rama sandbox, antes de comprometerse a un diseño.

## Cuándo usarlo
- La dimensión de incertidumbre del router es alta y un spike cuesta menos que planear a ciegas.

## Entradas
- La pregunta a resolver.
- Un tiempo acotado, declarado antes de empezar.

## Pasos
1. [amarillo] Crea una rama sandbox; declara la pregunta y el tiempo acotado antes de empezar.
2. [verde] Itera rápido: prueba, descarta; no te preocupes por la calidad final del código.
3. [verde] Registra cada intento y su resultado en `templates/explore-log.md`.
4. [rojo] No mezcles la rama sandbox con producción ni la fusiones sin pasar antes por `consolidate`.
5. [verde] Al agotar el tiempo o resolver la pregunta, cierra con un resumen: qué funcionó, qué no, qué aprendiste.

## Salidas
- `docs/explore-log/<tema>.md` (desde `templates/explore-log.md`).
- Rama sandbox (se descarta o alimenta `consolidate`).

## Gates
El tiempo acotado se respeta; nada de la rama sandbox llega a producción sin pasar por `consolidate`.

## Fallback
Usa una carpeta `scratch/` en vez de una rama si no puedes crear ramas.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate docs/explore-log` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
"lee y ejecuta este playbook"; registra tokens con `./abm tokens estimate --unit explore-<tema> <archivos>`.
