# Artículo 4 — Alwanin et al. (2026): clasificación de fraude y priorización económica con DXGBA

## Ficha bibliográfica

**Referencia:** Alwanin, R., Ben Ismail, M. M., & Bchir, O. (2026). *Customs fraud detection using a gradient boosting approach for joint classification and risk estimation*. **Scientific Reports, 16**, artículo 3432.  
**DOI:** https://doi.org/10.1038/s41598-025-33382-z  
**Contexto:** experimentos sobre un conjunto sintético inspirado en declaraciones de importación de Corea.  
**Tipo de evidencia:** artículo experimental supervisado; los resultados **no** provienen de recaudación real observada.  
**Fuente:** PDF completo proporcionado; Tablas 2–6, Figura 7 y apartado de datos/limitaciones.

## 1. Problema de investigación

La administración no solo debe detectar operaciones irregulares, sino decidir **cuáles investigar primero cuando la capacidad de fiscalización es limitada**. Dos declaraciones con probabilidad de incumplimiento comparable pueden representar consecuencias económicas diferentes. Un clasificador binario aislado no necesariamente maximiza los resultados del control.

El artículo propone entrenar conjuntamente una función de **clasificación de fraude** y otra de **regresión de una magnitud económica**, con el objetivo operativo de ordenar las declaraciones para auditoría.

La cuestión es distinta de la identificación de mercancías idénticas/similares. Aquí se analizan **operaciones y operadores**, no equivalencia semántica o técnica de descripciones comerciales.

## 2. Modelo DXGBA

**DXGBA** significa *Dual-learning XGBoost-Based Approach*: un marco inspirado en gradient boosting donde clasificación y regresión comparten información del proceso de aprendizaje.

Su objetivo combina, en términos generales:
- **Pérdida de clasificación:** entropía cruzada binaria para distinguir fraude/no fraude.
- **Pérdida de regresión:** error cuadrático para la variable económica.
- **Regularización:** restricciones a la complejidad de los árboles.

El documento desarrolla gradientes, segundas derivadas y ganancia de particiones en sus ecuaciones; se realiza búsqueda de hiperparámetros.

Una configuración destacada usa **learning rate 0,1, max depth 16, subsample 0,8, L1 0,5, L2 0,5 y gamma 1**. Estas cifras son propias del experimento y **no** parámetros recomendados automáticamente para SIVEP.

## 3. Conjunto de datos y variables

Se utilizaron **54 000 registros sintéticos generados con CTGAN**, en lugar de declaraciones reales directamente examinables, por limitaciones de confidencialidad.

De los campos disponibles, se seleccionaron **18 variables de entrada** y dos objetivos, identificados como:
- `Fraud`: etiqueta binaria.
- `Item price`: variable monetaria usada como objetivo de regresión en el conjunto.

Entre las entradas aparecen **HS6, peso neto, origen, país de embarque, importador, vendedor, declarante, transportista, datos del procedimiento, aduana, fecha y variables tributarias**.

**Hallazgo de lectura crítica:** el texto afirma que **78,42 %** de los registros son fraudulentos y **21,58 %** no fraudulentos, pero luego trata el fraude como clase minoritaria al justificar SMOTE. La inconsistencia debe consignarse; no es correcto resolverla silenciosamente suponiendo cuál frase es errónea.

**Otra imprecisión:** el trabajo presenta la regresión como estimación de ingresos tributarios potencialmente perdidos, aunque la variable objetivo de la Tabla 2 es `Item price`. La transformación jurídica/económica entre precio y tributos recuperables no queda suficientemente documentada.

## 4. Preparación y entrenamiento

El estudio presenta una evaluación con **validación cruzada de cinco particiones** y búsqueda de hiperparámetros. Examina:
- **SMOTE**, para generar observaciones sintéticas de la clase minoritaria.
- **Random Undersampling (RU)**, para reducir la clase mayoritaria.
- Combinaciones de ambos procedimientos.
- Codificación y normalización de características.

Selecciona la configuración **10 % SMOTE + RU**, por obtener el mejor F1 entre las opciones examinadas. También analiza **embeddings basados en hojas de árboles** y **autoencoders** para construir representaciones adicionales.

La existencia de embeddings en esta investigación **no significa que se hayan codificado semánticamente las descripciones de mercancías**: se refiere fundamentalmente a variables tabulares.

## 5. Resultados de clasificación

La Tabla 4 compara DXGBA con otros clasificadores:

