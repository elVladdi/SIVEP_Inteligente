# ADR-0006 — Entrada por ruta y respuesta fuera del chat

- Estado: **Aceptada**
- Fecha: 2026-11-21
- Origen: instrucción explícita del responsable
- Issue: #6

## Decisión
1. El usuario **no copia los prompts**; solo facilita una ruta/URL para que el agente lea y verifique el archivo de su rol.
2. Cada IA debe publicar la **respuesta íntegra sustantiva** junto al prompt recibido y la versión SHA del prompt de rol en `docs/ai-logs/YYYY-MM-DD/<id>.md`.
3. El mensaje al chat contiene, salvo instrucción contraria, **solo la ubicación de la respuesta completa** (URL verificable, preferiblemente permalink al commit y sección de respuesta).
4. Si el agente no puede publicar o trabaja con contenido restringido, no inventará enlaces ni expondrá datos; deberá informar el bloqueo o usar custodia autorizada.
5. Esta regla rige para IA coordinadora, desarrolladora y auditora, y para INICIO y CONTINUACIÓN en cualquier plataforma.

## Consecuencias
La documentación, estado y decisiones quedan en GitHub; el chat actúa como punto de entrada y entrega de ubicación. El cumplimiento real requiere permisos de lectura/escritura y verificación de publicación. No sustituye auditoría independiente ni aprobación humana de PR.
