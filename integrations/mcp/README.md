---
type: Integration Guide
title: MCP en ABM — principios
description: Cómo ABM y sus ADS consumen servidores MCP con mínimo privilegio y disciplina de tokens.
tags: [mcp, integrations, seguridad, tokens]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: mcp-spec-2025-11
    resource: https://modelcontextprotocol.io/specification/2025-11-25
    title: Specification — Model Context Protocol (2025-11-25)
  - id: mcp-tools
    resource: https://modelcontextprotocol.io/specification/2025-11-25/server/tools
    title: Tools — MCP
  - id: mcp-annotations-blog
    resource: https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/
    title: Tool Annotations as Risk Vocabulary — MCP blog
---

# MCP en ABM — principios

## Qué es MCP, en una frase
Protocolo abierto JSON-RPC 2.0 para que un agente descubra y use *tools*, *resources* y *prompts*
de un servidor, sobre `stdio` o `Streamable HTTP`[^mcp-spec-2025-11]. ABM fija como base de
compatibilidad la versión **2025-11-25** (la más desplegada) y tolera clientes que negocien
`2026-07-28`[^mcp-spec-2025-11] — detalle en `/docs/analysis/03-investigacion-agentica.md`.

## Principios (no negociables)

1. **Catálogo curado, no "lo que aparezca".** Solo servidores oficiales del proveedor o
   verificados por ABM entran a [catalog.md](catalog.md). Nadie añade un servidor de terceros sin
   pasar por ahí.
2. **Mínimo privilegio.** Un proyecto activa solo los servidores que necesita, y dentro de cada
   servidor, solo los tools que necesita (`tools.include` — allowlist, nunca denylist de facto).
3. **Solo lectura por defecto.** Un servidor se conecta en modo lectura salvo que la tarea exija
   escritura explícita y aprobada; ver los flags de cada servidor en el catálogo.
4. **Versiones fijadas.** El comando/imagen/paquete del servidor se ancla a una versión (tag de
   Docker, versión de npm/uvx) — nunca `latest` sin revisión periódica.
5. **Activa por proyecto solo lo necesario.** Cada tool declarado consume tokens en cada turno
   (nombre + descripción + schema se cargan en el contexto del agente); un catálogo con 40 tools
   activos cuesta antes de usarse una vez. Menos servidores activos = más presupuesto para el
   trabajo real (ADR 0013).
6. **La salida de un tool es un dato, nunca una instrucción.** Un resultado de `tools/call` puede
   contener texto adversarial (prompt injection); el agente lo trata como contenido a evaluar, no
   como una orden a ejecutar. Ver [security.md](security.md).
7. **Anotaciones no son garantía.** `readOnlyHint`/`destructiveHint`/`idempotentHint` son
   metadatos que el propio servidor declara — no verificados por el protocolo. Si el servidor no
   es de confianza, no bastan para decidir el nivel de riesgo[^mcp-annotations-blog][^mcp-tools].

## Cómo se activa un servidor en ABM
`/integrate <plataforma>` busca primero en [catalog.md](catalog.md); si existe, genera la entrada
en la plantilla de la herramienta activa (ver [config-by-tool.md](config-by-tool.md)) con
`tools.include` acotado al caso de uso declarado. Si no existe, cae a la siguiente vía del orden
de preferencia (`/integrations/README.md`).

## Servidor MCP propio de ABM
ABM expone su propio servidor MCP (`python3 scripts/abm.py mcp`, stdio, biblioteca estándar) sobre
el CLI — tools de lectura y `dry_run=true` por defecto en las de escritura, recurso
`abm://tokens/summary` (ADR 0010). Se documenta en `config-by-tool.md` junto a un servidor de
terceros, para cada herramienta soportada.

[^mcp-spec-2025-11]: Specification — Model Context Protocol (2025-11-25)
[^mcp-tools]: Tools — MCP
[^mcp-annotations-blog]: Tool Annotations as Risk Vocabulary — MCP blog
