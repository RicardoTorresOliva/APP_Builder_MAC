---
name: system-one
description: Cómo formular una decisión corta como preguntas tipadas atómicas (choice, score, boolean) con confianza y fallback, y llamarla con ./abm decide. Actívala para triage de riesgo, clasificación, enrutamiento de intención o cualquier decisión chica que hoy resolverías con un párrafo de razonamiento en el prompt.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# system-one

La capa System One (ADR 0011) resuelve decisiones cortas con una interfaz tipada en vez de texto
libre: `decide(state, questions) → answers`. Úsala cuando la decisión es pequeña, se repite y se
puede expresar como un tipo cerrado — no para razonamiento largo o generación de contenido.

## Tipos de pregunta
- **choice** — una opción entre un conjunto cerrado (p. ej. "¿qué modo metodológico?").
- **score** — un valor numérico en un rango (p. ej. severidad 0–1).
- **boolean** — sí/no, cuya confianza se calcula como `|2p − 1|` sobre la probabilidad `p`.

Cada respuesta trae valor, probabilidades y confianza — nunca solo el valor.

## Formular la pregunta (atómica)
Una pregunta = una decisión, sin ambigüedad de alcance. Mal: "¿está bien este módulo?". Bien:
"¿este hallazgo es un bug real, un falso positivo, o una mejora?" (choice de 3 opciones).

## Cadena de proveedores y fallback
`abm.yaml → decision.providers`: `typesafe-jev` (proveedor de decisión tipada externo, vía HTTP,
clave en variable de entorno) → `llm` (modelo de lenguaje con salida estructurada equivalente) →
`rules` (determinista, offline). Se usa el primero disponible; ante error, cae al siguiente. Sin
el proveedor externo, ABM funciona igual — el fallback `rules` es `no-verificado` para texto libre.

## Umbral de confianza por riesgo
`integrations/decision/thresholds.yaml`: actuar automáticamente en confianza alta (más estricta en
ceremonia Enterprise-Regulado), zona gris → modelo de lenguaje o cola de pendientes, confianza
baja → siempre humano. Nunca "adivinar" con confianza baja.

## Datos
El `state` puede llevar información sensible: pasa por el gate de datos del perfil antes de llamar
a `decide`. La clave del proveedor externo vive solo en variable de entorno o gestor de secretos,
nunca en código (regla 2).

## Usos ya identificados en ABM
Router metodológico y de comando, semáforo de riesgo de cada acción, triage de hallazgos de
`review`, filtro de prompt injection sobre salida de tools (regla 13), sugerencia del siguiente
comando/skill.

## Comando
`./abm decide` — admite `--json`; el consumo de cada llamada al proveedor externo se registra al
ledger como `provider-usage` (skill `token-ledger`).

## Detalle extra
`references/patrones.md`: siete recetas reutilizables (enrutamiento de intención, guardrails,
scoring de pasajes, verificación de citas, extracción verificada, clasificación jerárquica,
scoring compuesto), cada una con su fallback.
