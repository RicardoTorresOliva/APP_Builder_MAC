---
type: Playbook
title: integrate — integra una plataforma externa
description: Conecta el ADS con un tercero por la vía más segura disponible, de MCP a SQL de mínimo privilegio.
args: "<plataforma>"
tags: [comando, construir]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:00:00Z }
---

# integrate

## Propósito

Conecta el ADS con una plataforma externa eligiendo la vía más segura que cubra el caso, de más a menos preferida.

## Cuándo usarlo

- El ADS necesita hablar con un sistema de terceros: pagos, mensajería, CRM, y similares.

## Entradas

- `integrations/{mcp,api,webhooks,auth}/`.
- Credenciales en el gestor de secretos, nunca en el repo.

## Pasos

1. [verde] Evalúa las vías en orden de seguridad: MCP → API oficial con cliente tipado → SDK → webhooks firmados → colas o eventos → iPaaS → CSV/Excel → SQL de mínimo privilegio. Elige la primera que cubra el caso.
2. [amarillo] Configura la autenticación que exija la plataforma (OAuth2/OIDC u otra); nunca credenciales de producción al alcance del agente.
3. [verde] Implementa reintentos con backoff e idempotencia; valida la firma de todo webhook entrante.
4. [verde] Documenta la integración y su plan de salida (`portability.exit_plan`) en `integrations/`.
5. [rojo] Enviar datos reales a un tercero o activar un webhook en producción sin confirmación explícita es bloqueante (b).
6. [verde] Ejecuta `./abm secrets` para confirmar que no hay credenciales filtradas antes de cerrar.

## Salidas

- Integración documentada en `integrations/`.
- `.env.example` actualizado.

## Gates

Mínimo privilegio verificado; `./abm secrets` sin hallazgos.

## Fallback

Usa el SDK o la API oficial manualmente, documentando cada paso en `integrations/`.

## Reporte

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: `./abm secrets` → <resultado>
No verificado: <ítem → motivo, o "ninguno">
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Invocación por agentes

`./abm secrets --json`; "lee y ejecuta este playbook" para elegir la vía.
