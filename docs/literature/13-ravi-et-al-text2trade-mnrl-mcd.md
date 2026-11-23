# Artículo 13 — Ravi et al.: Text2Trade, recuperación semántica e incertidumbre

## Ficha bibliográfica

- **Autores:** Meenu Ravi, Jacob Howard, Grace Kenneally y Ari Fleischer.
- **Título:** *Text2Trade: A Semantic Search System with Monte Carlo Dropout Uncertainty Quantification for HS Code Retrieval*.
- **Institución:** The MITRE Corporation (EE. UU.).
- **Tipo de fuente:** **manuscrito de 5 páginas**, identificado como CHIIR '26. **No debe citarse como publicación definitiva en ACM sin verificación editorial**: el PDF conserva metadatos de plantilla, una fecha discordante y DOI incompleto.
- **Fuente examinada:** PDF aportado; Tablas 1–3, pp. 3–4; metodología y evaluación de secciones 3–4.
- **Objeto:** búsqueda y ranking de **códigos HS** a partir de descripciones de productos, no recuperación de operaciones individuales de valor histórico.

## 1. Problema de investigación

Una descripción comercial puede contener sinónimos, abreviaturas y términos distintos de los utilizados por la nomenclatura. Un buscador léxico puede no recuperar el código relevante si las expresiones no coinciden literalmente.

Los autores estudian dos cuestiones:

1. Si los **embeddings especializados mediante aprendizaje contrastivo** mejoran la recuperación de códigos frente a modelos preentrenados y baselines léxicos.
2. Si el **Monte Carlo Dropout (MCD)** permite explorar la estabilidad del ranking y mejorar la posición de los códigos correctos.

El segundo punto no debe confundirse con estimar una probabilidad legal de clasificación: estabilidad de una salida y corrección de la salida son conceptos diferentes.

## 2. Datos y particiones

Se recopilan resoluciones o registros comerciales de **CBP CROSS** (EE. UU.), **EBTI** (Unión Europea) y material de **USTR**, según el alcance declarado en el manuscrito.

| Partición | Descripciones | Códigos HS únicos | Longitud promedio |
|---|---:|---:|---:|
| Entrenamiento | **171.247** | 4.924 | 158 tokens |
| Prueba completa | **37.794** | 3.470 | 169 tokens |
| Prueba reducida | **1.000** | 598 | 172 tokens |

Las coberturas de códigos se calculan contra un universo de **6.895 códigos**: entrenamiento 71,4 %, prueba 50,3 % y prueba reducida 8,7 %.

Se usa una división **aleatoria** aproximadamente 80/20. El PDF no documenta una auditoría exhaustiva de registros duplicados o semánticamente próximos entre particiones, ni una partición retrospectiva temporal; por ello, las cifras no demuestran necesariamente recuperación de productos nuevos bajo desplazamiento temporal real.

## 3. Arquitectura de Text2Trade

### Embeddings

Se parte de **`all-MiniLM-L6-v2`**, un bi-encoder Sentence-BERT. Cada consulta y código/documento candidato recibe un embedding; la similitud coseno determina un ranking.

### Aprendizaje contrastivo con MNRL

El entrenamiento usa **Multiple Negatives Ranking Loss (MNRL)**, que favorece que un par descripción–código etiquetado se acerque en el espacio vectorial frente a negativos.

Los autores introducen negativos jerárquicos difíciles:
- Otros códigos dentro de la misma **partida HS4**.
- Alternativas del mismo **capítulo HS2**.
- Negativos aleatorios si no existen suficientes casos cercanos.

El objetivo de entrenamiento es **distinguir códigos**, no separar dos mercancías de distinta marca/modelo que comparten el mismo código. Por tanto, **las etiquetas HS no equivalen a etiquetas de identidad/similitud comercial**.

### Monte Carlo Dropout

En inferencia se habilita dropout para producir **50 ejecuciones estocásticas** y estudiar la variación de candidatos.

Se agregan:
- **Coseno medio** de cada código.
- **Frecuencia de aparición en el Top-3**.

La puntuación final informada es:

```text
score(c) = 0,8 × coseno_promedio(c) + 0,2 × frecuencia_Top3(c)
```

Los pesos son específicos del estudio. La puntuación **no está calibrada como probabilidad de que un código sea correcto**.

## 4. Definiciones de métricas

| Indicador | Qué mide aquí |
|---|---|
| Recall@1, @3, @5, @10 | Aparición del código correcto dentro de K candidatos |
| nDCG@10 | Ordenamiento de resultados, ponderando primeras posiciones |
| MAP@10 | Calidad promedio del ranking respecto a códigos relevantes |

