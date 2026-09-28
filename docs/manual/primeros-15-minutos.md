---
type: Onboarding
title: Tus primeros 15 minutos con ABM
description: Onboarding paso a paso, sin dar por sabido nada de programación, desde abrir el repo hasta ver el plan de tu proyecto.
tags: [manual, onboarding]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:59:30Z }
---

# Tus primeros 15 minutos con ABM

Sigue estos pasos en orden. Cada uno dice exactamente qué escribir. Si algo falla, cada paso
enlaza al arreglo en `/docs/troubleshooting.md`.

## Antes de empezar: qué es "la terminal" y por qué la vas a usar

La terminal es una ventana de texto donde escribes órdenes en vez de hacer clic. Tu herramienta de
IA (Claude Code, Codex, Cursor, y similares) normalmente ya tiene una integrada, o la abre por ti
cuando corre un comando. No necesitas saber programar para usarla: solo escribes exactamente lo que
este manual indica y presionas Enter.

- **macOS o Linux:** escribes `./abm <orden>` (por ejemplo, `./abm doctor`).
- **Windows:** escribes `abm.cmd <orden>` (por ejemplo, `abm.cmd doctor`).

Casi siempre no vas a escribir estas órdenes tú mismo: se las pides a tu agente de IA en lenguaje
normal (por ejemplo, "corré el diagnóstico") y él las ejecuta. Pero conviene que sepas leerlas,
porque el agente te va a mostrar su resultado.

## Paso 1 — Requisitos: Python y git

ABM necesita dos programas instalados en tu computadora: **Python 3.9 o más nuevo** (el lenguaje en
el que está escrito el CLI de ABM) y **git** (para guardar puntos de control de tu trabajo y poder
deshacer). Pídele a tu agente que corra:

```text
./abm doctor
```

Vas a ver algo como esto:

```text
✔ python: 3.11.4
✔ git: 2.42.0
– node: no instalado
Listo.
```

- `✔` significa que está bien.
- `✖` significa que falta algo **obligatorio**: instálalo antes de seguir. El mensaje de `doctor` te
  dice exactamente de dónde bajarlo.
- `–` significa que falta algo **opcional**: no te detiene, solo algunos stacks lo necesitan.

Si ves `✖ python` o `✖ git`, resuélvelo con `/docs/troubleshooting.md` antes de continuar.

## Paso 2 — Abre el proyecto en tu herramienta de IA

Abre la carpeta del proyecto (el repositorio) en tu herramienta de IA de preferencia (Claude Code,
Codex, Cursor, Antigravity, VS Code con Copilot, Gemini CLI, Windsurf/Devin Desktop, Kiro o
Hermes). No hace falta configurar nada más: ABM se adapta a la herramienta que abras.

## Paso 3 — `bootstrap`: chequeo único de la plataforma

Pídele a tu agente:

```text
/bootstrap
```

(en herramientas sin comandos `/`, pide "ejecuta el playbook `commands/bootstrap.md`"). Esto
detecta tu herramienta, corre el mismo diagnóstico del Paso 1, y confirma que los archivos propios
de tu herramienta (los que le permiten entender `/comandos`) están al día. Solo lo haces una vez
por herramienta nueva.

## Paso 4 — Describe tu proyecto en `START_PROJECT.md`

Abre el archivo `START_PROJECT.md` en la raíz del repositorio y completa lo que sepas: qué quieres
construir, quién lo va a usar, qué módulos tiene, y cualquier restricción (presupuesto, plazos,
datos personales). No hace falta llenarlo todo — lo que dejes en blanco, tu agente te lo pregunta o
lo asume con una opción por defecto razonable (y te avisa). También puedes simplemente contarle tu
proyecto en el chat, sin tocar el archivo.

## Paso 5 — `init-project`: arma el plan

Pídele a tu agente:

```text
/init-project
```

Esto elige el tipo de proyecto y cuánta formalidad necesita, te presenta 2 o 3 opciones de
tecnología con ventajas y desventajas (**la decisión final es tuya**), divide el trabajo en tareas
ordenadas, y publica un plan completo. Todavía no se escribe código.

## Paso 6 — Lee el plan

Tu agente te va a mostrar el plan: qué se va a construir, en qué orden, con qué tecnología, y qué
riesgos tiene. Léelo con calma. Si algo no se entiende, pide que te lo expliquen sin jerga. Si el
proyecto es simple (un prototipo), el plan avanza solo con lo reversible y solo te pide confirmar
al final; si es más formal o toca datos sensibles, espera tu aprobación explícita antes de seguir.

## Paso 7 — `start-execution`: empieza a construir

Cuando estés de acuerdo con el plan, pide:

```text
/start-execution
```

A partir de aquí, tu agente construye de forma autónoma, tarea por tarea, con verificaciones de
calidad en cada una. Se va a detener y preguntarte solo cuando encuentre algo que de verdad necesita
tu decisión (algo ambiguo, algo irreversible, o un cambio de alcance). Todo lo demás lo vas a poder
revisar después, en la cola de pendientes (`docs/manual/modo-turbo.md`) — no te va a interrumpir por
cada detalle menor.

## Qué sigue

- Para saber cómo deshacer algo si no te convenció: `docs/manual/como-deshacer.md`.
- Para entender por qué el agente a veces avanza solo y a veces pregunta: `docs/manual/modo-turbo.md`.
- Para ver cuánto está costando el proyecto: `docs/manual/tokens.md`.
- Para el catálogo completo de comandos: `docs/manual/cheatsheet.md`.
