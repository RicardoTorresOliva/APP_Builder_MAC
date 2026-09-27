---
name: review-independent
description: Cómo hacer una revisión adversarial independiente de un milestone o DU ya construido — contexto limpio, ./abm check, hallazgos con evidencia archivo:línea y severidad, nunca "parece bien" sin más. Actívala al cierre de cada milestone, o cuando alguien pida una segunda opinión sobre trabajo ya hecho.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# review-independent

Regla de oro: **quien revisa nunca es quien construyó**. Si esta sesión participó en construir lo
que va a revisar, detente y pide que otro agente/sesión lo revise (bloqueante e de `AGENTS.md`).

## Pasos
1. Arranca con contexto limpio: no asumas nada de la sesión que construyó. Relee el artefacto, el
   reporte de cierre y los `standards/` aplicables desde cero, sin heredar sus supuestos.
2. Corre `./abm check` (auditoría agregada) y anota su resultado tal cual.
3. Verifica completitud: ¿un consumidor real puede usar esto de punta a punta, incluidos estados
   vacíos y de error? (`deliverable_unit_completeness` del perfil).
4. Busca activamente lo que se pasó por alto, no solo confirmes lo que ya se afirmó: casos límite,
   supuestos sin verificar, secretos expuestos, alcance no pedido (regla 4), productos nombrados
   fuera de `stacks/`/`integrations/`/`examples/` (regla 7).
5. Por cada hallazgo real: `archivo:línea`, qué está mal, por qué importa, severidad
   (**bloqueante** | **mayor** | **menor**).
6. Si no hay hallazgos, dilo explícitamente con la evidencia de lo que se revisó — "parece bien"
   sin evidencia no es una revisión, es una opinión.

## Severidad (ver `references/severidades.md` para la tabla completa)
- **Bloqueante** — corresponde a alguna causa a–f de `AGENTS.md`, o rompe la completitud del DU.
- **Mayor** — no bloquea la entrega pero compromete seguridad, datos o un contrato que otros
  consumen.
- **Menor** — mejora legítima que no afecta la entrega actual; va a la cola de pendientes.

## Qué NO hace esta skill
No corrige el código o los artefactos que revisa — eso vuelve a quien construyó o a la cola de
pendientes con el hallazgo adjunto. No repite en prosa lo que ya dijo el reporte de cierre; solo
añade lo que ese reporte no cubrió o cubrió mal.

## Comando
`./abm check` — agrega los checks estáticos disponibles (OKF, lint, presupuesto, enlaces, secretos)
en una sola pasada; complementa, no reemplaza, la lectura humana del artefacto.

## Detalle extra
`references/severidades.md`: taxonomía completa de severidad con ejemplos de hallazgo bien y mal
formulado, y la plantilla de reporte de la revisión.
