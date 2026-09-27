---
type: Standard
title: Protocolo de comunicación del agente
description: Cómo informa un agente que construye u opera un ADS — semáforo, formato de reporte y ejemplos.
tags: [comunicacion, protocolo-de-salida, adr-0015]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
---

# Protocolo de comunicación del agente

Desarrolla AGENTS.md §Protocolo de salida y ADR 0015. Aplica a todo agente que construye u opera un
ADS. En operación, los agentes del ADS heredan esta brevedad salvo que el brief del caso de uso pida
otro tono (p. ej. atención al cliente); esa decisión queda registrada, no se asume.

## Semáforo por acción

| Semáforo | Significa | Formato |
|---|---|---|
| `[verde]` | reversible, dentro del alcance, sin ambigüedad | sin anuncio previo; aparece en el reporte agrupado |
| `[amarillo]` | reversible pero con impacto visible | una línea antes: qué, por qué, cómo se deshace |
| `[rojo]` | bloqueante (AGENTS.md §Bloqueantes) | máximo tres líneas: qué, riesgo, qué necesita del humano, con la opción recomendada |

## Formato de reporte (≤ 12 líneas, al cerrar unidad o fase)

```text
[<fase|FU|DU|WU>-<id>] HECHO | BLOQUEADO
Acciones: <una línea por acción, con archivo o commit>
Verificado: <check → resultado>
No verificado: <ítem → motivo>
Pendientes: <+n nuevos; total n>
Tokens: <consumo; fuente o "estimado">
Siguiente: <acción concreta>
```

## Ejemplos

**Amarillo — bien:**
> [amarillo] Voy a truncar la tabla `sesiones_temp` (solo datos de prueba, se regenera en el próximo
> seed) para poder migrar el índice. Reversible: `abm db seed`.

**Amarillo — mal (conversacional, sin la información que importa):**
> ¡Perfecto! Voy a hacer un pequeño cambio en la base de datos, no debería haber problema. ¿Te parece
> bien si continúo?

**Reporte — bien:**

```text
[WU3-api-pedidos] HECHO
Acciones: backend/pedidos/router.md, backend/pedidos/schema.json
Verificado: tests contrato → OK; okf validate → 0 errores
No verificado: carga a 1k rps → sin entorno de staging
Pendientes: +1 (P-014, definir SLO de latencia); total 4
Tokens: 12 400 (medido, ledger)
Siguiente: `review` sobre este DU
```

**Reporte — mal (relleno, sin evidencia, excede el largo):**
> ¡Listo! Terminé la unidad de pedidos, todo funciona genial y quedó muy prolijo. Hice varios
> archivos, corrí algunos tests y creo que todo está bien, aunque no llegué a probar absolutamente
> todo así que capaz conviene revisar con calma en algún momento. Cualquier cosa avisame y lo vemos
> juntos. ¡Gracias por la paciencia!

**Bloqueante — bien:**
> [rojo] La unidad pide publicar el paquete en el registro público. Riesgo: acción irreversible fuera
> de la rama. Necesito: confirmación explícita para publicar, o que quede en `pending` hasta el release.
> Recomiendo: dejarlo en `pending` y publicar junto al release.

## Frases prohibidas

Saludos ("¡Hola!", "¡Claro!"), elogios de relleno ("excelente pregunta"), disculpas sin causa
("disculpa las molestias"), repetir la instrucción recibida, anunciar sin ejecutar ("voy a
proceder a..." sin luego hacerlo en el mismo turno), preguntas retóricas, resúmenes duplicados del
mismo reporte, emojis decorativos, cierres de cortesía ("¡Que tengas un buen día!").

## Verificación mecánica

`abm lint playbooks` exige, en cada `commands/*.md`: las secciones del playbook, un semáforo en cada
paso numerado, y una plantilla de reporte en bloque de código de ≤ 12 líneas.
