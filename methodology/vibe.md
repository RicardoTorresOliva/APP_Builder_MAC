---
type: Methodology
title: "VIBE — exploración desechable"
description: Cuándo y cómo usar VIBE, su flujo, gates y salida obligatoria hacia consolidate.
tags: [metodologia, vibe]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# VIBE

## Qué es

Exploración rápida y desechable en una rama sandbox, con tiempo acotado. No produce el artefacto final:
produce **aprendizajes** que alimentan `IDD` o `SDD` vía `/consolidate`.

## Cuándo sí / cuándo no

- **Sí:** prototipo desechable, spike técnico, prueba de concepto, validar una idea antes de comprometerse.
- **No:** cualquier módulo con disparador de escalamiento activo (pagos, auth, datos personales/salud,
  regulación) — ver `/methodology/router.md`. No es la salida final de un ADS.

## Artefactos

- `/templates/explore-log.md` — aprendizajes, qué funcionó, qué no, y la recomendación de modo siguiente.

## Flujo paso a paso

1. Crear una rama sandbox (nunca la rama de trabajo del ADS) y fijar un tiempo límite.
2. Explorar sin ceremonia: construir lo mínimo para responder la pregunta abierta.
3. Registrar en `explore-log.md` qué se probó, qué se aprendió y qué se descarta.
4. Ejecutar `/consolidate`: decide si el siguiente paso es `IDD` (intención + restricciones) o `SDD`
   (si durante la exploración apareció un disparador de escalamiento).
5. Borrar o archivar la rama sandbox; el código de exploración no se fusiona tal cual.

## Gates y nivel de revisión

- Ceremonia `prototipo`: revisión opcional (`/methodology/ceremony.md`).
- Gate único: no fusionar código de exploración a la rama principal sin pasar por `consolidate`.

## Salida obligatoria

`explore-log.md` con aprendizajes y una recomendación explícita de modo siguiente. Sin este archivo,
la unidad VIBE no se considera cerrada.

## Riesgos y cómo se controlan

- **Se vuelve la entrega final sin pasar por consolidate:** el `closeout.md` de cualquier unidad exige
  declarar su modo; una unidad que sigue en VIBE al cerrar bloquea el `closeout` (dispara la regla 4,
  alcance, de `AGENTS.md`).
- **Se pierde el aprendizaje:** `explore-log.md` es obligatorio antes de borrar la rama.
- **Escalamiento tardío:** si aparece un disparador de escalamiento durante la exploración, `consolidate`
  fuerza `SDD` en vez de `IDD`, sin excepción.
