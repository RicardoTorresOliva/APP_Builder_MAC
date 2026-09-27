---
type: Playbook
title: bootstrap — chequeo único de plataforma
description: Detecta la plataforma, corre doctor y sync, y confirma que el repo está listo para trabajar.
args: ""
tags: [comando, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# bootstrap

## Propósito
Confirma una sola vez, al abrir el repo en una herramienta, que la plataforma quedó detectada y que los adaptadores generados están al día. No repite este chequeo en cada sesión: para eso está `session-start`.

## Cuándo usarlo
- Primera vez que abres el proyecto en una herramienta nueva, o tras clonarlo.
- `init-project` lo invoca automáticamente si no se ha corrido antes en la sesión.

## Entradas
- Repo clonado, sin configuración previa de sesión.
- `abm.yaml` (modo, ceremonia, presupuestos).

## Pasos
1. [verde] Identifica la plataforma anfitriona por tu propio contexto (ya sabes en qué herramienta corres).
2. [verde] Corrobora con `./abm doctor` — valida Python, git y la estructura del repo.
3. [verde] Corrobora con `./abm sync --check` — confirma que los adaptadores generados (p. ej. el puntero de tu plataforma) están al día.
4. [amarillo] Si `sync --check` reporta desfase, ejecuta `./abm sync --apply-turbo` para regenerarlos (reversible: son archivos generados, no fuente).
5. [verde] Informa la plataforma detectada, el resultado de doctor/sync y los comandos disponibles.

## Salidas
- Ninguno nuevo si todo está al día.
- Adaptadores regenerados si `sync` detectó desfase.

## Gates
`./abm doctor` sin errores críticos antes de continuar con cualquier otro comando; Python o git ausentes es bloqueante (c).

## Fallback
Sin CLI: verifica a mano Python 3.9+, git y la estructura de carpetas comparando con `index.md`; identifica la plataforma por el archivo que abrió la sesión (p. ej. su propio adaptador).

## Reporte
```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm doctor` y `./abm sync --check` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes
`./abm doctor --json` y `./abm sync --check --json`; MCP `abm_doctor`.
