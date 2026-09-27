---
type: Playbook
title: decide — capa System One
description: Resuelve una decisión tipada (choice/score/boolean) con la capa de decisión y su routing por confianza.
args: "[<pregunta tipada>]"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# decide

## Propósito
Usa el modelo de decisión tipada con confianza calibrada (capa System One) para decisiones cortas —choice, score o boolean— en vez de gastar un LLM completo en ellas.

## Cuándo usarlo
- Clasificación del encargo, semáforo de riesgo, triage de revisión, selección de comando, filtro de prompt injection: cualquier decisión tipada de bajo costo.

## Entradas
- `state` (contexto de la decisión).
- Preguntas tipadas.
- `integrations/decision/thresholds.yaml`.

## Pasos
1. [verde] Define las preguntas como `choice`, `score` o `boolean`, nunca como texto libre.
2. [amarillo] Si el `state` puede llevar datos personales, aplica antes el gate de datos del perfil.
3. [verde] Ejecuta `./abm decide` — usa el primer proveedor disponible de la cadena configurada; ante error, pasa al siguiente.
4. [verde] Aplica el routing por confianza (`integrations/decision/thresholds.yaml`): alta → actúa el código; zona gris → LLM o cola; baja → humano. Enterprise-Regulado exige el umbral más alto.
5. [verde] Registra la decisión (auditable) y su consumo en el ledger de tokens.

## Salidas
- Respuesta tipada con valor y confianza.
- Entrada en el ledger de tokens.

## Gates
Ninguna decisión de confianza baja se ejecuta sola: queda en cola o pasa a humano.

## Fallback
Sin proveedor disponible, usa las reglas deterministas documentadas en `integrations/decision/` (funciona siempre; calidad `no-verificado` para texto libre).

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm decide` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
`./abm decide --json`; MCP `abm_decide` (dry-run por defecto en escritura).
