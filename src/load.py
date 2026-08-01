import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

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
    """Load transformed sales data into PostgreSQL without duplicates."""

    engine = get_database_engine()

    columns = [
        "sale_date",
        "seller",
        "customer",
        "product",
        "quantity",
        "unit_price",
        "branch",
        "total"
    ]

    insert_sql = """
        INSERT INTO sales (
            sale_date,
            seller,
            customer,
            product,
            quantity,
            unit_price,
            branch,
            total
        )
        VALUES (
            :sale_date,
            :seller,
            :customer,
            :product,
            :quantity,
            :unit_price,
            :branch,
            :total
        )
        ON CONFLICT (sale_date, seller, customer, product, branch)
        DO NOTHING;
    """

    records = df[columns].to_dict(orient="records")

    with engine.begin() as connection:
        result = connection.execute(
            text(insert_sql),
            records
        )

    print(f"Processed {len(records)} rows.")
    print(f"Inserted {result.rowcount} new rows.")


if __name__ == "__main__":
    sales_data = extract_sales_data()

    transformed_data = transform_sales_data(sales_data)

    load_sales_data(transformed_data)

    print("ETL pipeline completed successfully.")