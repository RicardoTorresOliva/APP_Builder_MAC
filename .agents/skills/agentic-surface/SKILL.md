---
name: agentic-surface
description: Cómo hacer que un ADS sea operable por agentes externos según el Contrato ADS — ads.yaml, AGENTS.md, skill operate-<id>, llms.txt, servidor MCP con hints correctos, CLI --json/--dry-run, OpenAPI, errores problem+json, auditoría, y A2A solo si el ADS es o expone un agente. Verifica con ./abm agent-conformance. Actívala al construir o cerrar la superficie agéntica de cualquier ADS.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# agentic-surface

El nivel del Contrato ADS (`ads.yaml`, ADR 0009) fija qué exige esta skill: **mínimo** (todo ADS) o
**extendido** (software, datos, IA). Nunca subas o bajes el nivel por tu cuenta: lo declara el
perfil/`architect`.

## Nivel mínimo (todo ADS)
1. `ads.yaml` en la raíz: identidad (id, semver, perfil, dueño), capacidades con modo
   read/write/destructive.
2. `AGENTS.md` propio del ADS (no confundir con el de ABM).
3. Skill de operación `operate-<id>` (el `<id>` es el del ADS en `ads.yaml`) con frontmatter Agent
   Skills mínimo — plantilla en `templates/agentic/`.
4. `llms.txt` en la raíz del ADS.
5. Índice OKF (`index.md`/`log.md`) del bundle de documentación del ADS.
6. Ledger + reporte de tokens N1 (skill `token-ledger`).
7. Portabilidad declarada (plan de salida por proveedor).
8. Secretos fuera del repo.

## Nivel extendido (+ sobre el mínimo)
- Servidor MCP: stdio siempre; Streamable HTTP si el ADS se despliega como servicio. Protocolo
  base `2025-11-25`, tolerante a clientes que pidan `2026-07-28`. Tools con `readOnlyHint` y
  `destructiveHint` correctos y descripciones cortas.
- CLI con `--json` (y `--dry-run` si escribe), o API HTTP con OpenAPI.
- Errores en `application/problem+json` (RFC 9457): `{type, status, title, detail, instance}`.
- Webhooks firmados; log de auditoría de acciones de agentes.
- Dashboard de tokens N2/N3 según ceremonia.
- HITL obligatorio en toda capacidad marcada `destructive`.
- Plan de salida por proveedor, no solo declarado sino ejecutable.

## A2A (`/.well-known/agent-card.json`, v1.0)
Solo si el ADS **es** un agente o **expone** uno (no todo ADS extendido lo necesita). Si no aplica,
no lo agregues — agregar superficie que nadie consume es alcance no pedido (regla 4).

## Verificación
`./abm agent-conformance` corre el guion determinista: descubrir → listar → leer → `dry-run` →
tokens, contra el propio servidor MCP del ADS. Si el entorno tiene el agente orquestador externo
instalado, además una prueba con él en modo scripted de un solo turno. Estático: `./abm ads-check`
contra la forma de `ads.yaml`.

## Detalle extra
`references/checklist.md`: checklist archivo por archivo, por nivel, con la ruta exacta esperada.
