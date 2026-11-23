# Artículo 10 — Brinkmann, Shraga y Bizer (2024): ExtractGPT y atributos no observados

## Ficha bibliográfica

- **Referencia:** Brinkmann, A., Shraga, R., & Bizer, C. (2024). *ExtractGPT: Exploring the Potential of Large Language Models for Product Attribute Value Extraction*. Versión examinada: **arXiv:2310.12537v5**, 20 de septiembre de 2024.
- **Fuente:** https://arxiv.org/abs/2310.12537
- **Instituciones:** Universidad de Mannheim y Worcester Polytechnic Institute.
- **Tipo:** estudio experimental de **extracción de atributos de productos** desde texto; no estima precios ni determina mercancías idénticas o similares.
- **PDF examinado:** 15 páginas; secciones 3–5, Tablas 1, 4–11 y Figuras 2–4.

## 1. Problema

Extraer información estructurada desde títulos de productos es difícil cuando hay pocos registros etiquetados, diversos atributos por categoría, valores muy poco frecuentes y nuevas marcas o versiones de productos. Los autores preguntan hasta qué punto modelos de lenguaje instruidos por prompts o ajustados mediante fine-tuning superan a los extractores especializados y **generalizan a valores no vistos**.

Este trabajo está relacionado con el artículo 9, pero **no evalúa como objetivo central la normalización de unidades, nombres o valores**. Estudia principalmente **extracción de pares atributo–valor** y adaptación a nuevos productos.

## 2. Datos experimentales

Se emplean dos conjuntos públicos de comercio electrónico:

| Característica | OA-Mine | AE-110K |
|---|---:|---:|
| Categorías seleccionadas | 10 | 10 |
| Atributos específicos | 115 | 101 |
| Productos entrenamiento, conjunto pequeño | 286 | 311 |
| Productos entrenamiento, conjunto grande | 1.452 | 1.568 |
| Productos de prueba | 491 | 524 |
| Pares atributo–valor en prueba | 2.451 | 1.482 |

Los autores emplean una partición estratificada por categoría y una variante de entrenamiento reducido, aproximadamente el **20 %** de los productos de entrenamiento. Según el conjunto y partición, **71–82 % de los valores únicos de prueba son no observados en el entrenamiento**.

La diferencia entre valores observados y no observados permite estudiar un riesgo de dominio que las métricas agregadas suelen ocultar: identificar nuevos códigos de modelo, medidas o denominaciones comerciales sin confundirlos con valores conocidos.

## 3. Arquitectura experimental

### 3.1. Modelos

- **LLM:** GPT-3.5 Turbo, GPT-4, **Llama 3 8B** y **Llama 3 70B**.
- **Baselines especializados:** SU-OpenTag, AVEQA y MAVEQA.
- **Ajuste especializado:** fine-tuning de GPT-3.5 en conjuntos de entrenamiento.
- **Condiciones:** temperatura 0 en inferencia; los modelos Llama se experimentaron con hardware local significativo (hasta cuatro GPU NVIDIA RTX A6000).

### 3.2. Representación del esquema y demostraciones

Se comparan cuatro representaciones de atributos:

| Esquema | Descripción |
|---|---|
| `list` | Solo lista nombres de atributos |
| `textual` | Nombres y definiciones en lenguaje natural |
| `compact` | Definiciones condensadas |
| `json` | Representación mediante JSON Schema |

El protocolo añade, según variante, **valores de ejemplo** y **demostraciones**. Algunas demostraciones se eligen por similitud semántica con embeddings. Su función es ilustrar cómo responder, **no certificar equivalencia entre el producto consultado y el ejemplo**.

La salida se expresa como pares atributo–valor, con representación de atributos ausentes. Un formato JSON válido **no demuestra que los valores sean correctos**.

## 4. Definición de evaluación

Los autores distinguen acierto en el valor predicho, valor incorrecto, extracción inventada cuando debía haber ausencia, omisión de un valor presente y detección correcta de ausencia. Calculan **precisión, recall y F1** con comparación contra anotaciones de referencia.

Al evaluar extracción, una representación distinta pero semánticamente equivalente puede resultar penalizada si no coincide con la forma de referencia. Por eso estos resultados no deben interpretarse como tasas de comparabilidad comercial.

## 5. Resultados principales

### Zero-shot y tipo de esquema

La representación más estructurada no gana sistemáticamente. Ejemplos de F1:

