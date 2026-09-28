---
type: Methodology
title: "SDD — Spec-Driven Development"
description: Requirements (EARS) → design → tasks con trazabilidad requisito↔tarea↔test y revisión humana.
tags: [metodologia, sdd, ears, trazabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
---

# SDD (Spec-Driven Development)

## Qué es

Especificación formal en tres pasos — **requirements → design → tasks** — con trazabilidad explícita
requisito ↔ tarea ↔ test. Los requisitos se escriben en formato EARS ("Cuando `<evento>`, el sistema
debe `<respuesta>`"). Inspirado en el patrón de herramientas de SDD del ecosistema agent-native
(spec-kit-like, specs estructuradas al estilo de asistentes de código con specs propias); ABM no
depende de ninguna herramienta concreta.

## Cuándo sí / cuándo no

- **Sí:** cualquier disparador de escalamiento (pagos, auth, datos personales/salud, regulación),
  criticidad alta, equipo grande, sistema de largo plazo — ver `/methodology/router.md`.
- **No:** prototipo desechable (usa `VIBE`) o módulo de bajo riesgo con incertidumbre media (usa `IDD`,
  sobre-especificar ahí es sobre-ceremonia).

## Artefactos

- `/templates/spec/requirements.md` — requisitos EARS con ID `REQ-001…`.
- `/templates/spec/design.md` — diseño técnico que responde a esos requisitos.
- `/templates/spec/tasks.md` — tabla TASK ↔ REQ ↔ TEST.
- `/templates/adr.md` para decisiones de arquitectura relevantes.

## Flujo paso a paso

1. `requirements.md`: cada requisito en formato EARS, con ID único y criterio de aceptación verificable.
2. `design.md`: arquitectura y decisiones técnicas que satisfacen cada `REQ-*`; referencia los IDs.
3. `tasks.md`: descompone el diseño en tareas; cada fila enlaza `TASK` ↔ `REQ` ↔ `TEST`.
4. Construcción: cada tarea se implementa y se prueba contra su `TEST` declarado.
5. Revisión humana obligatoria antes de cerrar (disparadores de escalamiento) o según la ceremonia.
6. `closeout.md`: confirma que todo `REQ` tiene al menos un `TASK` y un `TEST` que lo cubre.

## Gates y nivel de revisión

- Revisión **humana obligatoria** cuando el módulo entró por un disparador de escalamiento
  (`review: human` en `router.yaml`), o cuando la ceremonia lo exige (`producto`, `enterprise-regulado`).
- Gate de trazabilidad: `tasks.md` no puede tener una fila sin `REQ` y sin `TEST`; ni un `REQ` sin tarea.
- Quality gate del perfil activo, igual que en cualquier otro modo.

## Salida obligatoria

`requirements.md` + `design.md` + `tasks.md` con la matriz de trazabilidad completa, más `closeout.md`
firmando la sincronía spec↔contratos↔código.

## Riesgos y cómo se controlan

- **Sobre-ceremonia en módulos triviales:** el router solo asigna `SDD` cuando hay un disparador o una
  dimensión lo justifica; si no, se desescala a `IDD` (`/methodology/router.md`).
- **Specs que se desactualizan:** si el módulo cambia con frecuencia y la spec no sigue el ritmo, la
  reclasificación correcta es `SPDD`, no seguir forzando `SDD` (`/methodology/spdd.md`).
- **Trazabilidad rota:** `/methodology/drift.md` compara `requirements.md`/`tasks.md` contra el código
  en cada `closeout` y marca los `REQ` sin cobertura.
