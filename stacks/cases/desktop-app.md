---
type: Stack Sheet
title: "Caso: App de escritorio"
description: Paquetes desktop (Tauri/Electron) con backend opcional de sincronización y equivalencias por nube.
tags: [stacks, desktop, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:30:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: tauri-releases
    resource: https://tauri.app/release/core/
    title: Tauri — Core releases
  - id: electron-timeline
    resource: https://www.electronjs.org/docs/latest/tutorial/electron-timelines
    title: Electron — Release timelines
  - id: flyio-pricing
    resource: https://fly.io/docs/about/pricing/
    title: Fly.io — Resource pricing
  - id: apple-dev-fee
    resource: https://developer.apple.com/programs/
    title: Apple Developer Program
  - id: coolify
    resource: https://coolify.io/self-hosted
    title: Coolify — Self-hosted
---

# Caso: App de escritorio

## Cuándo aplica

Aplicación instalable en Windows/macOS/Linux, con datos locales y sincronización opcional entre
dispositivos. Perfil de ADS: **software-app**.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend | Tauri 2 (WebView del sistema) + React/Vue [^tauri-releases] | Electron (Chromium embebido, ecosistema maduro) + React [^electron-timeline] | Tauri 2 + React/Vue (mismo shell, sin backend en la nube) [^tauri-releases] | Electron o .NET/WPF empaquetado según estándar interno |
| Backend | Embebido en el binario (SQLite local) | Backend compartido en la nube (Node/Postgres) para sincronizar | Ninguno, o backend propio mínimo autoalojado | Backend on-prem existente de la empresa |
| Base de datos | SQLite local | Postgres gestionado (compartido con la web app si existe) | SQLite local (sin sync) o Postgres self-hosted si hay sync | SQL Server/Oracle corporativo |
| Auth | Ninguna (app local) o cuenta ligera si sincroniza | Auth del backend compartido (Clerk/Auth0) | Ninguna, o Keycloak self-hosted si hay sync | SSO corporativo integrado al instalador (MDM) |
| Pagos | No aplica (o licencia one-time vía la pasarela ya elegida) | Igual, con suscripción vía Stripe si el backend la gestiona | Igual que vibe coder | Licenciamiento interno, sin pasarela pública |
| Deploy/hosting | Distribución directa (GitHub Releases) o Microsoft Store/Mac App Store | Backend en Fly.io/Render [^flyio-pricing] + auto-update vía electron-updater firmado | Distribución directa (GitHub Releases), sin backend en la nube | MDM corporativo (Intune/SCCM), sin tiendas públicas |
| LLM/System One | Opcional: asistente local o remoto vía gateway LLM (ver `/stacks/llm-providers.md`) | Igual, con medición de tokens si el uso es remoto | Igual, modelo local si se prioriza privacidad | Gateway LLM corporativo ya aprobado |
| Costo aprox./mes (2026-09) | US$0 (Tauri es MIT/Apache-2.0) [^tauri-releases]; US$99/año si se distribuye por Mac App Store [^apple-dev-fee]; certificado de firma Windows: n/d (no-verificado) | US$0 (Electron MIT) [^electron-timeline] + US$5–29/mes backend (Fly.io Launch/Scale) [^flyio-pricing] | US$0 (sin backend en la nube); GitHub Releases gratis para hospedar binarios | Variable, ya contratado por TI; n/d (no-verificado) |
| Curva de aprendizaje | Media (Rust en el core, aunque no se toque a diario) | Baja (ecosistema Node/Chromium conocido) | Media | Alta |

## Cuándo NO usar cada opción

- **Tauri:** no usar si dependés de APIs de Chromium muy específicas o de librerías nativas de Node
  sin puerto a Rust/WebView del sistema.
- **Electron:** no usar si el tamaño del instalador y el consumo de RAM son críticos (hardware
  limitado) — Tauri es sensiblemente más liviano.
- **Low-cost/self-hosted (sin sync):** no usar si el producto exige colaboración multi-dispositivo en
  tiempo real desde el lanzamiento.
- **Corporativa (MDM):** no usar para un producto de consumo masivo fuera de la organización.

## Comprar vs construir

El runtime desktop (Tauri/Electron) siempre se "compra" (se adopta open-source); lo que se construye
es la lógica de negocio y, si existe, la capa de sincronización entre dispositivos.

## Equivalencias por nube

Aplican solo si hay backend de sincronización; la app local en sí no depende de una nube.

| Bloque | AWS | Azure | GCP | On-prem |
|---|---|---|---|---|
| Compute del backend de sync | Fargate/Lambda | Container Apps/Functions | Cloud Run | Kubernetes propio |
| Base de datos | RDS/Aurora Postgres | Database for PostgreSQL | Cloud SQL Postgres | Postgres en VM |
| Distribución de binarios | S3+CloudFront | Blob Storage+Front Door | Cloud Storage+CDN | Servidor de artefactos interno |
| Auto-update | Endpoint HTTPS propio (Tauri updater/electron-updater apuntan a cualquier host) | Igual | Igual | Igual |

## Superficie agéntica y tokens por defecto

Nivel **mínimo** si es una app 100% local sin API; **extendido** si sincroniza con un backend propio
(API+MCP). Dashboard de tokens **N1**, **N2** si usa un LLM remoto. Si expone datos a un agente, lo
hace vía el backend de sincronización, nunca leyendo el almacenamiento local del dispositivo
directamente.

## Riesgos de lock-in y plan de salida

- **Tauri/Electron:** riesgo bajo — ambos son open-source; la UI (React/Vue) es portable entre uno y
  otro con una capa de abstracción fina del "shell" nativo (APIs de archivo, notificaciones).
- **Microsoft Store/Mac App Store:** riesgo medio por reglas de revisión y comisión en compras
  dentro de la app; plan de salida: mantener también distribución directa fuera de tienda.
- **Backend de sincronización (si existe):** mismos riesgos que el caso SaaS web app (ver
  `/stacks/cases/saas-web-app.md` y `/docs/adr/0012-portabilidad.md`).

[^tauri-releases]: Tauri — Core releases
[^electron-timeline]: Electron — Release timelines
[^flyio-pricing]: Fly.io — Resource pricing
[^apple-dev-fee]: Apple Developer Program
