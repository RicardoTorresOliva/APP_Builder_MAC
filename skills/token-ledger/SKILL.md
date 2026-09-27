---
name: token-ledger
description: Cómo registrar consumo de tokens con ./abm tokens record|estimate, generar el reporte N1 y el dashboard N2, vigilar presupuestos y atestar cifras oficiales. Actívala al cerrar cualquier FU/DU, al iniciar sesión para leer el resumen, o cuando un presupuesto de ads.yaml esté cerca del tope.
license: MIT
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# token-ledger

Toda unidad de trabajo registra su consumo. Nunca se cierra una FU/DU sin una línea en el ledger,
medida o estimada.

## Registrar consumo
- `./abm tokens record` — cuando tienes cifras medidas (telemetría del entorno o uso reportado por
  el proveedor). Fuente: `telemetry` o `provider-usage`.
- `./abm tokens estimate` — cuando no hay medición; fuente: `estimate`. Mejor un estimado explícito
  que nada (ADR 0013).
- Cada evento lleva: `ts`, `phase` (`build`/`run`), `source`, tokens de entrada/salida/caché,
  proveedor, modelo, herramienta, actor, unidad, comando, funcionalidad, tenant y costo.

## Reportar
- `./abm tokens report` — genera `TOKENS.md` (N1): tabla legible por humano y agente.
- `./abm tokens dashboard` — genera el dashboard HTML estático (N2), si la ceremonia lo exige.
- N3 (pipeline OTel hacia observabilidad) es una guía, no una orden: se documenta, no se ejecuta
  desde aquí.

## Presupuestos
- `./abm tokens budget` — compara el ledger contra `ads.yaml → tokens.budgets`.
- Umbral blando superado → `pending add` con el default aplicado, sigue trabajando.
- Tope duro superado → bloqueante (f de `AGENTS.md`): se detiene, informa en ≤ 3 líneas con la
  opción recomendada (ajustar presupuesto o recortar alcance) y espera al humano.

## Costo
Nunca se inventa un costo. Si el modelo/proveedor no tiene precio en
`integrations/observability/pricing.yaml` (con su fuente y fecha), el costo se reporta como "n/d".

## Atestación
`./abm tokens attest` — cuando se piden cifras oficiales (p. ej. para facturar o reportar a un
cliente), genera un concepto OKF `Attested Computation` con un atestador determinista: mismas
entradas, mismo resultado, siempre.

## Exposición a agentes
Recurso MCP de solo lectura `abm://tokens/summary` (ADR 0010): cualquier agente puede leer el
resumen de consumo sin credenciales de escritura, antes de decidir si sigue trabajando.

## Detalle extra
`references/ledger-schema.md`: campos exactos del evento, ruta por defecto del ledger y la regla
de "n/d" con ejemplos.
