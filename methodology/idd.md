---
type: Methodology
title: "IDD — Intent-Driven Development"
description: Minimum Viable Spec, intent tree Propósito→Usuario→Medios, y control del drift de intención.
tags: [metodologia, idd, intent-driven]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# IDD (Intent-Driven Development)

## Qué es

Se define la **intención**, no el "cómo": un Minimum Viable Spec (`intent.md`) organizado como árbol
**Propósito → Usuario → Medios**, más restricciones, criterios de éxito medibles y no-objetivos.
El agente decide el diseño técnico y lo registra en ADRs ligeros (`/templates/adr.md`).

## Cuándo sí / cuándo no

- **Sí:** incertidumbre media/alta, riesgo bajo/medio, MVP, greenfield o brownfield con margen, equipos
  pequeños/medianos. Menos ceremonia que SDD; se adapta a requisitos cambiantes.
- **No:** cualquier disparador de escalamiento activo (pagos, auth, datos personales/salud, regulación),
  equipo grande que necesita trazabilidad compartida, o sistema crítico de largo plazo → usar `SDD`.

## Artefactos

- `/templates/intent.md` — árbol Propósito→Usuario→Medios, restricciones, criterios de éxito, no-objetivos.
- `/templates/adr.md` — una decisión ligera por cada "cómo" no trivial que el agente resuelve.
- `/templates/closeout.md` al cerrar la unidad.

## Flujo paso a paso

1. Completar `intent.md`: Propósito (por qué existe), Usuario (para quién), Medios (qué lo logra).
2. Fijar restricciones y criterios de éxito medibles; declarar no-objetivos explícitos.
3. El agente diseña e implementa; cada decisión de diseño no trivial se registra en un `adr.md` ligero.
4. Quality gate del perfil activo (`profiles/<perfil>/profile.md`) al terminar.
5. `closeout.md`: confirma que el código cumple la intención declarada, o actualiza `intent.md` si cambió.

## Gates y nivel de revisión

- Revisión según ceremonia (`/methodology/ceremony.md`): opcional en `prototipo`, recomendada en `mvp`,
  obligatoria si el módulo es crítico dentro de un ADS `producto`.
- Gate de completitud del perfil activo tras cada FU/DU (regla 3 y 5 de `AGENTS.md`).

## Salida obligatoria

`intent.md` completo + ADRs ligeros de las decisiones de diseño + `closeout.md` con la sincronía
intención↔código confirmada.

## Riesgos y cómo se controlan

- **Drift de intención:** el código se aleja de `intent.md` sin que nadie lo note. Se controla con
  `/methodology/drift.md`: el `closeout` de cada unidad compara intención, spec (si existe) y código, y
  el `intent.md` se actualiza o el código se corrige antes de cerrar.
- **No-objetivos vagos:** un no-objetivo sin criterio verificable no cuenta; `intent.md` exige que cada
  no-objetivo sea comprobable.
- **Escalamiento no detectado:** si durante la construcción aparece un disparador de escalamiento
  (por ejemplo se agrega un flujo de pago), la unidad reclasifica a `SDD` antes de continuar.
