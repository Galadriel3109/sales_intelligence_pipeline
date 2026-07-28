from pathlib import Path

import pandas as pd


# Ruta donde guardaremos los archivos originales
RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Crear la carpeta si no existe
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# Datos de prueba de la sucursal Norte
norte = pd.DataFrame(
    {
        "Fecha": ["2026-07-01", "2026-07-02", "2026-07-03"],
        "Vendedor": ["Ana", "Luis", "Ana"],
        "Cliente": ["Cliente A", "Cliente B", "Cliente C"],
        "Producto": ["Laptop", "Monitor", "Teclado"],
        "Cantidad": [2, 3, 5],
        "Precio": [15000, 4500, 800],
    }
)


# Datos de prueba de la sucursal Centro
centro = pd.DataFrame(
    {
        "Fecha": ["2026-07-01", "2026-07-02", "2026-07-03"],
        "Vendedor": ["Carlos", "Maria", "Carlos"],
        "Cliente": ["Cliente D", "Cliente E", "Cliente F"],
        "Producto": ["Laptop", "Mouse", "Monitor"],
        "Cantidad": [1, 8, 2],
        "Precio": [15000, 500, 4500],
    }
)


# Datos de prueba de la sucursal Sur
sur = pd.DataFrame(
    {
        "Fecha": ["2026-07-01", "2026-07-02", "2026-07-03"],
        "Vendedor": ["Pedro", "Laura", "Pedro"],
        "Cliente": ["Cliente G", "Cliente H", "Cliente I"],
        "Producto": ["Monitor", "Teclado", "Laptop"],
        "Cantidad": [4, 6, 1],
        "Precio": [4500, 800, 15000],
    }
)


# Guardar los tres archivos Excel
norte.to_excel(RAW_DATA_DIR / "sucursal_norte.xlsx", index=False)
centro.to_excel(RAW_DATA_DIR / "sucursal_centro.xlsx", index=False)
sur.to_excel(RAW_DATA_DIR / "sucursal_sur.xlsx", index=False)


print("Archivos Excel creados correctamente.")
print(f"Ubicación: {RAW_DATA_DIR}")