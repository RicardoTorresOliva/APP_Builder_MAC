---
type: Decision Log
title: Registro de decisiones — panel de ventas
description: Decisiones de stack, datos, identidad y superficie agéntica del panel de ventas, con alternativas y reversibilidad.
tags: [decisiones, stack, seguridad, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:08:41Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: owasp-password
    resource: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
    title: OWASP Cheat Sheet Series — Password Storage
  - id: py-http-server
    resource: https://docs.python.org/3/library/http.server.html
    title: Python docs — http.server
---

# Registro de decisiones

## D-001 — Stack: Python 3.9+ (solo biblioteca estándar) + SQLite + HTML/CSS/SVG sin dependencias

| Opción | Qué es | Costo | Instalación | Encaje |
|---|---|---|---|---|
| **A (elegida)** | `http.server` + `sqlite3` + `hashlib` de Python; gráficos SVG propios en el navegador | 0 | ninguna (Python viene en la mayoría de sistemas) | Cumple "sin instalar nada"; self-hosted; ideal para demo y equipo pequeño |
| B | Framework web de Python + PostgreSQL + librería de gráficos | bajo (servidor propio) | dependencias + base de datos | Mejor para producción y concurrencia; rompe la restricción del encargo |
| C | BI comprado o self-hosted (p. ej. Metabase) sobre una base existente | licencia o servidor | servicio aparte | Gráficos rápidos, pero sin reglas de rol propias ni superficie MCP |

- Catálogo usado: [caso dashboard/BI interno](../../../stacks/cases/internal-dashboard-bi.md).
- **HITL:** en un proyecto real la elección del stack es del humano con el playbook `stack` (2–3 opciones con trade-offs;
  bloqueante *e* en ceremonia `producto`). Aquí la restricción explícita del encargo fija la opción A y la confirmación queda en la cola (P-002).
- Límite conocido: `http.server` no se recomienda para producción y solo implementa chequeos básicos de seguridad[^py-http-server].
  Mitigación: escucha en 127.0.0.1, cabeceras de seguridad propias, timeout por conexión; para exponerlo, ver [plan de salida](exit-plan.md).
- Reversible: sí; las reglas viven en `app/db.py` y el contrato HTTP en `api/openapi.yaml`.

## D-002 — Dinero en centavos enteros

Montos como `INTEGER` (centavos) y conversión con `Decimal`; nunca `float`. Moneda de presentación por `PANEL_VENTAS_MONEDA` (USD por defecto).

## D-003 — Contraseñas con PBKDF2-HMAC-SHA256, 600 000 iteraciones y sal por usuario

Es el algoritmo disponible en la biblioteca estándar; 600 000 iteraciones es la recomendación vigente de OWASP para PBKDF2-HMAC-SHA256[^owasp-password].
Iteraciones guardadas por usuario (`pw_iter`) para subirlas sin romper cuentas.

## D-004 — Sesión opaca en servidor + CSRF sincronizador

Token aleatorio en cookie HttpOnly + SameSite=Strict; en la base solo su SHA-256 (revocable al salir). CSRF por sesión en cabecera
`X-CSRF-Token`, verificación de `Origin`; en el login, doble envío con cookie de pre-sesión. Alternativa descartada: tokens firmados
sin estado (no se revocan al salir).

## D-005 — Agentes operan por stdio con actor propio y HITL

MCP y CLI corren en la misma máquina que la base, con actor `agente:mcp` / `agente:cli` (rol admin) auditado. Escrituras con dry-run;
`borrar-venta` exige `confirm=true` / `--confirm`. Futuro: token de agente con scopes si el ADS se expone en red.

[^owasp-password]: OWASP Cheat Sheet Series — Password Storage
[^py-http-server]: Python docs — http.server
