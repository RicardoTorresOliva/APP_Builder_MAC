---
type: Reference
title: Checklist de superficie agéntica por nivel de Contrato ADS
description: Checklist archivo por archivo para el nivel mínimo y extendido del Contrato ADS, con la ruta exacta esperada.
tags: [referencia, agentico, contrato-ads]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Checklist de superficie agéntica

Verificar con `./abm ads-check` (estático) y `./abm agent-conformance` (dinámico) antes de marcar
un ítem como hecho — no basta con que el archivo exista, tiene que responder correctamente.

## Nivel mínimo (todo ADS)

- [ ] `ads.yaml` en la raíz del ADS: id, semver, perfil, dueño, capacidades con modo
      read/write/destructive declarado por capacidad.
- [ ] `AGENTS.md` propio del ADS, no el de ABM.
- [ ] `operate-<id>/SKILL.md` (`<id>` = el del ADS en `ads.yaml`), frontmatter Agent Skills mínimo.
- [ ] `llms.txt` en la raíz: un H1, blockquote de resumen, secciones H2 de enlaces.
- [ ] `index.md`/`log.md` del bundle OKF del ADS.
- [ ] Ledger de tokens + `TOKENS.md` (N1) generado al menos una vez.
- [ ] Plan de salida por proveedor documentado (aunque sea breve).
- [ ] Sin secretos en el repo, logs, errores ni UI; `.env.example` presente si hay credenciales.

## Nivel extendido (+ sobre el mínimo)

- [ ] Servidor MCP (stdio; + Streamable HTTP si se despliega como servicio), protocolo
      `2025-11-25`, tolerante a `2026-07-28`.
- [ ] Cada tool del servidor MCP tiene `readOnlyHint`/`destructiveHint` correctos y una
      descripción corta (no un párrafo).
- [ ] CLI con `--json` (y `--dry-run` en toda orden que escribe), o API HTTP con OpenAPI.
- [ ] Errores HTTP en `application/problem+json` (`{type, status, title, detail, instance}`).
- [ ] Webhooks entrantes firmados y verificados.
- [ ] Log de auditoría de acciones de agentes (quién, qué, cuándo, resultado).
- [ ] Dashboard de tokens N2 (o N3 documentado) según la ceremonia del perfil.
- [ ] HITL exigido antes de ejecutar cualquier capacidad marcada `destructive` en `ads.yaml`.
- [ ] `/.well-known/agent-card.json` (A2A v1.0) **solo si** el ADS es o expone un agente —
      ausente y sin marcar como pendiente si no aplica, nunca agregado "por si acaso" (regla 4).

## Errores frecuentes que `agent-conformance` detecta

- Tool de escritura sin `dry_run` por defecto en `true`.
- `destructiveHint` en `false` para una tool que en realidad borra o sobrescribe.
- `llms.txt` con más de un H1, o sin el blockquote de resumen.
- Recurso de tokens que exige credenciales de escritura para una lectura.
- `ads.yaml` con nivel `extendido` declarado pero sin servidor MCP real (solo el archivo, sin
  tools registradas) — pasa `ads-check` estático pero falla `agent-conformance` dinámico.
