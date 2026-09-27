---
type: Guide
title: Quickstart de ABM v5
description: Procedimiento corto para preparar ABM una vez y producir un ADS nuevo.
tags: [quickstart, onboarding]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:13Z }
---

# Quickstart de ABM v5

Guía detallada para personas sin experiencia técnica: `docs/manual/primeros-15-minutos.md`.

## Una sola vez

1. Instala **Python 3.9+** y **git**. Verifica con `./abm doctor` (Windows: `abm.cmd doctor`).
2. (Opcional) Instala la CI: ya viene en `.github/workflows/abm-ci.yml`; si usas otra plataforma de CI, ejecuta `./abm check`.
3. (Opcional) Modo turbo con menos confirmaciones en tu herramienta: `./abm sync --apply-turbo` (lee `docs/manual/modo-turbo.md` antes: cambia permisos del agente).

## Por cada ADS

Elige una vía:

- **Repo limpio (recomendado):** `./abm new-ads ../mi-ads --id mi-ads --name "Mi ADS" --profile <perfil>` → entra en la carpeta, `git init`.
- **Plantilla:** "Use this template" en tu plataforma de repositorios y clona el repo nuevo.

Luego, en tu herramienta de IA:

1. `bootstrap` — verifica entorno y adaptadores.
2. Describe el encargo en `START_PROJECT.md`.
3. `init-project` — perfil, ceremonia, metodología por módulo, stack (tú eliges), plan. En modo turbo el plan se publica y su aprobación queda en la cola (`pending`).
4. `start-execution` — construye FU y DU; `review` por milestone; `closeout` por unidad.
5. `iterate` para cambios posteriores.
6. Si la sesión se corta: `session-start`.

Cómo invocar cada comando en tu herramienta: `docs/manual/herramientas.md`.
