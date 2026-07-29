# Sales Intelligence Pipeline

## Solución automatizada de datos para análisis de ventas

### 📌 Descripción

**Sales Intelligence Pipeline** es una solución de datos diseñada para automatizar el proceso de consolidación, transformación y análisis de información de ventas proveniente de diferentes sucursales.

El proyecto simula un escenario empresarial en el que **3 sucursales generan archivos Excel independientes** y la dirección necesita obtener información consolidada para responder preguntas como:

* ¿Qué sucursal vende más?
* ¿Qué producto genera mayor facturación?
* ¿Qué vendedor tiene el mejor desempeño?
* ¿Qué clientes representan mayor valor?
* ¿Cuál es la tendencia de ventas?

El objetivo es transformar un proceso manual y repetitivo en un **flujo automatizado de datos**, desde los archivos de origen hasta una base de datos preparada para análisis.

---

## 🎯 Objetivo del proyecto

Demostrar cómo una solución de datos puede automatizar un proceso completo de:

**Extracción → Transformación → Carga → Análisis**

El proyecto está orientado a ofrecer soluciones de datos a empresas que actualmente trabajan con información dispersa en archivos Excel y necesitan convertirla en información confiable para la toma de decisiones.

---

## 💼 Problema de negocio

La empresa recibe diariamente información de ventas de tres sucursales en archivos Excel separados.

Sin automatización, consolidar esta información requiere:

1. Abrir diferentes archivos.
2. Copiar y combinar información.
3. Limpiar y transformar los datos.
4. Calcular totales.
5. Cargar la información a una base de datos.
6. Crear reportes manualmente.

Este proceso consume tiempo y aumenta el riesgo de errores.

### Solución propuesta

Se construyó un pipeline automatizado que realiza estas tareas mediante Python, Pandas y PostgreSQL.

```text
Excel Sucursal Norte ──┐
Excel Sucursal Sur ────┼──→ EXTRACT
Excel Sucursal Centro ─┘
                         ↓
                    TRANSFORM
                         ↓
                    LOAD
                         ↓
                  PostgreSQL
                         ↓
                  SQL ANALYTICS
                         ↓
               Business Insights
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
* **Git / GitHub**

---

## 🔄 Proceso ETL

### 1. Extract

El pipeline lee automáticamente los archivos Excel ubicados en:

```text
data/raw/
```

Actualmente se utilizan tres archivos:

```text
sucursal_centro.xlsx
sucursal_norte.xlsx
sucursal_sur.xlsx
```

El proceso consolida la información de las tres sucursales.

**Resultado actual: 9 registros extraídos.**

---

### 2. Transform

Los datos son estandarizados para trabajar con una estructura común.

Entre las transformaciones realizadas:

* Normalización de nombres de columnas.
* Conversión de fechas.
* Validación de tipos de datos.
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

El proceso actualmente carga los registros mediante:

```python
df.to_sql(
    "sales",
    engine,
    if_exists="append",
    index=False
)
```

---

## 📊 Business Analytics

Una vez cargados los datos, SQL permite obtener indicadores relevantes para la dirección.

### Ventas por sucursal

| Sucursal |     Ventas |
| -------- | ---------: |
| Norte    | $47,500.00 |
| Sur      | $37,800.00 |
| Centro   | $28,000.00 |

**Sucursal líder:** Norte.

### Ventas por producto

| Producto | Unidades |     Ventas |
| -------- | -------: | ---------: |
| Laptop   |        4 | $60,000.00 |
| Monitor  |        9 | $40,500.00 |
| Teclado  |       11 |  $8,800.00 |
| Mouse    |        8 |  $4,000.00 |

**Producto con mayor facturación:** Laptop.

### Ventas por vendedor

| Vendedor | Transacciones |     Ventas |
| -------- | ------------: | ---------: |
| Ana      |             2 | $34,000.00 |
| Pedro    |             2 | $33,000.00 |
| Carlos   |             2 | $24,000.00 |
| Luis     |             1 | $13,500.00 |
| Laura    |             1 |  $4,800.00 |
| Maria    |             1 |  $4,000.00 |

**Vendedor líder:** Ana.

### Clientes

El cliente con mayor valor de compra registrado es:

**Cliente A — $30,000.00**

> Nota: los datos actuales son un dataset de demostración y cada cliente aparece una sola vez. Por lo tanto, este indicador representa el mayor valor de compra registrado, no frecuencia o recurrencia del cliente.

### Tendencia diaria

| Fecha      |     Ventas |
| ---------- | ---------: |
| 2026-07-01 | $63,000.00 |
| 2026-07-02 | $22,300.00 |
| 2026-07-03 | $28,000.00 |

El **1 de julio** fue el día con mayor facturación del dataset.

---

## 📈 Resultado

El pipeline procesa actualmente:

* **3 archivos Excel**
* **3 sucursales**
* **9 registros**
* **$113,300.00 en ventas**

El proceso completo puede ejecutarse mediante Python, evitando la consolidación manual de los archivos.

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
│   └── processed/
│
├── dashboard/
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

```bash
python src/load.py
```

El proceso realizará:

```text
Excel
 ↓
Extract
 ↓
Transform
 ↓
Load
 ↓
PostgreSQL
```

---

## 🧠 Aprendizajes técnicos

Este proyecto demuestra experiencia práctica en:

* Diseño de procesos ETL.
* Automatización de tareas repetitivas.
* Manipulación de datos con Python y Pandas.
* Integración Python + PostgreSQL.
* SQL para análisis de negocio.
* Manejo seguro de credenciales mediante variables de entorno.
* Control de versiones con Git.
* Organización de proyectos de datos.

---

## 💼 Aplicación para clientes

Este proyecto representa una solución que puede adaptarse a empresas que trabajan con:

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
Base de datos
      ↓
Análisis
      ↓
Dashboard / Reportes
      ↓
Información para tomar decisiones
```

### Propuesta de valor

**Convertir procesos manuales de datos en procesos automatizados, estructurados y medibles.**

---

## 🔮 Próximas mejoras

* [ ] Automatizar la ejecución completa mediante `pipeline.py`.
* [ ] Evitar registros duplicados durante nuevas cargas.
* [ ] Agregar validaciones de calidad de datos.
* [ ] Incorporar más datos históricos.
* [ ] Crear pruebas automatizadas.
* [ ] Crear dashboard de ventas.
* [ ] Automatizar reportes.
* [ ] Incorporar métricas adicionales de negocio.

---

## 👩‍💻 Proyecto

**Sales Intelligence Pipeline**

Proyecto de portafolio enfocado en **automatización, ETL, análisis de datos y Business Intelligence**.
