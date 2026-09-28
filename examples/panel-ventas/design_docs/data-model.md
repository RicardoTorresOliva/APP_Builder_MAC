---
type: Design Doc
title: Modelo de datos — panel de ventas
description: ERD, restricciones, índices y migraciones del panel de ventas (design doc HIGH del perfil software-app).
tags: [datos, erd, migraciones, ejemplo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:26Z }
---

# Modelo de datos

Base relacional embebida (archivo local). Dinero en centavos enteros; fechas ISO `AAAA-MM-DD`.
Implementación: `app/db.py` (`MIGRATIONS`).

```mermaid
erDiagram
  usuarios ||--o{ ventas : registra
  usuarios ||--o{ sesiones : abre
  ventas ||--o{ auditoria : "deja rastro"
  usuarios {
    int id PK
    text username UK "3..40"
    text nombre
    text rol "admin | vendedor (CHECK)"
    text pw_hash "PBKDF2-SHA256"
    text pw_salt "16 bytes por usuario"
    int pw_iter
  }
  ventas {
    int id PK
    int vendedor_id FK "ON DELETE RESTRICT"
    text fecha "CHECK formato"
    text cliente "1..120"
    text producto "1..80"
    int monto_centavos "CHECK > 0"
    text idem_key UK "usuario:clave"
  }
  sesiones {
    text token_hash PK "sha256 del token"
    int usuario_id FK "ON DELETE CASCADE"
    text csrf
    int expira_en
  }
  auditoria {
    int id PK
    text actor
    text accion "crear | borrar"
    int entidad_id
    text antes
    text despues
  }
```

## Migraciones (`schema_migrations`)

| Versión | Nombre | Up | Down |
|---|---|---|---|
| 1 | esquema inicial | `usuarios`, `ventas`, `sesiones` con CHECK, UNIQUE y FK | drop en orden inverso |
| 2 | índices y auditoría | `ix_ventas_fecha`, `ix_ventas_vendedor_fecha`, `ix_sesiones_expira`, `auditoria` | drop de la tabla e índices |

- Cada paso es una transacción; `python3 app/cli.py migrate --to N [--dry-run]` sube o baja.
- Índices cubren los filtros del resumen (rango de fechas y vendedor + fecha).
- Seeds idempotentes: 4 usuarios demo y ~180 ventas de 12 meses (semilla fija), solo si faltan.
- Datos personales: solo nombres de vendedores y razones sociales de clientes; retención indefinida en la demo.
- Sin multi-tenant: una base por equipo.
