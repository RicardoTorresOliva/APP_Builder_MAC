---
type: Integration Guide
title: Gestión de secretos
description: .env.example, gestor de secretos por plataforma, secret scanning en CI y rotación.
tags: [secretos, seguridad, integrations]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:36:27Z }
stale_after: 2026-12-28T00:00:00Z
---

# Gestión de secretos

## `.env.example`

Todo ADS versiona un `.env.example` con cada variable de entorno que necesita (nombre + comentario
de qué es), nunca con un valor real. `.env` real está en `.gitignore` desde el primer commit del
repo, no añadido después.

## Gestor de secretos por plataforma

Categoría, con ejemplos verificados por nube/plataforma: AWS Secrets Manager / Parameter Store,
Azure Key Vault, Google Cloud Secret Manager, y gestores multi-nube (p. ej. HashiCorp Vault) para
despliegues on-prem o multi-nube. El ADS lee el secreto en tiempo de arranque desde el gestor de la
plataforma de destino — nunca lo hornea en la imagen de contenedor ni lo deja en variables de CI
persistentes sin cifrar.

## Secret scanning en CI

El pipeline de CI corre un escáner de secretos (categoría; ejemplos: `gitleaks`, `trufflehog`, o el
secret scanning nativo de la plataforma Git) en cada push y sobre el historial completo antes del
primer push del repo. Un hallazgo bloquea el merge — no es un warning ignorable.

## Nunca credenciales de producción al alcance del agente

Un agente que construye o depura un ADS no recibe secretos de producción, ni siquiera de solo
lectura: usa credenciales de entorno de desarrollo/staging con datos sintéticos o anonimizados. Si
una tarea exige de verdad tocar producción (ADR 0014, bloqueante b), es un punto de HITL explícito,
nunca un secreto en el contexto del agente por defecto.

## Rotación

Todo secreto tiene un dueño y una fecha de rotación (política mínima: rotación forzada ante sospecha
de exposición, rotación programada según la sensibilidad). Un secreto que un escáner marcó como
expuesto se rota de inmediato, no solo se borra del repo — el valor ya circuló y no se puede
"des-exponer".

## Checklist

- [ ] `.env.example` versionado, `.env` ignorado desde el primer commit
- [ ] Secretos de producción fuera del entorno del agente
- [ ] Secret scanning activo en CI, bloqueante
- [ ] Rotación documentada por secreto, con dueño
