---
type: Standard
title: Tests de database
description: Qué tests se escriben, qué cubren y en qué momento corren.
tags: [database, tests]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Tests de database

Ver la pirámide general en `standards/testing/README.md`. Aquí, lo específico de datos.

| Nivel | Cubre | Cuándo corre |
|---|---|---|
| Migraciones | cada migración aplica limpio sobre una copia del esquema actual y revierte limpio (`up` seguido de `down` deja el esquema idéntico) | en cada PR que agregue o modifique una migración |
| Datos | integridad referencial, constraints (`UNIQUE`, `CHECK`, `NOT NULL`) y fixtures realistas que ejercitan los casos límite del dominio | en cada PR que toque el esquema o los seeds |
| RLS/permisos | una consulta con el rol o tenant equivocado no puede leer ni escribir filas ajenas | al introducir o modificar una política de RLS |
| Restauración (según perfil) | un backup reciente restaura y el dato resultante es consistente | en el ciclo que el perfil de backups declare |

## Reglas

- Los tests de migraciones corren contra una base efímera, nunca contra un ambiente compartido.
- Un test de datos que solo verifica que una fila se insertó no basta: debe verificar la integridad
  (relaciones, constraints) que la unidad introdujo.
- La prueba de RLS usa al menos dos tenants o roles distintos para confirmar el aislamiento, no uno solo.
