---
type: Stack Sheet
title: Equivalencias multinube
description: Matriz AWS / Azure / GCP / on-prem por bloque de infraestructura, IaC multinube y la regla de abstracción o plan de salida.
tags: [stacks, multicloud, portabilidad, iac]
status: stable
generated: { by: claude-code/web, at: 2026-09-27T23:57:00Z }
stale_after: 2026-12-28T00:00:00Z
sources:
  - id: aws-rds
    resource: https://aws.amazon.com/rds/
    title: Amazon RDS
  - id: azure-sql
    resource: https://azure.microsoft.com/en-us/products/azure-sql/database
    title: Azure SQL Database
  - id: gcp-cloudsql
    resource: https://cloud.google.com/sql
    title: Google Cloud SQL
  - id: iac-2026
    resource: https://www.env0.com/guides/pulumi-vs-terraform-vs-opentofu-side-by-side-feature-licensing-and-migration-comparison-2026
    title: "Pulumi vs Terraform vs OpenTofu (2026)"
  - id: opentofu
    resource: https://opentofu.org
    title: OpenTofu
  - id: pulumi
    resource: https://www.pulumi.com/docs/
    title: Pulumi Docs
  - id: terraform
    resource: https://developer.hashicorp.com/terraform
    title: Terraform Docs
  - id: cncf-12factor
    resource: https://12factor.net/
    title: The Twelve-Factor App
---

# Equivalencias multinube

Matriz de referencia por bloque de infraestructura. Úsala para traducir un requisito ("necesito
cómputo serverless") a la opción equivalente en la nube que ya tiene el cliente, y para completar
`portability.exit_plan` en `ads.yaml` cuando el bloque elegido es propietario. Todo precio concreto
varía por región, tier y compromiso: verifica en la calculadora oficial de la nube antes de
presupuestar; esta ficha compara capacidades y nombres de servicio, no tarifas.

## Matriz por bloque

| Bloque | AWS | Azure | GCP | On-prem / otras |
|---|---|---|---|---|
| Cómputo — contenedores | ECS / EKS (Kubernetes gestionado) | Container Apps / AKS | Cloud Run / GKE | Kubernetes autogestionado (kubeadm, k3s) |
| Cómputo — serverless (funciones) | Lambda | Functions | Cloud Functions / Cloud Run functions | OpenFaaS, Knative sobre Kubernetes propio |
| Cómputo — VMs | EC2 | Virtual Machines | Compute Engine | Hipervisor propio (KVM/VMware/Proxmox) |
| Base de datos relacional gestionada | RDS / Aurora[^aws-rds] | Azure SQL / Azure Database for PostgreSQL[^azure-sql] | Cloud SQL / AlloyDB[^gcp-cloudsql] | PostgreSQL/MySQL autogestionado con réplicas propias |
| Base de datos documental | DynamoDB / DocumentDB | Cosmos DB | Firestore / Bigtable | MongoDB Community, CouchDB autogestionados |
| Caché | ElastiCache (Redis/Memcached) | Azure Cache for Redis | Memorystore | Redis/Valkey autogestionado |
| Almacenamiento de objetos | S3 | Blob Storage | Cloud Storage | MinIO (compatible con la API de S3) |
| Colas / eventos | SQS / SNS / EventBridge | Service Bus / Event Grid | Pub/Sub / Cloud Tasks | RabbitMQ, NATS, Kafka autogestionados |
| Secretos | Secrets Manager / Parameter Store | Key Vault | Secret Manager | Vault (HashiCorp), SOPS + git cifrado |
| Identidad / IdP | Cognito / IAM Identity Center | Entra ID | Identity Platform / Cloud IAM | Keycloak, Authentik (OIDC/SAML autogestionado) |
| Observabilidad | CloudWatch / X-Ray | Azure Monitor / Application Insights | Cloud Monitoring / Cloud Trace | Pila OpenTelemetry + Prometheus/Grafana/Loki/Tempo propia |
| Servicio LLM gestionado | Bedrock | Azure AI Foundry | Vertex AI | Ollama/vLLM sobre GPU propia o alquilada |
| CDN | CloudFront | Azure CDN / Front Door | Cloud CDN | Cloudflare, proxy propio con cache |
| IaC nativo de la nube | CloudFormation / CDK | Bicep / ARM | Deployment Manager | — (usar IaC multinube, ver abajo) |

## IaC multinube (categoría)

| Opción | Enfoque | Licencia |
|---|---|---|
| Terraform[^terraform] | HCL declarativo, mayor ecosistema de providers | BSL 1.1 (no OSI desde 2023)[^iac-2026] |
| OpenTofu[^opentofu] | Fork 1:1 de Terraform, mismo HCL y formato de estado | Open source (MPL 2.0), gobernado por la Linux Foundation[^iac-2026] |
| Pulumi[^pulumi] | Infraestructura como código en un lenguaje de programación real (TS, Python, Go, C#) | Open source el SDK; SaaS de estado con tier gratuito y de pago[^iac-2026] |

Recomendación por defecto: OpenTofu cuando el equipo ya piensa en HCL y quiere licencia abierta sin
ambigüedad; Pulumi cuando el equipo prefiere expresar infraestructura en el mismo lenguaje que la
aplicación y quiere tipos y tests sobre la infraestructura. Terraform sigue siendo válido si el
cliente ya lo opera y no le preocupa la licencia BSL.

## Contenedores y 12-factor

Todo ADS software se empaqueta en contenedores (imagen reproducible, sin estado en el filesystem del
contenedor) y sigue los doce factores[^cncf-12factor]: configuración por entorno (nunca en el
código), procesos sin estado, backing services como recursos adjuntos intercambiables (una base de
datos es un recurso con URL, no un supuesto de red fijo), logs como flujo de eventos (no archivos
locales), y paridad dev/prod. Esto es lo que hace posible que el mismo ADS corra sin cambios en
Docker Compose local, Kubernetes de cualquier nube, o un PaaS (Render/Railway/Fly.io) — el
contenedor y las variables de entorno son el contrato de portabilidad.

## Regla: todo servicio propietario lleva abstracción o plan de salida

Si un ADS usa un servicio de plataforma sin equivalente directo en otra nube (p. ej. una feature
propietaria de un servicio LLM gestionado, un formato de cola específico), dos caminos, no uno:

1. **Abstracción en código**: una interfaz propia (puerto/adaptador) delante del servicio, de modo
   que cambiar de proveedor sea escribir un adaptador nuevo, no reescribir la lógica de negocio.
2. **Plan de salida documentado** (`portability.exit_plan` en `ads.yaml`): qué se pierde, cuánto
   cuesta migrar (tiempo/datos/reentrenamiento) y a qué equivalente de la matriz de arriba migraría
   el ADS si el proveedor deja de ser viable (precio, disponibilidad, políticas).

Un ADS sin ninguno de los dos caminos para un servicio propietario es lock-in injustificado y debe
señalarse en la revisión (`abm review`) y en la sección "Riesgos de lock-in" de la ficha de stack
correspondiente.

[^aws-rds]: Amazon RDS
[^azure-sql]: Azure SQL Database
[^gcp-cloudsql]: Google Cloud SQL
[^iac-2026]: "Pulumi vs Terraform vs OpenTofu (2026)"
[^opentofu]: OpenTofu
[^pulumi]: Pulumi Docs
[^terraform]: Terraform Docs
[^cncf-12factor]: The Twelve-Factor App
