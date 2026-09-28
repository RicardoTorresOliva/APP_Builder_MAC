---
type: Requirements
title: Requisitos — panel de ventas
description: Requisitos EARS del panel de ventas con trazabilidad a unidades y tests, alcance y riesgos (init-project, paso 6).
tags: [requisitos, ears, sdd, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:01Z }
---

# Requisitos — panel de ventas

Modo SDD en los tres módulos ([mapa metodológico](methodology-map.md)): cada requisito es verificable y
apunta a su unidad ([unidades](../implementation/user_units.md)) y a su test. Origen: E = explícito en el
encargo, I = implícito del perfil `software-app`, A = asumido (registrado en la cola).

## Requisitos (EARS)

| ID | Req | Origen | Unidad | Test |
|---|---|---|---|---|
| REQ-001 | El sistema deberá guardar cada contraseña solo como hash PBKDF2-HMAC-SHA256 con sal aleatoria por usuario y ≥ 600 000 iteraciones. | I | FU-02 | `test_auth.PasswordTest` |
| REQ-002 | Cuando una persona envía credenciales válidas, el sistema deberá crear una sesión en cookie HttpOnly y SameSite=Strict y redirigir al dashboard. | E | FU-02 | `test_api…hardened_session_cookie` |
| REQ-003 | Si las credenciales son inválidas, entonces el sistema deberá responder 401 con un mensaje único que no revele si el usuario existe. | I | FU-02 | `test_api…generic_message` |
| REQ-004 | Si un par (IP, usuario) acumula 5 intentos fallidos en 15 minutos, entonces el sistema deberá responder 429 con `Retry-After`. | I | FU-02 | `test_api…rate_limited` |
| REQ-005 | Mientras no exista sesión válida, el sistema deberá responder 401 problem+json en `/api/*` y redirigir las páginas a `/login`. | I | FU-02 | `test_api…requires_session` |
| REQ-006 | Cuando llega una petición que modifica estado, el sistema deberá exigir el token CSRF de la sesión y un `Origin` propio si viene. | I | FU-02 | `test_api…csrf`, `…cross_origin` |
| REQ-007 | Mientras la sesión sea de rol vendedor, el sistema deberá limitar lecturas y altas a las ventas de ese vendedor. | E | DU-01 | `test_api…only_own_sales`, `…create_for_other` |
| REQ-008 | Cuando una persona registra una venta válida, el sistema deberá guardarla y responder 201; con la misma `Idempotency-Key` deberá devolver la existente sin duplicar. | E | DU-01 | `test_api…idempotent` |
| REQ-009 | Si una venta trae datos inválidos (fecha futura o inexistente, textos vacíos, monto ≤ 0 o con más de 2 decimales), entonces el sistema deberá responder 422 problem+json con un error por campo. | I | DU-01 | `test_api…field_errors` |
| REQ-010 | Cuando se consulta el resumen de un rango, el sistema deberá devolver total, cantidad, ticket promedio y series por mes (sin huecos) y por vendedor. | E | DU-02 | `test_api…consistent`, `test_db…gaps` |
| REQ-011 | El dashboard deberá mostrar KPIs, barras por mes y por vendedor en SVG con tooltip por teclado y puntero, tabla de detalle, modo oscuro y estados de carga, vacío y error. | E | DU-02 | verificación en navegador (work_log) |
| REQ-012 | Donde el rol sea admin, el sistema deberá permitir borrar una venta y registrar el estado anterior en `auditoria`. | E | DU-01 | `test_api…admin_and_is_audited` |
| REQ-013 | El ADS deberá exponer status, resumen, crear y borrar venta por MCP stdio y CLI `--json`; las escrituras con dry-run y la destructiva solo con confirmación humana. | E | DU-03 | `test_mcp`, `agent-conformance` |
| REQ-014 | El esquema deberá evolucionar con migraciones versionadas y reversibles registradas en `schema_migrations`. | I | FU-01 | `test_db.MigrationTest` |
| REQ-015 | El sistema deberá responder todo error como `application/problem+json` sin trazas ni detalles internos. | I | FU-02 | `test_api…transport_errors` |

## Alcance

| Dentro | Fuera | Futuro (propuesta, no se construye) |
|---|---|---|
| Login, roles admin/vendedor, sesiones | Alta de usuarios desde la web | Gestión de usuarios y cambio de contraseña |
| Registro, listado y borrado auditado de ventas | Edición de ventas | Edición con historial |
| Resumen y gráficos por mes y vendedor | Metas y comisiones | Metas por vendedor |
| MCP y CLI para agentes | Despliegue en nube | Contenedor y TLS |

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Contraseña demo filtrada | Se genera al sembrar y solo se muestra en consola; nunca en el repo (`abm secrets`) |
| Servidor expuesto en red sin TLS | Escucha en 127.0.0.1 por defecto; `--secure-cookies` detrás de TLS |
| Agente borra datos por error | `borrar-venta` en `hitl_actions`; MCP exige `confirm=true`; CLI exige `--confirm` |
| SQLite con escrituras concurrentes | Adecuado para un equipo pequeño; plan de salida a base relacional en [plan de salida](../docs/exit-plan.md) |