| Configuración | OA-Mine | AE-110K |
|---|---:|---:|
| GPT-4 + `list` | 69,1 % | 56,3 % |
| GPT-4 + `json` | 68,1 % | 62,1 % |
| Llama 3 8B + `json` | 43,2 % | 22,0 % |
| Llama 3 70B + `list` | 67,3 % | 58,9 % |

El tipo de esquema es una **variable experimental** dependiente del modelo y de los datos. JSON Schema no es una garantía general de mayor exactitud.

### Mejor resultado promedio de extracción

| Sistema | F1 promedio comunicado |
|---|---:|
| **ExtractGPT, GPT-4 + `json-val-dem`** | **84,9 %** |
| Llama 3 70B | 82,8 % |
| Llama 3 8B | 79,8 % |
| AVEQA, variante comparada | 79,8 % |
| SU-OpenTag, variante comparada | 79,7 % |

La configuración principal de ExtractGPT obtiene **82,2 % en OA-Mine** y **87,5 % en AE-110K**. No debe ordenarse este 84,9 % frente al 91,32 % del artículo 9: los corpus, tareas y condiciones son diferentes.

### Capacidad ante valores no vistos

En el subconjunto de valores no observados con entrenamiento pequeño:

| Modelo | F1 en valores no vistos |
|---|---:|
| **ExtractGPT** | **72,6 %** |
| AVEQA | 53,2 % |
| SU-OpenTag | 37,0 % |
| MAVEQA | 12,5 % |

La ventaja de ExtractGPT sobre AVEQA es de **19,4 puntos porcentuales** bajo esta configuración, pero el 72,6 % implica todavía errores relevantes. La publicación demuestra generalización **relativa dentro de estas colecciones de comercio electrónico**, no exactitud perfecta sobre marcas/modelos nuevos en aduanas.

### Fine-tuning y transferencia entre dominios

Una versión ajustada de GPT-3.5 presenta resultados competitivos dentro del conjunto conocido, pero cuando se ajusta sobre uno de los corpus y se prueba en el otro disminuye el desempeño. Ejemplos de F1 documentados:

| Evaluación | Configuración de referencia no ajustada | Ajuste con el otro corpus |
|---|---:|---:|
| OA-Mine | 69,8 % | 53,9 % |
| AE-110K | 74,4 % | 55,9 % |

Estos datos advierten sobre **especialización y generalización fuera del dominio**, sin demostrar que todo fine-tuning sea perjudicial.

## 6. Fortalezas metodológicas

1. Varios modelos y baselines, con diferentes esquemas de salida.
2. Estudio separado de **muestras pequeñas** y **conjuntos mayores**.
3. Evaluación explícita de **valores no vistos**, útil para productos comerciales cambiantes.
4. Análisis de transferencia entre conjuntos, no únicamente validación dentro de uno.
5. Código y recursos experimentales referenciados por los autores, aunque las versiones concretas de modelos y datos condicionan una réplica.

## 7. Limitaciones

- Datos de **comercio electrónico**, no registros DAM.
- Los títulos de productos y las descripciones aduaneras pueden tener diferente detalle.
- F1 de extracción no mide identificación de mercancías comparables.
- La evaluación no pondera separadamente errores críticos de **marca, modelo, capacidad, material o condición**.
- No distingue suficientemente normalización y verificación documental; esa tarea se estudia específicamente en el artículo 9.
- La generalización a nuevos **productos, familias y sitios** es más amplia que la generalización a valores no vistos bajo particiones de estos dos corpus.
- Ningún resultado informa calidad de referencias de valor histórico ni aplicación de métodos de valoración.

## 8. Contribución científica y alcance

La principal contribución consiste en evaluar **extracción de valores de atributos previamente no observados** y el efecto de diferentes esquemas de prompt y cantidades de entrenamiento. El artículo distingue errores de extracción, omisión y predicción de valores ausentes.

Los resultados muestran ventajas condicionadas de modelos de lenguaje frente a extractores especializados, pero también pérdidas de rendimiento cuando los modelos ajustados se trasladan entre corpus. El estudio no evalúa la equivalencia comercial de productos ni la validez jurídica de referencias de valoración.

**Lecturas relacionadas:** [9 — extracción y normalización](09-brinkmann-baumann-bizer-2024-wdc-pave.md), [14 — preparación de EDI](14-pain-2021-clasificacion-transfer-learning.md) y [15 — interpretación de atributos](15-yang-et-al-2025-hscodecomp.md).

## 9. Conclusión

ExtractGPT constituye evidencia de **pertinencia muy alta** sobre extracción con pocos ejemplos y productos con valores nuevos. Su desempeño no debe confundirse con *product matching*, clasificación arancelaria ni valoración aduanera.
