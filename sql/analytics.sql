-- ============================================================
-- SALES INTELLIGENCE PIPELINE
-- Business Analytics Queries
-- ============================================================

-- 1. ¿Cuál sucursal vende más?
SELECT
    branch,
    SUM(total) AS total_sales
FROM sales
GROUP BY branch
ORDER BY total_sales DESC;


-- 2. ¿Cuál producto genera más ventas?
SELECT
    product,
    SUM(quantity) AS units_sold,
    SUM(total) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC;


-- 3. ¿Qué vendedor vende más?
SELECT
    seller,
    COUNT(*) AS number_of_sales,
    SUM(total) AS total_sales
FROM sales
GROUP BY seller
ORDER BY total_sales DESC;


-- 4. ¿Qué clientes compran más?
SELECT
    customer,
    COUNT(*) AS number_of_purchases,
    SUM(total) AS total_spent
FROM sales
GROUP BY customer
ORDER BY total_spent DESC;


-- 5. ¿Cuál es la tendencia de ventas por fecha?
SELECT
    sale_date,
    SUM(total) AS daily_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;


-- 6. Resumen general del negocio
SELECT
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    SUM(total) AS total_revenue,
    AVG(total) AS average_transaction
FROM sales;