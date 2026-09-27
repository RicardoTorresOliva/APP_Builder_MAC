---
type: Stack Sheet
title: "Caso: automatizaciones e integraciones"
description: Opciones de stack para flujos de automatización e iPaaS, de un flujo simple en n8n/Zapier a integración corporativa.
tags: [stacks, automatizacion, ipaas, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:08:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: n8n-pricing
    resource: https://n8n.io/pricing/
    title: n8n — Pricing
  - id: zapier-pricing
    resource: https://zapier.com/pricing
    title: Zapier — Pricing
  - id: make-pricing
    resource: https://www.make.com/en/pricing
    title: Make — Pricing
  - id: do-pricing
    resource: https://www.digitalocean.com/pricing/droplets
    title: DigitalOcean — Droplet pricing
---

# Caso: automatizaciones e integraciones

## Cuándo aplica (perfil de ADS)

Perfil `software-app` cuyo entregable es un flujo (o conjunto de flujos) que conecta sistemas ya
existentes — SaaS entre sí, o SaaS con un sistema interno — sin ser en sí mismo una aplicación con
interfaz propia para usuarios finales. Ceremonia Prototipo/MVP cuando el flujo es interno y de bajo
riesgo; sube de nivel si mueve dinero, datos personales o decisiones que antes tomaba una persona.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Ninguno (editor visual de la herramienta de automatización) | Ninguno + panel de estado propio si hace falta visibilidad | Ninguno (editor visual self-hosted) | Consola de la plataforma de integración corporativa |
| Backend | Motor de automatización low-code gestionado (n8n Cloud, Zapier o Make)[^n8n-pricing][^zapier-pricing][^make-pricing] | Igual, en plan de equipo, más un microservicio propio para lógica que el low-code no cubre bien | n8n self-hosted (open source, mismo motor, sin costo de licencia)[^n8n-pricing] | Plataforma de integración corporativa (ESB/iPaaS empresarial) u orquestador propio en la nube ya operada |
| Base de datos | La del motor (mínima, solo estado de ejecución) | Base de datos propia para lógica/estado de negocio del flujo | Postgres autogestionado junto al motor self-hosted | Base de datos corporativa existente |
| Auth | Credenciales OAuth de cada sistema conectado, gestionadas por la herramienta | Igual + secretos en un gestor dedicado | Igual + gestor de secretos propio (self-hosted) | SSO corporativo para el acceso a la consola; credenciales de servicio de mínimo privilegio para cada sistema |
| Pagos | N/D | N/D salvo que el flujo procese pagos (usar el proveedor de pagos, no el motor de automatización, para eso) | N/D | N/D |
| Deploy/hosting | SaaS del motor (sin infraestructura propia) | SaaS del motor en plan de equipo | VPS propio para el motor self-hosted[^do-pricing] | Nube corporativa u on-prem |
| LLM / System One | Nodo de IA del propio motor (opcional, para clasificar/redactar) | Gateway LLM propio conectado al flujo vía nodo HTTP | Modelo local vía Ollama si el flujo no puede salir a internet | Servicio LLM gestionado de la nube corporativa |
| Costo aproximado/mes | $0–24 (planes de entrada)[^n8n-pricing][^zapier-pricing][^make-pricing] | $50–300+ según tareas/ejecuciones[^zapier-pricing][^make-pricing] | $6–24 de VPS, sin costo de licencia[^do-pricing] | Variable por contrato; n/d (no-verificado) |
| Curva de aprendizaje | Baja | Media | Media (operar el motor self-hosted) | Alta (plataforma corporativa + gobernanza) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar cuando el flujo debe correr con SLA garantizado o cuando el volumen supera
  el tope de ejecuciones del plan de entrada de forma constante (el costo por tarea excedente crece
  rápido).
- **Pro/escalable**: sobra para un flujo interno de bajo riesgo y volumen bajo; el costo mensual de un
  plan de equipo no se justifica.
- **Low-cost/self-hosted**: no usar si el equipo no puede parchear y respaldar el motor self-hosted, o
  si se necesita soporte comercial con SLA.
- **Corporativa/legacy**: no usar como punto de partida de una automatización simple y de bajo riesgo
  — el costo y tiempo de aprobación de una plataforma corporativa es desproporcionado.

## Comprar vs construir

Para la mayoría de integraciones entre SaaS, **comprar el motor de automatización siempre gana**
frente a escribir el conector a mano: n8n, Zapier o Make ya resuelven autenticación OAuth, reintentos
y manejo de errores por ti. Construir a medida (un microservicio propio) se justifica solo cuando: la
lógica de negocio es demasiado compleja para un editor visual, el volumen hace que el costo por
tarea/operación del SaaS supere el costo de operar infraestructura propia, o el flujo necesita vivir
detrás de un firewall sin salida a internet.

## Equivalencias por nube

No hay bloque dedicado en `/stacks/clouds.md`; la infraestructura relevante es cómputo (contenedores
para el motor self-hosted), colas/eventos si el flujo se dispara por eventos en vez de por
programación, y secretos (gestor de secretos de la nube o de la herramienta) para las credenciales de
cada sistema conectado.

## Superficie agéntica y tokens por defecto

- Cada flujo es, en esencia, un agente determinista con pasos fijos; cuando incorpora un nodo de LLM,
  ese nodo hereda las mismas reglas que cualquier otro uso de LLM en ABM: la salida del LLM es un dato
  para el siguiente paso, nunca una instrucción que se ejecuta sin validar.
- HITL obligatorio antes de una acción roja disparada por el flujo (enviar dinero, borrar datos,
  notificar externamente a gran escala).
- **Dashboard de tokens por defecto**: N1, salvo que el flujo use un nodo de LLM en cada ejecución con
  volumen alto, en cuyo caso sube a N2.

## Riesgos de lock-in y plan de salida

- **Motor de automatización SaaS**: los flujos se definen en el formato propietario de la herramienta
  y no migran 1:1 a otra. Mitigación: documentar cada flujo en lenguaje simple (qué dispara, qué hace,
  qué sistemas toca) independiente de la herramienta, para poder reconstruirlo en otra si hace falta.
- **n8n self-hosted** reduce este riesgo porque el mismo motor corre gestionado o self-hosted — migrar
  de n8n Cloud a n8n self-hosted es un cambio de despliegue, no de flujos.
- **Plataforma de integración corporativa**: alto costo de salida una vez que muchos flujos de la
  organización dependen de ella; cualquier cambio se coordina a nivel de plataforma, no de este ADS.

[^n8n-pricing]: n8n — Pricing
[^zapier-pricing]: Zapier — Pricing
[^make-pricing]: Make — Pricing
[^do-pricing]: DigitalOcean — Droplet pricing
