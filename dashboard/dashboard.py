import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


st.set_page_config(
    page_title="Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


def get_database_engine():
    """Create a SQLAlchemy engine using DATABASE_URL."""

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is not configured in the .env file."
        )

    return create_engine(database_url)


def load_sales_data():
    """Load sales data from PostgreSQL."""

    engine = get_database_engine()

    query = """
        SELECT
            sale_date,
            seller,
            customer,
            product,
            quantity,
            unit_price,
            branch,
            total
        FROM sales
        ORDER BY sale_date;
    """

    return pd.read_sql(query, engine)


st.title("📊 Sales Intelligence Dashboard")
st.write("Sales performance overview")

sales_data = load_sales_data()
# Branch filter
# Filters

branches = ["All"] + sorted(
    sales_data["branch"].unique().tolist()
)

selected_branch = st.selectbox(
    "Select Branch",
    branches
)

products = ["All"] + sorted(
    sales_data["product"].unique().tolist()
)

selected_product = st.selectbox(
    "Select Product",
    products
)
sellers = ["All"] + sorted(
    sales_data["seller"].unique().tolist()
)

selected_seller = st.selectbox(
    "Select Seller",
    sellers
)


filtered_data = sales_data.copy()

if selected_branch != "All":
    filtered_data = filtered_data[
        filtered_data["branch"] == selected_branch
    ]

if selected_product != "All":
    filtered_data = filtered_data[
        filtered_data["product"] == selected_product
    ]

if selected_seller != "All":
    filtered_data = filtered_data[
        filtered_data["seller"] == selected_seller
    ]

total_revenue = filtered_data["total"].sum()
total_transactions = len(filtered_data)
total_units = filtered_data["quantity"].sum()
average_transaction = filtered_data["total"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Transactions", total_transactions)
col3.metric("Units Sold", total_units)
col4.metric("Average Transaction", f"${average_transaction:,.2f}")


st.subheader("Sales Data")

st.dataframe(
    filtered_data,
    use_container_width=True
)
st.subheader("Sales by Branch")

sales_by_branch = (
    filtered_data
    .groupby("branch", as_index=False)["total"]
    .sum()
    .sort_values("total", ascending=False)
)

st.bar_chart(
    sales_by_branch,
    x="branch",
    y="total"
)
st.subheader("Sales by Product")

sales_by_product = (
    filtered_data
    .groupby("product", as_index=False)["total"]
    .sum()
    .sort_values("total", ascending=False)
)

st.bar_chart(
    sales_by_product,
    x="product",
    y="total"
)
st.subheader("Sales by Seller")

sales_by_seller = (
    filtered_data
    .groupby("seller", as_index=False)["total"]
    .sum()
    .sort_values("total", ascending=False)
)

st.bar_chart(
    sales_by_seller,
    x="seller",
    y="total"
)
st.subheader("Sales Trend")

sales_trend = (
    filtered_data
    .assign(sale_date=pd.to_datetime(sales_data["sale_date"]).dt.date)
    .groupby("sale_date", as_index=False)["total"]
    .sum()
    .sort_values("sale_date")
)

st.line_chart(
    sales_trend,
    x="sale_date",
    y="total"
)