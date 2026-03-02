-- analysis_queries_SOLUTION.sql
-- ============================================================
-- SOLUTION FILE — For instructor/facilitator reference only.
-- Do NOT distribute to participants before the session ends.
-- This file lives on the solution-reference branch only.
-- ============================================================

-- ============================================================
-- BEGINNER LEVEL QUERIES
-- ============================================================

-- Query 1: Total Revenue by Region
SELECT
    region,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_transactions
GROUP BY region
ORDER BY total_revenue DESC;


-- Query 2: Top 5 Product Categories by Revenue
SELECT
    product_category,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(units_sold) AS total_units,
    COUNT(*) AS transaction_count
FROM sales_transactions
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 5;


-- Query 3: Transaction Count by Region (with avg order value)
SELECT
    region,
    COUNT(*) AS transaction_count,
    ROUND(AVG(revenue), 2) AS avg_revenue_per_transaction
FROM sales_transactions
GROUP BY region
ORDER BY transaction_count DESC;


-- ============================================================
-- INTERMEDIATE LEVEL QUERIES
-- ============================================================

-- Query 4: Monthly Revenue Trend (SQLite — uses strftime)
SELECT
    strftime('%m', date) AS month_number,
    CASE strftime('%m', date)
        WHEN '01' THEN 'January'
        WHEN '02' THEN 'February'
        WHEN '03' THEN 'March'
    END AS month_name,
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(*) AS transaction_count
FROM sales_transactions
GROUP BY strftime('%m', date)
ORDER BY month_number ASC;


-- Query 5: Revenue and Average Discount by Category
SELECT
    product_category,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(discount_pct), 3) AS avg_discount,
    COUNT(*) AS transaction_count
FROM sales_transactions
GROUP BY product_category
ORDER BY avg_discount DESC;


-- ============================================================
-- ADVANCED LEVEL QUERIES
-- ============================================================

-- Query 6: Top 10 Customers by Revenue
SELECT
    customer_id,
    COUNT(*) AS total_transactions,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_order_value,
    MAX(date) AS most_recent_purchase
FROM sales_transactions
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;


-- Query 7: Discount Impact Analysis
SELECT
    CASE
        WHEN discount_pct > 0 THEN 'Discounted'
        ELSE 'Full Price'
    END AS discount_group,
    COUNT(*) AS transaction_count,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_transactions
GROUP BY discount_group
ORDER BY avg_revenue DESC;
