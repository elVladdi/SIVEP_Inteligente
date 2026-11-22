# Artículo 12 — Lee et al. (2021): clasificación de mercancías con recuperación de frases

## Ficha bibliográfica

- **Referencia:** Lee, E., Kim, S., Kim, S., Park, S., Cha, M., Jung, S., Yang, S., Choi, Y., Ji, S., Song, M., & Kim, H. (2021). *Classification of Goods Using Text Descriptions With Sentences Retrieval*. Versión PDF examinada **arXiv:2111.01663v1**, 2 de noviembre de 2021, 7 páginas.
- **Fuente:** https://arxiv.org/abs/2111.01663
- **Instituciones:** KAIST, Institute for Basic Science y Korea Customs Service.
- **Objeto:** predicción de códigos HS en el **capítulo 85**, con recuperación de frases y casos de clasificación histórica; **no** recupera valores de transacciones para valoración.
- **Localización:** Figura 1 (p. 4), Tabla 3 (p. 5), Figura 2 (p. 6), secciones IV–VI.

## 1. Problema y pregunta

Las declaraciones incluyen descripciones comerciales que no siempre se ajustan a la terminología normativa. El trabajo estudia una forma de recomendar **partidas HS4 y subpartidas HS6** y mostrar información documental que apoye el análisis experto.

La dificultad no se reduce a identificar palabras semejantes. Los documentos contienen notas y excepciones, y una subpartida puede requerir características técnicas precisas. La investigación combina clasificación supervisada con **recuperación de frases normativas**, en lugar de interpretar la clasificación como una sola etapa.

## 2. Datos y diseño

Se reúnen **129.084 casos históricos** del capítulo 85:
- **122.221** decisiones/casos internacionales.
- **6.863** casos coreanos, incluidos **6.434** ordinarios, **237** de Consejo y **192** de Comité.

La fuente institucional coreana citada es el **Customs Law Information Portal (CLIP)**. Tras depuración por cambios de códigos, los autores conservan alrededor de **126.000 casos**.

Se utiliza separación temporal: los últimos tres meses dan el conjunto de prueba (**1.466 internacionales + 186 coreanos = 1.652 casos**); los tres meses anteriores, la validación (**1.733 + 102 = 1.835 casos**). Esta estrategia reduce determinados riesgos de aprovechar información futura, pero no sustituye una auditoría de duplicados o de mantenimiento de nomenclatura.

El universo evaluado comprende **265 subpartidas HS6** del capítulo 85.

## 3. Arquitectura y modelos

La **Figura 1** representa tres etapas:

1. **Clasificación HS4:** descripción de la mercancía → **KoELECTRA** → candidatos de partida.
2. **Recuperación de frases (AIR):** a partir de la partida candidata, seleccionar frases relevantes del manual HS mediante **Alignment Information Retrieval**, similitud coseno entre términos y ponderación **IDF**.
3. **Clasificación HS6:** combinar descripción y frases recuperadas (variante) → KoELECTRA → subpartidas candidatas.

La aplicación presenta también **casos históricos similares** en la subpartida candidata, identificados por coseno entre embeddings de descripciones. Esto corresponde a **antecedentes de clasificación**, no a comparadores jurídicos de valor.

KoELECTRA utiliza representaciones de **768 dimensiones**, entrenamiento con entropía cruzada categórica y una configuración reportada de 50 épocas. Los autores mencionan una GPU TITAN Xp y costos computacionales de preparación y entrenamiento.

En la variante con evidencia se recuperan hasta **siete frases**.

## 4. Evaluación y métricas

La métrica principal es **Accuracy@K** de código arancelario: acierto si el HS correcto figura entre las primeras K propuestas. La calidad de frases se aborda separadamente con ejemplos de **precisión** y **recall** frente a frases seleccionadas por expertos.

### Resultados de clasificación (Tabla 3)

