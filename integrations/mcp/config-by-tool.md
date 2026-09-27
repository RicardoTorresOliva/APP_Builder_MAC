---
type: Reference
title: Configuración MCP por herramienta
description: Plantilla del servidor MCP de ABM y de un servidor de terceros para cada herramienta agéntica soportada.
tags: [mcp, configuracion, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: gh-mcp
    resource: https://github.com/github/github-mcp-server
    title: GitHub MCP Server (repo oficial) — modo lectura y stdio local
---

# Configuración MCP por herramienta

Rutas por herramienta tomadas de `/docs/compat-matrix.md`. En cada una: el servidor propio de ABM
(`python3 scripts/abm.py mcp`, stdio) y un servidor de terceros del catálogo — **GitHub MCP
Server**, en modo local (Docker) y solo lectura (`GITHUB_READ_ONLY=1`)[^gh-mcp] — como ejemplo
consistente entre formatos. Sustituye el token por una variable de entorno o el gestor de secretos
de la plataforma (`/integrations/secrets.md`); nunca lo escribas literal en el archivo.

## Claude Code — `.mcp.json` (raíz del proyecto)

```json
{
  "mcpServers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"] },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}" }
    }
  }
}
```

## VS Code / GitHub Copilot — `.vscode/mcp.json`

```json
{
  "servers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"] },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}" }
    }
  }
}
```

## Cursor — `.cursor/mcp.json`

```json
{
  "mcpServers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"] },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_PAT}" }
    }
  }
}
```

## Gemini CLI — `.gemini/settings.json`

```json
{
  "mcpServers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"], "trust": false },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_PAT" },
      "includeTools": ["get_file_contents", "search_code"]
    }
  }
}
```

## Google Antigravity — `.agents/mcp_config.json` (workspace)

```json
{
  "mcpServers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"] },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_PAT}" }
    }
  }
}
```

## Kiro — `.kiro/settings/mcp.json`

```json
{
  "mcpServers": {
    "abm": {
      "command": "python3", "args": ["scripts/abm.py", "mcp"],
      "disabled": false, "autoApprove": []
    },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_PAT}" },
      "disabled": false, "autoApprove": []
    }
  }
}
```

## Codex — `.codex/config.toml` (solo si el proyecto es *trusted*)

```toml
[mcp_servers.abm]
command = "python3"
args = ["scripts/abm.py", "mcp"]

[mcp_servers.github]
command = "docker"
args = ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"]
env = { GITHUB_PERSONAL_ACCESS_TOKEN = "${GITHUB_PAT}" }
enabled_tools = ["get_file_contents", "search_code"]
```

## Hermes — `~/.hermes/config.yaml`

```yaml
mcp_servers:
  abm:
    command: python3
    args: ["scripts/abm.py", "mcp"]
    tools:
      include: ["abm_okf_validate", "abm_ads_check", "abm_tokens_report"]
  github:
    command: docker
    args: ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
           "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: ${GITHUB_PAT}
    tools:
      include: ["get_file_contents", "search_code"]
```

## Windsurf (global) — `~/.codeium/windsurf/mcp_config.json`

```json
{
  "mcpServers": {
    "abm": { "command": "python3", "args": ["scripts/abm.py", "mcp"] },
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
               "-e", "GITHUB_READ_ONLY=1", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_PAT" }
    }
  }
}
```

## Notas

- Las claves y rutas exactas de cada herramienta están verificadas en `/docs/compat-matrix.md`
  (sección MCP de cada herramienta, con su fuente oficial).
- El servidor `abm` es siempre stdio y de solo lectura por defecto (sus tools de escritura llevan
  `dry_run=true`) — ver `/integrations/mcp/README.md`.
- Para un ADS que expone su propio servidor MCP en vez de "abm", el mismo patrón aplica sustituyendo
  el `command`/`args` por el del ADS y acotando `tools.include` al caso de uso concreto.

[^gh-mcp]: GitHub MCP Server (repo oficial) — modo lectura y stdio local
