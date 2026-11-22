# Artículo 14 — Pain (2021): clasificación HS desde documentación EDI mediante embeddings

## Ficha bibliográfica

- **Autor:** Koustav Pain (Tukai).
- **Título:** *Harmonized System Code Classification Using Transfer Learning with Pre-Trained Weights*.
- **Institución:** Dalhousie University (Canadá).
- **Tipo:** **tesis de maestría** en Ciencias de la Computación, julio de **2021**, **89 páginas**; **no** revista revisada por pares.
- **Fuente primaria:** PDF completo proporcionado. Capítulos 5–6; Figura 5.1; Tablas 6.1–6.8; especial atención a pp. 48–58 de la numeración interna y pp. 60–70 del archivo.
- **Objeto:** limpieza de documentos de transporte **EDI** y recuperación de códigos HS a partir de descripciones comerciales; **no** valoración de mercancías.

## 1. Problema

Los manifiestos y mensajes de transporte intercambiados por **Electronic Data Interchange** combinan términos de productos con códigos HS, contenedores, campos logísticos, direcciones, pesos, fechas y formatos inconsistentes. No siempre existe una descripción comercial clara que pueda utilizarse directamente en clasificación.

El autor estudia cómo:
1. Extraer información pertinente de archivos EDI heterogéneos.
2. Limpiar las descripciones para aislar el producto.
3. Recomendar códigos HS mediante clasificación supervisada o **similitud textual semántica (STS)**.

El problema real del estudio es recuperar **códigos**, no determinar equivalencia comercial entre dos mercancías.

## 2. Datos

Se analizaron datos de **siete transportistas**, de los cuales **cuatro** contribuyen al experimento principal por disponibilidad/calidad de datos.

| Conjunto | Transacciones evaluadas |
|---|---:|
| Shipper 1 | **9.684** |
| Shipper 2 | **6.823** |
| Shipper 3 | **12.248** |
| Shipper 4 | **4.264** |
| **Total** | **33.019** |

El autor describe más de 30.000 documentos EDI, sin que el número de documentos y de transacciones tenga que ser idéntico. Los datos reales están sujetos a **confidencialidad**, lo cual limita la reproducción independiente.

## 3. Arquitectura

### 3.1. Parsing documental

Se evalúan herramientas de lectura EDI y se construye un parser mediante **expresiones regulares** adaptado a formatos diversos. La tesis indica que fueron necesarias alrededor de **107 expresiones adicionales** para variaciones de códigos HS, e informa aproximadamente **87 % de exactitud** del parser.

La fuente no permite reconstruir plenamente denominador, tipos de error y exactitud por campo; **87 % no equivale a extracción correcta de marca, modelo o capacidad**.

### 3.2. Normalización del texto comercial

Se emplean limpieza de ruido, corrección ortográfica, traducción al inglés y reducción de información no considerada útil para clasificar.

Ejemplo del capítulo 5: de una descripción de pescado que contiene datos de logística y temperatura, queda aproximadamente:

```text
wet salted saithe pollachius virens
```

Se conservan atributos taxonómicos pertinentes para el código, eliminando detalles logísticos.

**Riesgo para SIVEP:** una limpieza que elimina números, modelos, pesos, cantidades, composición o capacidades puede ser inadecuada para determinar identidad/similitud comercial, aunque sea aceptable en algunos escenarios de clasificación HS. La representación debe evaluarse contra el objetivo concreto.

### 3.3. Métodos de predicción

Se exploran:
- **NER** (spaCy) para identificar entidades/productos.
- **Naive Bayes**, **Random Forest** y **SVM**, entrenados con características TF-IDF.
- **Similitud semántica (STS)** entre embeddings de la descripción de la operación y descripciones oficiales HS.

En STS se comparan **Universal Sentence Encoder (USE)**, **InferSent**, BERT/DistilBERT, RoBERTa y **XLM-R multilingüe**, empleando coseno y recomendaciones Top-k.

El título menciona *transfer learning* por reutilización de modelos preentrenados, pero **no** implica un entrenamiento contrastivo de producto de la clase estudiada en Text2Trade.

## 4. Resultados de NER y clasificación tradicional

| Método | Precisión | Recall | F1 |
|---|---:|---:|---:|
| NER spaCy | 14,32 % | 27,22 % | **18,77 %** |
| Naive Bayes | 31,46 % | 46,22 % | **37,44 %** |
| Random Forest | 27,57 % | 34,13 % | 30,50 % |
| SVM | **37,26 %** | **48,42 %** | **42,11 %** |

