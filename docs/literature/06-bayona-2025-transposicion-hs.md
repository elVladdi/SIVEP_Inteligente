# Artículo 6 — Bayona (2025): transposición de líneas arancelarias con TF-IDF y Sentence-BERT

## Ficha bibliográfica

**Referencia:** Bayona, P. (2025). *Beyond Six Digits: Automated Tariff Line HS Transposition Using Natural Language Processing*. **WTO Staff Working Paper ERSD-2025-04**. Organización Mundial del Comercio, 25 de marzo de 2025.  
**Fuente institucional:** documento de trabajo de la OMC; **no** debe presentarse como revista revisada por pares ni como posición oficial de la OMC.  
**Objeto:** correspondencia entre líneas arancelarias de las versiones **SA 2017 y SA 2022**, más allá de los seis dígitos.  
**Fuente examinada:** PDF proporcionado. Tablas 4, 8, 13 y 14; gráfico 1; sección sobre puntuaciones de coseno y errores de matching.

## 1. Problema de investigación

Cuando se revisa el Sistema Armonizado, las líneas arancelarias nacionales pueden cambiar, subdividirse o reagruparse. Un analista que intenta unir series de comercio de distintos años debe transponer miles de líneas de una versión a otra.

El trabajo manual resulta laborioso y complejo porque una línea puede tener:
- Un código distinto después de la revisión.
- Una descripción reformulada o abreviada.
- Un texto escueto, como «Los demás», cuyo sentido depende de capítulos y partidas superiores.
- Relaciones uno-a-uno, uno-a-varios o varios-a-uno.

La autora pregunta cómo **automatizar correspondencias con reglas y similitud de textos**, reduciendo tiempo de trabajo sin perder exactitud.

**Diferencia respecto de SIVEP:** compara **textos normativos de líneas arancelarias**, no descripciones de DAM individuales ni antecedentes de valoración. Por eso sus resultados no miden el reconocimiento de mercancías jurídicamente idénticas/similares.

## 2. Diseño metodológico de tres rondas

### Ronda 1 — correspondencias determinísticas

Se emplean tablas oficiales de correlación entre versiones del SA y relaciones estructurales de códigos. Las correspondencias con una única alternativa válida pueden asignarse sin IA.

### Ronda 2 — coincidencia exacta de descripciones

Las líneas no resueltas se comparan por igualdad textual, considerando también descripciones de niveles superiores cuando la línea nacional aislada no es informativa.

### Ronda 3 — similitud NLP para casos difíciles

Se comparan dos técnicas:
- **TF-IDF:** vectores ponderados por relevancia de palabras y frecuencia documental.
- **Sentence-BERT (SBERT):** embeddings de oraciones con representación semántica.

En ambos casos se utiliza la **similitud coseno** entre vectores. Se compara el mejor candidato solo entre **líneas permitidas por las correlaciones SA6**, lo que reduce falsos candidatos.

Las decisiones se someten a **verificación humana línea por línea**. Esta evaluación humana constituye un elemento fuerte del diseño, aunque responde a correspondencia normativa y no a valoración de mercancías.

## 3. Datos

La investigación utiliza dos economías anonimizadas:

| Característica | Economía A | Economía B |
|---|---|---|
| Dificultad de las descripciones | Relativamente sencilla | Técnica y más compleja |
| Líneas procesadas | **7 946** | **9 802** |
| Versiones del SA | 2017 → 2022 | 2017 → 2022 |
| Métodos en ronda 3 | TF-IDF y SBERT | TF-IDF y SBERT con/sin subencabezados |

Se utilizan nomenclaturas reales y reglas/correlaciones institucionales. El caso práctico se relaciona con necesidades de armonización arancelaria surgidas durante análisis vinculados con la adhesión de Perú al CPTPP, según la descripción contextual de la autora.

## 4. ¿Cuántos casos resuelve cada etapa?

| Método | Economía A | Economía B |
|---|---:|---:|
| Ronda 1: regla de código/correlación | 4 044 (50,9 %) | 3 418 (34,9 %) |
| Ronda 2: texto exacto | 3 727 (46,9 %) | 5 773 (58,9 %) |
| Ronda 3: similitud textual | **175 (2,2 %)** | **611 (6,2 %)** |
| **Total** | **7 946** | **9 802** |

Esto significa que las reglas y coincidencias exactas procesan **97,8 %** de la economía A y **93,8 %** de la B, antes de utilizar embeddings. Las técnicas de IA se reservan para una fracción pequeña pero ambigua y costosa de analizar manualmente.

**Interpretación:** antes de adoptar modelos complejos debemos medir cuánto puede resolverse mediante campos estructurados, coincidencia exacta normalizada y reglas de dominio.

## 5. Resultados del método comparativo en la ronda 3

| Escenario de comparación | TF-IDF | SBERT | Resultado |
|---|---:|---:|---|
| Economía A (más sencilla) | **81,1 %** | **90,1 %** reportado | Gana SBERT |
| Economía B con subencabezados añadidos | **85,4 %** | **83,5 %** | Gana TF-IDF |
| Economía B sin subencabezados añadidos | **85,6 %** | **89,5 %** | Gana SBERT |