| Modelo | HS4 Top-1 | HS6 Top-1 | HS6 Top-3 | HS6 Top-5 |
|---|---:|---:|---:|---:|
| LSTM | 68,7 % | 43,1 % | 67,3 % | 74,7 % |
| **KoELECTRA sin frases** | 93,6 % | 89,1 % | **95,5 %** | **96,8 %** |
| KoELECTRA con frases | 93,6 % | **89,6 %** | 93,7 % | 94,4 % |

**Hallazgo crítico:** la incorporación de frases mejora ligeramente el **Top-1 HS6** (+0,5 pp), pero **reduce Top-3** (−1,8 pp) y **Top-5** (−2,4 pp). Por tanto, el máximo **95,5 %** presentado en el resumen corresponde a la **variante sin frases en la predicción**, no a una mejora causada por ellas.

La recuperación de evidencia puede ser útil para interpretación incluso cuando no mejora, o incluso empeora, la métrica de clasificación. Son resultados diferentes.

### Calidad de las frases y evaluación preliminar

- En un **ejemplo individual** sobre una cámara, los autores comunican **precisión 0,75** y **recall 0,75** entre frases recuperadas y utilizadas por especialistas. No es una media global.
- En una exploración adicional con **once decisiones no publicadas**, se menciona una exactitud Top-3 cercana a **0,82**. Esta muestra no permite inferencia robusta.

## 5. Aportaciones metodológicas

- Separación de **clasificación, búsqueda normativa y presentación de antecedentes**.
- Evaluación de ablación **con/sin frases** que cuestiona la presunción de mejora automática por añadir contexto.
- Uso de casos previos como evidencia de **clasificación** para análisis humano.
- Consideración de **orden temporal** en datos históricos.
- Reconocimiento explícito de que la puntuación de confianza del clasificador requiere calibración cautelosa.

## 6. Limitaciones

1. Cobertura limitada al capítulo 85 y a 265 subpartidas.
2. El alto Top-3 mide **código**, no mercancía comercialmente idéntica o similar.
3. La precisión/recall de evidencia se ilustran principalmente con un caso.
4. Los casos históricos son **resoluciones de clasificación** y no registros de transacciones de valor.
5. No mide corrección jurídica de una referencia de valoración ni estado de verificación del valor.
6. El corpus podría contener traducciones y cambios normativos difíciles de replicar.
7. El rendimiento de una muestra de once casos no equivale a prueba externa exhaustiva.

## 7. Relación con el artículo 11

Los artículos **12 y 11 comparten autores, instituciones y enfoque**; el 11 representa una ampliación de la línea investigadora, no una segunda validación totalmente independiente.

| Aspecto | Artículo 12 (2021) | Artículo 11 (versión estudiada 2023) |
|---|---|---|
| Capítulos | 85 | 84, 85 y 90 |
| Subpartidas | 265 | 925 |
| Clasificador destacado | KoELECTRA | KLUE-RoBERTa |
| Evidencia | Recuperación AIR, frases previas a HS6 | Recuperación documental apoyada en decisiones expertas |
| Evaluación con funcionarios | No equivalente | 32 funcionarios |

Las cifras Top-3 de ambos trabajos **no son comparables directamente** por cambios de datos, cobertura y protocolo.

## 8. Relevancia para SIVEP Inteligente

La contribución más importante es **demostrar experimentalmente que añadir más evidencia no garantiza mejorar la predicción**. En nuestro problema, una lista de referencias históricas puede parecer convincente sin ser técnicamente o jurídicamente pertinente; por eso la evidencia debe examinarse por su contenido y procedencia.

La separación entre **recomendación, recuperación documental y evaluación humana** constituye un antecedente de arquitectura explicable, no un resultado obtenido en valoración.

**Conclusión:** pertinencia **alta** para diseño y evaluación de evidencias; no acredita identidad/similitud de mercancías ni admisibilidad de antecedentes de valor.

**Lecturas relacionadas:** [11](11-lee-et-al-2024-explainable-customs.md), [7](07-kim-kim-choi-2025-the-rag.md) y [5](05-morgero-macedo-2025-articulo-17.md).
