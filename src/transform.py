import pandas as pd


REQUIRED_COLUMNS = [
    "Fecha",
    "Vendedor",
    "Cliente",
    "Producto",
    "Cantidad",
    "Precio",
    "Sucursal",
]


def transform_sales_data(df):
    """Validate and transform consolidated sales data."""

    # Validate required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Convert data types
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["Cantidad"] = pd.to_numeric(
        df["Cantidad"],
        errors="coerce"
    )
    df["Precio"] = pd.to_numeric(
        df["Precio"],
        errors="coerce"
    )

    # Check for missing values
    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError(
            "The dataset contains missing values."
        )

    # Calculate total sales
    df["Total"] = df["Cantidad"] * df["Precio"]

    return df


if __name__ == "__main__":
    from extract import extract_sales_data

    sales_data = extract_sales_data()
    transformed_data = transform_sales_data(sales_data)

    print("\nTransformed data:")
    print(transformed_data)

    print("\nData types:")
    print(transformed_data.dtypes)

    print("\nTotal sales:")
    print(transformed_data["Total"].sum())