---
type: Guide
title: Modo turbo y cola de pendientes
description: Qué es turbo frente a checkpoint, los bloqueantes, la cola de pendientes, el semáforo de riesgo, y cómo activar turbo en cada herramienta.
tags: [manual, turbo, pendientes]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:01:00Z }
stale_after: 2027-01-15T00:00:00Z
sources:
  - id: compat-matrix
    resource: docs/compat-matrix.md
    title: Matriz de compatibilidad multi-herramienta
  - id: tools-yaml
    resource: adapters/tools.yaml
    title: Herramientas y plantillas turbo de abm sync
---

# Modo turbo y cola de pendientes

## Turbo vs. checkpoint

ABM trabaja en uno de dos modos:

- **Turbo (el modo por defecto):** el agente avanza solo en todo lo que es reversible, sin pedirte
  permiso paso a paso. Cuando algo queda por decidir pero no es urgente, aplica una opción por
  defecto razonable y lo anota en una cola para que lo revises cuando quieras — así no te interrumpe
  todo el tiempo.
- **Checkpoint:** como turbo, pero el plan necesita tu aprobación explícita antes de que se empiece
  a construir. Se usa en proyectos con ceremonia muy formal (por ejemplo, "enterprise-regulado") o
  cuando vos lo pedís.

En ambos modos, hay seis situaciones que **siempre** detienen el trabajo, sin importar el modo —
los "bloqueantes":

1. Una acción destructiva o que no se puede deshacer, fuera de la rama de trabajo (borrar datos,
   reescribir el historial de otra persona).
2. Publicar algo, cobrar dinero real, o enviar información a un tercero.
3. Falta una credencial (contraseña, llave de acceso) y no hay forma de seguir sin ella.
4. Un cambio de permisos o de seguridad que afecta algo fuera del repositorio.
5. Una duda donde equivocarse sería caro o imposible de deshacer.
6. Se superó el tope máximo (duro) de tokens.

Ante cualquiera de estas seis, el agente se detiene con un mensaje corto: qué pasó, qué riesgo hay,
y qué necesita de vos.

## El semáforo de cada acción

Cada acción que hace el agente tiene un color:

| Semáforo | Significa | Cómo te enteras |
|---|---|---|
| 🟢 Verde | Reversible y sin ambigüedad | No te avisa antes; aparece resumida en el reporte al cerrar la tarea |
| 🟡 Amarillo | Reversible, pero con un efecto visible | Te avisa en una línea antes: qué va a hacer, por qué, y cómo se deshace |
| 🔴 Rojo | Bloqueante (una de las seis situaciones de arriba) | Se detiene y te pregunta, en tres líneas como máximo |

## La cola de pendientes

Todo lo que en turbo se resolvió con una opción por defecto (en vez de preguntarte al momento) se
anota en `docs/_work/PENDIENTES.md`. Cada fila tiene: un ID, el tipo (decisión, aprobación,
credencial, revisión, o propuesta de algo que no pediste), el contexto en una línea, la opción que
ya se aplicó, la alternativa, y qué pasa si no respondés. Vos lo revisás cuando quieras, todo junto,
en vez de que te interrumpan uno por uno:

```text
/pending list                                    # ver la cola
/pending resolve P-003 --answer "tu respuesta"   # responder un ítem
```

Si algo que "parece útil" no formaba parte de lo que pediste, tampoco se construye solo: entra a
esta misma cola como propuesta, para que decidas si vale la pena.

## Cómo activar turbo en cada herramienta

`./abm sync --apply-turbo` instala una plantilla de permisos lista para usar en las herramientas que
guardan esa configuración dentro del repositorio:

| Herramienta | Dónde queda la configuración |
|---|---|
| Claude Code | `.claude/settings.json` (lectura y comandos seguros se aprueban solos; lo destructivo, de producción, pagos o red externa siempre pide confirmación) |
| Codex | `.codex/config.toml` (política de aprobación y modo de sandbox) |
| Gemini CLI | `.gemini/settings.json` (modo de aprobación por defecto) |
| VS Code + Copilot | `.vscode/settings.json` (lista de comandos de terminal aprobados) |
| Cursor | Se configura dentro de la app (Settings → Agents → Approvals & Execution); no es un archivo del repositorio |
| Windsurf / Devin Desktop | Se configura dentro de la app (nivel "Turbo" de auto-ejecución en la terminal) |
| Antigravity | Se configura dentro de la app |
| Kiro | A nivel de tu usuario: `~/.kiro/settings/permissions.yaml`; hay un ejemplo listo en `adapters/turbo/kiro/` para copiar |
| Hermes | A nivel de tu usuario: `~/.hermes/config.yaml` → `approvals.mode`; hay un ejemplo listo en `adapters/turbo/hermes/` para copiar |

En todos los casos, lo destructivo, la publicación a producción, los pagos y el acceso a secretos
siguen pidiendo confirmación siempre — turbo acelera lo reversible, nunca salta un bloqueante.
