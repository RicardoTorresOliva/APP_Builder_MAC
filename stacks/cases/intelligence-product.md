---
type: Stack Sheet
title: "Caso: producto de inteligencia/consultoría"
description: Opciones de stack para el perfil intelligence-product (informe argumentado + dataset o dashboard validado entregados juntos).
tags: [stacks, inteligencia, research, data, portabilidad]
status: stable
generated: { by: claude-code/web, at: 2026-09-28T00:11:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: anthropic-pricing
    resource: https://platform.claude.com/docs/en/about-claude/pricing
    title: Claude Platform Docs — Pricing
  - id: vercel-pricing
    resource: https://vercel.com/docs/plans/hobby
    title: Vercel — Hobby plan
  - id: supabase-pricing
    resource: https://supabase.com/pricing
    title: Supabase — Pricing
  - id: langfuse-pricing
    resource: https://langfuse.com/pricing
    title: Langfuse — Pricing
---

# Caso: producto de inteligencia/consultoría

## Cuándo aplica (perfil de ADS)

Perfil `intelligence-product` (compuesto: hereda de `research-report` + `data-product`, ver
`profiles/intelligence-product/profile.md`): el entregable es un informe argumentado respaldado por
un dataset o dashboard validado, entregados juntos — típico de consultoría, investigación de mercado
o inteligencia competitiva. `ads_contract_level: extendido` siempre. No es una app que otros operan
día a día; es un paquete que se entrega y se re-audita.

## Opciones

| Capa | Recomendada vibe coder | Pro/escalable | Low-cost/self-hosted | Corporativa/legacy |
|---|---|---|---|---|
| Frontend (presentación) | Documento/dashboard generado desde notebook o generador de sitios estático | Dashboard de BI interactivo (ver `/stacks/cases/internal-dashboard-bi.md`) + informe exportado | Notebook + sitio estático autogestionado | Publicado en el portal corporativo/intranet existente |
| Backend (pipeline) | Notebook o script único que ingiere, limpia y calcula | Pipeline con pasos versionados (ingesta → limpieza → cálculo → publicación) | Igual, orquestado con un programador de tareas self-hosted | Pipeline en la plataforma de datos ya operada por la empresa |
| Base de datos | Archivos versionados (Parquet/CSV) o Postgres del BaaS[^supabase-pricing] | Data warehouse relacional gestionado | Postgres autogestionado | Data warehouse corporativo existente |
| Auth | Enlace con contraseña/acceso restringido para el informe entregable | Control de acceso por rol en el dashboard | Igual, autogestionado | SSO corporativo para acceso al informe y al dataset |
| Pagos | N/D | N/D salvo que el informe se venda como producto (medir accesos) | N/D | N/D |
| Deploy/hosting | PaaS gratuito para el sitio del informe[^vercel-pricing] | Contenedor para el dashboard + almacenamiento del dataset | VPS único | Nube corporativa u on-prem |
| LLM / System One | Gateway con un modelo capaz para redacción asistida y verificación de citas[^anthropic-pricing] | Igual + observabilidad de cada llamada (Langfuse) para auditar cómo se generó cada afirmación[^langfuse-pricing] | Modelo local vía Ollama para borradores, con verificación humana obligatoria antes de publicar | Servicio LLM gestionado de la nube corporativa (gobernanza de datos si las fuentes son confidenciales) |
| Costo aproximado/mes | $0–30 (tiers gratuitos + tokens de redacción)[^vercel-pricing][^anthropic-pricing] | $100–500 según volumen de investigación y observabilidad[^langfuse-pricing] | $6–24 de VPS | Variable por contrato; n/d (no-verificado) |
| Curva de aprendizaje | Baja–media | Media–alta (pipeline versionado + gate de citas) | Media | Alta (integración con la plataforma de datos corporativa) |

## Cuándo NO usar cada opción

- **Vibe coder**: no usar un notebook único sin control de versiones cuando el informe respalda una
  decisión de negocio significativa — sin trazabilidad no hay forma de auditar cómo se llegó a una
  cifra titular.
- **Pro/escalable**: sobra un pipeline versionado completo con observabilidad para un informe de
  alcance pequeño y de una sola vez sin actualización periódica.
- **Low-cost/self-hosted**: no usar si el equipo no puede garantizar que el borrador generado por un
  modelo local pase por verificación humana antes de publicarse — el riesgo de una cita inventada en
  un informe entregado a un cliente es alto.
- **Corporativa/legacy**: no usar la plataforma de datos corporativa completa para un informe puntual
  y de bajo riesgo — el tiempo de aprovisionamiento no se justifica.

## Comprar vs construir

No existe un producto empaquetado equivalente a "generador de informes de consultoría"; lo que sí se
compra son las piezas: la capa de BI/dashboard (ver `/stacks/cases/internal-dashboard-bi.md` para esa
decisión) y el gateway LLM. Lo que se construye siempre a medida es el **pegamento**: la lógica que
conecta cada afirmación del informe con una cifra reproducible del dataset (Attested Computation OKF)
— esa trazabilidad es el valor del producto y no existe en ninguna herramienta genérica.

## Equivalencias por nube

Ver `/stacks/clouds.md`, bloque de base de datos relacional gestionada (para el dataset) y de
almacenamiento de objetos (para los documentos fuente y el informe exportado, p. ej. PDF). El
servicio LLM gestionado sigue la misma matriz que cualquier otro caso con IA.

## Superficie agéntica y tokens por defecto

- Gate de cero invención: toda afirmación del informe basada en datos debe citar una vista o cifra
  validada del dataset; un agente que redacta sin esa cita no pasa el quality gate del perfil.
- Verificación de citas como paso obligatorio antes de publicar, no opcional ni solo "recomendado".
- **Dashboard de tokens por defecto**: N2 como mínimo, porque el volumen de tokens de investigación y
  redacción suele ser alto y variable por encargo — conviene visibilidad de costo por entregable desde
  el MVP del propio ADS (que en este caso es el informe mismo).

## Riesgos de lock-in y plan de salida

- **Notebook/formato de análisis propietario**: mitigar manteniendo los datos fuente y el código de
  transformación en formatos abiertos (Parquet/CSV, scripts versionados), no solo en el estado de un
  notebook interactivo.
- **Herramienta de BI para el dashboard**: ver riesgos de lock-in en
  `/stacks/cases/internal-dashboard-bi.md` — este caso hereda esa decisión cuando el entregable incluye
  un dashboard.
- **Proveedor LLM para redacción**: mitigado por el gateway LLM; el riesgo real no es de proveedor sino
  de calidad — un cambio de modelo sin repetir la verificación de citas puede introducir afirmaciones
  no respaldadas en un informe ya validado.

[^anthropic-pricing]: Claude Platform Docs — Pricing
[^vercel-pricing]: Vercel — Hobby plan
[^supabase-pricing]: Supabase — Pricing
[^langfuse-pricing]: Langfuse — Pricing
