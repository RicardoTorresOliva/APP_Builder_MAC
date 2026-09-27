---
type: Playbook
title: release — cierra una versión
description: Cierra una versión del ADS con semver, changelog y verificación previa completa.
args: "[<versión>]"
tags: [comando, entregar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# release

## Propósito

Cierra una versión del ADS —semver, changelog, notas— tras confirmar que todo el milestone pasó revisión y Contrato ADS.

## Cuándo usarlo

- Al completar un milestone que se entrega como versión.

## Entradas

- `implementation/task_tracker.md`.
- Historial de cambios desde la última versión.

## Pasos

1. [verde] Verifica que todas las unidades del milestone pasaron `review` y `ads-check`.
2. [verde] Sube el semver del ADS en `ads.yaml`; nunca baja el nivel del Contrato ADS.
3. [verde] Redacta el changelog: qué se agregó, cambió, corrigió; riesgos residuales conocidos.
4. [amarillo] Etiqueta la versión en el control de versiones (reversible: es una etiqueta, no un despliegue).
5. [rojo] Publicar la versión como disponible para terceros (paquete público, aviso a clientes) es bloqueante (b) — confirma con el humano.
6. [verde] Actualiza `docs/project_memory.md` con la versión liberada y el siguiente objetivo.

## Salidas

- `ads.yaml` con nuevo semver.
- Changelog.
- Etiqueta de versión.

## Gates

Ninguna versión se libera con hallazgos críticos abiertos de `review`, `security` o `ads-check`.

## Fallback

Redacta el changelog a mano y coordina el anuncio por el canal que uses, sin automatizar la etiqueta.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm ads-check` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm ads-check --json` antes de etiquetar; sin orden CLI propia para el versionado semántico.
