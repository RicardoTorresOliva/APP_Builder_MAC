---
type: Stack Sheet
title: "Caso: aplicaciones en tiempo real"
description: Opciones de stack para chat, notificaciones en vivo, dashboards colaborativos y streaming de eventos.
tags: [stacks, realtime, websockets, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:07:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: supabase-pricing
    resource: https://supabase.com/pricing
    title: Supabase — Pricing
  - id: ably-pricing
    resource: https://ably.com/docs/platform/pricing
    title: Ably — Pricing overview
  - id: pusher-pricing
    resource: https://pusher.com/channels/
    title: Pusher Channels — Pricing
  - id: do-pricing
    resource: https://www.digitalocean.com/pricing/droplets
    title: DigitalOcean — Droplet pricing
  - id: vercel-pricing
    resource: https://vercel.com/docs/plans/hobby
    title: Vercel — Hobby plan
---

# Caso: aplicaciones en tiempo real

## Cuándo aplica (perfil de ADS)

Perfil `software-app` cuyo requisito central es la propagación de eventos en vivo entre clientes
(chat, presencia, notificaciones, colaboración simultánea sobre el mismo documento, dashboards que
se actualizan sin recargar). Se distingue del resto porque el diseño gira en torno a conexiones
persistentes y consistencia eventual, no solo a request/response.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Framework de componentes + cliente realtime del BaaS | Igual + reconexión/backoff y presencia robustos | Igual, sin cambios | Integrado en el portal corporativo existente |
| Backend | Suscripciones a cambios de base de datos del BaaS (Postgres changes) | Servicio dedicado de WebSockets/pub-sub | Servidor WebSocket propio (protocolo pub/sub compatible), autogestionado | Bus de eventos corporativo como backbone (ver `/stacks/legacy.md`) |
| Base de datos | Postgres del BaaS con replicación lógica[^supabase-pricing] | Postgres gestionado + CDC hacia el canal realtime | Postgres autogestionado + Redis pub/sub | Base de datos corporativa existente + CDC hacia el bus |
| Auth | Auth del BaaS con tokens por canal | IdP gestionado + autorización por canal/sala | Auth self-hosted (OIDC) | SSO corporativo |
| Pagos | N/D | N/D salvo medidor de uso si el realtime es el producto | N/D | N/D |
| Deploy/hosting | PaaS gratuito + BaaS[^vercel-pricing] | Contenedores con autoscaling horizontal (las conexiones no comparten estado entre réplicas sin un backplane) | VPS único con Redis[^do-pricing] | Nube corporativa u on-prem, con balanceo consciente de conexiones persistentes |
| LLM / System One | N/D (no aplica salvo resumen de conversación) | Gateway opcional para resumir/moderar mensajes | N/D | Servicio LLM gestionado de la nube corporativa si se necesita moderación |
| Costo aproximado/mes | $0–29 (tiers gratuitos)[^supabase-pricing][^ably-pricing] | $49–500+ según conexiones concurrentes[^ably-pricing][^pusher-pricing] | $6–24 de VPS[^do-pricing] | Variable por contrato; n/d (no-verificado) |
| Curva de aprendizaje | Baja–media | Alta (escalado de conexiones, backpressure) | Alta (operar pub/sub y reconexión propios) | Alta (integrar con el bus corporativo) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar si se esperan miles de conexiones concurrentes o si la latencia tiene un
  SLO estricto — los límites del tier gratuito del BaaS se alcanzan rápido.
- **Pro/escalable**: sobra para una función de "notificación ocasional" que un polling cada pocos
  segundos resolvería más simple y barato.
- **Low-cost/self-hosted**: no usar sin experiencia operando WebSockets a escala (reconexión,
  balanceo con afinidad, backpressure) — es la parte más fácil de subestimar de este caso.
- **Corporativa/legacy**: no usar como arquitectura de un prototipo — montar sobre el bus corporativo
  añade fricción de aprobación y despliegue que un prototipo no necesita.

## Comprar vs construir

Rara vez se "compra" realtime como producto terminado; se compra la **infraestructura de mensajería**
(Ably, Pusher, o el realtime del BaaS) y se construye la lógica de aplicación encima. Construir el
servidor de WebSockets propio desde cero solo se justifica cuando el volumen ya hace más barato
operarlo que pagar por conexión/mensaje, o cuando hay un requisito de residencia de datos que ningún
proveedor gestionado cumple.

## Equivalencias por nube

No hay un bloque "realtime" dedicado en `/stacks/clouds.md`; se compone de cómputo (contenedores o
serverless con conexiones persistentes — nota: no todo serverless soporta WebSockets de larga
duración, verifica el límite de timeout del proveedor), caché/pub-sub (Redis gestionado o
equivalente) y, si el origen de los eventos es una base de datos existente, el bloque de CDC/eventos
de `/stacks/legacy.md`.

## Superficie agéntica y tokens por defecto

- Un agente que participa en un canal realtime (p. ej. un bot de soporte) se audita igual que
  cualquier otro actor: cada mensaje que envía queda registrado con quién lo autorizó.
- Si el LLM resume o modera la conversación, la salida del modelo es un dato más del canal, nunca una
  instrucción para otros agentes que lean el canal.
- **Dashboard de tokens por defecto**: N1 si el LLM es accesorio (resumen ocasional); N2 si la
  moderación o el resumen corren en cada mensaje y el volumen de tokens es significativo.

## Riesgos de lock-in y plan de salida

- **Realtime del BaaS**: protocolo y semántica de canales propios del proveedor. Plan de salida:
  mantener el modelo de eventos (qué evento, qué payload) documentado de forma independiente del SDK,
  para poder reimplementar el transporte sin rediseñar la lógica de la aplicación.
- **Proveedor de mensajería gestionado (Ably/Pusher)**: ambos usan protocolos propios, no
  intercambiables sin cambiar el cliente. Mitigación: aislar el cliente realtime detrás de una
  interfaz propia (`connect`, `subscribe`, `publish`) en el frontend y el backend.
- **Bus corporativo**: alto costo de cambiarlo una vez adoptado por toda la organización, no solo por
  este ADS — coordina cualquier decisión de bus con el equipo de plataforma, no de forma aislada.

[^supabase-pricing]: Supabase — Pricing
[^ably-pricing]: Ably — Pricing overview
[^pusher-pricing]: Pusher Channels — Pricing
[^do-pricing]: DigitalOcean — Droplet pricing
[^vercel-pricing]: Vercel — Hobby plan
