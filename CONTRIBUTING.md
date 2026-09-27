---
type: Guide
title: Cómo contribuir a ABM
description: Flujo de cambios, reglas de estilo y verificaciones obligatorias antes de proponer un cambio a ABM.
tags: [contribuir, calidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:47:53Z }
---

# Cómo contribuir a ABM

1. Trabaja en una rama; nunca directamente en la principal.
2. Cambios de gobernanza (`AGENTS.md`, perfiles, contrato, OKF) → ADR en `docs/adr/` (plantilla `templates/adr.md`).
3. Edita **fuentes**, no salidas generadas: `commands/`, `skills/`, `agents/`, `AGENTS.md`. Luego `./abm sync`.
4. Todo `.md` nuevo es OKF (skill `okf-author`); el núcleo no nombra productos (regla 7).
5. Antes de proponer el cambio:
   - `./abm check` en verde;
   - `python3 -m unittest discover -s scripts/tests`;
   - `./abm okf index` si añadiste o renombraste documentos;
   - registra el consumo de tokens del cambio (`./abm tokens estimate --unit <id> <archivos>`).
6. Commits con Conventional Commits (`feat:`, `fix:`, `docs:`…), uno por unidad de trabajo.
7. Versión: semver en `abm.yaml`, `ads.yaml`, `scripts/abmkit/__init__.py` y `CHANGELOG.md`.
