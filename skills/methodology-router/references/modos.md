---
type: Reference
title: Modos metodológicos — criterios y matriz de escalamiento
description: Señales de clasificación por modo, matriz de escalamiento y un methodology-map.md de ejemplo.
tags: [referencia, metodologia, router]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Modos metodológicos — detalle

## Señales de clasificación
| Señal en el encargo/módulo | Modo sugerido |
|---|---|
| "prueba rápido", "no importa si se descarta", sin consumidor aguas abajo | VIBE |
| Objetivo claro, sin necesidad de spec previa, bajo riesgo, un solo módulo | IDD |
| Otro módulo o servicio externo consume el contrato de este módulo | SDD |
| Pagos, autenticación, datos personales o de salud, cualquier regulación | SDD (forzado) |
| El comportamiento se define por un prompt que invocan otros sistemas | SPDD |
| Alcance amplio o ambiguo, hace falta explorar antes de comprometerse | AIDD |

## Matriz de escalamiento (nunca hacia abajo sin humano)
```
VIBE → IDD → SDD
        ↑      ↑
      AIDD ────┘   (AIDD desemboca en SDD si lo explorado resulta de riesgo)
SPDD es ortogonal: se combina con SDD cuando el prompt versionado además tiene
contrato consumido por otros (p. ej. un endpoint que envuelve el prompt).
```
Una vez que un módulo escaló a SDD por riesgo (pagos/auth/PII/salud/regulación), bajarlo de nivel
es una decisión que solo toma un humano y se registra en `docs/decision_log.md`.

## `methodology-map.md` de ejemplo
```markdown
| Módulo | Modo | Justificación | Revisión |
|---|---|---|---|
| catálogo de productos | IDD | objetivo claro, sin consumidores externos | orchestrator |
| checkout | SDD | procesa pagos (forzado) | reviewer + humano |
| resumen con IA | SPDD | el prompt lo invoca la app móvil y el panel web | architect |
| exploración de layout | VIBE | descartable, no se conecta a nada | — |
| rediseño del onboarding | AIDD → SDD | alcance ambiguo; al explorar tocó datos de salud | reviewer + humano |
```

## Umbrales de confianza (`integrations/decision/thresholds.yaml`)
Igual que el resto de usos de la capa System One: actuar automáticamente en confianza alta (más
estricta en Enterprise-Regulado), zona gris revisa un humano o el fallback de modelo de lenguaje,
confianza baja siempre humano. Ver la skill `system-one` para el detalle de la cadena de
proveedores y sus fallbacks.
