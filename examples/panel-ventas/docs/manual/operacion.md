---
type: Manual
title: Manual de operación — panel de ventas
description: Cómo arrancar, sembrar, migrar, respaldar y operar el panel de ventas, para personas y agentes.
tags: [manual, operacion, agentes, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:08:41Z }
---

# Manual de operación

Todas las órdenes se ejecutan desde `examples/panel-ventas/`.

## Personas

| Tarea | Orden |
|---|---|
| Arrancar (migra y siembra si está vacía) | `python3 app/server.py --port 8765` → <http://127.0.0.1:8765> |
| Contraseña demo fija para una sesión | `PANEL_VENTAS_DEMO_PASSWORD=... python3 app/server.py` (no la guardes en archivos) |
| Detrás de TLS | `python3 app/server.py --host 0.0.0.0 --secure-cookies` (solo con proxy TLS delante) |
| Respaldo | copia `data/panel.db` con el servidor detenido |
| Migrar / revertir | `python3 app/cli.py migrate --to 1 --dry-run --json`, luego sin `--dry-run` |

Las contraseñas demo se generan al sembrar y se muestran una sola vez en consola. Si las pierdes: borra `data/panel.db` y vuelve a arrancar.

## Agentes

| Capacidad | MCP (`python3 ops/mcp_server.py`) | CLI |
|---|---|---|
| status (read) | `status` | `python3 app/cli.py status --json` |
| ventas-resumen (read) | `ventas_resumen {desde?, hasta?}` | `python3 app/cli.py ventas-resumen --desde 2026-01-01 --json` |
| crear-venta (write) | `crear_venta {..., dry_run: true}` → revisar → `dry_run: false` | `... crear-venta ... --dry-run --json` → sin `--dry-run` |
| borrar-venta (destructive) | `borrar_venta {id}` (vista previa) → confirmación humana → `{id, dry_run: false, confirm: true}` | `... borrar-venta --id N --dry-run` → `--confirm` |

- Errores: objeto problem+json (`type`, `title`, `status`, `detail`, `errors[]`). CLI: código 1 datos, 2 uso o confirmación.
- Auditoría: `ops/audit/agent-actions.jsonl` (cada llamada MCP) y tabla `auditoria` (altas y bajas).
- Tokens: recurso MCP `panel-ventas://tokens/summary`, [reporte](../../TOKENS.md) y `ops/tokens/dashboard.html`.
