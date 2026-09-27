---
type: Integration Guide
title: Hermes Agent — integración con ABM
description: Instalación, carga de AGENTS.md, plantilla mcp_servers, modo one-shot para CI y límites conocidos.
tags: [hermes, agentes, mcp, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: hermes-skills
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
    title: "Hermes Agent: Skills System"
  - id: hermes-home
    resource: https://hermes-agent.nousresearch.com/
    title: Hermes Agent — Nous Research
  - id: hermes-license
    resource: https://github.com/NousResearch/hermes-agent/blob/main/LICENSE
    title: LICENSE — NousResearch/hermes-agent
  - id: hermes-context-files
    resource: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/context-files.md
    title: Context Files (AGENTS.md) — Hermes Agent
  - id: hermes-mcp-config
    resource: https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
    title: MCP Config Reference — Hermes Agent
  - id: hermes-cli-commands
    resource: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
    title: CLI Commands Reference — Hermes Agent
  - id: hermes-config
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
    title: Configuration — Hermes Agent
  - id: hermes-security
    resource: https://hermes-agent.nousresearch.com/docs/user-guide/security
    title: "Hermes Agent: Security"
  - id: hermes-repo
    resource: https://github.com/NousResearch/hermes-agent
    title: NousResearch/hermes-agent (repo root)
---

# Hermes Agent — integración con ABM

## Instalación
`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`[^hermes-skills]. Open-source,
self-hosted, licencia MIT[^hermes-home][^hermes-license].

## Carga nativa de `AGENTS.md`
Confirmado por el proveedor: Hermes carga el `AGENTS.md` del directorio de trabajo en el system
prompt al iniciar sesión, sin flag ni configuración, recorriendo la cadena de directorios (raíz del
repo git → cwd) — el más específico prevalece[^hermes-context-files]. Esto es lo que permite que
`/adapters/hermes/SKILL.md` solo exponga el comando surface, sin reescribir ninguna regla de
gobernanza.

## Skills
Fuente de verdad: `~/.hermes/skills/` (global). Proyecto: `.hermes/skills/` (nativo) o
`.agents/skills/` (alias cross-tool, el que usa el generador de ABM)[^hermes-skills].

## Plantilla `mcp_servers`
En `~/.hermes/config.yaml`, para el servidor propio de ABM y un ADS con `tools.include`
acotado[^hermes-mcp-config]:

```yaml
mcp_servers:
  abm:
    command: python3
    args: ["scripts/abm.py", "mcp"]
    tools:
      include: ["abm_okf_validate", "abm_ads_check", "abm_tokens_report"]
  mi-ads:
    command: python3
    args: ["scripts/abm.py", "mcp"]     # dentro del repo del ADS
    tools:
      include: ["abm_ads_check"]        # allowlist acotada al caso de uso
```

## Modo one-shot para CI
`hermes chat -q "<prompt>"` o `hermes -z "<prompt>"` — scriptable, sin interacción, código de
salida `1` en fallo/parcial/presupuesto excedido[^hermes-cli-commands]. Con `--usage-file
usage.json` escribe costo/tokens/modelo/llamadas al terminar, incluso si falla[^hermes-cli-commands]:

```
hermes -z "revisa el último PR" --usage-file usage.json
./abm tokens record --source telemetry --file usage.json
```

`abm tokens record --source telemetry` traduce ese reporte al esquema común del ledger (ADR 0013)
— así el consumo de una sesión Hermes en CI queda en el mismo ledger que el resto de fuentes.

## `approvals.mode`
`smart` (default recomendado) \| `manual` \| `off`, en `config.yaml`. Capa adicional:
`security.tirith_enabled`, un escáner de comandos peligrosos pre-ejecución[^hermes-config]
[^hermes-security].

## Delegación
`delegate_task` lanza subagentes sin visión de la conversación — `goal`/`context` deben ser
autocontenidos[^hermes-repo]. Confirmado en `/adapters/hermes/SKILL.md`: un subagente que produjo
una unidad no debe revisarla él mismo, y una delegación no es durable (si la sesión padre cierra
antes de que el hijo responda, el trabajo se pierde en silencio).

## Limitaciones conocidas
- No hay un formato de reglas con `globs` separado de `AGENTS.md` (no-verificado en la
  documentación revisada).
- No hay un directorio `agents/<role>.md` versionable — la delegación es un mecanismo de runtime
  (`delegate_task`), no de archivo de configuración.
- Sin exportador OTel confirmado; el análisis de tokens del dashboard local es solo estimado
  (`dashboard.show_token_analytics`, local-estimate-only).

[^hermes-skills]: Skills System — Hermes Agent
[^hermes-home]: Hermes Agent — Nous Research
[^hermes-license]: LICENSE — NousResearch/hermes-agent
[^hermes-context-files]: Context Files (AGENTS.md) — Hermes Agent
[^hermes-mcp-config]: MCP Config Reference — Hermes Agent
[^hermes-cli-commands]: CLI Commands Reference — Hermes Agent
[^hermes-config]: Configuration — Hermes Agent
[^hermes-security]: Hermes Agent: Security
[^hermes-repo]: NousResearch/hermes-agent (repo root)
