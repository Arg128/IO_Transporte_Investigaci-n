# Borrador del Proyecto - Modelo de Transporte

## 1. Definición de la Función Objetivo

### ¿Qué se optimiza?
El modelo decide **cuánto enviar** y **cómo hacerlo** en la red logística de Arequipa.

### Aspectos clave a definir

- **Cantidad a enviar:** desde un origen hacia un destino (transporte desde $i \to j$) para minimizar costos o minimizar tiempo.
- **Momento del envío:** especificar el intervalo temporal (días/semanas/horas) en el que se asigna el flujo.
- **Rutas disponibles:** elegir según el croquis de carreteras (arcos) y posibles conexiones (transbordo).
- **Capacidad de carga:** respetar la capacidad máxima de transporte (peso/vehículo) y/o capacidad de nodos si aplica.

---

## 2. Formulación del Modelo (Modelo Matemático y Estructura)

### Estructura de red
Construir un croquis de transporte con transbordo:
- **Nodos:** orígenes, puntos intermedios y destinos
- **Arcos:** carreteras/rutas

### Costos y parámetros
- Incorporar costos (flete y/o costos logísticos asociados a rutas)
- Beneficios si aplica
- Tiempos de recorrido por ruta

### Variables de decisión
Representar el flujo que viaja por cada arco (o la asignación origen–destino, según el nivel de detalle que se use).

### Función objetivo

- **Principal:** minimizar costo total
- **Alternativa:** minimizar tiempo total
- **Posible variante:** minimizar costo ponderado por tiempo (tiempo + costo con ponderación)

---

## 3. Restricciones (Garantizar Factibilidad y Operación)

- **Oferta y demanda:** respetar oferta en orígenes y satisfacer demanda en destinos.
- **Capacidad de transporte / capacidad de nodos:** no exceder el límite de carga por vehículo o por ruta; si hay nodos con capacidad, imponer su límite.
- **Cumplimiento de demanda:** no dejar demanda sin atender (o permitirlo solo si el modelo contempla penalización/insatisfacción).
- **Seguridad/operación:** incorporar límites por ruta (por ejemplo, restricciones de peso o condiciones operativas definidas en el caso).
- **No negatividad:** flujos/variables deben ser $\geq 0$.

---

## 4. Decisión Final (Qué se Reporta en "Decisión")

La salida operativa final del modelo se resume en:

1. **Plan de envíos óptimo:** cantidad por ruta/arco y/o asignación origen–destino.
2. **Elección de rutas** que mejor optimicen el objetivo (costo y/o tiempo).
3. **Utilización de capacidades:** qué rutas/vehículos se saturan y cuáles tienen holgura.
4. **Comparación de escenarios:** base vs. optimizado.

---

## 5. Metodología

### 5.1 Recolección de datos
- Descripción del sistema logístico en Arequipa: identificar orígenes, nodos intermedios (si aplica) y destinos.
- **Supuestos:** detallar por qué se simplifica el sistema (p. ej., un producto agregado, capacidades constantes, intervalos fijos, etc.).

**Datos requeridos:**
- Matriz de costos (y/o costos logísticos por ruta)
- Matriz de distancias/tiempos
- Ofertas y demandas
- Capacidades (vehículos y/o nodos)
- Restricciones operativas (si existen)

### 5.2 Retroanálisis del modelo seleccionado (para las pruebas)
- Realizar una revisión (estado del arte / retrospectiva) del modelo elegido: transporte clásico, flujo en redes, min-cost flow, etc.
- Identificar supuestos típicos, variables usuales y métodos de solución (para justificar la elección de estrategia computacional y pruebas).

### 5.3 Definición de objetivos según el marco teórico
Traducir el marco teórico a:
- Función objetivo (min costo / min tiempo / costo + tiempo ponderado)
- Criterios de evaluación
- Métricas a reportar (costo total, tiempo total, factibilidad, uso de capacidad, etc.)

### 5.4 Construcción del modelo matemático
Definir:
- Variables (flujo por arco o asignación)
- Función objetivo
- Restricciones de oferta/demanda, capacidades, cumplimiento y operación

### 5.5 Implementación computacional (software)

**Pila tecnológica:**
- **Kimai:** herramienta principal para correr/estructurar experimentos o prototipos
- **Python / OR-Tools (CP-SAT):** para modelos exactos y/o enfoques híbridos con restricción

**Alternativas según implementación:**
- Python + Pyomo (si se usa para formular y resolver)
- Pandas/NumPy para preprocesamiento
- Matplotlib/Seaborn para visualizaciones
- Jupyter + Git para reproducibilidad

### 5.6 Diseño experimental
Definir escenarios y condiciones comparables:

**Escenario A (sin optimización):**
- Rutas "usual" o un método base (asignación proporcional / heurística simple)

**Escenario B (optimizado):**
- Solución con el modelo matemático (y, si aplica, con procedimientos exacto + heurístico + metaheurístico)

### 5.7 Ejecución y análisis de resultados

**Comparar:**
- Costo total
- Tiempo total
- Uso/carga de capacidades (qué tan cerca se está de saturar)
- Cumplimiento de restricciones

**Incluir análisis de sensibilidad:**
- +10% demanda
- -10% costo por ruta
- Variación de capacidad o "cierre" de una ruta (si se puede simular)

---

## 6. Análisis y Conclusión

### Resultados que se deben demostrar

**Evidencia de mejora de Escenario B sobre Escenario A:**
- Reducción de costo y/o tiempo
- Mejor distribución del flujo
- Menores violaciones o mayor cumplimiento de restricciones

**Explicación de por qué el modelo elige esas rutas:**
- Relación entre costos/tiempos/capacidades

**Hallazgos clave por sensibilidad:**
- Cómo cambia la solución ante variaciones

### Conclusiones

Concluir respecto al/los objetivos:
- Si se logró minimizar costo, tiempo o costo + tiempo
- Cuáles rutas/arcos dominan el plan óptimo
- Qué restricciones resultaron "críticas" (las más limitantes)
- Aterrizarlo al contexto Arequipa (implicancia logística para la red de distribución de carga agroexportable)

---

## 7. Preguntas para Cerrar el Modelo

1. ¿El modelo será transporte clásico (origen → destino sin intermedios) o flujo en red con transbordo (con nodos intermedios)?
2. ¿El objetivo final será solo costo o costo y tiempo?
3. ¿Qué nivel de detalle se maneja en las restricciones de capacidad?
