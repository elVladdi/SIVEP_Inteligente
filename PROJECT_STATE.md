# Estado del proyecto — SIVEP Inteligente

Fecha de actualización: 2026-11-21. Estado: F0, preparación metodológica. No hay modelo ni acceso operativo implementado.

## Decisiones vigentes
- SIVEP es la fuente histórica prevista; se espera trabajar con datos del formato B de las DAM peruanas.
- El sistema ofrece referencias y alertas al especialista, quien conserva la decisión final.
- Usos: riesgo anticipado de subvaloración, ranking explicable de antecedentes, priorización de DAM canal verde en control posterior, y trazabilidad de valores históricos.
- Primera prioridad científica: determinar cómo identificar mercancías idénticas, similares y no comparables.
- Desarrollo colaborativo: IA coordinadora, IA desarrolladora (por ejemplo Codex), IA auditora independiente (por ejemplo Claude), colaboradores humanos y responsable final.
- **Todos los prompts y respuestas visibles de las tres funciones de IA deben registrarse** en este repositorio antes de cerrar una tarea; consultar docs/ai-logs/README.md y ADR-0003.
- Repositorio público: no almacenar información real o sensible de SIVEP/DAM.

## Pendiente de validación o decisión
- Familia piloto de mercancías; nivel de partida SA 6, NANDINA 8 o nacional 10 dígitos.
- Diccionario preciso de campos SIVEP/formato B y permisos de acceso.
- Protocolo jurídico-técnico de comparabilidad; selección de modelos y métricas.
- Estrategia de despliegue, licencia, responsables y controles de seguridad.
- Mecanismo de captura automática de prompts y respuestas en las plataformas externas, sujeto a sus capacidades y permisos.

## Revisión de literatura documental
- Se prepararon **ocho fichas ampliadas** y un [índice con cuadros comparativos](docs/literature/README.md) en una rama/PR de documentación independiente (issue #9).
- El trabajo es de **CONFIGURACIÓN**, sin activación de IA Coordinadora ni experimentos ejecutados.
- Aportes centrales para el primer experimento: comparación de recuperación exacta, BM25, TF-IDF, embeddings y técnicas híbridas, con validación experta. **No se ha aprobado todavía una arquitectura final.**

## Próximos pasos
1. Revisión bibliográfica y normativa crítica; matriz de evidencias y límites de aplicación.
2. Diseño de protocolo de etiquetado de mercancías por expertos.
3. Inventario y clasificación de datos disponibles (sin publicar registros).
4. Abrir issues de investigación y definir criterios de aceptación.

**Fuente de verdad:** acuerdos aprobados en ADR, estado versionado, issues y PR. El contexto de chat no equivale a una decisión formal.