---
type: Playbook
title: deploy — publica el ADS
description: Publica el ADS en su entorno de destino tras pasar la checklist previa y con rollback listo.
args: "[<entorno>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# deploy

## Propósito
Publica el ADS, o una versión de él, en su entorno de destino, con checklist previa cumplida y plan de rollback listo antes de tocar producción.

## Cuándo usarlo
- Tras pasar `review`, `security` y `ads-check`.
- El perfil marca la unidad o el ADS como listo para publicarse.

## Entradas
- Checklist previa (tests verdes, secretos fuera del repo, `ads-check` sin errores).
- Plan de rollback.

## Pasos
1. [verde] Verifica la checklist previa: tests verdes, `./abm check` sin errores, `./abm secrets` limpio.
2. [verde] Prepara el plan de rollback antes de publicar: cómo revertir, en cuánto tiempo.
3. [amarillo] Publica primero a un entorno de staging o equivalente si existe.
4. [rojo] Publicar a producción, activar cobros reales o exponer credenciales de producción es siempre bloqueante (b) — requiere confirmación explícita del humano, con la opción recomendada.
5. [verde] Tras publicar, verifica de punta a punta en el entorno real (o el staging) que todo renderiza o corre.
6. [verde] Documenta la publicación (versión, entorno, hora, quién aprobó) en `docs/work_log.md`.

## Salidas
- ADS publicado.
- Entrada de publicación en `work_log.md`.

## Gates
Checklist previa al 100 % antes del paso rojo; rollback documentado y, si es posible, probado.

## Fallback
Sigue la checklist a mano y pide confirmación explícita por el canal que uses antes del paso de producción.

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm check` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
`./abm check --json` para la checklist previa; el paso de publicación en sí no tiene orden CLI neutral (depende del proveedor elegido en `stack`).
