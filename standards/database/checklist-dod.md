---
type: Checklist
title: Definition of Done — database
description: Casillas verificables para cerrar una FU/DU de datos.
tags: [database, dod, checklist]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# DoD — database

- [ ] ERD en Mermaid actualizado si la unidad cambió entidades o relaciones.
- [ ] Migración versionada, reversible y probada en ambas direcciones (`up`/`down`).
- [ ] Seeds idempotentes: correr dos veces no duplica ni falla.
- [ ] Claves foráneas, `UNIQUE` y `CHECK` declaradas para la integridad que aplica.
- [ ] Índice presente en columnas de filtro/join/orden de consultas frecuentes; plan de ejecución
      revisado en la consulta crítica.
- [ ] RLS y permisos por rol activos en tablas multi-tenant o con datos sensibles.
- [ ] Cambios sobre datos sensibles quedan auditados (quién, qué, cuándo, antes/después).
- [ ] Backup y restauración probados (no solo configurados).
- [ ] Estrategia multi-tenant documentada y consistente con el resto del esquema.
- [ ] Tipos de la aplicación generados desde el esquema, sin duplicado manual.
- [ ] Columnas con datos personales clasificadas; política de retención/purga definida.
- [ ] Tests de migraciones y de datos en verde.
