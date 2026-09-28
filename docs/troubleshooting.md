---
type: Troubleshooting
title: Solución de problemas de ABM
description: Errores típicos de ABM con su causa en una línea y los pasos exactos para resolverlos.
tags: [troubleshooting, errores]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:02:30Z }
---

# Solución de problemas de ABM

Cada entrada tiene la causa en una línea y los pasos exactos. Si el mensaje no aparece acá, pídele
a tu agente que corra `/doctor` primero — suele señalar la causa real.

## "Falta Python" / `✖ python` en `doctor`

**Causa:** no tenés Python 3.9 o más nuevo instalado, o no está en el PATH de tu terminal.

1. Instalá Python desde [python.org](https://www.python.org/downloads/) (marcá la opción "Add
   Python to PATH" si instalás en Windows).
2. Cerrá y volvé a abrir la terminal (o tu herramienta de IA).
3. Corré `/doctor` de nuevo para confirmar `✔ python`.

## "abm: permiso denegado" (`Permission denied`)

**Causa:** el archivo `abm` (el lanzador de macOS/Linux) no tiene permiso de ejecución — pasa
seguido después de descargar o clonar el repositorio en algunos sistemas.

1. En la terminal, dentro de la carpeta del proyecto, escribí:

   ```text
   chmod +x abm
   ```

   Esto le da permiso al archivo `abm` para ejecutarse (`chmod` = "change mode", cambia los
   permisos; `+x` = agrega permiso de ejecución). Es seguro: solo afecta ese archivo.
2. Volvé a intentar `./abm doctor`.
3. En Windows no hace falta este paso: usás `abm.cmd doctor` directamente.

## `sync --check` falla ("desfasada" o "huérfana")

**Causa:** los archivos generados para tu herramienta (comandos, skills, configuración) no
coinciden con las fuentes actuales — pasó tiempo desde la última vez que se generaron, o cambiaron
los comandos.

1. Corré:

   ```text
   ./abm sync
   ```

2. Esto regenera los archivos desfasados y borra los que ya no corresponden ("huérfanos"). Es
   reversible: son archivos generados, nunca tu propio trabajo.
3. Si además querés instalar la configuración de turbo: `./abm sync --apply-turbo`.

## `ads-check` falla

**Causa:** el proyecto no cumple todavía con el nivel mínimo (o el nivel declarado) de lo que
necesita para que otro agente lo pueda descubrir y operar de forma segura.

1. Leé el detalle del hallazgo: te dice exactamente qué falta (por ejemplo, `AGENTS.md` del
   proyecto, la skill de operación, o el índice de conocimiento).
2. Corré `/connect` para generar o completar lo que falta.
3. Volvé a correr `./abm ads-check` hasta que no haya errores.

## `okf validate` falla

**Causa:** algún documento del proyecto no tiene el encabezado (frontmatter) completo que exige el
formato de ABM — por ejemplo, le falta `type`, `title`, `description`, `status` o `generated`.

1. Abrí el archivo que señala el error (la ruta viene en el mensaje).
2. Completá el campo que falta arriba del todo del archivo, entre las líneas `---`.
3. Volvé a correr `./abm okf validate <la misma ruta>`.
4. Si no sabés qué formato usar, pedile a tu agente que lo arregle: es un chequeo mecánico y lo
   resuelve fácil.

## Presupuesto duro de tokens superado

**Causa:** una tarea gastó más tokens de los que el proyecto tiene permitido como tope máximo —
esto es uno de los seis bloqueantes de ABM, se detiene a propósito.

1. El agente te va a mostrar el estado del presupuesto (ver `docs/manual/tokens.md`).
2. Elegí una opción: ampliar el presupuesto de esa tarea o de esa unidad, o recortar lo que falta
   por hacer (dividir la tarea en partes más chicas).
3. Confirmá tu elección; el agente sigue desde ahí. No sigue solo sin que decidas.

## "El agente conversa demasiado" (saluda, se disculpa, repite lo que le pediste)

**Causa:** no está siguiendo el protocolo de salida de ABM (acciones y evidencia, sin relleno
conversacional) — puede pasar si la sesión mezcló otras instrucciones.

1. Pedile directamente: "segui el protocolo de salida de `AGENTS.md` y `standards/communication.md`:
   sin saludos, sin disculpas de relleno, reportá con la plantilla de cierre".
2. Si sigue pasando, es útil empezar una sesión nueva y correr `/session-start` para que retome
   desde la memoria del proyecto en vez de una conversación larga.

## "El agente me pregunta todo" (te interrumpe por cada detalle)

**Causa:** el proyecto puede estar en modo `checkpoint` en vez de `turbo`, o el agente no está
aplicando la cola de pendientes para lo reversible.

1. Revisá `abm.yaml → mode`: si dice `checkpoint` y vos querés menos interrupciones, cambialo a
   `turbo` (es el modo recomendado por defecto).
2. Recordale: "lo reversible aplicalo con un default y anotalo en `/pending add`, no me preguntes
   por cada detalle — preguntame solo ante un bloqueante real (ver `AGENTS.md`)".
3. Más contexto: `docs/manual/modo-turbo.md`.

## `abm secrets` encuentra algo

**Causa:** parece haber una contraseña, llave de acceso o token filtrado en el repositorio.

1. No lo publiques ni lo subas a un repositorio compartido todavía.
2. Sacá ese valor del archivo y reemplazalo por una variable de entorno o una entrada en
   `.env.example` (sin el valor real).
3. Si el secreto ya se guardó antes (aunque lo borres ahora, quedó en el historial), es necesario
   **rotarlo** (generar uno nuevo y desactivar el viejo) en el servicio correspondiente — borrar el
   archivo no alcanza.

## `links` encuentra enlaces rotos

**Causa:** un documento enlaza a un archivo que no existe (o la ruta tiene un error de tipeo).

1. El mensaje te dice el archivo y el enlace roto exacto.
2. Corregí la ruta, o creá el archivo si todavía no existía.
3. Volvé a correr `./abm links`.

## No sé qué comando usar

**Causa:** no hace falta memorizar los 36 nombres.

1. Pedile a tu agente `/help` y describí lo que querés hacer en tus propias palabras — te sugiere
   el comando correcto, incluso con alias en español.
2. También podés revisar `docs/manual/cheatsheet.md`, todos los comandos en una sola página.
