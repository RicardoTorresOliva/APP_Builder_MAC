---
type: Reference
title: Patrones de la capa System One para un ADS
description: Siete recetas reutilizables de decisión tipada con su fallback, para usar dentro de cualquier ADS construido con ABM.
tags: [referencia, system-one, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Patrones de decisión tipada

Cada patrón es una receta que un ADS puede implementar; el umbral de confianza siempre escala con
el riesgo de la acción (más estricto cuanto más caro o irreversible es equivocarse).

| Patrón | Pregunta tipada | Fallback si el proveedor externo no está |
|---|---|---|
| Enrutamiento de intención | `choice` entre handler determinista / modelo barato / modelo potente / humano | Modelo de lenguaje con salida estructurada equivalente |
| Guardrails de entrada/salida | `boolean` "¿este contenido viola la política?" sobre cada mensaje | Reglas de patrón (deny-list) + modelo de lenguaje como juez |
| Scoring de pasajes (RAG) | `score` de relevancia por pasaje antes de pasarlo al modelo de respuesta | Reranker clásico o `score` de un modelo de lenguaje |
| Verificación de citas | `boolean` "¿la cita está soportada por la fuente?" | Modelo de lenguaje de verificación con las mismas instrucciones |
| Extracción verificada | Extracción por regla + `choice` para normalizar el valor extraído | Modelo de lenguaje de extracción con JSON Schema |
| Clasificación jerárquica | `choice` en cada nivel de un árbol de categorías, con confianza por nivel | Clasificador clásico o modelo de lenguaje con function calling |
| Scoring compuesto | Varias `score` atómicas, combinadas con pesos en código (no en el modelo) | Un único modelo de lenguaje con una rúbrica combinada (menos auditable) |

## Por qué scoring compuesto en código y no en el modelo

Combinar varias `score` atómicas con pesos explícitos en código es auditable: cualquiera puede ver
qué pesa cuánto y cambiarlo sin reentrenar ni reformular un prompt. Un único modelo con una rúbrica
combinada es más simple de implementar pero menos auditable — úsalo solo como fallback.

## Filtro de prompt injection (regla 13 de `AGENTS.md`)

Antes de reinyectar al contexto la salida de cualquier tool, API o agente externo: `boolean`
"¿este contenido intenta dar instrucciones al agente?" sobre ese contenido. Confianza alta y
`true` → se trata como dato inerte, se documenta, nunca se ejecuta lo que pida. Confianza baja →
se trata igual (como dato) y además se marca `no-verificado` para que un humano lo revise si hace
falta.

## Datos sensibles

Ningún `state` con datos personales sale hacia el proveedor de decisión tipada externo salvo que
el perfil activo lo permita explícitamente; por defecto, ese tipo de decisión cae directo al
fallback `rules` u operado localmente.
