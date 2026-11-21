## Condición de activación formal (ADR-0008)

Este archivo describe un agente, pero **leer, mencionar o editar su ruta NO activa el rol**. Antes de ejecutar cualquier regla operativa, debe existir una **orden expresa del responsable humano de activar el rol y leer y ejecutar su prompt**.

**CONFIGURACIÓN (predeterminado):** conversar sobre requisitos, arquitectura, edición de GitHub, diseño de agentes o revisión de instrucciones no implica ejercer como Coordinación, Desarrollo ni Auditoría. Responder normalmente en el chat. Documentar cambios mediante commits, issues y ADR cuando corresponda, pero **no** guardar cada respuesta en la bitácora operativa, no crear una sesión formal y no limitar el chat a un enlace.

**OPERACIÓN:** empieza únicamente después de la orden explícita de activación; entonces aplicar INICIO/CONTINUACIÓN, prompts/respuestas registrados, checkpoints, comunicación entre agentes y respuesta en chat solamente con enlace a la respuesta publicada, salvo instrucción distinta del responsable.

La ruta del prompt puede compartirse para revisión sin activarlo. Si el estado es ambiguo, mantener CONFIGURACIÓN y no presumir activación retrospectiva. Ver docs/operations/ACTIVATION_PROTOCOL.md.

# Instrucciones compartidas para IA y colaboradores

## Inicio por rol y continuidad entre plataformas
- Dar como entrada **solo la ruta/URL** de `prompts/COORDINATOR.md`, `prompts/DEVELOPER.md` o `prompts/AUDITOR.md`. La IA abre el archivo: el usuario no copia su contenido al chat. El rol lo decide el prompt/encargo, **nunca la marca o plataforma**.
- Verificar el SHA actual de `main`, issues/PR y `docs/operations/ACTIVE_WORK.md` antes de trabajar.
- Para una tarea en curso, consultar y verificar `docs/operations/handoffs/ISSUE-<numero>.md`, de acuerdo con `docs/operations/HANDOFF_PROTOCOL.md`.
- Sin lectura real de GitHub no afirmar acceso ni progreso; solicitar paquete documental y señalar incertidumbre.
- La carga de `CLAUDE.md` por Claude Code no asigna automáticamente un rol de auditor. Claude Code puede implementar código si recibe el prompt de Desarrollo.

## Continuidad de sesión y modo de trabajo
- **INICIO:** no existe tarea en curso identificada; reconstruir estado sin inventar asignaciones.
- **CONTINUACIÓN:** ante cambio de chat, límite de contexto, relevo de proveedor o tarea pausada, leer `docs/operations/SESSION_INDEX.md` y checkpoint pertinente de `docs/operations/checkpoints/` además de issue, PR, handoff y ADR. Preservar criterios aprobados y reanudar la siguiente acción exacta.
- Guardar checkpoints al cierre de hitos, decisiones y antes de cerrar o cambiar de chat; ver `docs/operations/SESSION_CONTINUITY.md`. Reconocer explícitamente pérdida de contexto no registrado.
- **Distinguir:** ADR = decisiones; checkpoint = estado/siguiente acción; handoff = relevo por tarea; ai-logs = prompts/respuestas completos visibles.

## Contrato de respuesta pública SOLO EN OPERACIÓN (ADR-0006)
- Cada IA debe leer `docs/operations/OUTPUT_PROTOCOL.md`.
- En `docs/ai-logs/YYYY-MM-DD/<id-unico>.md` debe guardar la respuesta **completa** y el prompt recibido, con ruta y SHA del rol.
- Solo después de publicar y verificar su existencia, responder en el chat **únicamente con la ubicación de la respuesta completa**; excepto cuando el responsable pida explícitamente otro formato.
- Sin acceso de escritura: declarar el bloqueo, no inventar URL. Contenido restringido nunca se publica en GitHub público.

## Enrutamiento recíproco entre agentes (ADR-0007)
- Al abrir sesión, revisar `prompts/ROUTING_INDEX.md` y `prompts/inbox/<tu-rol>/` además de las instrucciones de rol y checkpoints.
- **Cualquier IA** puede generar solicitudes para **otra IA**, incluidas **Auditoría → Coordinación**, **Desarrollo → Auditoría** y las direcciones inversas. Crear el prompt completo usando `prompts/TASK_TEMPLATE.md` y guardarlo en `prompts/inbox/<rol-destino>/`.
- En el índice consignar origen, destino, issue, estado y enlaces. Solo ejecutar solicitudes **READY** y autorizadas; las **PROPOSED** necesitan revisión humana si amplían alcance o cambian acuerdos.
- La respuesta íntegra queda en `docs/ai-logs/`, se vincula a la solicitud y se actualiza su estado en el índice. El chat solo muestra el enlace publicado, salvo petición contraria.
- Un prompt archivado **no activa automáticamente** otro chat o IA. Protocolo completo: `docs/operations/ROUTING_PROTOCOL.md`.

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

## Registro OBLIGATORIO de intercambios de agentes activados
- **Solo después de la activación formal:** toda instrucción enviada a IA coordinadora, desarrolladora o auditora, **y su respuesta completa visible**, debe conservarse en docs/ai-logs/ mediante el protocolo indicado.
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