No son Precision@k de DAM históricas comerciales. Cuando existe un único código de referencia por consulta, Recall@k se interpreta en la práctica como éxito de recuperación de ese código hasta la posición k.

## 5. Resultados principales: **prueba completa de 37.794 consultas**

| Sistema | Recall@1 | Recall@3 | Recall@5 | Recall@10 | nDCG@10 | MAP@10 |
|---|---:|---:|---:|---:|---:|---:|
| **Text2Trade con MNRL, sin MCD** | **74,0 %** | **91,0 %** | **94,0 %** | **97,0 %** | **0,851** | **0,774** |
| BM25 | 54,4 % | 72,7 % | 78,6 % | 83,8 % | 0,689 | 0,612 |

La Tabla 2 compara además SVM, LSTM, MiniLM preentrenado y MPNet preentrenado. La mejora frente a BM25 demuestra ventaja del **modelo especializado en esa tarea de recuperación de códigos HS**, no superioridad general sobre textos DAM o comparabilidad de mercancías.

**Precaución esencial:** el **97,0 %** de la prueba completa corresponde a Text2Trade **sin MCD**. No atribuir el **97,8 %** del otro experimento a esta muestra.

## 6. Ablación MNRL + MCD en **1.000 consultas**

| Configuración | Recall@1 | Recall@3 | Recall@10 |
|---|---:|---:|---:|
| SBERT preentrenado | 10,0 % | 19,3 % | 30,9 % |
| SBERT + MCD | 19,9 % | 27,1 % | 44,3 % |
| SBERT + MNRL | 70,6 % | 87,2 % | 95,7 % |
| **SBERT + MNRL + MCD** | **74,3 %** | **87,5 %** | **97,8 %** |

La mejora de MCD respecto a **MNRL sin MCD** es de **+3,7 puntos** en Recall@1, **+0,3** en Recall@3 y **+2,1** en Recall@10. La ganancia mucho mayor respecto del modelo preentrenado procede del **ajuste contrastivo**, no de MCD por sí solo.

### Variación por sector

El artículo informa Recall@10 de aproximadamente **96 % en textiles**, **89 % en maquinaria** y **78 % en químicos/farmacéuticos**. No se incluyen suficientes conteos e intervalos para atribuir esas diferencias únicamente al tipo de mercancía.

## 7. Costos, límites y discrepancias editoriales

1. Se informa una latencia de unos **13,30 ms por consulta** para una configuración **sin MCD**; no representa necesariamente el costo de 50 pasadas estocásticas.
2. La evaluación **no** documenta robustamente rendimiento en mercancías comerciales nuevas con división temporal.
3. Un código de entrenamiento cubre **solo parte** del universo de códigos utilizado.
4. MCD cuantifica principalmente **variación del ranking**, no confianza legal ni calibración de clasificación.
5. La formulación editorial de una mejora porcentual del 74 % frente al preentrenado no se deriva de manera transparente de las cifras de Recall@10 mostradas: conservar **las cifras de la tabla y la muestra correspondiente**.
6. El manuscrito tiene **metadatos de conferencia de plantilla**, sin DOI editorial verificable en la versión suministrada.
7. Los algoritmos optimizan **recuperación de códigos**, no correspondencia entre registros de la misma mercancía.

## 8. Contribución metodológica y alcance

Text2Trade evidencia, en las pruebas comunicadas, el efecto del **aprendizaje contrastivo MNRL** sobre recuperación de códigos HS y el aporte adicional de MCD a la estabilidad y ordenamiento de candidatos. Los negativos difíciles se generan según cercanía en la jerarquía de códigos.

Las etiquetas positivas corresponden a **códigos**, no a parejas de productos idénticos o similares. Una misma subpartida puede contener mercancías con distintas especificaciones; por ello, el rendimiento de recuperación de códigos no debe interpretarse como precisión de emparejamiento comercial.

## 9. Relación con evidencia previa

El trabajo de [Bayona (6)](06-bayona-2025-transposicion-hs.md) aborda una tarea distinta de correspondencia de líneas arancelarias; sus métricas no son directamente comparables con las de Text2Trade.

Otros trabajos relacionados: [Kim et al. (7)](07-kim-kim-choi-2025-the-rag.md) sobre recuperación híbrida y [Pain (14)](14-pain-2021-clasificacion-transfer-learning.md) sobre embeddings en documentación EDI.

**Conclusión:** pertinencia **alta para recuperación semántica**, pero sin resultados directos de mercancías idénticas/similares ni valores históricos admisibles para valoración.
