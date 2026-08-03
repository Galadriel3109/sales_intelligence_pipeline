# Sales Intelligence Pipeline

## Solución automatizada de datos para análisis y toma de decisiones

### 📌 Descripción

**Sales Intelligence Pipeline** es una solución de datos que automatiza el proceso completo de consolidación, transformación, almacenamiento y análisis de información de ventas proveniente de diferentes sucursales.

El proyecto simula un escenario empresarial en el que diferentes sucursales generan archivos Excel independientes y la dirección necesita transformar esa información dispersa en datos confiables para responder preguntas como:

* ¿Qué sucursal genera más ingresos?
* ¿Qué producto tiene mayor facturación?
* ¿Qué vendedor genera más ventas?
* ¿Qué clientes representan mayor valor?
* ¿Cómo evolucionan las ventas a lo largo del tiempo?
* ¿Qué ocurre cuando se incorporan nuevos datos?

La solución automatiza el flujo completo:

**Excel → Python ETL → PostgreSQL → SQL Analytics → Dashboard interactivo**

El objetivo es convertir procesos manuales y repetitivos en **procesos automatizados, estructurados y medibles**.

---

## 🎯 Objetivo del proyecto

Demostrar cómo una solución de datos puede automatizar un proceso completo de:

**Extracción → Transformación → Carga → Análisis → Visualización**

El proyecto está orientado a empresas que actualmente trabajan con información dispersa en Excel u otras fuentes y necesitan:

* Reducir trabajo manual.
* Disminuir errores.
* Centralizar información.
* Automatizar cargas de datos.
* Obtener indicadores de negocio.
* Facilitar la toma de decisiones mediante dashboards.

---

## 💼 Problema de negocio

Una empresa recibe diariamente información de ventas de diferentes sucursales en archivos Excel separados.

Sin automatización, consolidar esta información requiere:

1. Abrir diferentes archivos.
2. Copiar y combinar información.
3. Limpiar y transformar los datos.
4. Calcular totales.
5. Cargar la información a una base de datos.
6. Crear reportes manualmente.
7. Repetir el proceso cada vez que llegan nuevos archivos.

Este proceso consume tiempo y aumenta el riesgo de errores y duplicados.

### Solución propuesta

Se construyó un pipeline automatizado utilizando Python, Pandas y PostgreSQL.

```text
Excel Sucursal Norte ──┐
Excel Sucursal Sur ────┼──→ EXTRACT
Excel Sucursal Centro ─┘
                         ↓
                    TRANSFORM
                         ↓
                 VALIDATION / CLEANING
                         ↓
                      LOAD
                         ↓
                   PostgreSQL
                         ↓
                  SQL ANALYTICS
                         ↓
              STREAMLIT DASHBOARD
                         ↓
                BUSINESS INSIGHTS
```

---

## ⚙️ Tecnologías utilizadas

* **Python 3.12**
* **Pandas**
* **OpenPyXL**
* **SQLAlchemy**
* **psycopg2**
* **PostgreSQL**
* **SQL**
* **python-dotenv**
* **Streamlit**
* **Plotly**
* **Git / GitHub**

---

## 🔄 Proceso ETL

### 1. Extract

El pipeline lee automáticamente los archivos Excel ubicados en:

```text
data/raw/
```

Actualmente se utilizan:

```text
sucursal_centro.xlsx
sucursal_norte.xlsx
sucursal_sur.xlsx
```

La información de las diferentes sucursales se consolida en un único DataFrame para continuar el procesamiento.

---

### 2. Transform

Los datos son estandarizados para trabajar con una estructura común.

Entre las transformaciones realizadas:

* Normalización de nombres de columnas.
* Conversión de fechas.
* Validación de tipos de datos.
* Estandarización de campos.
* Cálculo del importe total de cada venta.

La fórmula utilizada es:

```text
Total = Cantidad × Precio
```

Ejemplo:

```text
4 × $4,500 = $18,000
```

---

### 3. Load

Los datos transformados se cargan automáticamente en PostgreSQL mediante SQLAlchemy.

Base de datos:

```text
sales_intelligence
```

