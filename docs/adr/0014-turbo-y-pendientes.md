---
type: ADR
title: "ADR 0014 — Modo turbo, cola de pendientes y Planning Gate"
description: Cómo se reconcilia la velocidad con las reglas 1 y 4 de AGENTS.md.
tags: [adr, decision]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:23:32Z }
---

# ADR 0014 — Modo turbo, cola de pendientes y Planning Gate

**Estado:** aceptado · **Fecha:** 2026-09-27

## Contexto

La regla 1 (Planning Gate) y la 4 (preguntar ante alcance) detienen el trabajo aunque lo pendiente sea reversible. El usuario pide turbo por defecto.

## Decisión

- `abm.yaml → mode: turbo | checkpoint` (por defecto `turbo`).
- **Bloqueantes únicos:** a) destructivo o irreversible fuera de la rama; b) producción, pagos, publicación o envío a terceros; c) credencial ausente sin fallback; d) cambio de permisos o seguridad con impacto externo; e) ambigüedad cuyo default equivocado sea irreversible o más caro que parar.
- **Planning Gate en turbo:** el plan se publica, "Aprobar plan" entra en la cola y la ejecución reversible (en rama) continúa. En `checkpoint`, en ceremonia Enterprise-Regulado o ante un bloqueante, el gate detiene.
- **Alcance:** lo que "parece útil" y no se pidió entra en la cola como propuesta; no se construye.
- **Cola** `docs/_work/PENDIENTES.md` con `abm pending list|add|resolve`.
- **Configuración turbo por herramienta** generada por `sync`: lectura y comandos seguros sin confirmación; destructivo, producción, pagos, red externa y lectura de secretos siempre con confirmación o denegados.

## Consecuencias

- Menos interrupciones; el humano revisa decisiones en lote.

## Alternativas descartadas

- Eliminar el Planning Gate: pierde control en proyectos regulados.
