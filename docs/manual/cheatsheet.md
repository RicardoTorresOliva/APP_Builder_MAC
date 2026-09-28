---
type: Cheatsheet
title: Cheatsheet de comandos de ABM
description: Los 36 comandos de ABM en una sola página, agrupados por fase, con su alias en español.
tags: [manual, cheatsheet]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:58:00Z }
---

# Cheatsheet de comandos de ABM

Una página con los 36 comandos. Cada uno tiene su propia guía en `docs/manual/comandos/<nombre>.md`.
Si no recuerdas el nombre en inglés, di el alias en español o simplemente `/help`.

## Arranque

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `bootstrap` | arranque | Comprueba, una sola vez por herramienta, que el proyecto está listo para trabajar. |
| `doctor` | diagnóstico | Revisa tu computadora y el proyecto, y dice en simple qué falta. |
| `session-start` | reanudar | Lee el resumen del proyecto y dice por dónde retomar el trabajo. |
| `help` | ayuda | Muestra este catálogo y traduce alias en español. |
| `pending` | pendientes | Lista y resuelve en lote las decisiones que quedaron en cola. |

## Descubrir y definir

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `init-project` | iniciar | Planifica un proyecto nuevo: perfil, stack, plan — sin código todavía. |
| `assess` | evaluar | Inventaría un sistema existente antes de tocarlo. |
| `methodology` | metodología | Decide cuánto rigor y revisión necesita cada parte del proyecto. |
| `intent` | intención | Registra qué problema resuelve una tarea, antes de especificarla. |
| `spec` | especificar | Convierte la intención en requisitos y diseño verificables. |
| `prompt-contract` | contrato-prompt | Fija entradas, salidas y límites de un asistente con IA antes de construirlo. |
| `plan` | planificar | Ordena el trabajo en tareas y publica el plan de ejecución. |
| `stack` | pila | Explora 2-3 opciones de tecnología y espera que tú elijas. |
| `explore` | explorar | Prueba algo rápido y desechable en una rama aparte, con tiempo límite. |
| `consolidate` | consolidar | Convierte lo aprendido en una exploración en diseño definitivo. |

## Construir

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `start-execution` | ejecutar | Construye de forma autónoma el plan ya aprobado, tarea por tarea. |
| `ui` | interfaz | Construye pantallas y componentes, con sus estados vacíos y de error. |
| `api` | servicio | Construye el servicio que conecta la pantalla con los datos. |
| `db` | datos | Diseña o cambia cómo se guardan los datos, siempre de forma reversible. |
| `connect` | conectar | Prepara el proyecto para que otro agente lo opere de forma segura. |
| `decide` | decidir | Resuelve una decisión chica y repetitiva sin gastar un asistente completo. |
| `integrate` | integrar | Conecta el proyecto con un servicio externo por la vía más segura. |
| `test` | pruebas | Verifica la tarea priorizando los caminos más importantes. |

## Asegurar

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `review` | revisar | Pide una segunda opinión independiente sobre lo último construido. |
| `security` | seguridad | Audita la tarea contra problemas de seguridad conocidos. |
| `drift` | deriva | Detecta cuándo plan, especificación y código dejaron de coincidir. |
| `perf` | rendimiento | Verifica velocidad, escalabilidad básica y costo por unidad. |
| `a11y` | accesibilidad | Verifica que cualquier persona pueda usar la interfaz. |
| `ads-check` | verificar-ads | Verifica que el proyecto cumple lo mínimo para ser operado por agentes. |

## Medir

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `tokens` | tokens | Registra, reporta y verifica el consumo y presupuesto de tokens. |

## Entregar e iterar

| Comando | Alias (ES) | Qué hace |
|---|---|---|
| `deploy` | desplegar | Publica el proyecto tras pasar la checklist previa, con plan de rollback. |
| `release` | publicar | Cierra una versión: número, changelog y verificación previa completa. |
| `closeout` | cerrar | Cierra una tarea: sincroniza todo y actualiza la memoria del proyecto. |
| `iterate` | iterar | Aplica un cambio pedido después de la entrega, con su spec-delta. |
| `fix` | corregir | Corrige un bug reproducible con el cambio mínimo verificable. |
| `refactor` | refactorizar | Reordena el código sin cambiar lo que hace hacia afuera. |

## Cómo se invocan

Cada herramienta tiene su propia forma; el detalle completo está en `docs/manual/herramientas.md`.
En resumen: en Claude Code, Antigravity, VS Code + Copilot, Gemini CLI, Windsurf/Devin Desktop y
Kiro escribes `/<comando>` (o el nombre en tu chat); en Codex, Cursor y Hermes pide "ejecuta el
playbook `commands/<comando>.md`" o activa la skill `abm-playbooks`. En cualquier otra herramienta,
el fallback universal siempre funciona: "Lee y ejecuta `commands/<comando>.md`".

Ver también: `docs/manual/README.md` (índice), `docs/manual/primeros-15-minutos.md` (onboarding).
