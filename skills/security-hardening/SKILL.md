---
name: security-hardening
description: Revisa una superficie web/API o un diseño de agente/LLM contra OWASP Top 10, ASVS, OWASP GenAI LLM Top 10 y OWASP Top 10 for Agentic Applications, y contra la cadena de suministro (lockfiles, SBOM, secretos). Úsala antes de un release, al otorgar una herramienta nueva a un agente, o cuando se agrega una dependencia.
license: "Propietaria SLG (ver LICENSE)"
metadata: { okf_type: Skill, abm_version: "5.0.0" }
---

# security-hardening

## Pasos

1. Si la unidad expone una superficie web o de API, recorre `standards/security/web-api.md`
   (OWASP Top 10:2025 + ASVS del nivel que el perfil exige) y registra hallazgo → severidad → mitigación.
2. Si la unidad invoca un modelo de lenguaje o tiene un agente con herramientas, recorre
   `standards/security/llm-agentic.md` (OWASP GenAI LLM Top 10 2026 + OWASP Top 10 for Agentic
   Applications 2026); confirma que ningún dato recibido de un tool, API o agente externo se trate
   como instrucción.
3. Verifica scopes mínimos y tokens revocables del agente o servicio; una ampliación de alcance sin
   necesidad concreta se rechaza o se lleva a pendiente.
4. Si la unidad agrega o actualiza una dependencia, recorre `standards/security/supply-chain.md`:
   lockfile actualizado, SBOM regenerado, licencia registrada, sin vulnerabilidad alta/crítica sin
   mitigar.
5. Corre `abm secrets` (o el escaneo de secretos del ADS) sobre los archivos tocados.
6. Toda acción que caiga en un bloqueante de AGENTS.md (irreversible, producción/pagos, credencial
   ausente, cambio de permisos) se detiene y se reporta en rojo, sin ejecutarse.
7. Registra cada hallazgo con severidad (bloqueante/mayor/menor, ver `review-criteria.md` de la
   capa correspondiente) y su mitigación o su entrada en `abm pending add`.

## Criterios de salida

- Ningún hallazgo bloqueante sin mitigar antes de release.
- SBOM, lockfile y secret scanning limpios o con hallazgo documentado y mitigado.
- Reporte final según `standards/communication.md` (≤ 12 líneas), con severidades explícitas.
