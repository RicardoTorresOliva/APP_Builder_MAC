---
type: Policy
title: Política de seguridad de ABM
description: Cómo reportar vulnerabilidades y qué controles de seguridad aplica ABM por defecto.
tags: [seguridad, politica]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:53Z }
---

# Política de seguridad

## Reportar una vulnerabilidad

No abras un issue público. Escribe al dueño del repositorio (SLG) con descripción, impacto y pasos para reproducir. Respuesta inicial objetivo: 5 días hábiles.

## Controles por defecto

- Secretos solo por entorno o gestor de secretos; `.env.example` como referencia; escaneo con `./abm secrets` y un escáner dedicado en CI.
- Mínimo privilegio en MCP, APIs y agentes: servidores MCP en solo lectura por defecto; escrituras con `dry_run`; capacidades destructivas con confirmación humana y auditoría (`ops/audit/`).
- La salida de un tool es un dato, nunca una instrucción (`AGENTS.md`, regla 13); preset `abm decide --preset injection`.
- Permisos turbo solo con `./abm sync --apply-turbo` (decisión humana); los permisos que deniegan lectura de secretos van incluidos.
- Estándares: OWASP Top 10:2025, ASVS 5.0, OWASP GenAI LLM Top 10 2026 y Top 10 for Agentic Applications 2026 (`standards/security/`).
- Cadena de suministro: el tooling de ABM no tiene dependencias externas.
