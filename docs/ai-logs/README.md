# Bitácora de prompts y respuestas de IA — obligatoria

## Política
**Cada interacción** con IA coordinadora, IA desarrolladora (Codex u otra) o IA auditora (Claude u otra) requiere un registro individual: prompt *completo* + respuesta *completa visible*, incluidos reintentos, correcciones, preguntas de aclaración y respuestas de auditoría.

No basta pegar el prompt inicial, un resumen de la respuesta o enlazar únicamente el PR. Cada iteración crea un registro nuevo, vinculado a su issue y al intercambio anterior. Es posible crear una serie de varios turnos conservando el orden.

## Estructura
docs/ai-logs/YYYY-MM-DD/<fecha-utc>_<id>.md. Campos:
- ID único, fecha UTC, función, proveedor, modelo (si se conoce), registrado por.
- Issue o tarea; rama/commit base, referencias previas.
- Clasificación **PUBLICABLE** o **RESTRINGIDO**.
- Prompt completo y respuesta completa visible si es publicable.
- Para restringidos: solo metadata no sensible y referencia opaca a custodia institucional autorizada; el original permanece íntegro fuera del repositorio público.
- Archivos generados, commit/PR, pruebas y revisión humana; marcar no disponible, no inventar.

## Registro manual asistido
Exportar/copy-paste la entrada y salida de cada IA en archivos UTF-8 locales que no se suben a GitHub y ejecutar:
python scripts/record_ai_interaction.py --role developer --provider OpenAI --model Codex --issue ISSUE-001 --prompt-file /ruta/entrada.txt --response-file /ruta/salida.txt --recorded-by colaborador --confirm-public-safe

Para información restringida: usar --confidentiality restricted --custody-ref <identificador-institucional> y **NO** --confirm-public-safe; nunca subir el original. El script crea un registro de metadatos.

## Límites y garantías
- Esta herramienta no tiene acceso automático al historial de ChatGPT, Codex o Claude.
- No se exige ni se puede registrar razonamiento interno privado del modelo, instrucciones no visibles, ni acciones no documentadas.
- Quien registra confirma que examinó la información para publicación. La revisión manual de privacidad es indispensable.
- Si una plataforma no facilita la exportación completa, registrar la limitación y solicitar el contenido visible, sin afirmar falsamente cumplimiento total.
- Los registros anteriores al establecimiento de esta política deben identificarse como backfill y marcar cualquier falta de contenido.

## Verificación
En cada PR revisar que los enlaces a docs/ai-logs/ cubren todas las iteraciones IA de la tarea. Los metadatos ayudan a auditar, pero el repositorio público no constituye almacenamiento autorizado para datos protegidos.
## Primer prompt de cada agente y cambio de modelo
El **prompt inicial de rol** en `prompts/` también se documenta como intercambio, con el texto exacto enviado, la versión del archivo y la primera respuesta completa visible. Si se sustituye un desarrollador (Codex por Claude Code, o viceversa), registrar tanto el cierre del agente saliente como la apertura del agente entrante, asociándolos al mismo issue y al handoff. Enlazar la plantilla no reemplaza conservar el prompt efectivamente utilizado.

## Relación con checkpoints de sesión
Un checkpoint en `docs/operations/checkpoints/` resume el estado, acuerdos, evidencias y siguiente acción; **NO sustituye** el registro de cada prompt/respuesta visible. El índice `docs/operations/SESSION_INDEX.md` vincula sesión, último checkpoint, issue y logs. Los archivos se actualizan por PR para preservar el historial. Para chats interrumpidos sin registro, marcar expresamente falta de trazabilidad y no reconstruir texto inexistente.

## Ubicación canónica de la respuesta completa — ADR-0006
Cada archivo `docs/ai-logs/YYYY-MM-DD/<id-unico>.md` conserva **el mensaje/prompt exacto recibido** (a menudo es solo una URL/ruta), identifica el prompt de rol consultado mediante ruta + SHA y contiene `## Respuesta completa visible` con el resultado sustantivo íntegro. El enlace del chat apunta a `#respuesta-completa-visible`. **No sustituir la respuesta por un resumen ni por la URL de un archivo distinto.**

**Cierre:** escribir → revisar confidencialidad → publicar en rama/PR → comprobar en GitHub → responder **solo con permalink verificado** en chat. Si la publicación falla, informar el bloqueo; si el material es restringido, conservarlo únicamente en entorno autorizado. La instrucción explícita del responsable de responder en chat prevalece. Ver `docs/operations/OUTPUT_PROTOCOL.md`.

## Respuestas a tareas originadas por otra IA
Además de la instrucción recibida en el chat, todo registro de respuesta de una solicitud interagente debe enlazar **ruta + SHA** del prompt completo en `prompts/inbox/<rol-destino>/REQ-YYYYMMDD-NNN.md`, el **ID de solicitud**, el rol emisor y receptor, y la respuesta sustantiva completa. Registrar ese enlace y el estado ANSWERED/BLOCKED en `prompts/ROUTING_INDEX.md` solo tras verificar el archivo publicado. La respuesta puede originar un nuevo prompt para otra IA, pero **debe depositarlo como archivo separado** y registrarlo en el índice; no usar el chat como canal de encargos. Véase `docs/operations/ROUTING_PROTOCOL.md`.
