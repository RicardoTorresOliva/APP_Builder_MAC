---
type: Reference
title: Catálogo de stacks
description: Índice de los 14 casos de stack, cómo los usa el comando stack, leyenda de columnas y política de revisión.
tags: [stacks, indice, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:12:00Z }
stale_after: 2026-12-28T00:00:00Z
---

# Catálogo de stacks

Cada caso es una **Stack Sheet**: perfil de ADS al que aplica, cuatro paquetes coherentes de
Frontend+Backend+DB+auth+deploy (y LLM/System One cuando el caso usa IA), cuándo NO usar cada uno,
comprar vs construir, equivalencias por nube y riesgos de lock-in con plan de salida. Los productos
nombrados aquí son sugerencias verificadas a la fecha de revisión, nunca defaults obligatorios — la
elección final es humana (regla 7, sin lock-in en el núcleo).

## Índice de los 14 casos

| Caso | Para qué sirve |
|---|---|
| [Landing/marketing](/stacks/cases/landing-marketing.md) | Sitio de marketing o landing page, foco en velocidad de publicación y SEO |
| [Web app SaaS](/stacks/cases/saas-web-app.md) | Aplicación SaaS multi-tenant con auth y pagos |
| [Dashboard/BI interno](/stacks/cases/internal-dashboard-bi.md) | Panel de datos para uso interno, sobre un data-product existente |
| [E-commerce](/stacks/cases/e-commerce.md) | Tienda en línea, catálogo, checkout y pagos |
| [App móvil](/stacks/cases/mobile-app.md) | Aplicación nativa o multiplataforma para iOS/Android |
| [Desktop](/stacks/cases/desktop-app.md) | Aplicación de escritorio multiplataforma |
| [API/backend puro](/stacks/cases/api-backend.md) | Servicio de backend sin interfaz propia, consumido por otros clientes |
| [ERP/CRM/backoffice](/stacks/cases/erp-crm-backoffice.md) | Sistema interno de gestión; incluye comprar vs construir (Odoo/ERPNext) |
| [Apps con IA (RAG/agentes)](/stacks/cases/ai-app-rag-agents.md) | Aplicación con recuperación aumentada o agentes con herramientas |
| [Tiempo real](/stacks/cases/realtime.md) | Chat, notificaciones en vivo, colaboración simultánea |
| [Automatizaciones/integraciones](/stacks/cases/automation-integrations.md) | Flujos iPaaS que conectan sistemas existentes |
| [CLI/extensiones](/stacks/cases/cli-extensions.md) | Herramienta de línea de comandos o extensión de editor/navegador |
| [Integración sobre legacy corporativo](/stacks/cases/legacy-integration.md) | El ADS es, en sí mismo, una capa de modernización o puente hacia sistemas existentes |
| [Producto de inteligencia/consultoría](/stacks/cases/intelligence-product.md) | Informe argumentado + dataset o dashboard validado, entregados juntos |

Ver también `/stacks/clouds.md` (equivalencias AWS/Azure/GCP/on-prem), `/stacks/llm-providers.md`
(gateway LLM, matriz de capacidades y System One), `/stacks/legacy.md` (patrones de integración con
legacy) y `/stacks/languages.md` (lenguajes dominantes en entornos corporativos).

## Cómo lo usa el comando `stack`

`/stack` (o `abm stack` desde la CLI) hace preguntas simples sobre el ADS que se va a construir
(¿quién lo usa?, ¿qué tan crítico es?, ¿hay un legacy que integrar?, ¿usa IA?, ¿qué nube o restricción
ya existe?), identifica el caso más cercano de este índice, recomienda un paquete (vibe coder, pro,
low-cost o corporativo según las respuestas) y **explica el porqué**: qué señal de las respuestas
llevó a esa recomendación y qué cambiaría la elección. La recomendación es siempre un punto de
partida para decidir en conjunto (human-in-the-loop de stack), nunca una elección automática y final.

## Leyenda de las columnas

| Columna | Significado |
|---|---|
| Recomendada vibe coder | El paquete más rápido de llevar a un prototipo funcionando, priorizando velocidad sobre control fino |
| Pro/escalable | Paquete pensado para crecer en tráfico, equipo y complejidad, con más control operativo |
| Low-cost/self-hosted | Paquete que minimiza costo recurrente operando la infraestructura propia, a cambio de más trabajo operativo |
| Corporativa/legacy | Paquete que asume restricciones corporativas ya existentes (IdP, nube, cumplimiento, sistemas heredados) |
| Frontend / Backend / Base de datos / Auth / Pagos / Deploy | La pieza de esa capa en ese paquete; "Pagos" y "LLM/System One" solo aparecen cuando el caso los usa |
| Costo aproximado/mes | Estimado con fuente y fecha citada al pie; "n/d (no-verificado)" cuando no se pudo confirmar un precio concreto |
| Curva de aprendizaje | Esfuerzo relativo para un equipo que no conoce ya ese paquete |

## Política de revisión (`stale_after`)

Cada ficha de este catálogo lleva `stale_after` en su frontmatter (fecha ISO UTC, ~3 meses desde su
última revisión) y una lista `sources` con la URL y fecha de cada precio o versión citada. Pasada esa
fecha, `abm okf validate` marca el archivo como contenido caducado (aviso, o bloqueante si el tipo
está en `okf.critical_stale_types`). Revisar una ficha caducada significa: volver a verificar cada
precio/versión citado con WebSearch o Firecrawl, actualizar las notas al pie y `sources`, y mover
`stale_after` otros ~3 meses. Nunca se extiende `stale_after` sin volver a verificar el contenido.
