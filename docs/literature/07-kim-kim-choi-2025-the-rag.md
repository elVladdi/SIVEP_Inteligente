# Artículo 7 — Kim, Kim y Choi (2025): THE-RAG para recomendar códigos arancelarios

## Ficha bibliográfica

**Referencia:** Kim, H., Kim, G., & Choi, K. (2025). *Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework*. **The Journal of Information Systems / 정보시스템연구, 34**(3), 167–189.  
**DOI:** https://doi.org/10.5859/KAIS.2025.34.3.167  
**Idioma:** coreano, con resumen en inglés en la p. 188.  
**Institución:** Hanbat National University, Corea del Sur.  
**Tipo de evidencia:** estudio experimental de clasificación HS6 con recuperación documental y LLM. **No** mide similitud de mercancías para valoración.  
**Fuente examinada:** PDF de **23 páginas** proporcionado por el responsable. Referencias: Figura 2 (p. 173), Figura 4 (p. 176), Tablas 1–3 (pp. 178–181), Tablas 4–6 (pp. 182–183).

> **Numeración:** este es el séptimo artículo definitivo. Sustituye en la serie al artículo *An Ensemble Deep Learning Framework for Automated HS Code Classification in International Trade*, cuyo PDF no se consiguió. No deben mezclarse resultados de ambos.

## 1. Problema y objetivos

Identificar correctamente códigos arancelarios es complejo por la diversidad de mercancías, las descripciones técnicas extensas y la estructura jerárquica de capítulos, partidas y subpartidas. Una respuesta basada solo en conocimiento interno de un LLM puede omitir información normativa o confundir denominaciones.

La investigación busca determinar:
1. Si combinar **recuperación densa, BM25 y reranking** mejora las recomendaciones frente a un LLM sin RAG.
2. Cómo influye la **segmentación de documentos en chunks** de diferentes tamaños.
3. Cuánto incide la capacidad del LLM para comprender **textos técnicos en coreano**.
4. Si un razonamiento **jerárquico en dos etapas** permite recomendar códigos de seis dígitos.

Los autores denominan la solución **THE-RAG**, *Two-stage Hybrid-rEranking RAG*.

## 2. Arquitectura de recuperación

La Figura 2, p. 173, representa el siguiente ciclo:

**Consulta de producto** → recuperación **densa** (embeddings de Transformer y similitud coseno, **Top-3**) **en paralelo** con recuperación **sparse BM25** (**Top-3**) → unión de hasta seis documentos → **reranking** → selección de **Top-3** → incorporación del contexto al LLM.

El procedimiento completo se ejecuta en **dos etapas**:
- **Primera:** recuperar documentación y predecir hasta **tres capítulos HS2**.
- **Segunda:** utilizar esos capítulos como filtro de búsqueda, recuperar el contexto correspondiente y generar **tres subpartidas HS6** con una justificación textual.

Los investigadores mencionan **ColBERT** y la *late interaction* de tokens como técnica de reordenamiento. El documento usa ocasionalmente la etiqueta “cross-encoder”, pero ColBERT **no debe equipararse sin más a un cross-encoder clásico** que procesa conjuntamente consulta y documento en cada inferencia.

**Observación técnica:** las señales léxicas y semánticas pueden recuperar documentos distintos; BM25 privilegia términos exactos, los embeddings aproximan expresiones y el reranking reordena los candidatos combinados. El artículo no separa de forma completa las ganancias de cada componente.

## 3. Corpus, normalización y chunks

El índice documental se construye con fuentes coreanas de:
- **Arancel / nomenclatura:** capítulos, partidas, subpartidas y códigos nacionales.
- **Notas explicativas HS:** documentación por capítulo y partida.
- **Casos oficiales de clasificación:** descripciones de mercancías con códigos determinados, utilizados en la evaluación.

Los autores describen una estructura de aproximadamente **97 capítulos, 1 228 partidas y 5 609 subpartidas**.

