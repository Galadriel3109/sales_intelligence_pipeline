from extract import extract_sales_data
from transform import transform_sales_data
from load import load_sales_data


def run_pipeline():
    """Run the complete sales ETL pipeline."""

    print("Starting Sales Intelligence ETL pipeline...")

    # 1. Extract
    raw_data = extract_sales_data()

    # 2. Transform
    transformed_data = transform_sales_data(raw_data)

    # 3. Load
    load_sales_data(transformed_data)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()