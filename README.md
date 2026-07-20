# Optimización de la Red Logística de Agroexportación: Arequipa y Corredores del Sur / Lima

## 1. Definición de la Función Objetivo Agroexportadora

### ¿Qué se optimiza?
El modelo decide **cuánto volumen de productos agroexportables (toneladas o contenedores reefers)** enviar y **a través de qué rutas/modos** en la red de distribución logístico-agrícola de Arequipa hacia los centros de consolidación (Puno, Cusco) y salida internacional (Lima / Callao / Matarani).

### Aspectos clave a definir

- **Cantidad a enviar ($x_{ijkt}$):** Flujo del producto agrícola $k$ (ej. uva, palta, alcachofa, quinua) desde el origen agroindustrial $i$ (ej. Majes-Siguas, La Joya) hacia el nodo/destino $j$, mediante el modo/ruta $t$.
- **Ventana de perecibilidad (Tiempo crítico):** Definir el intervalo temporal máximo ($T_{max}$) de transporte para evitar el deterioro de la carga perecedera y la pérdida del valor FOB.
- **Rutas e Infraestructura:** Mapeo de carreteras (Panamericana Sur PE-1S, Interoceánica PE-34A/34G) identificando nodos de acopio, plantas de empaque y hubs de refrigeración.
- **Capacidad de Cadena de Frío y Transporte:** Límites de flota de camiones refrigerados (reefers), peso bruto permitido por eje (normativa MTC) y capacidad de almacenamiento en frío por nodo.

---

## 2. Formulación del Modelo Matemático y Red Logística

### Estructura de Red Agroexportadora
Construcción del grafo de transporte con transbordo y procesamiento:
- **Nodos de Origen:** Zonas de producción agrícola en Arequipa y regiones aledañas (Cusco para café/cacao, Puno para quinua).
- **Nodos Intermedios (Transbordo / Cadena de Frío):** Plantas de empaque/procesamiento en Arequipa, almacenes de frío y controles de pesaje/seguridad vial.
- **Nodos Destino:** Puerto del Callao / Aeropuerto Jorge Chávez (Lima), Puerto de Matarani, o mercados regionales.
- **Arcos:** Tramos carreteros y corredores logísticos.

### Costos y Parámetros Específicos
- **Costo de Flete y Refrigeración:** $c_{ij}$ (costo de transporte por tonelada + costo de mantenimiento de cadena de frío/combustible de termoking).
- **Penalizaciones:** Costo por pérdida de calidad debido a demoras o congestión en ruta.
- **Tiempos de Tránsito:** Tiempos reales de recorrido considerando pendientes de la sierra/costa y siniestralidad de los tramos (MTC/ONSV).

### Variables de Decisión
- $x_{ij}$: Toneladas de carga agroexportable enviadas del nodo $i$ al $j$.
- $y_{ij} \in \{0,1\}$: Variable binaria de activación de ruta estratégica o parada técnica en planta de frío.

### Función Objetivo

- **Principal:** Minimizar el costo logístico total de agroexportación (flete terrestre + costos operativos de frío + penalización por degradación de producto).
- **Multiobjetivo / Ponderado:** Minimizar una función balanceada de costo y tiempo de tránsito para garantizar que el producto llegue a puerto dentro del *laycan* (ventana de embarque) del buque.

---

## 3. Restricciones Operativas y de Calidad

- **Conservación de Oferta y Demanda:** No exceder la producción cosechada en las zonas agrícolas de Arequipa/Sur y cumplir con la demanda requerida en los puertos de exportación o plantas de procesamiento.
- **Capacidad de Cadena de Frío:** No superar la disponibilidad de camiones reefers en la región ni la capacidad estática de almacenamiento refrigerado.
- **Límites Normativos de Transporte:** Restricciones de tonelaje máximo por camión según normativa del MTC.
- **Puntos Críticos de Restricción Vial:** Contemplar restricciones de flujo en tramos de alta siniestralidad vial o cuellos de botella geográficos.
- **No Negatividad e Integridad:** $x_{ij} \ge 0$, y variables enteras/binarias según el tipo de flota.

---

## 4. Reporte de Resultados y Salidas de Decisión

