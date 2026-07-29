import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from extract import extract_sales_data
from transform import transform_sales_data


load_dotenv()


def get_database_engine():
    """Create a SQLAlchemy engine using environment variables."""

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is not configured in the .env file."
        )

    return create_engine(database_url)


def load_sales_data(df):
    """Load transformed sales data into PostgreSQL."""

    engine = get_database_engine()

    df.to_sql(
        "sales",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows into PostgreSQL.")


if __name__ == "__main__":
    sales_data = extract_sales_data()

    transformed_data = transform_sales_data(sales_data)

    load_sales_data(transformed_data)

    print("ETL pipeline completed successfully.")