| Modelo | Exactitud | Precisión | Recall | F1 | AUC |
|---|---:|---:|---:|---:|---:|
| Regresión logística | 51,72 % | 0,2427 | 0,5837 | 0,3428 | 0,5614 |
| XGBoost | 71,75 % | 0,4007 | 0,6225 | 0,4875 | 0,7592 |
| DATE | 56,47 % | 0,3140 | **0,8273** | 0,4528 | 0,7558 |
| **DXGBA** | **71,94 %** | **0,4039** | 0,6305 | **0,4923** | **0,7638** |

DXGBA presenta el mejor F1 y AUC de esos comparadores, pero la diferencia de F1 frente a XGBoost es **pequeña** (0,4923 frente a 0,4875). DATE ofrece mayor recall con una compensación negativa en precisión.

La Tabla 3 ilustra la sensibilidad al remuestreo: sin SMOTE, DXGBA alcanza **82,44 % de exactitud, precisión 0,8589, recall 0,2227 y F1 0,3536**; con 10 % SMOTE + RU, los valores cambian a **71,94 %, 0,4039, 0,6305 y 0,4923**.

**Conclusión:** optimizar F1 o recall no es equivalente a minimizar la carga de revisión humana. Cada métrica responde a un objetivo diferente.

## 6. Resultados de priorización económica

El resultado más llamativo se refiere al porcentaje de magnitud económica acumulada al revisar un subconjunto priorizado:

| Fracción de operaciones revisadas | Cobertura económica reportada |
|---|---:|
| 2 % | 44,07 % |
| 5 % | 65,22 % |
| **10 %** | **87,98 %** |
| 20 % | 92,80 % |

Estas cifras proceden de **simulaciones sobre datos sintéticos**, no de una fiscalización que haya cobrado efectivamente esos importes. El texto contiene además una cifra de **88,63 %** en un pasaje para 10 %, distinta del **87,98 %** de la Tabla 5. La matriz de revisión emplea la cifra tabulada y registra la discrepancia.

Las variantes con embeddings y autoencoders no mejoran el F1 respecto al DXGBA original, aunque algunas mejoran métricas aisladas. Es evidencia contra la idea de que más complejidad implica mejor desempeño global.

## 7. Explicabilidad mediante SHAP

Los autores utilizan **SHAP** para interpretar contribuciones de variables como peso, código HS y condiciones tributarias en las predicciones.

Pero una explicación SHAP (“este atributo elevó la probabilidad de fraude”) **no equivale** a una explicación documental de valoración (“estas DAM históricas corresponden a mercancías comparables por atributos verificables”). Para SIVEP serán dos explicaciones potencialmente complementarias, con obligaciones de evidencia distintas.

## 8. Limitaciones de validez

1. Datos **sintéticos**: no se demuestra rendimiento con declaraciones reales.
2. Inconsistencia textual en la prevalencia de fraude.
3. Ambigüedad entre **item price** y tributos potencialmente recuperables.
4. No incorpora texto descriptivo de mercancía como mecanismo de matching.
5. No prueba generalización temporal a operaciones futuras.
6. Un alto porcentaje económico simulado no demuestra valor fiscal determinado o recaudación efectiva.
7. El sistema se basa en etiquetas; una DAM nunca revisada **no debe convertirse automáticamente en etiqueta de ausencia de fraude**.

## 9. Aporte a SIVEP Inteligente

**Etapa apropiada:** priorización de DAM con posible subvaloración para **control posterior**, una vez que existan comparabilidad, señales de valor y resultados de revisión confiables.

Experimentos propios sugeridos:
- Comparar rankings por **probabilidad de alerta**, **brecha porcentual de valor**, **impacto tributario estimado** y un **modelo conjunto**.
- Usar métricas **Precision@presupuesto**, lift y porcentaje de resultados verificados capturados con capacidad de revisión fija.
- Tratar **no inspeccionado** como estado desconocido; controlar sesgo de selección de los controles previos.
- Verificar calendarios, costos de falsos positivos y incertidumbre de cálculos económicos.

**No usar DXGBA como sustituto del recuperador de mercancías** ni asumir el 87,98 % como beneficio esperable.

## 10. Conclusión

El artículo aporta una arquitectura y métricas para **priorización del riesgo económico**; su valor para el primer experimento de identificación de mercancías es limitado. Su evidencia fiscal es simulada y debe citarse con esa salvedad.

**Relacionados:** [2 — anomalías de valoración](02-alqaryouti-2024-dubai.md), [3 — intervalos predictivos](03-chan-ng-chung-2023-hong-kong.md), [8 — plataforma integral](08-outram-swartz-2026-fronteras.md).

---
*Las cifras son de un estudio con datos sintéticos. No constituyen resultados institucionales de SUNAT.*
