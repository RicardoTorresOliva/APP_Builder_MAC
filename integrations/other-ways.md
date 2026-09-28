---
type: Integration Guide
title: Otras vías de integración
description: SDKs, colas y eventos, iPaaS, CSV/Excel y SQL de mínimo privilegio, y cuándo usar cada una.
tags: [integrations, sdk, ipaas, sql]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
---

# Otras vías de integración

Para cuando no hay MCP oficial (`/integrations/mcp/catalog.md`) ni conviene generar un cliente
propio desde OpenAPI (`/integrations/api/README.md`).

## SDKs oficiales

Usar el SDK del proveedor cuando no publica OpenAPI pero sí mantiene una librería oficial (maneja
auth, reintentos y paginación por ti). Fijar la versión exacta en el lockfile del proyecto; un SDK
sin pin puede introducir un cambio de comportamiento silencioso en la siguiente instalación.

## Colas y eventos

Para desacoplar sistemas o mover alto volumen sin acoplar a la disponibilidad del otro extremo: el
productor publica, el consumidor procesa a su ritmo, con reintentos y una cola de mensajes muertos
(dead-letter) para lo que falla repetidamente. Preferible a un webhook cuando el volumen es alto o
el consumidor necesita reprocesar histórico.

## iPaaS (n8n, Make, Zapier)

Plataformas de integración no-code/low-code: conectan dos sistemas con un flujo visual, sin escribir
un cliente. Útiles para prototipos y equipos sin ingeniería de plataforma dedicada. Riesgo: el flujo
vive fuera del repo del ADS (no versionado junto al código salvo que la plataforma lo permita
exportar) y los datos en tránsito pasan por la infraestructura del iPaaS — evaluar antes de enviar
datos personales o secretos por esa vía (`/integrations/secrets.md`).

## Import/export CSV o Excel

Para migraciones puntuales o intercambios con un sistema sin API. Validar el esquema en el borde
(columnas esperadas, tipos, encoding) antes de cargar — un CSV no tiene contrato como una API
tipada.

## SQL directo

Último recurso: acopla al esquema interno de un sistema de terceros, sin contrato ni versión. Solo
con:

- credenciales de mínimo privilegio, dedicadas a la integración (nunca la credencial de
  administración);
- preferentemente solo lectura, sobre una réplica o vista, no la base de escritura;
- conexión acotada por red (lista de IP permitidas / peering privado), no expuesta a internet.

## Cuándo usar cada una

| Situación | Vía |
|---|---|
| Proveedor sin OpenAPI, con SDK mantenido | SDK oficial |
| Alto volumen, necesito reprocesar histórico | Colas / eventos |
| Prototipo rápido, sin equipo de plataforma | iPaaS |
| Sistema legado sin ninguna API | CSV/Excel o SQL de mínimo privilegio |
| Migración única, no integración continua | CSV/Excel |