La Figura 4 (p. 176) distingue dos colecciones: documentos de **nivel capítulo** y documentos de **nivel partida**, enriquecidos con metadatos de niveles inferiores, como `chapter_code`, `heading_code` y `HSK_code`.

Los chunks evaluados contienen **250, 500, 1 000, 1 500, 2 000, 2 500, 3 000 y 3 500 tokens**.

### Por qué importa el chunking

Los textos normativos y de mercancías pueden tener diferentes niveles jerárquicos y detalles. Un chunk corto puede excluir información determinante; uno grande puede incluir ruido, fragmentos irrelevantes o demasiado contexto para el LLM.

La **unidad de recuperación** y la **fragmentación de documentos normativos** son decisiones diferentes. El estudio no demuestra que fragmentar una descripción comercial corta en chunks extensos mejore su clasificación.

## 4. Diseño experimental

La primera evaluación utiliza **100 casos oficiales de clasificación**. Las descripciones tienen promedios informados de **101,14 tokens** y **225,38 caracteres**.

Los autores miden **Accuracy@1** y **Accuracy@3** a nivel capítulo HS2, partida HS4 y subpartida HS6. La métrica indica si el código correcto aparece dentro de las primeras K recomendaciones **del sistema completo**.

Se comparan:
- Gemini 1.5 Flash y Gemini 1.5 Flash 8B con THE-RAG.
- Los mismos LLM sin recuperación documental, bajo un baseline de instrucciones **CoT**.
- Diferentes tamaños de chunks.
- En un experimento aparte, Llama 3.1 8B y EXAONE 3.5 7.8B, en condiciones de chunking más restringidas.

La investigación **no ofrece un estudio de ablación exhaustivo** que aísle el aporte independiente de BM25, embeddings, ColBERT y jerarquización.

## 5. Resultados iniciales — 100 casos

### Tabla de exactitud para subpartida HS6

| Configuración | Sin RAG (CoT) | Mejor THE-RAG | Diferencia |
|---|---:|---:|---:|
| Gemini 1.5 Flash, **Top-1** | 23 % | **43 %** | +20 pp |
| Gemini 1.5 Flash, **Top-3** | 44 % | **60 %** | +16 pp |
| Gemini 1.5 Flash 8B, **Top-1** | 5 % | **25 %** | +20 pp |
| Gemini 1.5 Flash 8B, **Top-3** | 8 % | **33 %** | +25 pp |

Fuentes: **Tablas 1 y 2, pp. 178–179**.

Para Flash, el mejor Top-3 HS6 aparece con **3 000 tokens**; el mejor Top-1 HS6, con **3 500 tokens**. Por tanto, **no existe un único tamaño de chunk óptimo para todas las métricas**.

Los autores reportan para la diferencia de **60 % contra 44 %** una prueba de **McNemar**, `chi² = 8,03`, `p = 0,0046`. Esta evidencia se refiere a la comparación de clasificaciones bajo la configuración señalada; **no** valida directamente la recuperación de mercancías comparables.

### Evolución de Top-3 HS6 con el tamaño del chunk (Gemini 1.5 Flash)

| Tokens | Top-3 HS6 |
|---:|---:|
| 250 | 44 % |
| 500 | 44 % |
| 1 000 | 47 % |
| 1 500 | 51 % |
| 2 000 | 59 % |
| 2 500 | 58 % |
| **3 000** | **60 %** |
| 3 500 | 56 % |

La exactitud aumenta al incorporar contexto **hasta cierto punto**, y después puede retroceder.

## 6. Evaluación ampliada — 1 000 casos

La sección §4.4 aumenta el conjunto a **1 000 casos**, divididos en diez bloques de 100. Los datos cubren **71 capítulos**, aunque seis (85, 39, 90, 84, 64 y 23) representan **51,4 %** del conjunto.

