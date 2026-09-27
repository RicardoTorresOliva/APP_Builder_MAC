---
type: Standard
title: Seguridad de la cadena de suministro
description: Lockfiles, actualización de dependencias, SBOM, licencias y secret scanning.
tags: [seguridad, supply-chain, sbom, licencias]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Seguridad de la cadena de suministro

Cubre `A03:2025 Software Supply Chain Failures` (`standards/security/web-api.md`), `LLM04:2026
Supply Chain` y `ASI04 Agentic Supply Chain Vulnerabilities` (`standards/security/llm-agentic.md`).

## Lockfiles
- Todo gestor de paquetes del stack usa lockfile versionado en el repo; ninguna instalación en CI o
  en producción resuelve versiones "flotantes" sin lockfile.
- El lockfile se actualiza mediante un cambio revisable (PR), nunca a mano fuera de control de versiones.

## Actualización de dependencias
- Actualización automática de dependencias (categoría: bot de actualización de dependencias) con PR
  individual por actualización, para poder revertir sin arrastrar cambios no relacionados.
- Vulnerabilidad conocida de severidad alta o crítica sin parche disponible: mitigación documentada
  (aislar, deshabilitar la función afectada) hasta que exista parche; no se ignora en silencio.

## SBOM (Software Bill of Materials)
- Cada release genera un SBOM en un formato estándar (categoría: formato SBOM interoperable, p. ej.
  el usado por el ecosistema de la cadena de suministro de software) que lista dependencias directas
  e indirectas con su versión y licencia.
- El SBOM se conserva junto al artefacto de release para poder responder a una vulnerabilidad nueva
  sin tener que reconstruir el árbol de dependencias desde cero.

## Licencias
- Licencia de cada dependencia registrada; una licencia incompatible con la del ADS (o con su modelo
  de distribución) bloquea el release hasta resolverse, no se descubre después.

## Secret scanning
- Todo commit se escanea antes de aceptarse (pre-commit o CI) buscando credenciales, llaves y
  tokens; un hallazgo bloquea el merge (AGENTS.md regla 2).
- Un secreto que ya llegó a la historia de git se rota de inmediato; borrar el commit no basta.

## Verificación
`abm secrets` para el escaneo local; el gate de CI del ADS falla si el SBOM, el lockfile o el
escaneo de secretos no pasan. `skills/security-hardening/SKILL.md` incluye este archivo en su recorrido.
