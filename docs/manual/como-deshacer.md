---
type: Guide
title: Cómo deshacer un cambio
description: Los checkpoints de git explicados sin jerga, y los comandos exactos para volver atrás de forma segura.
tags: [manual, deshacer, git]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:30Z }
---

# Cómo deshacer un cambio

ABM guarda tu trabajo con **git**, la misma herramienta que usa casi todo el mundo para programar.
No hace falta que sepas usarla a fondo: con esta página te alcanza para volver atrás si algo no te
convenció.

## Qué es un "commit" (un punto de control)

Un **commit** es una fotografía de todos los archivos del proyecto en un momento dado, con un
mensaje que dice qué cambió. Piénsalo como un punto de guardado en un videojuego: podés seguir
jugando desde ahí, y si algo sale mal más adelante, podés volver a ese punto exacto. Tu agente crea
commits mientras trabaja; nada se pierde entre uno y el siguiente.

## Antes de deshacer: mira qué cambió

Pídele a tu agente, o escribe tú mismo en la terminal:

```text
git status
```

Te muestra qué archivos se modificaron desde el último commit. Para ver la lista de commits
recientes (los puntos de control disponibles):

```text
git log --oneline
```

Cada línea es un commit: un código corto y una descripción de una línea de qué se hizo.

## Deshacer cambios que todavía no guardaste

Si `git status` muestra archivos modificados y querés descartarlos (volver a como estaban en el
último commit):

```text
git restore <archivo>
```

Para descartar **todos** los cambios sin guardar (con cuidado: esto no se puede deshacer):

```text
git restore .
```

## Volver a un commit anterior

Si ya se guardó un commit y el resultado no te convence, podés ver ese archivo como estaba antes:

```text
git checkout <código-del-commit> -- <archivo>
```

Para volver **todo** el proyecto a como estaba en un commit anterior, sin perder el historial de lo
que pasó después (la forma segura, recomendada):

```text
git revert <código-del-commit>
```

Esto crea un commit nuevo que deshace los cambios de ese commit — no borra nada, así que siempre
podés volver a avanzar si te arrepentís.

## Ramas: el trabajo principal y las ramas "sandbox"

Una **rama** es una línea de trabajo separada. ABM trabaja siempre dentro de una rama propia del
proyecto (nunca directo sobre la versión publicada), y cuando necesita **probar algo incierto** —
el comando `explore`, en modo VIBE — crea además una **rama sandbox**: una línea de trabajo
totalmente aparte, pensada para tirarse. Nada de lo que se prueba ahí llega al proyecto real hasta
pasar por `consolidate`; si la prueba no sirve, la rama se borra sin ningún impacto:

```text
git branch                     # ver en qué rama estás
git branch -D <rama-sandbox>   # borrar una rama sandbox que ya no sirve
```

## Cuándo pedir ayuda en vez de deshacer solo

Si no estás seguro de qué comando usar, pídele a tu agente "deshace el último cambio" o "volvé al
commit anterior" — sabe ejecutar estos mismos comandos. Lo único que **no** se deshace con git son
las acciones fuera del repositorio (publicar algo en producción, enviar un cobro real, borrar datos
en un sistema externo): por eso esas acciones son siempre un bloqueante que espera tu confirmación
explícita antes de ejecutarse (ver `docs/manual/modo-turbo.md`).
