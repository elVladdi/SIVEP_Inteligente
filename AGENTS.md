# Instrucciones compartidas para IA y colaboradores

## Lectura inicial obligatoria
1. README.md y PROJECT_STATE.md.
2. docs/decisions/README.md y los ADR pertinentes.
3. docs/operations/WORKFLOW.md.
4. docs/ai-logs/README.md.
5. Issue y archivos relacionados con la tarea.

## Reglas de dominio
- Recomendaciones asistidas, no decisiones administrativas automáticas.
- Separar búsqueda textual, comparabilidad técnica, criterios jurídicos, indicadores estadísticos de riesgo y determinación del valor en aduana.
- Igual subpartida o elevada similitud semántica NO prueban identidad ni similitud jurídica.
- No fijar familia piloto, nivel arancelario, modelo o valores sin decisión documentada.
- Verificar precedencia temporal en simulaciones retrospectivas.
- No inventar resultados de pruebas, campos de SIVEP, evidencias o referencias.

## Registro OBLIGATORIO de intercambios de IA
- Toda instrucción enviada a IA coordinadora, desarrolladora o auditora, **y su respuesta completa visible**, debe conservarse en docs/ai-logs/ mediante el protocolo indicado.
- Incluir función, sistema/proveedor/modelo si se conoce, fecha UTC, autor, issue, commit/versión base, artefactos y estado de revisión.
- Registrar iteraciones, correcciones y auditorías, no solo el prompt final ni el resumen.
- En el repositorio público solo se guardan contenidos aptos para publicación. Intercambios confidenciales: registrar metadata y referencia al archivo íntegro en depósito institucional autorizado, nunca datos restringidos.
- Nunca afirmar que se capturaron automáticamente conversaciones de otras plataformas si no se recibió su exportación o no se integró un mecanismo de registro.
- No incluir razonamiento interno privado de modelos, instrucciones de sistema confidenciales ni datos que no fueron entregados al agente.

## Entrega y cambios
- Trabajo por rama y PR; pruebas reproducibles, documentación, análisis de seguridad.
- No modificar decisiones aceptadas silenciosamente; proponer nuevo ADR.
- El agente ejecutor no se autoaudita ni se autoaprueba.
- Cada PR con trabajo IA debe enlazar sus registros de prompt/respuesta; no fusionar si falta trazabilidad relevante.
- Cuando no se puede publicar un intercambio íntegro, registrar la excepción y custodiar el original fuera del repositorio público.