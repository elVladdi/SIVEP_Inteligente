# SIVEP Inteligente

**Estado:** fase 0 — definición metodológica y revisión de literatura. **No existe todavía un modelo entrenado ni una integración operativa con SIVEP.**

Proyecto de investigación y desarrollo para recuperar antecedentes de mercancías idénticas o similares en registros históricos del **Sistema de Verificación de Precios (SIVEP)**, construir referencias trazables de valoración y apoyar el análisis de riesgo de posible subvaloración en Declaraciones Aduaneras de Mercancías (DAM) peruanas.

> **Decisión humana obligatoria:** los resultados del sistema son recomendaciones documentadas. No sustituyen el análisis del especialista, no constituyen automáticamente duda razonable y no establecen por sí solos el valor en aduana.

## Casos de uso previstos

1. Apoyo al análisis anticipado de operaciones con indicios de riesgo de subvaloración.
2. Búsqueda, ranking y explicación de referencias históricas para el especialista.
3. Priorización de DAM de canal verde en acciones de control posterior.
4. Mejora continua de una base histórica de valores con procedencia y estados de validación distinguibles.

## Primera prioridad

Definir y validar una **metodología de identificación de mercancías idénticas, similares y no comparables** sobre descripciones del formato B de DAM y otros atributos disponibles en SIVEP. El alcance inicial de mercancías y el nivel arancelario (SA 6, NANDINA 8 o nacional 10 dígitos) **aún no se han elegido**.

## Empezar con cualquier IA (prompts universales)

Para comenzar una sesión nueva o **retomar la misma tarea en otro modelo**, pega el primer prompt completo correspondiente a su rol: [Coordinadora](prompts/COORDINATOR.md), [Desarrolladora](prompts/DEVELOPER.md) o [Auditora](prompts/AUDITOR.md). Consulta la [guía de inicio](prompts/README.md).

Al pasar a otro chat del mismo modelo, usa el **mismo prompt** y selecciona modo **CONTINUACIÓN**. El agente recupera el último [checkpoint de sesión](docs/operations/SESSION_INDEX.md) según el [protocolo](docs/operations/SESSION_CONTINUITY.md); no necesita memoria de los mensajes anteriores si los acuerdos y el progreso quedaron registrados.

La continuidad está documentada en [trabajo actual](docs/operations/ACTIVE_WORK.md) y [protocolo de traspaso](docs/operations/HANDOFF_PROTOCOL.md); el agente verificará issues, PR, SHA y handoff en GitHub, sin depender del chat anterior.

## Cómo empezar

- [PROJECT_STATE.md](PROJECT_STATE.md): estado vigente, acuerdos, dudas y tareas siguientes.
- [AGENTS.md](AGENTS.md): instrucciones comunes para agentes de IA y colaboradores.
- [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md): alcance, objetivos y restricciones.
- [docs/operations/WORKFLOW.md](docs/operations/WORKFLOW.md): coordinación de IA, auditoría y cambios.
- [docs/ai-logs/README.md](docs/ai-logs/README.md): bitácora obligatoria de todos los prompts y respuestas visibles de las tres IA.
- [docs/ai-logs/2026-11-21/coordinator-0001.md](docs/ai-logs/2026-11-21/coordinator-0001.md): primera interacción documentada.
- [docs/decisions/README.md](docs/decisions/README.md): registro de decisiones (ADR).
- [docs/roadmap/ROADMAP.md](docs/roadmap/ROADMAP.md): fases y criterios de aceptación.
- [CONTRIBUTING.md](CONTRIBUTING.md) y [SECURITY.md](SECURITY.md): colaboración y protección de información.

## Principios

- Evidencia trazable: cada referencia muestra origen, similitudes, diferencias y restricciones.
- Separación estricta entre indicador de riesgo y aplicación jurídica de métodos de valoración.
- Comparabilidad técnica y comercial antes de estadísticas de precios.
- Reproducibilidad: código, versiones, pruebas y decisiones documentadas.
- Datos sintéticos en este repositorio público; datos reales solo en sistemas autorizados.

## Licencia

**Pendiente de decisión.** Hasta seleccionar una licencia, la visibilidad pública del repositorio no equivale a una licencia general de reutilización.
