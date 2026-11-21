# Artículo 3 — Chan, Ng y Chung (2023): detección de anomalías con NLP y regresión probabilística

## Ficha bibliográfica

**Referencia:** Chan, B., Ng, I., & Chung, N. (2023). *Anomaly detection in trade declarations using deep learning techniques: A risk-assessment approach to identify misclassification and incorrect valuation*. **Statistical Journal of the IAOS, 39**, 825–834.  
**DOI:** https://doi.org/10.3233/SJI-230081  
**Institución:** Census and Statistics Department, Hong Kong, China.  
**Tipo de evidencia:** investigación experimental aplicada a validación de datos estadísticos del comercio; no determina valores aduaneros conforme a métodos de la OMC.  
**Fuente examinada:** PDF proporcionado; Figuras 2 y 4–9 y Tablas 1–2, páginas 825–834.

## 1. Problema investigado

Hong Kong recibe del orden de **20 millones de declaraciones comerciales anuales**. La autoridad estadística necesita detectar errores en código de mercancía, valor, cantidades y otras variables, sin inspeccionar individualmente cada registro.

El procedimiento convencional puede utilizar **rangos por código arancelario**. Pero un mismo código cubre mercancías de calidad y naturaleza diversas: un rango para todos los productos puede ser tan amplio que no identifique un error de una mercancía específica.

La pregunta técnica es si los textos comerciales pueden proporcionar información suficiente para **estimar un rango de valor condicionado al producto**, en vez de comparar únicamente contra una media de la partida.

**Contexto jurídico:** Hong Kong es, con carácter general, un puerto libre y el problema institucional inmediato del estudio es la **calidad de las estadísticas de comercio**, no el rechazo del valor de transacción por una aduana de valoración.

## 2. Solución: tres modelos complementarios

El sistema incluye:
1. **Clasificación de códigos arancelarios** a partir de descripciones.
2. **Detección de anomalías del valor unitario**, condicionada a la descripción y demás datos.
3. **Detección de anomalías del valor total**, útil para distinguir discrepancias de precio de posibles errores en cantidades.

Las funciones comparten parte de la arquitectura de procesamiento de texto, pero deben evaluarse por separado.

### 2.1. Representación especializada del texto

Los autores utilizan limpieza y segmentación de textos comerciales chinos y **Word2Vec** para producir representaciones de términos. Informan que las alternativas preentrenadas públicas no satisfacían completamente sus necesidades y entrenaron embeddings usando **más de diez millones de descripciones comerciales únicas**.

**Resultado conceptual:** la terminología real de las declaraciones justifica evaluar representaciones adaptadas al dominio, no confiar automáticamente en embeddings genéricos.

### 2.2. Clasificación de mercancías

Usan una **Gated Convolutional Neural Network (GCNN)** con mecanismos de selección de características y *focal loss* para tratar el desequilibrio entre clases. La entrada combina descripción, origen y destino; la salida es una distribución de probabilidades sobre códigos.

Para predicciones cuya probabilidad mayor excede **0,7**, los autores informan mayor exactitud que en el conjunto completo, a costa de cubrir una menor proporción de registros.

### 2.3. Regresión probabilística de valor unitario

El modelo predice los parámetros de una distribución del **logaritmo del valor unitario**:

```text
log(valor_unitario) | atributos  ~  Normal(mu(atributos), sigma²(atributos))
```

En una aproximación, los límites se construyen a partir de `exp(mu ± k*sigma)`, con multiplicadores experimentales señalados alrededor de **3–5**. El objetivo es detectar operaciones con valores incompatibles con la distribución prevista para la **descripción específica de la mercancía**, no fijar un precio mínimo.

Los atributos mencionados incluyen descripción, código arancelario corregido y países de origen/destino.

### 2.4. Modelo de valor total

Se estima también una distribución del importe total. La comparación entre **total compatible** y **unitario anómalo** puede señalar un error de cantidad, en vez de un error en el precio de la mercancía.

## 3. Ejemplo ilustrativo: oro y plata bajo el mismo código

Las Figuras 4 y 5 presentan operaciones con **monedas de oro y de plata** clasificadas bajo una misma línea HKHS, **71189000**.

El rango convencional para ese código era aproximadamente **HK$0,2 a HK$3 366 por gramo**: demasiado amplio para discriminar adecuadamente. El artículo muestra una moneda de oro a **HK$9,6/g** y una de plata a **HK$740/g**, valores que el rango único no detectaría como inconsistentes.

