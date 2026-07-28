from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def extract_sales_data():
    """Read all Excel files from the raw data directory."""

    excel_files = list(RAW_DATA_DIR.glob("*.xlsx"))

    if not excel_files:
        raise FileNotFoundError(
            f"No Excel files found in {RAW_DATA_DIR}"
        )

    dataframes = []

    for file in excel_files:
        df = pd.read_excel(file)

        # Identify the branch from the filename
        branch = file.stem.replace("sucursal_", "").title()

        df["Sucursal"] = branch

        dataframes.append(df)

        print(f"Read: {file.name} | Rows: {len(df)}")

    consolidated_data = pd.concat(
        dataframes,
        ignore_index=True
    )

    print(
        f"Total rows extracted: {len(consolidated_data)}"
    )

    return consolidated_data


if __name__ == "__main__":
    sales_data = extract_sales_data()

    print("\nConsolidated data:")
    print(sales_data)