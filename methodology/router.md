---
type: Methodology
title: Router metodológico
description: Seis dimensiones, reglas de decisión, disparadores de escalamiento/desescalamiento y cómo lo ejecuta `abm methodology classify`.
tags: [metodologia, router, clasificacion]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# Router metodológico

Asigna un modo (`VIBE`, `IDD`, `SDD`, `SPDD`, `AIDD`) a un encargo o módulo. Versión máquina-legible:
`/methodology/router.yaml` (la consume `abm methodology classify`). Decisión: `/docs/adr/0006-router-metodologico.md`.

## Las seis dimensiones (0–2)

| Dimensión | Pregunta guía | 0 | 1 | 2 |
|---|---|---|---|---|
| Incertidumbre | ¿Qué tan claro está el problema y la solución? | Requisitos y solución conocidos | Objetivo claro, camino técnico por definir | Problema o solución exploratorios |
| Criticidad/riesgo | ¿Qué pasa si falla o se hace mal? | Sin impacto real | Impacto moderado y reversible | Impacto alto o irreversible (dinero, datos personales/salud, seguridad, cumplimiento) |
| Horizonte | ¿Para qué vida útil se construye? | Prototipo desechable | MVP que evolucionará | Producto o sistema de largo plazo |
| Tamaño del equipo | ¿Cuánta gente coordina el módulo? | Una persona o un agente | Equipo pequeño (2–5) | Equipo grande o varios equipos |
| Brownfield | ¿Sobre qué se construye? | Greenfield | Brownfield parcial, con margen | Brownfield estricto: stack fijo, legacy |
| Autonomía deseada | ¿Cuánta libertad tiene el agente? | Ninguna: revisa cada paso | Media: decide dentro de la spec | Alta: explora, decide y construye |

Cada nivel y sus palabras clave de detección están en `router.yaml → dimensions`.

## Algoritmo de clasificación (orden = prioridad)

1. **Disparadores de escalamiento** (`router.yaml → triggers.escalate`): si el texto o el módulo menciona
   pagos, auth, datos personales, salud o regulación → `SDD` + `review: human`, **sin excepción**, aunque
   las dimensiones digan otra cosa.
2. **Disparadores de desescalamiento** (`triggers.deescalate`): si no hubo escalamiento y el texto indica
   prototipo desechable → `VIBE`; landing/contenido → `IDD`; herramienta interna de bajo riesgo → `IDD`.
3. **Reglas por dimensión** (`rules`, en orden, gana la primera que cumple):

| # | Condición | Modo | Por qué |
|---|---|---|---|
| 1 | criticidad = 2 | SDD | Riesgo alto: trazabilidad requisito↔tarea↔test y revisión humana |
| 2 | horizonte = 0 y criticidad ≤ 1 | VIBE | Prototipo desechable de riesgo bajo/medio |
| 3 | equipo = 2 | SDD | Equipo grande: contrato compartido y trazable |
| 4 | incertidumbre = 2, criticidad ≤ 1, autonomía = 2 | AIDD | Explorar → consolidar → construir con revisión humana |
| 5 | autonomía = 2, horizonte ≥ 1, brownfield ≤ 1 | SPDD | Módulo vivo con mucha autonomía: contrato de prompt sincronizado |
| 6 | incertidumbre ≥ 1, criticidad ≤ 1 | IDD | MVP o incertidumbre media/alta, riesgo bajo/medio |
| 7 | criticidad = 1, horizonte = 2 | SDD | Riesgo medio en producto/sistema de largo plazo |

4. Si ninguna regla aplica: `default_mode: IDD`.

## Cómo lo ejecuta `abm methodology classify`

- **Entrada estructurada** (las 6 dimensiones puntuadas 0–2, o triggers explícitos): aplica el algoritmo
  de forma **determinista**, sin LLM. Salida: modo, regla o disparador que ganó, y confianza 1.0.
- **Entrada de texto libre**: infiere las 6 dimensiones con la capa System One `decide`
  (`/docs/adr/0011-capa-system-one.md`), una pregunta `Choice` por dimensión contra el texto como `state`.
  Cada respuesta trae `confidence`. Con confianza ≥ 0,60 aplica el algoritmo normalmente; por debajo,
  la dimensión queda `no-verificado` y el módulo entra a `abm pending add` para que un humano la confirme,
  usando mientras tanto el modo más conservador que sea consistente con las dimensiones sí resueltas.
- El resultado (modo, dimensiones, confianza, regla ganadora) se escribe en `methodology-map.md`
  (`/templates/methodology-map.md`).

## Mezcla y ceremonia

- Un ADS entero no comparte un solo modo: cada módulo se clasifica por separado. Ver `/methodology/mixing.md`.
- La ceremonia del ADS (`/methodology/ceremony.md`) fija el `default_mode` de partida y el nivel de gates;
  el router puede escalar un módulo puntual por encima de ese default, nunca por debajo de un disparador
  de escalamiento.

## Ver también

`/methodology/router.yaml` · `/methodology/mixing.md` · `/methodology/ceremony.md` ·
`/templates/methodology-map.md` · `/docs/adr/0006-router-metodologico.md` · `/docs/adr/0011-capa-system-one.md`
