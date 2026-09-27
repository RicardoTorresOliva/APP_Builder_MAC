---
type: Playbook
title: init-project — planifica un proyecto nuevo
description: Elige perfil y ceremonia, clasifica la metodología, explora el stack con el humano y publica el plan.
args: "[<descripción del proyecto>]"
tags: [comando, descubrir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# init-project

## Propósito

Planifica un ADS nuevo de punta a punta: perfil, ceremonia, metodología por módulo, requisitos, stack elegido con el humano, design docs, unidades de trabajo, Contrato ADS y conocimiento montado. Termina en un plan publicado, no en código.

## Cuándo usarlo

- Al arrancar un ADS nuevo, con `START_PROJECT.md` o una descripción en la conversación.

## Entradas

- `START_PROJECT.md` o la conversación.
- `profiles/<name>/profile.md`.
- `stacks/README.md`, `stacks/cases/*.md`.
- `templates/agentic/ads.yaml`.

## Pasos

1. [verde] Si es la primera vez en el repo, ejecuta antes `bootstrap`.
2. [verde] Lee la descripción del proyecto; elige el perfil (`profiles/<name>/profile.md`) o uno compuesto si es híbrido; regístralo como `active_profile` en `docs/project_memory.md`.
3. [amarillo] Fija la ceremonia en `abm.yaml → ceremony` (prototipo/mvp/producto/enterprise-regulado) según tamaño, riesgo y regulación; explica el porqué en una línea.
4. [verde] Clasifica el encargo con `./abm methodology classify` (seis dimensiones); vuelca el resultado en `methodology-map.md` (modo por módulo + justificación + nivel de revisión).
5. [amarillo] Separa preguntas: las bloqueantes (b/c/d/e de AGENTS.md) esperan respuesta; el resto se asume y se registra con `./abm pending add`.
6. [verde] Redacta `planning/requirements.md` (explícito/implícito/asumido), `planning/scope.md` (dentro/fuera/futuro) y `planning/risks.md`.
7. [rojo] Explora el stack desde `stacks/README.md` y `stacks/cases/*.md`; presenta 2–3 opciones con trade-offs. La elección es bloqueante (e), salvo ceremonia prototipo o mvp: aplica la recomendada y encola "confirmar stack".
8. [verde] Produce los design docs que exige el perfil, al nivel de detalle que indica (HIGH/MEDIUM/LIGHT).
9. [verde] Descompón en FU y DU en `implementation/user_units.md` con criterio de aceptación atado a la regla de completitud del perfil; agrupa en milestones en `implementation/task_tracker.md`.
10. [verde] Genera `ads.yaml` desde `templates/agentic/ads.yaml` con el nivel de Contrato ADS que fija el perfil (nunca lo baja).
11. [verde] Monta `knowledge/` (bundles del perfil), genera `knowledge/index.md` y `knowledge/log.md`; actualiza `docs/project_memory.md`.
12. [amarillo] Publica el plan (perfil, ceremonia, modo por módulo, stack, FU/DU, riesgos). En turbo, "Aprobar plan" entra en la cola y lo reversible sigue; en checkpoint o Enterprise-Regulado, espera aprobación explícita.

## Salidas

- `docs/project_memory.md`, `methodology-map.md`, `planning/{requirements,scope,risks}.md`.
- `implementation/{user_units,task_tracker}.md`.
- `ads.yaml`.
- `knowledge/index.md`, `knowledge/log.md`.
- Plan publicado.

## Gates

Todo requisito mapea a una FU/DU; el stack fue elegido por el humano o encolado según ceremonia; `ads.yaml` está al nivel del perfil; `knowledge/index.md` enlaza los design docs.

## Fallback

Sigue el mismo flujo a mano: clasifica con la tabla de dimensiones de `methodology/router.md` y copia `templates/agentic/ads.yaml` para el manifiesto.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm okf validate planning implementation ads.yaml` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm methodology classify --json`, `./abm pending add --json`; sin orden CLI única para todo el flujo — "lee y ejecuta este playbook".