| Modelo y objetivo | THE-RAG Top-3 | Sin RAG Top-3 | Diferencia |
|---|---:|---:|---:|
| Gemini 1.5 Flash 8B — HS6 | **24,3 %** | 8,3 % | +16 pp |
| Gemini 1.5 Flash — HS6 | **49,3 %** | 30,4 % | +18,9 pp |
| Gemini 1.5 Flash — HS4 | **66,5 %** | 56,6 % | +9,9 pp |

Fuentes: **Tablas 4–6, pp. 182–183**. Para el conjunto ampliado los autores usan una configuración de **2 500 tokens**, seleccionada según el diseño de validación descrito.

**Hallazgo:** al ampliar la muestra, el rendimiento del modelo Flash en HS6 disminuye de **58 % a 49,3 %** para la configuración de 2 500 tokens. El 60 % del experimento inicial con otra configuración **no debe presentarse como desempeño general del sistema**.

### Advertencia editorial

En Tablas 5 y 6 algunas filas están rotuladas `gemini-1.5-flash-8b` pese a que sus títulos y la discusión describen `gemini-1.5-flash`. La matriz de revisión sigue el texto y el título, **dejando constancia de la inconsistencia**.

## 7. Comparación adicional de LLM (500 tokens)

| Modelo | Top-3 HS6 sin RAG | Top-3 HS6 con THE-RAG |
|---|---:|---:|
| Gemini 1.5 Flash 8B | 8 % | **24 %** |
| Llama 3.1 8B | **14 %** | 9 % |
| EXAONE 3.5 7.8B | 2 % | **7 %** |

En esa configuración, **RAG perjudica el resultado de Llama**. Por tanto, la mejora no es universal ni depende simplemente del número de parámetros. Los autores relacionan resultados con la comprensión del coreano, pero la tabla por sí sola **no demuestra** una jerarquía general de capacidad lingüística entre modelos.

## 8. Limitaciones

1. Problema de **clasificación arancelaria**, no de equivalencia de mercancías para valoración.
2. Evalúa **respuesta final del RAG**, no Recall@k del retriever ni Precision@k de documentos.
3. No separa completamente contribuciones de cada componente en experimentos de ablación.
4. Modelos/hiperparámetros de recuperación no documentados con detalle suficiente para réplica exacta.
5. La evidencia de explicación textual no incluye una métrica formal de **fidelidad a fuentes normativas**.
6. Resultado sensible al chunk, modelo y composición de casos; alta concentración de la muestra en seis capítulos.
7. Debe verificarse la separación entre ejemplos de evaluación y documentos de decisiones históricas utilizados para indexar: el artículo no aporta una auditoría completa de fugas de respuesta.

## 9. Contribución metodológica y condiciones de validez

El trabajo estudia una arquitectura de **recuperación híbrida y reordenamiento** para apoyar la clasificación HS mediante documentación oficial. Los experimentos muestran mejoras respecto del LLM sin RAG bajo determinadas configuraciones, pero también degradaciones para otros modelos y tamaños de fragmento.

La evaluación mide **acierto de código arancelario**, no exhaustividad ni precisión de los documentos recuperados y tampoco equivalencia entre mercancías. La falta de ablaciones completas y el posible solapamiento entre decisiones indexadas y casos evaluados limitan la atribución causal de las mejoras.

## 10. Conclusión

THE-RAG combina **recuperación léxica y semántica, reordenamiento y razonamiento jerárquico**. Sus resultados acreditan mejoras condicionadas de clasificación HS, pero no demuestran calidad de emparejamiento entre mercancías individuales.

**Relacionados:** [6 — TF-IDF y SBERT](06-bayona-2025-transposicion-hs.md), [1 — agrupamiento de mercancías](01-vijayakumar-2025-india.md), [5 — validación de referencias](05-morgero-macedo-2025-articulo-17.md).

---
*Resumen basado en texto, figuras y tablas del artículo coreano. Se conservan sus inconsistencias editoriales sin inventar correcciones.*
