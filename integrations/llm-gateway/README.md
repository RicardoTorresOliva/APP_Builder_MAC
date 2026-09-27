---
type: Integration Guide
title: Gateway LLM — categoría
description: Interfaz de chat compatible como lingua franca, variables de configuración y evals mínimos para cambiar de proveedor.
tags: [llm, gateway, integrations, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: litellm-repo
    resource: https://github.com/BerriAI/litellm
    title: "LiteLLM: open source AI Gateway (MIT core, self-hosted)"
  - id: litellm-vs-openrouter
    resource: https://api7.ai/openrouter-vs-litellm
    title: "OpenRouter vs LiteLLM (2026): Hosted vs Self-Hosted"
---

# Gateway LLM — categoría

Capa de abstracción entre ABM/los ADS y "un proveedor de LLM cualquiera", para poder cambiar de
proveedor por configuración, no por código (§4.10 del prompt maestro, portabilidad multi-LLM).

## Interfaz: chat compatible como lingua franca

La interfaz mínima común es la de chat completions con mensajes `{role, content}` y streaming
opcional — el formato que la mayoría de gateways y proveedores ya hablan. ABM no define un formato
propio: cualquier endpoint que hable esa interfaz sirve como backend del fallback `llm`.

## Variables de entorno

El fallback `llm` de `decide()` (`/integrations/decision/README.md`) y cualquier ADS que necesite un
LLM genérico leen:

| Variable | Qué es |
|---|---|
| `ABM_LLM_BASE_URL` | URL base del endpoint compatible |
| `ABM_LLM_API_KEY` | Credencial del proveedor o gateway |
| `ABM_LLM_MODEL` | Identificador del modelo a usar |

Cambiar de proveedor es cambiar estas tres variables — nunca una ruta de código distinta por
proveedor.

## Opciones (categoría, con licencia/hosting)

| Tipo | Ejemplo verificado | Licencia / hosting |
|---|---|---|
| Proveedores directos | API propia de cada proveedor de modelos frontera | SaaS, propietario |
| LLM gestionado por nube | Servicio de IA generativa de AWS/Azure/GCP | SaaS, dentro del perímetro de nube contratado |
| Gateway multi-proveedor autoalojado | LiteLLM — proxy OSS para 100+ proveedores tras una interfaz OpenAI-compatible[^litellm-repo] | Núcleo MIT, autoalojable (Docker/Kubernetes); nivel Enterprise de pago para SSO/auditoría[^litellm-vs-openrouter] |
| Gateway multi-proveedor gestionado | Marketplace SaaS de enrutamiento multi-LLM con una sola clave[^litellm-vs-openrouter] | SaaS únicamente, sin autoalojado |
| Modelos abiertos/locales | Runtime de inferencia local para modelos con pesos abiertos | Open-source, autoalojable, sin llamada externa |

## Cambio de proveedor por configuración

Un ADS declara su proveedor activo en su propia config (no en código); el gateway/proxy traduce la
interfaz de chat estándar a las particularidades del proveedor real. Migrar de proveedor implica:
apuntar las tres variables a otro backend, correr los evals mínimos (abajo) y desplegar — sin tocar
lógica de negocio.

## Evals mínimos antes de cambiar de modelo

Un cambio de proveedor o de modelo no se despliega sin un set mínimo de evals de regresión: salida
estructurada (el JSON Schema sigue validando), casos límite conocidos del dominio del ADS, y
latencia/costo dentro del presupuesto (`/integrations/observability/README.md`). Sin esto, "cambié
de modelo para ahorrar" es un experimento no controlado en producción.

[^litellm-repo]: LiteLLM: open source AI Gateway (MIT core, self-hosted)
[^litellm-vs-openrouter]: OpenRouter vs LiteLLM (2026): Hosted vs Self-Hosted