Los intervalos condicionados al producto incorporan información textual: para oro, un límite inferior aproximado de **HK$110/g**; para plata, un límite superior aproximado de **HK$87/g**. Las dos declaraciones se señalan como anomalías bajo la metodología propuesta.

**Interpretación:** el producto concreto importa más que una categoría arancelaria genérica para explicar la variabilidad del valor. Son ejemplos del estudio, no referencias de mercado reutilizables.

## 4. Datos, evaluación y resultados

Los experimentos se centran en dos capítulos HKHS: **71** (joyería, metales y productos relacionados) y **8** (frutas y frutos). Se indica una partición aleatoria **80/20** de entrenamiento y prueba para el problema de clasificación.

### Clasificación

| Métrica | Capítulo 71 | Capítulo 8 |
|---|---:|---:|
| Exactitud global | **89,4 %** | **96,5 %** |
| Cobertura con probabilidad máxima > 0,7 | 72,7 % | 95,6 % |
| Exactitud dentro de predicciones > 0,7 | 98,2 % | 99,1 % |

La exactitud condicionada a umbral no debe citarse sin señalar que se aplica a un **subconjunto seleccionado**.

### Anomalías de valor unitario

| Capítulo | F1 | Exactitud |
|---|---:|---:|
| 71 | **70,5 %** | **86,6 %** |
| 8 | **80,8 %** | **99,1 %** |

Los autores comparan resultados favorables frente a reglas convencionales, que alcanzan alrededor de **50 % de F1** en los escenarios descritos.

### Anomalías de valor total

Se reporta **F1 = 81,6 %** en una prueba **simulada** del capítulo 71, introduciendo anomalías artificiales en aproximadamente **5 %** del conjunto de evaluación. No debe confundirse con ese mismo rendimiento sobre errores reales verificados.

## 5. Fortalezas metodológicas

- Incorpora realmente las **descripciones comerciales** como variables predictivas.
- Distingue rangos **condicionados por producto**, frente a rangos generales por código HS.
- Utiliza regresión probabilística, no una única predicción de precio.
- Diferencia incoherencias de **valor unitario** e **importe total**.
- Expone métricas y ejemplos concretos, útiles para diseñar una comparación experimental.

## 6. Limitaciones y precauciones

1. No recupera ni muestra **declaraciones históricas individuales** que sustenten una referencia.
2. No acredita identidad/similitud jurídica entre mercancías.
3. Su finalidad es asegurar estadísticas comerciales, no realizar valoración fiscal.
4. La evaluación se concentra en dos capítulos; la generalización a otras mercancías requiere pruebas.
5. Las pruebas con división aleatoria pueden beneficiarse de patrones repetidos o conocimiento del futuro en un despliegue retrospectivo; conviene evaluar por tiempo.
6. La prueba de valor total utiliza **anomalías simuladas**, por lo que no sustituye casos reales validados.
7. Un intervalo predictivo no es un **valor de transacción de mercancía idéntica/similar** y no puede reemplazar la aplicación de los métodos de valoración.

## 7. Aporte a SIVEP Inteligente

**Componente respaldado:** análisis de valores y estimación estadística **una vez** identificada correctamente la mercancía.

Propuestas propias para experimentos posteriores:
- Comparar **mediana/cuántiles de antecedentes recuperados** con **regresión probabilística por atributos** y modelos predictivos de cuantiles.
- Definir cuidadosamente el **valor unitario**, moneda, Incoterm/base FOB-CIF y unidad comercial antes de entrenar.
- Evaluar intervalos con **cobertura**, anchura media, error y calibración por familia comercial.
- Contrastar discrepancias de precio unitario con valor total y cantidad para diferenciar tipos de errores.
- Mostrar de forma explícita la diferencia entre **valor histórico documentado** y **estimación probabilística del modelo**.
- Aplicar exclusivamente indicadores para el especialista, nunca valores mínimos automáticos.

## 8. Conclusión

El artículo demuestra experimentalmente que **interpretar la descripción comercial mejora el análisis contextual del valor** frente a rangos gruesos por código. Es una referencia fuerte para un **módulo posterior de estimación y anomalías**, pero **no resuelve el primer problema de SIVEP: recuperar DAM de mercancías idénticas o similares y acreditar su comparabilidad**.

**Relacionados:** [2 — distancias/LOF](02-alqaryouti-2024-dubai.md), [5 — condiciones jurídicas](05-morgero-macedo-2025-articulo-17.md), [8 — solución integrada](08-outram-swartz-2026-fronteras.md).

---
*Resultados reproducidos de las tablas del PDF. No constituyen tasas esperadas para SUNAT.*
