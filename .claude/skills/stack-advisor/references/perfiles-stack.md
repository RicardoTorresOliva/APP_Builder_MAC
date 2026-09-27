---
type: Reference
title: Criterios de los cuatro perfiles de stack
description: Señales para decidir qué perfil de stacks/ (vibe coder, pro, low-cost, corporativo) calza con un proyecto, en categorías, sin nombrar productos.
tags: [referencia, stack, catalogo]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Criterios por perfil de stack

Ninguna fila nombra un producto: eso vive en el `stacks/<caso>.md` correspondiente, que sí puede
hacerlo (regla 7: los productos solo en `stacks/`, `integrations/`, `examples/` y `docs/`).

| Señal del proyecto | vibe coder | pro | low-cost | corporativo |
|---|---|---|---|---|
| Horizonte | prototipo/demo | producto en evolución | proyecto personal/side | regulado/empresa |
| Presupuesto mensual tolerado | alto por hora ahorrada | medio, con retorno claro | mínimo o gratuito | ya asignado, no es el filtro principal |
| Curva de aprendizaje aceptable | ninguna, todo generado/gestionado | media, el equipo ya la domina o la puede absorber | baja, un solo mantenedor | la que exija el proveedor homologado |
| Prioridad de gobernanza/cumplimiento | ninguna | según el dominio | ninguna | máxima, no negociable |
| Tolerancia a lock-in del proveedor | alta, se puede migrar después | media, se documenta el plan de salida | alta, sensible sobre todo al costo | baja, ya viene fijado por la organización |
| Observabilidad exigida | mínima | completa desde el día uno | básica | la que exija el proveedor homologado |

## Cómo usarlo

1. Puntúa el proyecto en cada fila (una marca por columna que más calce).
2. La columna con más marcas es el perfil candidato; si hay empate entre dos, presenta ambos
   `stacks/<caso>.md` al humano en vez de decidir por él.
3. Un proyecto corporativo con presupuesto ajustado no es automáticamente "low-cost": la fila de
   gobernanza pesa más que la de presupuesto en ese perfil — sigue siendo corporativo.

## Portabilidad (ADR 0012)

Todo perfil, incluido vibe coder, documenta un plan de salida del proveedor elegido antes de
entregar, aunque sea breve. La ausencia de plan de salida es más grave en corporativo (puede ser
bloqueante e) que en vibe coder (se anota como pendiente).
