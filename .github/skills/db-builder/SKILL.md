---
name: db-builder
description: Modela o modifica el esquema de datos (migraciones, índices, RLS, seeds) aplicando el estándar de database de ABM — ERD en Mermaid, migraciones reversibles, integridad, auditoría, multi-tenant y privacidad. Úsala en cualquier FU/DU que cambie el esquema.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# db-builder

## Pasos

1. Lee `standards/database/standard.md` (rango relevante) antes de tocar el esquema.
2. Actualiza el ERD en Mermaid si la unidad agrega o cambia entidades o relaciones.
3. Decide normalización vs. desnormalización; si desnormalizas, documenta el motivo medido, no
   anticipado.
4. Escribe la migración con su camino de reversión (`up`/`down`); si no tiene reversión posible,
   documenta por qué.
5. Agrega los índices que las consultas frecuentes de la unidad necesitan; revisa el plan de
   ejecución de la consulta crítica antes de cerrar.
6. Declara claves foráneas, `UNIQUE` y `CHECK` para la integridad que la unidad introduce.
7. Si la tabla es multi-tenant o tiene datos sensibles, activa RLS y permisos por rol; agrega el
   registro de auditoría para sus cambios.
8. Escribe seeds idempotentes (correr dos veces no duplica ni falla).
9. Regenera los tipos de aplicación desde el esquema; no los mantengas a mano en paralelo.
10. Clasifica toda columna con datos personales nueva y define su retención/purga
    (`standards/database/standard.md` §Privacidad).
11. Escribe o actualiza tests según `standards/database/testing.md` (migraciones, datos, RLS si aplica).
12. Corre `standards/database/checklist-dod.md` completo antes de reportar la unidad como hecha.

## Criterios de salida

- Migración aplica y revierte limpio contra una base efímera.
- Todas las casillas de `standards/database/checklist-dod.md` marcadas o justificadas.
- RLS probado con al menos dos tenants/roles cuando aplica.
- Reporte final según `standards/communication.md` (≤ 12 líneas).
