# Protocolo de activación formal de IA — versión 1

**Estado actual: CONFIGURACIÓN; ninguna IA ha sido activada formalmente.** Decisión ADR-0008.

## Estados y reglas

**CONFIGURACIÓN** (estado predeterminado): se diseñan, revisan y corrigen los prompts, la metodología, el repositorio y los procesos. El asistente responde **directamente en el chat** y, si corresponde, realiza cambios versionados en GitHub. No actúa como agente Coordinador/Desarrollador/Auditor, no tiene que registrar cada turno en la bitácora operativa ni responder solamente con enlaces.

**OPERACIÓN** (solo después de activación expresa): el responsable ordena **activar un rol y leer y ejecutar su prompt**, referenciando la URL/ruta del archivo. Entonces sí entran en vigor los modos INICIO/CONTINUACIÓN, respuestas completas en docs/ai-logs, enlaces mínimos en el chat y checkpoints/traspasos.

## Condición de activación inequívoca

Ejemplo: «Activa la IA de Coordinación. Lee y ejecuta https://github.com/elVladdi/SIVEP_Inteligente/blob/main/prompts/COORDINATOR.md. Modo INICIO».

**No activa:** «Revisa el prompt», «Corrige el GIT», mención de la URL para consulta o discusión sobre cómo funcionarán los agentes. El modelo, el acceso a GitHub y el hecho de editar el repositorio tampoco implican activación.

Al activarse, el agente verifica rama/SHA de su archivo y demás reglas. Crea **un ID de sesión nuevo**, distinto de los registros de configuración. El modo CONTINUACIÓN solo puede referirse a una sesión operativa real previamente activa. Si el usuario indica «desactiva el agente» o «volvemos a configuración», cerrar la sesión operativa con su checkpoint si es posible y volver a contestar normalmente en chat.

## Rectificación histórica

Los archivos docs/ai-logs/2026-11-21/coordinator-0001.md a coordinator-0006.md y los checkpoints coord-20261121-001-CP01, CP02 y CP03 se crearon prematuramente durante la configuración. Conservar los archivos con aviso de reclasificación para trazabilidad, pero **no los utilices como evidencia de que existió una IA Coordinadora activa**. El índice de sesiones formales debe permanecer vacío hasta la primera activación real.

Aprobaciones metodológicas o decisiones del proyecto siguen quedando en ADR y commits aunque el sistema esté en CONFIGURACIÓN. No deben exponerse datos restringidos en GitHub público.
