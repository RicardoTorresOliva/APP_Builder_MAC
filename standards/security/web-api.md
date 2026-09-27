---
type: Standard
title: Seguridad web y de API
description: OWASP Top 10 y OWASP ASVS aplicados al frontend y al backend de un ADS.
tags: [seguridad, owasp, web, api]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T02:00:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - { id: owasp-top10, resource: "https://owasp.org/Top10/2025/", title: "OWASP Top 10:2025" }
  - { id: owasp-asvs, resource: "https://owasp.org/www-project-application-security-verification-standard/", title: "OWASP Application Security Verification Standard (ASVS) 5.0" }
---

# Seguridad web y de API

## OWASP Top 10 (web)[^owasp-top10]
Vigente: **OWASP Top 10:2025** (sucesora de la edición 2021). Toda superficie web o de API se revisa
contra sus diez categorías antes de un release:

| # | Categoría |
|---|---|
| A01:2025 | Broken Access Control |
| A02:2025 | Security Misconfiguration |
| A03:2025 | Software Supply Chain Failures |
| A04:2025 | Cryptographic Failures |
| A05:2025 | Injection |
| A06:2025 | Insecure Design |
| A07:2025 | Authentication Failures |
| A08:2025 | Software or Data Integrity Failures |
| A09:2025 | Security Logging and Alerting Failures |
| A10:2025 | Mishandling of Exceptional Conditions |

`A03:2025` (cadena de suministro) se cubre en detalle en `standards/security/supply-chain.md`.

## OWASP ASVS[^owasp-asvs]
Vigente: **ASVS 5.0**. Catálogo de requisitos de verificación organizado en niveles crecientes de
rigor (L1: higiene mínima aplicable a todo; L2: la mayoría de aplicaciones con datos sensibles; L3:
alto valor o alta exposición) sobre autenticación, gestión de sesión, control de acceso,
criptografía, validación de entrada, protección de datos y configuración. El nivel exigido lo fija
el perfil del ADS (`profiles/<name>/profile.md`); un ADS con datos personales o de pagos no baja de L2.

## Prácticas obligatorias por capa
- **Frontend:** ningún secreto ni token de larga vida en código de cliente; cabeceras de seguridad
  (CSP, `X-Content-Type-Options`, etc.) configuradas por defecto; entrada de usuario nunca se
  interpola sin escapar en HTML/SQL/shell.
- **Backend:** validación de entrada en el borde (A05, A06); autenticación y autorización explícitas
  por endpoint (A01, A07); errores que no filtran detalles internos (A09, A10); dependencias con
  version pinning y sin vulnerabilidades conocidas de severidad alta/crítica sin mitigar (A03, A08).
- **Ambos:** secretos fuera del repo (`.env.example` + gestor de secretos, AGENTS.md regla 2);
  ningún dato de producción al alcance del agente sin necesidad explícita.

## Verificación
`skills/security-hardening/SKILL.md` recorre esta lista contra el ADS antes de cada release; el
resultado (hallazgo → severidad → mitigación) queda en el reporte de la unidad.

[^owasp-top10]: OWASP Top 10:2025 — https://owasp.org/Top10/2025/
[^owasp-asvs]: OWASP Application Security Verification Standard (ASVS) 5.0 — https://owasp.org/www-project-application-security-verification-standard/
