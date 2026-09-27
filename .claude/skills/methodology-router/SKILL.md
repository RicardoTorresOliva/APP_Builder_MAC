---
name: methodology-router
description: Cómo clasificar un encargo y sus módulos en un modo metodológico (VIBE, IDD, SDD, SPDD, AIDD) con ./abm methodology classify, escribir el methodology-map.md del ADS y saber cuándo escalar a revisión humana. Actívala al iniciar un ADS, al añadir un módulo nuevo, o cuando el módulo toque pagos, auth o datos personales/de salud.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# methodology-router

El **modo metodológico** se asigna por módulo, no por proyecto entero: un mismo ADS puede tener un
módulo en VIBE y otro en SDD.

## Pasos

1. Clasifica: `./abm methodology classify` (o la tool `abm_methodology_classify`) con el módulo y
   su descripción. Devuelve el modo sugerido y su confianza.
2. Si la confianza está en zona alta (según `integrations/decision/thresholds.yaml`, más estricta
   en Enterprise-Regulado): aplica el modo sugerido y sigue.
3. Si está en zona gris: revisa manualmente contra la tabla de abajo antes de decidir.
4. Si es baja, o el módulo toca pagos, autenticación, datos personales o de salud: escala a
   **SDD con revisión humana**, sin excepción, aunque la clasificación automática sugiera otra cosa.
5. Escribe o actualiza `methodology-map.md` del ADS: una fila por módulo con modo, justificación y
   quién revisa.

## Los cinco modos (cuándo usar cada uno)

- **VIBE** — exploración desechable: prototipo descartable, sin contrato que otro módulo consuma.
- **IDD** — intención mínima viable: se conoce el objetivo, no hace falta spec formal previa.
- **SDD** — spec → diseño → tareas: módulo con contrato que otros consumen, o con riesgo (pagos,
  auth, PII, salud, regulación). Exige revisión humana.
- **SPDD** — contratos de prompt versionados: módulo cuyo comportamiento depende de un prompt que
  otros sistemas invocan (necesita versión y compatibilidad hacia atrás).
- **AIDD** — explorar → consolidar → construir con revisión humana: alcance amplio o ambiguo que
  necesita descubrimiento antes de comprometerse a una spec.

## Mezcla y escalamiento

Un módulo puede mezclar modos en fases distintas (p. ej. AIDD para descubrir, luego SDD para
construir la parte con riesgo). El escalamiento nunca es automático hacia abajo: una vez en SDD
por riesgo, solo un humano lo puede bajar de nivel.

## Deriva

La deriva entre intención, spec, contratos y código se controla con `drift`; el `closeout` de cada
unidad los sincroniza. Si `drift` encuentra desalineación en un módulo SDD/SPDD, no se autocorrige
en silencio: se reporta y se resuelve con quien tenga contexto.

## Comando

`./abm methodology classify` — admite `--json` y no escribe nada por sí solo; quien escribe el
`methodology-map.md` es quien invoca la skill (`architect` u `orchestrator`).

## Detalle extra

`references/modos.md`: criterios de clasificación completos, matriz de escalamiento y ejemplos de
`methodology-map.md`.
