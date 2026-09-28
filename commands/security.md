---
type: Playbook
title: security — auditoría de seguridad
description: Audita la unidad o el ADS contra OWASP y verifica que no haya secretos expuestos.
args: "[<unidad>]"
tags: [comando, asegurar]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# security

## Propósito

Audita la unidad o el ADS completo contra los estándares de seguridad del núcleo (OWASP) y confirma que no hay secretos expuestos.

## Cuándo usarlo

- Antes de `release`.
- En toda unidad que toque autenticación, pagos o datos personales.

## Entradas

- `standards/security/` (OWASP Top 10, ASVS, y la guía OWASP para IA/agéntico si aplica).

## Pasos

1. [verde] Verifica el checklist de `standards/security/` según el tipo de unidad (web, API, agente con IA).
2. [verde] Confirma que no hay secretos en el repo, logs, errores ni interfaz con `./abm secrets`.
3. [amarillo] Si la unidad usa IA generativa, verifica el filtro de prompt injection y que la salida de tools se trata como dato.
4. [verde] Verifica mínimo privilegio en credenciales e integraciones.
5. [rojo] Toda vulnerabilidad explotable en producción, o credencial de producción expuesta, es bloqueante (b/c/d).
6. [verde] Documenta hallazgos y mitigaciones en `docs/work_log.md`.

## Salidas

- Hallazgos de seguridad en `work_log.md`.
- `./abm secrets` limpio.

## Gates

0 hallazgos críticos sin mitigar antes de `release`.

## Fallback

Recorre el checklist de `standards/security/` a mano; busca secretos por patrones comunes si `abm secrets` no está disponible.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm secrets` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm secrets --json`; `./abm ads-check --json` (la seguridad forma parte del Contrato ADS).