1. **Plan de Envíos Óptimo Agroexportador:** Tonelaje exacto a mover por tipo de producto, ruta y tipo de vehículo reefer.
2. **Asignación Eficiente de Rutas:** Determinación de si la carga de Puno/Cusco debe consolidarse en Arequipa antes de ir a Lima o despacharse de forma directa.
3. **Puntos Saturation & Cuellos de Botella:** Identificación de nodos de acopio o tramos carreteros que operan al límite de su capacidad.
4. **Evaluación de Impacto / Análisis de Escenarios:** Comparativa de costos entre el esquema de transporte empírico actual vs. el modelo optimizado de IO.

---

## 5. Metodología

### 5.1 Recolección y Procesamiento de Datos Agroexportadores
- Cartografía logística de Arequipa y sus conexiones con Lima, Puno y Cusco (vías nacionales y departamentales).
- **Supuestos del Modelo:** Considerar demanda estacional por campañas agrícolas (picos de cosecha de uva, palta, alcachofa, etc.).

**Variables y Datos Requeridos:**
- Matriz de distancias y tiempos entre Arequipa, Lima, Cusco y Puno.
- Tarifas de flete reefer y carga seca por tonelada/kilómetro.
- Volumen de producción exportable (toneladas/mes) por distrito/valle agrícola.
- Indicadores de infraestructura vial y accidentabilidad por tramo.

### 5.2 Marco Teórico y Retroanálisis
- Revisión de modelos de **Programación Lineal**, **Flujo de Costo Mínimo (Min-Cost Flow)** y **Modelos de Transporte con Transbordo y Cadena de Frío**.
- Justificación de algoritmos exactos o heurísticos aplicados a cadenas de suministro perecederas.

### 5.3 Métricas de Evaluación
- **Costo Total Logístico por Tonelada Exportada (USD/Tn).**
- **Lead Time promedio de entrega en puerto.**
- **Porcentaje de uso de la capacidad de la flota reefer.**

### 5.4 Construcción del Modelo Matemático
- Formulación rigurosa del modelo en notación algebraica con variables continuas y binarias.

### 5.5 Implementación Computacional

**Pila Tecnológica Recomendada:**
- **Python:** Lenguaje base para el pipeline de datos.
- **Modeladores y Solvers:** `PuLP`, `Pyomo` o `Google OR-Tools` (CP-SAT/Linear Solver) para resolver la red de transporte.
- **Análisis de Datos:** `Pandas` y `NumPy` para estructurar matrices de origen-destino y costos.
- **Visualización:** `Matplotlib` / `Seaborn` o mapas interactivos (`Folium`) para representar los flujos óptimos de carga sobre los corredores del sur.

### 5.6 Diseño Experimental

**Escenario A (Línea Base / Operación Tradicional):**
- Asignación empírica de rutas basada únicamente en la distancia más corta, sin considerar cuellos de botella, costos de frío ni tiempos de espera.

**Escenario B (Optimizado mediante IO):**
- Asignación mediante el modelo matemático de costo mínimo/tiempo con restricciones de capacidad y cadena de frío.

### 5.7 Análisis de Sensibilidad Agroexportador
Simular variaciones críticas del mercado peruano:
- **Variación de Cosechas:** Incremento de $+15\%$ en la producción de uva/palta en Majes-Siguas.
- **Interrupción de Vías:** Simulación del cierre o bloqueo temporal de la Panamericana Sur (Tramo Arequipa - ICA - Lima).
- **Pico de Fletes:** Incremento de $+10\%$ en costos de combustible o peajes.

---

## 6. Análisis y Conclusiones

### Resultados a Demostrar
- **Cuantificación del Ahorro:** Porcentaje de reducción en costos logísticos y tiempos de tránsito del Escenario B respecto al Escenario A.
- **Justificación de Rutas:** Explicación técnica de la reorientación de flujos (por qué consolidar carga de Puno/Cusco en Arequipa antes de enviar a Lima).
- **Vulnerabilidad de la Red:** Identificación de arcos críticos donde una interrupción impactaría gravemente la cadena agroexportadora.

### Conclusiones
- Impacto de la Investigación de Operaciones en la competitividad agroexportadora de la Región Arequipa.
- Identificación de la restricción más limitante (flota reefer, capacidad de almacenamiento o infraestructura vial).
- Recomendaciones estratégicas para la gestión logística regional y la toma de decisiones de transporte.
