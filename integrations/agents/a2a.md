---
type: Integration Guide
title: A2A (Agent2Agent) — cuándo y cómo
description: Cuándo publicar un Agent Card A2A, sus campos obligatorios y la relación con MCP.
tags: [a2a, agentes, protocolo, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: a2a-spec
    resource: https://a2a-protocol.org/latest/specification/
    title: Agent2Agent (A2A) Protocol Specification
  - id: a2a-lf-press
    resource: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    title: A2A Protocol Surpasses 150 Organizations — Linux Foundation
---

# A2A (Agent2Agent) — cuándo y cómo

## Cuándo usarlo
Solo si el ADS **es** un agente o **expone** un agente a otros agentes (por ejemplo, un ADS que
atiende consultas conversacionales de otro sistema). Un ADS que es solo una API o una base de datos
no necesita A2A — le basta con MCP y/o OpenAPI. No implementar A2A "por si acaso": es superficie
adicional que auditar y mantener.

## Qué es
Protocolo para que agentes se descubran y se comuniquen entre sí, gobernado por la **Linux
Foundation**; integrado en agosto de 2026 a la Agentic AI Foundation (AAIF), el mismo hogar que
ahora también aloja MCP[^a2a-lf-press]. Versión estable vigente: **1.0**[^a2a-spec], liberada en
marzo de 2026 con Agent Cards firmadas y una arquitectura alineada a la web[^a2a-lf-press].

## Descubrimiento: Agent Card
`GET https://{dominio-del-servidor}/.well-known/agent-card.json`, sin autenticar[^a2a-spec].
Campos obligatorios del `AgentCard`:

| Campo | Qué es |
|---|---|
| `name`, `description` | Identidad legible |
| `version` | Versión del agente (no del protocolo) |
| `supportedInterfaces` | Array de `AgentInterface`: `{url, protocolBinding, protocolVersion, tenant?}`, bindings `JSONRPC`\|`GRPC`\|`HTTP+JSON`[^a2a-spec] |
| `capabilities` | `AgentCapabilities` |
| `defaultInputModes`, `defaultOutputModes` | Modalidades por defecto |
| `skills` | Array de `AgentSkill`: `{id, name, description, tags[]}` obligatorios; `examples`/`inputModes`/`outputModes` opcionales[^a2a-spec] |

Opcionales: `provider`, `documentationUrl`, `securitySchemes`, `securityRequirements`, `signatures`
(JWS sobre JSON canonicalizado, RFC 8785/7515), `iconUrl`[^a2a-spec].

## Relación con MCP
Declarada explícitamente por el proyecto: **A2A y MCP son complementarios, no alternativos**. MCP
conecta un agente a herramientas y datos; A2A conecta agentes entre sí[^a2a-lf-press]. Un ADS que es
un agente típicamente expone ambos: MCP para que otro agente lo opere como herramienta, A2A si
además debe conversar como par.

## En ABM
Un ADS que declara A2A lo hace en su `ads.yaml` (nivel "Extendido" del contrato — ver
`/docs/adr/0009-contrato-ads.md`) y publica el Agent Card junto al resto de la superficie agéntica
(`AGENTS.md`, `llms.txt`, SKILL.md de operación — `/docs/adr/0010-superficie-agentica.md`).

[^a2a-spec]: Agent2Agent (A2A) Protocol Specification
[^a2a-lf-press]: A2A Protocol Surpasses 150 Organizations — Linux Foundation
