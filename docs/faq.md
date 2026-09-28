---
type: FAQ
title: Preguntas frecuentes sobre ABM
description: Respuestas cortas a las dudas más comunes de alguien que usa ABM sin saber programar.
tags: [faq]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:03:00Z }
---

# Preguntas frecuentes sobre ABM

## ¿Necesito saber programar para usar ABM?

No. Le describís tu proyecto en lenguaje normal a tu agente de IA, seguís el plan que te presenta,
y elegís entre las opciones que te da (por ejemplo, de tecnología). El manual completo está pensado
para alguien que no programa: empezá por `docs/manual/primeros-15-minutos.md`.

## ¿Qué es un "ADS"?

Es el nombre que usa ABM para lo que vas a construir: una app, una API, un dashboard, un ERP, una
automatización, un asistente con IA, un informe, o un producto de datos. ABM es la fábrica; el ADS
es lo que produce. Ver `docs/glossary.md` para más términos.

## ¿Puedo usar cualquier herramienta de IA?

Sí, ABM está pensado para funcionar igual sin importar cuál uses (Claude Code, Codex, Cursor,
Antigravity, VS Code con Copilot, Gemini CLI, Windsurf/Devin Desktop, Kiro o Hermes). La forma de
invocar un comando cambia un poco según la herramienta — la tabla completa está en
`docs/manual/herramientas.md`. Si tu herramienta no está en la lista, siempre funciona pedirle
"lee y ejecuta `commands/<nombre>.md`".

## ¿Por qué el agente a veces avanza solo y otras veces me pregunta?

Porque trabaja en modo **turbo** por defecto: avanza solo en todo lo reversible, y solo te pregunta
ante seis situaciones concretas (algo destructivo, publicar o cobrar de verdad, falta una
credencial, un cambio de seguridad, una duda cara de equivocar, o un tope de presupuesto superado).
Todo lo demás queda anotado en una cola para que lo revises cuando quieras, en vez de interrumpirte.
Detalle completo: `docs/manual/modo-turbo.md`.

## ¿Qué pasa si no me gusta el resultado?

Todo el trabajo se guarda en puntos de control (commits de git) que se pueden deshacer. Ver
`docs/manual/como-deshacer.md` para los comandos exactos, o simplemente pedile a tu agente "deshacé
el último cambio".

## ¿Cómo elijo la tecnología (el "stack") de mi proyecto?

No la elige el agente por su cuenta: el comando `stack` te presenta 2 o 3 opciones reales, con
ventajas, desventajas y costo, y espera tu elección. Si no entendés una opción, pedí que te la
expliquen sin jerga antes de decidir.

## ¿Cuánto va a costar? ¿Cómo lo sé?

ABM lleva la cuenta de cuántos tokens (la unidad de uso de un modelo de IA) usa cada tarea, y genera
un reporte fácil de leer (`TOKENS.md`) o un panel visual, según qué tan formal sea tu proyecto. Ver
`docs/manual/tokens.md`. Si el consumo se pasa de un tope máximo, el trabajo se detiene y te
pregunta cómo seguir — no sigue gastando solo.

## ¿Puedo pausar y retomar otro día?

Sí. Al volver, pedile a tu agente `/session-start`: lee el resumen del proyecto y te dice
exactamente por dónde seguir, sin que tengas que repetirle todo desde cero.

## ¿Qué pasa si el proyecto toca pagos o datos personales?

ABM sube automáticamente el nivel de rigor y de revisión en esas partes — más verificación, y las
decisiones importantes esperan tu confirmación explícita en vez de aplicarse solas. No hace falta
que lo pidas: el comando `methodology` lo detecta y lo aplica.

## ¿El agente construye cosas que no le pedí?

No debería. Si algo "parece útil" pero no formaba parte de lo que pediste, se anota como propuesta
en la cola de pendientes para que decidas — no se construye por su cuenta.

## ¿En qué idioma me va a hablar el agente?

En español neutro, tuteándote. Algunos términos técnicos que se usan igual en todos lados (como
"token", "deploy", "spec" o "prompt") se dejan en inglés a propósito, porque así los vas a
encontrar en el resto de la documentación y en internet.

## No encuentro la respuesta acá

Revisá `docs/troubleshooting.md` si es un error concreto, `docs/glossary.md` si es un término que no
reconocés, o pedile a tu agente `/help` para que te oriente.
