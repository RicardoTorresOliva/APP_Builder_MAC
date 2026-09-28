---
type: Guide
title: Disciplina de tokens
description: Reglas y ejemplos concretos para que un agente use el mínimo de tokens necesario, en ABM y en cualquier ADS que produce.
tags: [tokens, contexto, guia]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:03:30Z }
---

# Disciplina de tokens

Aplica a todo agente que opera ABM y a todo ADS que ABM construye. Cada regla trae un ejemplo de
cómo se ve mal y cómo se ve bien. Desarrolla `AGENTS.md` §Tokens y contexto.

## Carga progresiva

Carga siempre lo mínimo (`AGENTS.md`, `index.md`, `knowledge/index.md`) y abre un documento completo
solo cuando la tarea lo exige de verdad. Nunca precargues `standards/`, `stacks/` o `integrations/`
completos "por si acaso".

- **Mal:** leer los 12 archivos de `standards/backend/` antes de tocar un solo endpoint.
- **Bien:** leer `standards/backend/standard.md` solo cuando la unidad es de tipo API, y
  `checklist-dod.md` recién al cerrarla.

## Grep antes de leer

Localiza primero con búsqueda de texto (`grep`/`ripgrep`) o por rangos de líneas; recién ahí abrís el
archivo completo, y solo la parte que necesitás.

- **Mal:** `Read` de un archivo de 2000 líneas para encontrar una función.
- **Bien:** `grep -n "function nombreFuncion" archivo.ts` → `Read` con `offset`/`limit` alrededor de
  esa línea.

## Subagentes que devuelven conclusiones, no volcados

Un subagente de exploración o revisión reporta hallazgos con evidencia (`archivo:línea`), nunca el
contenido íntegro de lo que leyó — eso vuelve a ocupar el contexto del agente que lo llamó por nada.

- **Mal:** el subagente pega los 40 archivos que revisó en su respuesta.
- **Bien:** "el endpoint de pagos no valida el monto negativo — `backend/pagos/router.py:88`".

## Modelo por tarea

Usá un modelo rápido y barato para búsqueda, formato y tareas mecánicas; uno potente para
arquitectura y revisión; y la capa System One (`/decide`) para decisiones cortas y tipadas en vez de
gastar un párrafo de razonamiento de un modelo completo.

- **Mal:** el modelo más caro disponible para renombrar variables en 30 archivos.
- **Bien:** un modelo rápido para el renombrado mecánico; el modelo potente solo para decidir el
  nuevo nombre si hay ambigüedad real.

## Prefijos estables para el caché

Mantené el principio del prompt (instrucciones, contexto fijo) igual entre llamadas seguidas: varios
proveedores reusan lo ya procesado si el inicio no cambió, y eso ahorra tokens y tiempo.

- **Mal:** reordenar o reformular las instrucciones de sistema en cada llamada.
- **Bien:** las instrucciones y el contexto fijo van siempre primero y en el mismo orden; lo que
  cambia (la pregunta puntual) va al final.

## Diffs en vez de reescrituras completas

Editá con cambios puntuales (diff) en vez de reescribir el archivo entero cuando solo cambia una
parte.

- **Mal:** reescribir un archivo de 300 líneas para cambiar dos.
- **Bien:** un `Edit` con el fragmento exacto que cambia.

## MCP mínimo por proyecto

Activá solo los servidores MCP que esa tarea necesita — cada herramienta conectada consume tokens
en su sola descripción, aunque no se use. Las descripciones de las tools deben ser cortas.

- **Mal:** tener conectados diez servidores MCP "por si sirven" en un proyecto que solo necesita dos.
- **Bien:** activar únicamente el servidor de la plataforma con la que esta unidad se integra.

## CLIs de scaffolding en vez de generar boilerplate

Cuando existe una herramienta de línea de comandos que genera la estructura base de un proyecto o
componente, usala en vez de escribir ese código repetitivo a mano, token por token.

- **Mal:** escribir a mano la estructura completa de un componente nuevo, archivo por archivo.
- **Bien:** correr el generador oficial del framework elegido y ajustar solo lo específico de esta
  unidad.

## Capa System One para decisiones cortas

Para una decisión chica y bien definida (clasificar, calificar riesgo, elegir entre opciones
conocidas), usá `/decide` en vez de resolverla con un párrafo de razonamiento de un modelo completo.
Ver `skills/system-one/SKILL.md`.

- **Mal:** pedirle a un modelo completo que razone en prosa si un mensaje es spam.
- **Bien:** `/decide` con una pregunta `boolean` — responde con un valor y su confianza, y cuesta una
  fracción de lo anterior.

## Salidas breves

El protocolo de salida de ABM (`standards/communication.md`) ya está diseñado para gastar menos
tokens de salida: sin relleno conversacional, con un formato de reporte de largo fijo. Seguirlo no
es solo estilo — es también disciplina de tokens.

## Verificación

`./abm token-budget -v` mide cada archivo del núcleo contra su presupuesto declarado en
`abm.yaml → budgets`; corré este comando antes de cerrar una unidad que agregó o modificó
documentación.