Tabla:

```text
sales
```

La solución utiliza una estrategia de **carga incremental**, evitando insertar nuevamente registros que ya existen.

Para controlar duplicados se utiliza una restricción única basada en:

```text
sale_date
seller
customer
product
branch
```

Esto permite ejecutar nuevamente el pipeline sin duplicar las ventas previamente cargadas.

Ejemplo:

```text
Processed 10 rows.
Inserted 0 new rows.
ETL pipeline completed successfully.
```

Cuando se incorpora una nueva venta:

```text
Processed 10 rows.
Inserted 1 new rows.
ETL pipeline completed successfully.
```

---

## 🗄️ Base de datos

PostgreSQL almacena la información consolidada en la tabla:

```text
sales
```

La estructura principal incluye:

```text
sale_date
seller
customer
product
quantity
unit_price
branch
total
```

Actualmente el dataset contiene:

* **3 sucursales**
* **10 transacciones**
* **34 unidades vendidas**
* **$122,300.00 en ingresos**

---

## 📊 Business Analytics

Una vez cargados los datos, SQL permite obtener indicadores relevantes para la dirección.

### Ventas por sucursal

| Sucursal |     Ventas |
| -------- | ---------: |
| Norte    | $47,500.00 |
| Sur      | $46,800.00 |
| Centro   | $28,000.00 |

**Sucursal líder:** Norte.

---

### Ventas por producto

| Producto | Unidades |     Ventas |
| -------- | -------: | ---------: |
| Laptop   |        4 | $60,000.00 |
| Monitor  |       11 | $49,500.00 |
| Teclado  |       11 |  $8,800.00 |
| Mouse    |        8 |  $4,000.00 |

**Producto con mayor facturación:** Laptop.

---

### Ventas por vendedor

| Vendedor | Transacciones |     Ventas |
| -------- | ------------: | ---------: |
| Pedro    |             3 | $42,000.00 |
| Ana      |             2 | $34,000.00 |
| Carlos   |             2 | $24,000.00 |
| Luis     |             1 | $13,500.00 |
| Laura    |             1 |  $4,800.00 |
| Maria    |             1 |  $4,000.00 |

**Vendedor líder por facturación:** Pedro.

---

### Clientes

El mayor valor de compra registrado corresponde a:

**Cliente A — $30,000.00**

Los datos actuales son un dataset de demostración y cada cliente aparece una sola vez. Por lo tanto, este indicador representa el mayor valor de compra registrado y no permite todavía medir frecuencia o recurrencia.

---

### Tendencia diaria

| Fecha      |     Ventas |
| ---------- | ---------: |
| 2026-07-01 | $63,000.00 |
| 2026-07-02 | $22,300.00 |
| 2026-07-03 | $28,000.00 |
| 2026-07-04 |  $9,000.00 |

El **1 de julio** fue el día con mayor facturación del dataset.

---

## 📈 Dashboard interactivo

El proyecto incluye un dashboard desarrollado con **Streamlit**.

El dashboard presenta:

### KPIs

* Total Revenue
* Transactions
* Units Sold
* Average Transaction

### Visualizaciones

* Sales by Branch
* Sales by Product
* Sales by Seller
* Sales Trend

### Filtros interactivos

El usuario puede analizar los datos mediante:

```text
Sucursal
Producto
Vendedor
```

Los filtros pueden combinarse para realizar análisis específicos.

Por ejemplo:

```text
Sucursal: Sur
Producto: Monitor
Vendedor: Pedro
```

Resultado:

```text
Total Revenue:        $27,000
Transactions:               2
Units Sold:                  6
Average Transaction:    $13,500
```

Esto permite analizar información sin necesidad de ejecutar consultas SQL manualmente.

---

## 🧠 Flujo completo de la solución

```text
                 FUENTES DE DATOS
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
       Excel Norte          Excel Sur
             │                   │
             └─────────┬─────────┘
                       │
                  Excel Centro
                       ↓
                 PYTHON / ETL
                       │
             ┌─────────┼─────────┐
             ↓         ↓         ↓
          Extract   Transform  Validation
                       │
                       ↓
                    PostgreSQL
                       │
                       ↓
                  SQL Analytics
                       │
                       ↓
              Streamlit Dashboard
                       │
                       ↓
               Business Insights
                       │
                       ↓
              Toma de decisiones
```

