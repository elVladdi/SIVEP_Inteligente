# Entrada por ruta y respuesta documentada — Protocolo v1

**Aprobado:** 2026-11-21, ADR-0006. Aplica a Coordinación, Desarrollo y Auditoría, en INICIO o CONTINUACIÓN.

## Entrada (sin copiar prompts)
1. El usuario indica la **ruta/URL del archivo de rol** y opcionalmente modo, issue/PR o sesión. No pega su contenido.
2. La IA consulta realmente la ruta con sus herramientas, identifica rama y **SHA** de la versión, lee el prompt y el contexto exigido por éste. Si no puede acceder, **no finge haberlo leído**: solicita acceso o un paquete documental.

## Respuesta completa fuera del chat (por defecto)
1. Elaborar la **respuesta sustantiva completa** de la tarea, incluidos decisiones y sus fundamentos explícitos, pruebas y límites, rutas de artefactos, issue y PR pertinentes.
2. Crear por interacción el archivo `docs/ai-logs/YYYY-MM-DD/<id-unico>.md` (por ejemplo, con `scripts/record_ai_interaction.py`). Incluir fecha UTC, modelo/rol, issue/PR, mensaje completo recibido, ruta y SHA del archivo de rol consultado, y sección **`## Respuesta completa visible`** con la respuesta sustantiva íntegra. Citar archivos y commits; no inventar resultados.
3. Revisar confidencialidad y guardar en una **rama/PR autorizada**, no modificar silenciosamente `main`. Publicar, después **verificar** existencia mediante lectura desde GitHub.
4. Responder **solamente con el permalink del commit a esa sección**, `https://github.com/elVladdi/SIVEP_Inteligente/blob/<SHA>/docs/ai-logs/YYYY-MM-DD/<id>.md#respuesta-completa-visible`. Si el sistema no permite permalink, usar una URL a la rama accesible y comprobada. No incluir saludos, explicaciones ni resúmenes en el chat, salvo orden expresa.
5. Los registros son la fuente única de **prompt y respuesta completa**, de modo que no se precisa duplicar la respuesta en otra carpeta. Enlaces a código, informes especializados o PR son anexos, nunca reemplazo del texto sustantivo.

## Excepciones
- **Instrucción expresa del usuario:** si pide responder en chat, hacerlo y mantener la trazabilidad de la respuesta.
- **No hay acceso de lectura/escritura o falla la publicación:** no inventar URL ni afirmar que la respuesta quedó guardada; informar el bloqueo brevemente y especificar qué permiso o herramienta falta. Solo enlazar archivos locales si se han creado y son accesibles al usuario.
- **Información restringida:** repositorio público; no subir datos reales de SIVEP/DAM, secretos o texto protegido. Custodiar la interacción íntegra en entorno institucional aprobado y, si resulta seguro, registrar solamente metadatos no sensibles en GitHub. En el chat, enlace al lugar autorizado si existe; si no, explicar el impedimento sin divulgar contenido.
- No reclamar recuperación de chats externos ni sincronización automática si no existe integración comprobada.

El modo CONTINUACIÓN usa también `docs/operations/SESSION_INDEX.md`, checkpoints, ADR e issues/PR; las respuestas siguen el mismo protocolo.

## Respuesta a prompts emitidos por otra IA
Leer `prompts/ROUTING_INDEX.md` y el archivo de la solicitud en `prompts/inbox/<tu-rol>/`. El registro de respuesta bajo `docs/ai-logs/` debe incluir ID de solicitud, ruta y SHA del prompt de tarea, rol emisor/destino, issue, y todos los resultados visibles. Publicar y comprobar URL, actualizar estado del índice y en chat **solo devolver el enlace**. Si la respuesta identifica trabajo para otro agente, crear además **un nuevo prompt dirigido** y actualizar el índice: no colocar el pedido solamente dentro del texto de la respuesta. Ver `docs/operations/ROUTING_PROTOCOL.md`.