Las cifras corresponden a las condiciones descritas en Tablas 6.1 y 6.2, con conjuntos/casos delimitados. No constituyen una comparación universal de estas familias de algoritmos: las clases escasas y descripciones ruidosas hacen especialmente difícil el aprendizaje supervisado.

## 5. La métrica «recommendation precision@10» no es Precision@10 convencional

La tesis distingue entre:
- **Precision@k estándar:** cantidad de resultados relevantes entre los primeros k, dividida por k.
- **Precisión de recomendación@k** creada para el estudio: asigna acierto cuando el código deseado aparece en las primeras posiciones, incluso si otros candidatos comparten significado pero no el código esperado; se aproxima a un **Hit@k** promediado.
- **Recall@k**: proporción de resultados relevantes de un grupo de código presentes entre los primeros k, usando una definición de relevancia más amplia que la de etiqueta exacta.

El autor **evita construir F1** con esta precisión particular y recall porque no representan el par convencional. Es fundamental **no** comparar su «precision de recomendación» con Precision@10 de recuperación de mercancías individuales.

El protocolo también prevé recall = 1 en determinados casos con denominador de resultados relevantes igual a cero, una convención que puede afectar medias.

## 6. Resultados STS por transportista

Las Tablas 6.4–6.7 identifican las configuraciones destacadas para cada grupo:

| Grupo | Modelo destacado | «Precisión de recomendación@10» | Recall@10 |
|---|---|---:|---:|
| Shipper 1 | USE Large v5 | **53,15 %** | **75,24 %** |
| Shipper 2 | USE Large v5 | **70,10 %** | **81,36 %** |
| Shipper 3 | XLM-R multilingüe | **50,11 %** | **71,05 %** |
| Shipper 4 | USE Large v5 | **58,31 %** | **73,68 %** |

En el Shipper 3, con terminología más heterogénea o multilingüe, XLM-R supera a USE bajo la métrica de recomendación; los conjuntos también difieren por distribución de productos, por lo que no se puede atribuir la diferencia exclusivamente al idioma.

USE presenta un rendimiento favorable en tres grupos pese a que algunos competidores obtienen mejores puntuaciones en benchmarks generales STS. **El rendimiento externo en tareas lingüísticas no asegura superioridad sobre datos aduaneros/EDI concretos**.

### Comparación exploratoria con HScodeNet

La Tabla 6.8 presenta pocos ejemplos con traducción al mandarín y restricciones de longitud; los sistemas no se evalúan en un benchmark homogéneo. No permite concluir que USE supere en general a HScodeNet.

## 7. Rendimiento y reproducción

La tesis informa que una fase computacional permite procesar aproximadamente **10.000 transacciones en menos de un minuto con GPU**, y que la solución se usó en un entorno del colaborador. No queda probado el tiempo integral de interpretación desde EDI bruto hasta validación humana ni una evaluación independiente de producción.

Los originales son confidenciales; la investigación no publica una matriz de errores completa por tipo de producto o un protocolo de reproducción suficiente para replicar todas las cifras.

## 8. Fortalezas y limitaciones

**Fortalezas:**
- Documentos operativos reales, menos limpios que textos académicos.
- Compara extracción, clasificadores y embeddings.
- Presenta resultados separados por **transportista**.
- Discute métricas Top-k adaptadas y efectos del idioma.
- Identifica que limpieza y disponibilidad de atributos alteran la tarea.

**Limitaciones:**
1. Documentos y etiquetas no públicos; reproducción incompleta.
2. «Precisión de recomendación» no equivalente a Precision@k estándar.
3. Eliminar números y características puede alterar **identidad comercial**.
4. No usa etiquetas expertas de mercancías idénticas/similares.
5. Recomendación de HS ≠ referencia de valor de transacción.
6. Los resultados por grupos no incluyen un análisis causal del papel de idioma o ruido.
7. La comparación con HScodeNet es exploratoria.

## 9. Aportación a SIVEP Inteligente

Contribuye principalmente a comprender **la relación entre preprocesamiento de descripciones comerciales y calidad de la recuperación**. El aporte es metodológico: una transformación de texto útil para el código HS podría destruir atributos esenciales para comparar mercancías históricas.

Se relaciona directamente con [extracción de atributos (9)](09-brinkmann-baumann-bizer-2024-wdc-pave.md), [ExtractGPT (10)](10-brinkmann-shraga-bizer-2024-extractgpt.md), [Bayona (6)](06-bayona-2025-transposicion-hs.md) y [Text2Trade (13)](13-ravi-et-al-text2trade-mnrl-mcd.md).

**Conclusión:** pertinencia **alta para preparación de texto y recuperación**, sin aportar un método validado de mercancías idénticas/similares para valoración.
