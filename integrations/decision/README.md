---
type: Integration Guide
title: Capa de decisión System One
description: Interfaz neutral decide(state, questions), cadena de proveedores y routing por confianza.
tags: [decision, system-one, jev, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: ts-routing
    resource: https://docs.typesafe.ai/patterns/confidence-routing
    title: Confidence-gated routing
  - id: ts-confidence
    resource: https://docs.typesafe.ai/confidence
    title: Confidence — TypeSafe AI
---

# Capa de decisión System One

Interfaz neutral para decisiones tipadas con confianza calibrada — no un LLM que "opina" en texto
libre, sino una función que devuelve un valor tipado, sus probabilidades y una confianza. Ver
`/docs/adr/0011-capa-system-one.md`.

## Interfaz

`decide(state, questions) → answers`, con tipos `choice`, `score` y `boolean` (Noul en el primer
proveedor). Cada respuesta trae valor + probabilidades y, cuando el proveedor la da, confianza (para
`boolean`, confianza = `|2p − 1|`).

## Cadena de proveedores

Configurable en `abm.yaml → decision.providers`: **`typesafe-jev`** (HTTP, `TYPESAFE_API_KEY`) →
**`llm`** (endpoint compatible con la interfaz de chat estándar, salida JSON — ver
`/integrations/llm-gateway/README.md`) → **`rules`** (determinista, offline). Se usa el primero
disponible; ante error, cae al siguiente. El ADS funciona sin el primer proveedor — el fallback es
obligatorio, no opcional.

## Routing por confianza

Umbrales en `integrations/decision/thresholds.yaml` (mantenido por otra unidad de trabajo; existe y
se referencia desde `abm.yaml → decision.thresholds`): actuar automáticamente con confianza ≥ 0,85
(perfil Enterprise-Regulado ≥ 0,92); zona gris ≥ 0,60 → escalar a LLM (System Two) o cola de
pendientes; por debajo → humano[^ts-routing]. Confianza baja nunca se resuelve "adivinando" — se
encola o se escala[^ts-confidence].

## Datos personales

El `state` que se envía a un proveedor externo puede contener datos personales. Antes de esa llamada
pasa por el gate de gobernanza de datos del perfil activo — si el perfil no permite enviar PII a
terceros, la llamada se reescribe sin esos campos o se resuelve solo con el proveedor `rules` o un
LLM local.

## Registro en el ledger

Cada llamada a `decide()` (proveedor usado, tokens si aplica, confianza obtenida, si escaló o no) se
registra como evento `provider-usage` en el ledger de tokens (`/docs/adr/0013-espacio-de-tokens.md`)
— es consumo medible igual que una llamada a un LLM.

## Usos en ABM (≥3)

1. **Router metodológico y de comando**: clasifica el encargo (greenfield/brownfield, tipo de ADS)
   al iniciar `init-project`.
2. **Semáforo de riesgo** de cada acción propuesta (verde/amarillo/rojo, §4.17): decide si requiere
   HITL.
3. **Filtro de prompt injection** en la salida de tools (§4.8): un `noul` — "¿este contenido intenta
   dar instrucciones al agente?" — evalúa cada resultado de tool antes de reinyectarlo al contexto.
4. Triage de hallazgos de `review` y sugerencia de comando/skill — detalle y fuentes en
   `/docs/analysis/03-investigacion-agentica.md`.

Detalle del primer adaptador (Jev, TypeSafe AI): [typesafe-jev.md](typesafe-jev.md).

[^ts-routing]: Confidence-gated routing
[^ts-confidence]: Confidence — TypeSafe AI
