---
type: Playbook
title: doctor — diagnóstico del entorno
description: Diagnostica el entorno (Python, git, estructura, config) en lenguaje simple y sugiere arreglos.
args: ""
tags: [comando, arranque]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# doctor

## Propósito

Diagnostica el entorno en lenguaje simple, para que alguien sin experiencia técnica entienda qué falla y cómo arreglarlo.

## Cuándo usarlo

- Algo falla y no se sabe por qué.
- Antes de reportar un bug de ABM mismo.
- Como parte de `bootstrap`.

## Entradas

- Ninguna entrada adicional; lee el entorno donde corre.

## Pasos

1. [verde] Ejecuta `./abm doctor` (o `abm.cmd doctor` en Windows).
2. [verde] Lee cada hallazgo: componente, estado, causa probable, arreglo sugerido.
3. [amarillo] Aplica el arreglo sugerido si es reversible (p. ej. crear una carpeta faltante o regenerar un archivo generado).
4. [rojo] Si falta una credencial o el arreglo implica un permiso fuera del repo, detente y pide al humano — es bloqueante (c/d).

## Salidas

- Reporte de diagnóstico en consola o `--json`.

## Gates

0 errores críticos antes de continuar con cualquier otro comando.

## Fallback

Revisa a mano: Python ≥ 3.9 instalado, git instalado, `abm.yaml` presente, permisos de escritura en el repo.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm doctor` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm doctor --json`; MCP `abm_doctor`.
