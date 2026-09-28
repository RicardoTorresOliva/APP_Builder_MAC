---
type: Manual
title: Manual de ABM
description: Índice del manual para no programadores y cómo usarlo según lo que necesites hacer.
tags: [manual, indice]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:59:00Z }
---

# Manual de ABM

Este manual explica ABM (APP_Builder_MAC) sin dar por sabido que sabes programar. Está pensado para
que puedas pedirle a tu agente de IA que construya tu proyecto (tu ADS) y entender lo que hace en
cada paso. Tuteo, español neutro; los términos técnicos que se usan igual en todas partes (spec,
deploy, token, prompt) se dejan en inglés porque así los vas a ver en el resto del manual.

## Si es tu primera vez aquí

Empieza por `docs/manual/primeros-15-minutos.md`: en 15 minutos abres el proyecto en tu herramienta
de IA, lo pones a punto y arrancas tu primer proyecto.

## Cómo usar este manual

| Necesitas | Ve a |
|---|---|
| Ver todos los comandos en una página | `docs/manual/cheatsheet.md` |
| Entender un comando en detalle (qué escribir, qué obtienes, errores comunes) | `docs/manual/comandos/<nombre>.md` |
| Empezar de cero, paso a paso | `docs/manual/primeros-15-minutos.md` |
| Deshacer algo que salió mal | `docs/manual/como-deshacer.md` |
| Entender el modo turbo y la cola de pendientes | `docs/manual/modo-turbo.md` |
| Leer cuánto está costando el proyecto (tokens) | `docs/manual/tokens.md` |
| Saber cómo invocar comandos en tu herramienta concreta | `docs/manual/herramientas.md` |
| Una duda puntual, rápida | `/docs/faq.md` |
| Algo falló y necesitas el arreglo exacto | `/docs/troubleshooting.md` |
| Términos que no reconoces | `/docs/glossary.md` |

## Los 36 comandos

Cada comando (`bootstrap`, `init-project`, `start-execution`, `review`, `tokens`…) es un
**playbook**: un procedimiento que tu agente sigue paso a paso, con semáforo de riesgo en cada
acción — verde avanza solo, amarillo te avisa antes, rojo se detiene y te pregunta. El catálogo
completo, agrupado por fase (arranque, descubrir, construir, asegurar, medir, entregar), está en
`docs/manual/cheatsheet.md`; la página de cada uno vive en `docs/manual/comandos/`.

## Cómo se invocan

No todas las herramientas de IA tienen comandos con `/`. `docs/manual/herramientas.md` tiene la
tabla completa; cada página de comando trae además su propia tabla de invocación. El fallback que
funciona en cualquier herramienta: pide "lee y ejecuta `commands/<nombre>.md`".

## Qué hace ABM por ti

ABM guía a un agente de IA para construir tu proyecto (tu ADS: una app, una API, un dashboard, un
ERP, una automatización, un informe…) siguiendo siempre el mismo orden: primero un plan que puedas
entender, después la construcción con verificaciones de calidad en cada paso, y siempre con la
posibilidad de deshacer. El agente nunca construye algo que no pediste "porque parece útil" — eso
lo anota en una cola para que lo decidas tú (`docs/manual/modo-turbo.md`).
