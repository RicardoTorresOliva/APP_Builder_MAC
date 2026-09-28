---
type: Guide
title: Cómo leer TOKENS.md y el dashboard
description: Qué es un token, cómo leer el reporte TOKENS.md y el dashboard de tokens, qué es un presupuesto blando o duro, y qué hacer si se supera.
tags: [manual, tokens, presupuesto]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:01:30Z }
---

# Cómo leer TOKENS.md y el dashboard

## Qué es un token

Un **token** es la unidad con la que se mide (y se cobra) el uso de un modelo de IA — algo así como
los minutos de una llamada telefónica. Cuantos más tokens usa una tarea, más tarda y más cuesta.
ABM lleva la cuenta de cuántos tokens usó construir tu proyecto, y también cuántos usa tu proyecto
ya en funcionamiento (si tiene su propio asistente de IA).

## El reporte simple: `TOKENS.md`

Se genera con `/tokens report` (o el alias "tokens") y es un archivo de texto que podés abrir como
cualquier otro. Trae:

- **Total:** cuántos tokens se usaron en total, separados en "entrada" (lo que se le mandó al
  modelo) y "salida" (lo que respondió), y en cuántos eventos.
- **Estimados:** cuántos de esos números no vienen de una medición exacta, sino de una estimación
  (caracteres del texto producido, dividido 4) — se marca así cuando la herramienta no entrega el
  número exacto.
- **Tablas por fase, por tarea y por modelo:** para ver en qué se fue el consumo — construcción vs.
  uso real, qué tarea costó más, qué modelo se usó.
- **Presupuestos:** una tabla con cada límite declarado, cuánto se usó, y su estado.

## El panel visual: dashboard (nivel N2)

Si tu proyecto lo exige (ceremonia MVP o producto), `/tokens dashboard` genera un archivo HTML que
podés abrir en el navegador, sin necesitar internet ni instalar nada. Muestra los mismos datos que
`TOKENS.md`, pero en gráficos: tokens totales, costo en dólares, tokens por tarea y por modelo, la
tendencia por día, y el estado de tus presupuestos con un semáforo de color.

Hay tres niveles de detalle según qué tan formal es el proyecto: **N1** (el reporte de texto,
alcanza para un prototipo o un informe), **N2** (el panel visual, para MVP o producto), y **N3**
(un panel en vivo conectado a la infraestructura de monitoreo, para proyectos enterprise o
regulados).

## Presupuesto blando vs. presupuesto duro

Cada límite de tokens puede tener dos niveles:

- **Blando:** un aviso. Si lo superás, no se detiene nada — el hecho queda anotado en la cola de
  pendientes (`docs/manual/modo-turbo.md`) para que lo revises cuando quieras.
- **Duro:** un tope real. Si lo superás, la tarea se detiene ahí mismo — es uno de los seis
  bloqueantes de ABM (ver `docs/manual/modo-turbo.md`).

En el reporte y en el panel vas a ver el estado de cada presupuesto con tres colores:

| Estado | Qué significa |
|---|---|
| ✔ dentro | El consumo está bajo ambos límites |
| ⚠ umbral blando | Se pasó el aviso, pero no se detuvo nada — revisalo en la cola cuando puedas |
| ✖ tope duro superado | Se detuvo la tarea; necesita tu decisión antes de seguir |

## Qué hacer si se supera un presupuesto

- **Umbral blando:** no hace falta actuar ya — aparece en `/pending list` con el contexto y podés
  responderlo junto con el resto de la cola.
- **Tope duro:** el agente se detiene y te presenta dos caminos: ampliar el presupuesto (si el
  trabajo lo justifica) o recortar lo que falta por hacer (dividir la tarea, simplificar el
  alcance). Ninguna de las dos pasa sin que vos la confirmes.

## Cifras oficiales, para cuando hace falta un número exacto

Si necesitás un número de costo que se pueda auditar (por ejemplo, para reportarlo a alguien más),
`/tokens attest` recalcula los totales desde el registro original de eventos y confirma que
coinciden con lo que dice `TOKENS.md` — así el número queda respaldado, no es una estimación suelta.
