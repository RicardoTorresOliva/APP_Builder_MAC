---
type: Reference
title: knowledge/ — sub-bundle OKF del ADS
description: Conocimiento de diseño del ADS activo, en OKF v0.2, navegado desde knowledge/index.md.
tags: [okf, conocimiento]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:31:52Z }
---

# knowledge/ — sub-bundle OKF del ADS

Conocimiento de diseño del ADS activo en **OKF v0.2** (Open Knowledge Format de Google Cloud), con las reglas del perfil ABM: `/okf/PROFILE.md`. `init-project` monta aquí los `knowledge_bundles` del perfil y regenera `index.md`. Interoperable con `conocimiento/` de AGE_Builder (fábrica de arneses de SLG) sin conversión.

## Reglas del sub-bundle
- **Un archivo = un concepto**, nombre corto en kebab-case, sin espacios ni tildes.
- **Frontmatter** según el perfil ABM: `type`, `title`, `description`, `status`, `generated: { by, at }`; `sources` con notas al pie y `stale_after` si caduca.
- **Enlaces** entre conceptos con `/ruta.md` o relativos.
- **`index.md`** (obligatorio): listado por secciones `* [Título](ruta) - descripción`, sin frontmatter.
- **`log.md`** (obligatorio): encabezados `## YYYY-MM-DD`, lo más reciente primero, una entrada por escritura.

Ejemplo de concepto:

```markdown
---
type: Practice
title: Estructura de propuesta que convierte
description: Qué hace que una propuesta comercial cierre.
tags: [propuestas, conversion]
status: stable
generated: { by: human:ana, at: 2026-07-22T10:00:00Z }
---

Una propuesta convierte cuando es corta, habla del problema del cliente antes que de la empresa
y cierra con un único siguiente paso. Ver [tono comercial](/knowledge/tono-comercial.md).
```

## Qué va aquí
- Conocimiento de diseño que el agente debe leer antes de producir.
- Conocimiento estable del dominio, estándares y referencias de las que depende el ADS.
- Lo que cambia a menudo no se congela aquí: se consulta en vivo.

## Qué NO va aquí
- Gobernanza: solo en `AGENTS.md`.
- Bundles de ejemplo: en `examples/`, etiquetados y nunca referenciados por el núcleo.
