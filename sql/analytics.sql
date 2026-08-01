-- Sales Intelligence Analytics
-- Business analysis queries

-- 1. Sales by branch
SELECT
    branch,
    SUM(total) AS total_sales
FROM sales
GROUP BY branch
ORDER BY total_sales DESC;


-- 2. Sales by product
SELECT
    product,
    SUM(quantity) AS units_sold,
    SUM(total) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC;


-- 3. Sales performance by seller
SELECT
    seller,
    COUNT(*) AS number_of_sales,
    SUM(total) AS total_sales
FROM sales
GROUP BY seller
ORDER BY total_sales DESC;


-- 4. Customer purchases
SELECT
    customer,
    COUNT(*) AS number_of_purchases,
    SUM(total) AS total_spent
FROM sales
GROUP BY customer
ORDER BY total_spent DESC;


-- 5. Daily sales
SELECT
    DATE(sale_date) AS sale_date,
    SUM(total) AS daily_sales
FROM sales
GROUP BY DATE(sale_date)
ORDER BY sale_date;


-- 6. General business summary
SELECT
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    SUM(total) AS total_revenue,
    AVG(total) AS average_transaction
FROM sales;