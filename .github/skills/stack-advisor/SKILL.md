---
name: stack-advisor
description: Cómo recomendar un stack para un ADS usando el catálogo de stacks/, respetando que la elección final es humano-en-el-bucle (HITL), consciente de costo, y sabiendo cuándo NO recomendar nada. Actívala en init-project/stack, o cuando alguien pida "qué tecnología uso" para una parte del ADS.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# stack-advisor

Esta skill NUNCA nombra un producto por su cuenta en su propio cuerpo (regla 7: `skills/` es
núcleo). Su trabajo es guiar la exploración y apuntar al catálogo `stacks/`, donde sí viven los
nombres concretos.

## Pasos

1. Identifica la dimensión que hace falta decidir (front, back, datos, IA, nube, mensajería…) y el
   perfil del ADS (`profiles/<name>/profile.md`) con sus `stack_candidates`.
2. Ubica el o los `stacks/<caso>.md` cuyo perfil de audiencia calce con el proyecto (ver los cuatro
   perfiles abajo) y ábrelos — ahí están las opciones concretas con matriz de costo/complejidad.
3. Presenta 2–3 opciones categorizadas al humano con su trade-off (costo, curva de aprendizaje,
   portabilidad, madurez); nunca fijes una por tu cuenta.
4. Registra la elección en `docs/decision_log.md` y, si cambia una decisión de arquitectura ya
   tomada, avisa a `architect` para que actualice el contrato.
5. Si el proyecto es brownfield, corre `assess` primero: el stack ya existe, no se reemplaza sin
   que el humano lo pida explícitamente.

## Los cuatro perfiles de stack (categorías, detalle en `references/`)

- **vibe coder** — velocidad de exploración, mínima fricción de setup, tolera más costo por hora
  de desarrollo ahorrada.
- **pro** — equipo con estándares propios, prioriza control y observabilidad sobre velocidad
  inicial.
- **low-cost** — presupuesto ajustado, prioriza planes gratuitos/de entrada y menor superficie
  operativa.
- **corporativo** — gobernanza, cumplimiento y proveedor ya homologado priman sobre cualquier otra
  cosa.

## Cuándo NO usar esta skill

- El humano ya declaró un stack: no lo cuestiones, ejecútalo (documenta si detectas un riesgo).
- El encargo es brownfield y el stack no está en discusión (usa `assess`, no `stack`).
- La decisión es puramente de arquitectura (patrón, no producto): eso es `architect`, no esta
  skill.

## HITL y costo

La elección de stack es siempre HITL: nunca se fija un producto sin que el humano lo confirme,
incluso en modo turbo (regla 1). Toda opción presentada declara su orden de magnitud de costo
cuando se conoce; si no se conoce, se marca `no-verificado` en vez de inventarlo.

## Detalle extra

`references/perfiles-stack.md`: criterios completos por perfil (equipo, presupuesto, gobernanza,
horizonte) para elegir cuál abrir en `stacks/`.