---

## 📁 Estructura del proyecto

```text
sales_intelligence_pipeline/
│
├── data/
│   ├── raw/
│   │   ├── sucursal_centro.xlsx
│   │   ├── sucursal_norte.xlsx
│   │   └── sucursal_sur.xlsx
│   │
│   └── processed/
│
├── dashboard/
│   └── dashboard.py
│
├── docs/
│   └── project_overview.md
│
├── images/
│
├── notebooks/
│
├── reports/
│
├── sql/
│   ├── analytics.sql
│   └── schema.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   ├── generate_test_data.py
│   └── test_connection.py
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Ejecución

### 1. Clonar el proyecto

```bash
git clone git@github.com:Galadriel3109/sales_intelligence_pipeline.git
cd sales_intelligence_pipeline
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

Crear un archivo `.env` con la conexión a la base de datos:

```text
DATABASE_URL=postgresql+psycopg2://postgres:TU_PASSWORD@localhost:5432/sales_intelligence
```

**El archivo `.env` no debe subirse a GitHub.**

### 5. Ejecutar el pipeline

Desde la raíz del proyecto:

```bash
python src/pipeline.py
```

El proceso realizará:

```text
Excel
 ↓
Extract
 ↓
Transform
 ↓
Validation
 ↓
Incremental Load
 ↓
PostgreSQL
```

### 6. Ejecutar el dashboard

Con el entorno virtual activo:

```bash
streamlit run dashboard/dashboard.py
```

El dashboard se abrirá en:

```text
http://localhost:8501
```

---

## 🧠 Aprendizajes técnicos

Este proyecto demuestra experiencia práctica en:

* Diseño y desarrollo de procesos ETL.
* Automatización de tareas repetitivas.
* Manipulación de datos con Python y Pandas.
* Lectura y procesamiento de archivos Excel.
* Integración Python + PostgreSQL.
* SQL para análisis de negocio.
* Cargas incrementales.
* Prevención de registros duplicados.
* Manejo seguro de credenciales mediante variables de entorno.
* Desarrollo de dashboards interactivos.
* Control de versiones con Git.
* Organización de proyectos de datos.

---

## 💼 Aplicación para clientes

Este proyecto representa una solución adaptable a empresas que trabajan con:

* Excel.
* CSV.
* Sistemas administrativos.
* Datos de ventas.
* Inventarios.
* Información de clientes.
* Reportes manuales.

Una solución personalizada puede automatizar el flujo:

```text
Fuentes de datos
      ↓
Extracción automática
      ↓
Limpieza y transformación
      ↓
Validación
      ↓
Base de datos
      ↓
Análisis
      ↓
Dashboard / Reportes
      ↓
Información para tomar decisiones
```

### Propuesta de valor

> **Convertir procesos manuales de datos en soluciones automatizadas, estructuradas y medibles que permitan a las empresas tomar mejores decisiones.**

---

## 🔮 Próximas mejoras

* [ ] Agregar validaciones avanzadas de calidad de datos.
* [ ] Incorporar más datos históricos.
* [ ] Crear pruebas automatizadas.
* [ ] Mejorar visualizaciones con Plotly.
* [ ] Agregar métricas adicionales de negocio.
* [ ] Automatizar reportes.
* [ ] Incorporar alertas ante anomalías o cambios relevantes.
* [ ] Preparar despliegue del dashboard para usuarios externos.

---

## 👩‍💻 Proyecto de portafolio

**Sales Intelligence Pipeline**

Proyecto de portafolio enfocado en:

**Automatización + ETL + PostgreSQL + SQL + Business Intelligence + Dashboards**

El proyecto demuestra cómo transformar información dispersa en archivos Excel en una solución automatizada capaz de **procesar datos, evitar duplicados, almacenarlos, analizarlos y presentarlos mediante un dashboard interactivo para apoyar la toma de decisiones.**
