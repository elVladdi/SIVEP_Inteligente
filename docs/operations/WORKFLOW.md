# Flujo de trabajo supervisado y documentado

## Participantes
- **Responsable humano:** aprueba objetivos, decisiones, resultados y autorización para compartir información.
- **IA coordinadora:** traduce requerimientos en tareas, genera prompts versionados, identifica bloqueos, consolida hallazgos; mantiene PROJECT_STATE.md y ADR.
- **IA desarrolladora:** implementa en rama acotada, prueba y propone cambios por PR.
- **IA auditora:** verifica de forma independiente diseño, pruebas, seguridad, resultados y trazabilidad.
- **Colaboradores humanos:** investigación, código, revisión y etiquetado experto autorizado.

## Ciclo obligatorio
1. Issue con propósito, entradas, salidas, restricciones, criterios y versión base.
2. Prompt del coordinador al desarrollador, registrado.
3. Respuesta del desarrollador y cada iteración, registradas.
4. Revisión por auditor con prompt y respuesta completos, registrados.
5. Correcciones, pruebas y registro de cada intercambio adicional.
6. Revisión humana, ADR si se adopta decisión, actualización de estado y cierre de issue.

## Trazabilidad de una respuesta
Cada respuesta pertenece a un registro de docs/ai-logs/ con identificador, rol, proveedor, modelo si consta, fecha, issue, versión base, prompt, respuesta, artefactos y clasificación de confidencialidad. Los pasos de otros chats no se importan automáticamente: requieren exportación o registro por el agente con acceso al repo.

## Puertas de calidad
Sin fusión si faltan pruebas, falta auditoría exigida, existe fuga de datos, los experimentos no son reproducibles o no están registradas las interacciones IA relevantes. El auditor no sustituye la aprobación humana.