Los porcentajes son **exactitudes de correspondencia de líneas en la fase evaluada**, no medidas de Precision@k de mercancías en SIVEP.

**Nota de auditoría:** el documento comunica **90,1 %** para SBERT de economía A, pero uno de los recuentos tabulados permite obtener una cifra levemente distinta según cómo se sumen categorías. Mantener la cifra publicada **con nota de inconsistencia aritmética**, no corregir la fuente sin validación.

## 6. Desempeño general y tiempo

La automatización completa informa **99,6 % de exactitud global** para economía A y **98,8 %** para economía B. Esas cifras **incluyen las rondas determinísticas**, no la exactitud aislada de SBERT.

Los tiempos computacionales de la ronda NLP (Tabla 13) son:

| Economía | TF-IDF | SBERT |
|---|---:|---:|
| A | 1,2 min | 4,4 min |
| B | 1,6 min | 6,1 min |

La publicación estima que el proceso operativo completo puede reducir de **2–3 semanas a aproximadamente medio día**, hasta **30 veces más rápido**, con verificación humana. El tiempo total de operación no debe confundirse con el tiempo de ejecución de un algoritmo.

## 7. Hallazgo crítico: coseno alto NO garantiza correspondencia correcta

La sección sobre similitud coseno informa:

| Tipo de correspondencia | SBERT, media de coseno | TF-IDF, media de coseno |
|---|---:|---:|
| Correcta | 0,82 | 0,80 |
| Incorrecta | 0,81 | 0,80 |

Algunos emparejamientos **incorrectos de SBERT llegan a 0,98** y los de TF-IDF también pueden alcanzar puntuaciones muy altas. El solapamiento muestra que **un umbral universal de coseno no prueba equivalencia**.

Este hallazgo es prioritario para SIVEP: una similitud de 0,95 entre dos descripciones no demuestra que sean mercancías idénticas, especialmente si difieren en una característica decisiva.

## 8. Análisis de errores técnicos

El artículo estudia fallos por:
- **Negaciones y desigualdades:** eliminar «no excede» o un límite numérico puede invertir el significado de una subpartida.
- **Unidades y dimensiones:** tamaños y medidas son decisivos en categorías de productos.
- **Sinónimos especializados:** TF-IDF puede reconocer mejor algunos nombres químicos como *bromomethane/methyl bromide* en contextos concretos; SBERT puede acercarse erróneamente a una categoría genérica.
- **Denominaciones científicas y textos técnicos:** las palabras exactas pueden ser más informativas que la similitud semántica general.
- **Enriquecimiento excesivo de la descripción:** añadir subencabezados a SBERT puede introducir ruido y disminuir la exactitud.

**Implicación:** preservar números, símbolos, capacidad, marca, modelo, proporciones, negaciones y unidades; no asumir que todo enriquecimiento textual es beneficioso.

## 9. Fortalezas y limitaciones

**Fortalezas:** comparación directa de dos representaciones, reglas simples como línea base, candidatos restringidos, verificación humana, discusión de errores y tiempos.

**Limitaciones:**
- Nomenclaturas oficiales más estandarizadas que descripciones libres de DAM.
- No analiza valores monetarios ni condiciones de venta.
- No determina identidad/similitud jurídica.
- SBERT no aparece adaptado mediante entrenamiento específico de descripciones comerciales.
- Compara principalmente una correspondencia final, no exhaustivamente rankings de antecedentes Top-5/Top-10.
- El éxito global depende ampliamente de las reglas de las dos primeras rondas.

## 10. Experimentos derivados para SIVEP

**Diseño inicial sugerido por nuestra investigación:**

1. **Coincidencia exacta estructurada:** atributos técnicos normalizados por tipo de producto.
2. **Baseline TF-IDF + coseno** para recuperación de antecedentes.
3. **SBERT + coseno**, verificando idioma español y terminología de importaciones.
4. **Combinación híbrida** y reranking opcional.
5. **Filtros arancelarios experimentales:** comparar SA6, NANDINA8 y subpartida nacional solo cuando definamos la familia piloto.
6. **Evaluación humana:** múltiples etiquetas de comparabilidad; medir Precision@k, Recall@k, *false-identical rate*, cobertura y latencia.
7. **Ablaciones:** descripción libre sola versus texto más atributos; preprocesamiento con y sin conservación de modelos/números; reglas estrictas frente a filtros flexibles.

**No asumir** que la mayor exactitud de transposición arancelaria se replica en mercancías de SIVEP.

## 11. Conclusión

El sexto trabajo es una **referencia metodológica prioritaria para nuestro primer experimento**: demuestra ventajas y límites de TF-IDF, SBERT, restricciones por código y verificación humana. Su hallazgo más importante es que **la similitud numérica no sustituye la evaluación de características discriminantes**.

**Relacionados:** [1 — India](01-vijayakumar-2025-india.md), [7 — THE-RAG](07-kim-kim-choi-2025-the-rag.md).

---
*Documento de trabajo de la OMC; se cita como investigación de su autora y no como regla oficial de valoración.*
