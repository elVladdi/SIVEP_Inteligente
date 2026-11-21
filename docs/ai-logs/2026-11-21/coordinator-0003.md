# Interacción coordinator-0003 — consulta sobre continuidad de chats

- Fecha: 2026-11-21 (hora no registrada)
- Rol: coordinadora; proveedor OpenAI; modelo GPT-6
- Issue asociado: #5 (abierto en respuesta a aprobación posterior)
- Clasificación: PUBLICABLE
- Origen: conversación de este proyecto en ChatGPT
- Integridad: registro del texto visible. El diagrama de cajas se transcribe linealmente con todos sus textos; no es la serialización exacta de la presentación visual.

## Prompt completo del usuario

````text
Ahora, ese prompt también sirve para cuando la extensión del chat de una IA llega al máximo y obligatoriamente tengo que abrir otro chat pero en el mismo modelo (ChatGPT) y mismo proyecto y continuar exactamente donde se quedó, sin perder criterio, acuerdos ?
````

## Respuesta visible del asistente

**Sí. Los prompts que hemos creado también sirven para continuar el trabajo cuando un chat alcanza su límite de contexto**, incluso si abres otro chat dentro del mismo proyecto de ChatGPT y utilizas el mismo modelo.

Sin embargo, hay una distinción importante: **recuperar el contexto general del proyecto no es lo mismo que continuar exactamente donde terminó la conversación anterior**.

Nuestro sistema ya contempla la primera posibilidad, pero debemos reforzarlo para garantizar la segunda.

## ¿Cómo debería funcionar?

[Diagrama visible: Chat 1 — IA coordinadora: investiga, acuerda criterios, asigna tareas y toma decisiones aprobadas → Punto de control de continuidad: registra conversación, acuerdos, tareas activas, resultados y siguiente acción exacta → Repositorio SIVEP_Inteligente: fuente persistente de contexto, decisiones, código y trazabilidad → Chat 2 — IA coordinadora: lee el mismo prompt inicial, recupera el último estado validado y continúa la tarea pendiente.]

## ¿Qué debemos mejorar?

Propongo incorporar explícitamente dos modos de funcionamiento a los tres agentes:

| Modo | Comportamiento |
|---|---|
| **INICIO** | El agente no tiene una tarea anterior que continuar. Examina GitHub, identifica el estado del proyecto y recibe o propone una nueva tarea. |
| **CONTINUACIÓN** | El agente identifica la sesión anterior, recupera el último punto de control, las decisiones, los resultados y las tareas pendientes, y continúa desde allí. |

Además, cada sesión debe tener un **punto de control de continuidad** que registre:

1. Último objetivo en desarrollo y grado de avance.
2. Acuerdos aprobados y criterios metodológicos aplicables.
3. Alternativas evaluadas y razones para aceptarlas o descartarlas.
4. Tareas concluidas, pendientes y bloqueadas.
5. Archivos modificados, commits, pruebas y resultados.
6. **Siguiente acción exacta**, para evitar repetir trabajos anteriores.
7. Referencias a los prompts y respuestas completos de esa sesión.

Ese punto de control debe conservarse en GitHub y estar vinculado a la tarea. No necesitamos conservar el razonamiento interno privado del modelo: sí necesitamos preservar las decisiones, sus fundamentos explícitos y las evidencias que las sustentan.

## Mi recomendación

Convertiría los tres prompts actuales en **protocolos de inicio y recuperación de sesiones**, con la siguiente regla:

> Al iniciar cualquier conversación, independientemente de si se trata del mismo modelo, otro modelo o una plataforma diferente, el agente debe verificar el repositorio, recuperar el último estado documentado de su trabajo y determinar si corresponde iniciar una tarea nueva o continuar una anterior.
>
> Si continúa una tarea, no debe modificar los criterios o acuerdos aprobados ni repetir las actividades ya completadas sin una justificación documentada.

Esto también implica una obligación al finalizar una sesión: **guardar el punto de control antes de abandonar el chat**, siempre que sea posible.

Si un chat se interrumpe inesperadamente sin guardar el punto de control, el nuevo agente podrá reconstruir el último estado documentado, aunque no necesariamente todos los detalles del trabajo no registrado.

**En conclusión:** el esquema que ya creamos es la base adecuada. Mi propuesta es reforzarlo con un protocolo formal de continuidad de sesiones para las tres IA. Así la continuidad dependerá de GitHub y de los registros verificables, no de la memoria ni de la capacidad de contexto de cada modelo.

## Estado posterior

La propuesta fue aprobada por el usuario en el mensaje siguiente: «Aprobado». Véase coordinator-0004.md.
