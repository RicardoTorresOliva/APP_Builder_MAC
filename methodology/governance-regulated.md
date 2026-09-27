---
type: Methodology
title: Gobernanza para Enterprise-Regulado
description: Capa opcional de trazabilidad alineada con ISO/IEC 42001, NIST AI RMF y el Reglamento europeo de IA.
tags: [metodologia, gobernanza, cumplimiento, enterprise-regulado]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T21:00:00Z }
stale_after: 2026-12-27T00:00:00Z
sources:
  - id: iso-42001
    resource: https://www.iso.org/standard/42001
    title: "ISO/IEC 42001:2023 — Artificial intelligence management system"
  - id: nist-ai-rmf
    resource: https://www.nist.gov/itl/ai-risk-management-framework
    title: NIST AI Risk Management Framework
  - id: eu-ai-act
    resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
    title: "Reglamento (UE) 2024/1689 (Ley de IA)"
---

# Gobernanza para Enterprise-Regulado

> Este capítulo es **orientativo, no asesoría legal**. Mapea artefactos que ABM ya produce a marcos de
> referencia públicos; no sustituye una evaluación legal o de cumplimiento formal por parte del ADS.

Capa opcional que activa la ceremonia `enterprise-regulado` (`/methodology/ceremony.md`) para dar
trazabilidad alineada con tres marcos: el sistema de gestión de IA de ISO/IEC 42001[^iso-42001], el
marco de gestión de riesgo de IA de NIST[^nist-ai-rmf] y el reglamento europeo de IA[^eu-ai-act].

## Artefacto ABM → requisito de marco

| Artefacto de ABM | Aporta a |
|---|---|
| `intent.md` / `spec/requirements.md` (propósito, usuario, restricciones) | ISO 42001 — objetivos y alcance del sistema de gestión de IA[^iso-42001]; AI RMF — función *Map*[^nist-ai-rmf] |
| `adr.md` (decisiones registradas) | ISO 42001 — evidencia de decisiones documentadas[^iso-42001]; AI RMF — función *Govern*[^nist-ai-rmf] |
| `spec/tasks.md` (trazabilidad REQ↔TASK↔TEST) | AI RMF — función *Measure* (verificación)[^nist-ai-rmf]; Reglamento de IA — documentación técnica de sistemas de alto riesgo[^eu-ai-act] |
| `closeout.md` (sincronía + quality gate) | AI RMF — función *Manage* (tratamiento de riesgo)[^nist-ai-rmf] |
| Ledger de tokens (`/docs/adr/0013-espacio-de-tokens.md`) | ISO 42001 — recursos y monitoreo del sistema de gestión[^iso-42001] |
| `router.yaml → triggers.escalate` + revisión humana obligatoria | Reglamento de IA — supervisión humana en sistemas de alto riesgo[^eu-ai-act] |
| `docs/project_memory.md` / `work_log.md` | ISO 42001 y AI RMF — registro continuo para auditoría[^iso-42001][^nist-ai-rmf] |

## Cómo se activa

1. El perfil del ADS fija `ceremony: enterprise-regulado` (`/methodology/ceremony.md`).
2. Cada `closeout.md` añade una sección "Trazabilidad regulatoria" que cita la fila de la tabla anterior
   que aplica a la unidad cerrada.
3. `abm ads-check` verifica que el nivel `extendido` del Contrato ADS incluye el log de auditoría de
   acciones de agentes exigido en este nivel (`/docs/adr/0009-contrato-ads.md`).

## Límites explícitos

- No certifica cumplimiento: solo mapea artefactos existentes a las categorías de estos marcos.
- No cubre obligaciones sectoriales adicionales (salud, financiero) fuera de lo que ya activan los
  disparadores de escalamiento del router (`/methodology/router.md`).
- Los tres marcos citados cambian; revisar esta tabla si `stale_after` venció o si un marco publica una
  revisión mayor.

## Ver también

`/methodology/ceremony.md` · `/methodology/router.md` · `/docs/adr/0009-contrato-ads.md`

[^iso-42001]: ISO/IEC 42001:2023 — Artificial intelligence management system
[^nist-ai-rmf]: NIST AI Risk Management Framework
[^eu-ai-act]: Reglamento (UE) 2024/1689 (Ley de IA)
