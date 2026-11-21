# Prompt interagente — REQ-YYYYMMDD-NNN

> Plantilla. Guardar copia como `prompts/inbox/<rol-destino>/REQ-YYYYMMDD-NNN.md`. **No crear una tarea real sin issue o autorización documentada.**

- **ID:** REQ-YYYYMMDD-NNN
- **Creado en UTC:**
- **Emisor (rol):** coordinator | developer | auditor
- **Destinatario (rol):** coordinator | developer | auditor
- **Solicitante humano/autorización:** issue / instrucción aprobada / estado PROPOSED
- **Issue y/o PR:**
- **Referencia base:** rama + SHA comprobados
- **Estado inicial en índice:** PROPOSED | READY
- **Prioridad:** ordinaria | alta (justificada)
- **Requiere decisión humana:** sí | no, motivo
- **Prompt del rol destinatario:** `prompts/<ROL>.md` (leer versión actual en el repo)
- **Privacidad:** PUBLICABLE | RESTRINGIDO (en este último caso no guardar texto confidencial aquí)

## Contexto mínimo verificable
[Hechos, enlaces a ADR, checkpoint, informe, issue o código. Diferenciar hallazgos, hipótesis y decisiones.]

## Instrucción concreta al destinatario
[Qué debe hacer, por qué, entregable esperado; no introducir objetivos fuera del issue.]

## Archivos y fuentes autorizados
[Rutas exactas; datos sintéticos o permitidos.]

## Restricciones y límites de autoridad
[El rol que audita no se autoaprueba; los cambios metodológicos o de alcance requieren decisión humana.]

## Criterios de aceptación
1. [Verificable]
2. [Verificable]

## Salida y trazabilidad
- Respuesta completa en `docs/ai-logs/YYYY-MM-DD/<id-unico>.md` con ID, ruta+SHA de esta solicitud, resultado íntegro y pruebas.
- Estado y enlace de respuesta en `prompts/ROUTING_INDEX.md`.
- En el chat únicamente la ubicación verificada de la respuesta, salvo instrucción expresa diferente.

## Siguiente paso o ruta de escalamiento
[Qué hacer si está bloqueada; a qué rol dirigir eventual solicitud adicional.]
