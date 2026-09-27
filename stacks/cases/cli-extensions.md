---
type: Stack Sheet
title: "Caso: CLI y extensiones"
description: Opciones de stack para herramientas de línea de comandos y extensiones de editor/navegador, con foco en distribución y portabilidad de runtime.
tags: [stacks, cli, extensiones, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:09:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: node-releases
    resource: https://nodejs.org/en/about/previous-releases
    title: Node.js — Releases
  - id: go-releases
    resource: https://go.dev/doc/devel/release
    title: Go — Release History
  - id: python-downloads
    resource: https://www.python.org/downloads/
    title: Python — Downloads
---

# Caso: CLI y extensiones

## Cuándo aplica (perfil de ADS)

Perfil `software-app` cuyo entregable no es una app web sino un binario/paquete que el usuario instala
localmente: una herramienta de línea de comandos, una extensión de editor (VS Code y similares) o de
navegador. El "frontend" es la interfaz de terminal o el panel de la extensión; no hay backend propio
salvo que la herramienta llame a una API externa.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend (interfaz) | CLI con framework de línea de comandos sobre Node.js[^node-releases] | Igual, con salida `--json` y códigos de salida estables para uso por agentes | Igual, sin cambios | Igual + empaquetado firmado para distribución interna |
| Backend (runtime) | Node.js 24 LTS[^node-releases] o Python 3.14[^python-downloads] | Go 1.27, binario estático sin dependencia de runtime instalado[^go-releases] | Igual que pro/escalable (Go no añade costo) | Lenguaje ya estándar en la empresa (Java/.NET/Go) por facilidad de firma y despliegue interno |
| Base de datos / estado | Archivo de configuración local (JSON/TOML) | Igual + caché local con invalidación explícita | Igual, sin cambios | Configuración centralizada distribuida por la plataforma interna |
| Auth | API key de usuario en variable de entorno o archivo de config | OAuth device flow contra el proveedor que consume | Igual que pro/escalable | SSO corporativo vía token de servicio de corta duración |
| Pagos | N/D | N/D salvo telemetría de uso para licenciamiento | N/D | N/D |
| Deploy/hosting (distribución) | Registro público del lenguaje (npm/PyPI), gratis | Igual + binarios firmados en GitHub Releases | Igual, sin costo adicional | Registro de paquetes interno (mínimo privilegio, sin salida a internet) |
| LLM / System One | N/D salvo que la CLI sea "asistida por IA" (usar el gateway LLM estándar) | Gateway LLM con modelo económico para tareas puntuales | Modelo local vía Ollama si la CLI debe funcionar sin red | Servicio LLM gestionado de la nube corporativa |
| Costo aproximado/mes | $0 (publicación en npm/PyPI es gratuita) | $0 de licencia; costo de CI para builds multiplataforma | $0 | Variable por infraestructura de registro interno; n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media (builds multiplataforma, firma de binarios) | Baja–media | Alta (integración con el registro y la política interna) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar Node.js/Python si el público objetivo espera un binario único sin runtime
  instalado (por ejemplo, herramientas de infraestructura o DevOps que corren en entornos mínimos).
- **Pro/escalable**: sobra compilar a binario estático si la herramienta ya asume un entorno con
  Node.js/Python disponible (p. ej. un plugin de un ecosistema que ya lo requiere).
- **Low-cost/self-hosted**: no aplica una restricción real aquí — la distribución pública es gratis por
  defecto; esta columna solo importa cuando se añade CI propio.
- **Corporativa/legacy**: no usar un registro interno para una herramienta de uso público — añade
  fricción sin beneficio si no hay requisito de confidencialidad o cumplimiento.

## Comprar vs construir

No aplica un "comprar" equivalente a un producto empaquetado: una CLI o extensión es, casi siempre,
la forma más barata de resolver el problema (más barata que una app con interfaz web completa) y se
construye directamente. La pregunta relevante es de **alcance**: extender una CLI/extensión existente
del ecosistema (un plugin) frente a publicar una herramienta nueva independiente — extiende cuando el
ecosistema objetivo ya tiene una convención de plugins madura; publica independiente cuando el flujo
no encaja en ningún host existente.

## Equivalencias por nube

No aplica una matriz de nube para el runtime de la CLI en sí (corre en la máquina del usuario). Si la
CLI llama a un backend propio, ese backend sigue la matriz general de `/stacks/clouds.md`
(cómputo serverless para una API ligera es el patrón más común).

## Superficie agéntica y tokens por defecto

Este es el caso donde la superficie agéntica es la funcionalidad misma: una CLI bien diseñada para
agentes es una CLI bien diseñada para humanos, con `--json` en toda salida, `--dry-run` en toda
operación que cambia estado, y códigos de salida estables y documentados. Si la CLI expone un
servidor MCP propio, aplican las mismas reglas de mínimo privilegio y auditoría que cualquier otro
ADS con superficie agéntica (ver §4.8 del prompt maestro). **Dashboard de tokens por defecto**: N1
únicamente si la CLI integra un LLM; si no usa IA, no aplica ledger de tokens.

## Riesgos de lock-in y plan de salida

- **Framework de CLI elegido**: bajo riesgo — la lógica de negocio de los comandos es portable; solo
  el parsing de argumentos y el help text dependen del framework, y reescribir esa capa es barato.
- **Registro de paquetes**: si se depende de features propietarias de un registro privado (por
  ejemplo, un proxy con caché específico), documentar el equivalente en un registro estándar
  (npm/PyPI/crates.io privado) como plan de salida.
- **API externa que la CLI consume**: si la CLI es un cliente delgado de una sola API propietaria, el
  lock-in es del servicio que envuelve, no de la CLI — documentarlo en el `ads.yaml` de ese servicio,
  no aquí.

[^node-releases]: Node.js — Releases
[^go-releases]: Go — Release History
[^python-downloads]: Python — Downloads
