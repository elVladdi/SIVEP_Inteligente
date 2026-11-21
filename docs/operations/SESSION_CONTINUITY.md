# Protocolo de continuidad de sesiones IA — v1

**Este protocolo de checkpoints corresponde solamente a agentes OPERATIVOS formalmente activados.** No aplicar a conversaciones de CONFIGURACIÓN ni reutilizar checkpoints históricos de diseño. Ver ADR-0008 y docs/operations/ACTIVATION_PROTOCOL.md.

## Propósito y alcance
Recuperar una tarea en otro chat del **mismo modelo y proyecto**, o en otro modelo/proveedor, sin depender de memoria oculta. Aplica a coordinación, desarrollo y auditoría, tanto si el contexto se agota como si hay interrupción o relevo voluntario.

## INICIO vs CONTINUACIÓN
- **INICIO:** no hay sesión/tarea que recuperar. Leer archivos canónicos y obtener o proponer asignación de issue sin ejecutar tareas no autorizadas.
- **CONTINUACIÓN:** el usuario pide retomar, hay cierre por límite de contexto, existe relevo o una tarea fue pausada. Proporcionar la misma ruta del prompt de rol para que la IA lo lea (sin copiarlo), localizar último checkpoint de la sesión/tarea y cotejar evidencia con repositorio.
- Si hay varios candidatos igualmente plausibles, exponer opciones y pedir que se identifique uno; no seleccionar arbitrariamente. Un rol en otro modelo es legítimo si la asignación humana lo confirma.

## Fuentes, con responsabilidades distintas
1. `docs/decisions/ADR-*.md` — decisiones aprobadas y su fundamento.
2. `PROJECT_STATE.md` — situación general y restricciones.
3. `docs/operations/ACTIVE_WORK.md` — índice de tareas/PR.
4. `docs/operations/SESSION_INDEX.md` — sesiones activas y último checkpoint.
5. `docs/operations/checkpoints/YYYY-MM-DD/<session-id>-CPnn.md` — estado de una sesión en un hito determinado.
6. `docs/operations/handoffs/ISSUE-<numero>.md` — relevo por issue o tarea.
7. `docs/ai-logs/` — cada prompt y respuesta visible completos o referencia de custodia autorizada.
8. GitHub issues, PR, branches, commits y tests — evidencia del estado técnico real.

## Crear un checkpoint
- Asignar a la sesión un identificador **estable y único** (p. ej. `coord-20261121-001`; no usar identificadores personales). Numerar checkpoints CP01, CP02...; cada archivo es **inmutable** tras su publicación: una actualización genera CP siguiente.
- Crear archivo desde `docs/operations/checkpoints/TEMPLATE.md`; registrar rol, modelo si consta, rama, SHA verificado (a la fecha del checkpoint), issue/PR, objetivos, acuerdos aprobados con ADR, propuestas pendientes, alternativas/criterios explícitos, tareas realmente completadas con evidencia, última acción realizada, riesgos, siguiente acción exacta, rutas de logs y handoff.
- Actualizar `SESSION_INDEX.md` para enlazar **el último** checkpoint de esa sesión. Si es trabajo ligado a issue, vincularlo también desde `ACTIVE_WORK.md` y handoff.
- Guardar mediante commit/PR según política. Los checkpoints no reemplazan la grabación completa de prompts/respuestas ni son una auditoría independiente.

## Cuándo capturarlo
- Tras **cada acuerdo, decisión, cambio de enfoque, resultado experimental o hito significativo**.
- Antes de cambio de modelo, cierre voluntario, petición de pausar o abrir nuevo chat.
- Cuando se anticipe un límite de contexto, **antes** de alcanzarlo si es posible. No existe detección infalible del cierre ni guardado automático entre herramientas.
- Como mínimo, al terminar una sesión de trabajo que produjo avance. Registrar una sesión sin avances solo cuando aporte una decisión o un estado relevante.

## Arranque CONTINUACIÓN (pasos verificables)
1. Abrir y leer el prompt de rol mediante su ruta/URL verificada y declarar **CONTINUACIÓN**.
2. Leer `SESSION_INDEX.md`: resolver sesión por ID/issue explícito, o buscar último checkpoint pertinente al rol y tarea. No confundir sesiones paralelas.
3. Leer checkpoint y los ADR/issue/PR/handoff/logs referenciados; recuperar criterio aprobado y razonamiento **explícito** (nunca cadena privada).
4. Comprobar `main`, rama, HEAD SHA, diffs y últimas pruebas. Si hubo trabajo posterior al checkpoint, actualizar diagnóstico en lugar de ejecutar instrucciones obsoletas.
5. Producir resumen de recuperación: acuerdos inamovibles salvo autorización, último avance comprobado, pendientes, incertidumbres y **siguiente acción exacta**.
6. Continuar a partir del último estado verificable, registrar nuevos turnos e ir creando nuevos checkpoints por hitos.

## Chat perdido o interrumpido sin checkpoint
1. Emplear el último checkpoint existente y los commits/logs/PR posteriores que realmente sean legibles.
2. Reconstruir los hechos documentados, distinguiendo **verificado** de **inferido** y **no disponible**.
3. No fabricar textos de prompts, respuestas, criterios ni pruebas inexistentes; reportar explícitamente el tramo no documentado.
4. Si el hueco afecta a una decisión fundamental, solicitar al responsable una confirmación; dejar registro posterior, sin atribuir aprobación retrospectiva.

## Privacidad y acceso
Repositorio público: sin DAM/SIVEP reales, información institucional confidencial o secretos. Checkpoints de tareas restringidas contendrán solo metadatos publicables y referencia de custodia autorizada. Sin acceso a GitHub: pedir paquete mínimo de continuidad; **no declarar** recuperación exacta ni lectura inexistente.

## Entrada y salida de chat nuevo
El mensaje inicial proporciona **la ruta/URL** del mismo prompt, no su texto. El agente documenta la respuesta completa y el prompt en `docs/ai-logs/`, publica, verifica y **solo devuelve su enlace** en chat. Ver ADR-0006 y `docs/operations/OUTPUT_PROTOCOL.md`.
