---
type: Playbook
title: perf — rendimiento y escalabilidad
description: Verifica rendimiento, escalabilidad básica y costo por unidad antes de entregar.
args: "[<unidad>]"
tags: [comando, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# perf

## Propósito

Verifica rendimiento y escalabilidad básica de una unidad o del ADS antes de entregar, incluido el costo por unidad.

## Cuándo usarlo

- Antes de `release`.
- En unidades con datos de volumen o tráfico esperado.

## Entradas

- `standards/backend/` y `standards/database/` (checklist de escalabilidad).

## Pasos

1. [verde] Verifica servicios sin estado, caché donde aplique y colas para trabajo asíncrono.
2. [verde] Verifica índices y ausencia de N+1 en las consultas críticas.
3. [amarillo] Si el perfil lo exige, corre una prueba de carga básica sobre las rutas críticas.
4. [verde] Registra SLO/SLI relevantes y el costo por unidad, incluidos tokens si aplica.
5. [rojo] Ejecutar una prueba de carga contra producción o un proveedor de terceros sin aviso es bloqueante (b).

## Salidas

- Resultado de rendimiento en `docs/work_log.md`.

## Gates

Rutas críticas dentro del SLO declarado antes de `release`.

## Fallback

Sin herramienta de carga, estima con datos de ejemplo a volumen realista y documenta el resultado como `no-verificado`.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `docs/work_log.md` → sección Rendimiento → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

"lee y ejecuta este playbook"; `./abm tokens record --phase run ...` si mides consumo en producción.
