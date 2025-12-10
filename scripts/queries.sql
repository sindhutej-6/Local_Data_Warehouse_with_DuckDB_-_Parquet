-- 1. Top 5 best-selling products by revenue
SELECT 
    p.category,
    p.product_name,
    SUM(f.sale_amount) AS revenue
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.category, p.product_name
ORDER BY revenue DESC
LIMIT 5;

------------------------------------------------------------

-- 2. Sales by state (monthly aggregation)
-- NOTE: fact_sales does not have sale_date in current ETL. 
-- If you want monthly aggregation, you need to add a sale_date column in sales.csv.
-- For now, we can do total sales by state:

SELECT
    s.state,
    SUM(f.sale_amount) AS total_sales
FROM fact_sales f
JOIN dim_stores s ON f.store_id = s.store_id
GROUP BY s.state
ORDER BY total_sales DESC;

------------------------------------------------------------

-- 3. Top 10 customers by total spending
SELECT
    c.customer_id,
    c.customer_name,
    SUM(f.sale_amount) AS total_spent
FROM fact_sales f
JOIN dim_customers c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 10;
