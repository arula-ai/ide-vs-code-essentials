-- analysis_queries.sql
-- ============================================================
-- Business Analytics Queries — NovaTrend Retail Q1 2024
-- ============================================================
--
-- HOW TO USE THIS FILE:
-- ─────────────────────────────────────────────────────────────
-- These queries run inside the Jupyter notebook (exploration.ipynb)
-- using Python's built-in sqlite3 library.
--
-- The notebook handles the database connection for you.
-- Your job: write the SQL, then paste it into the notebook cells.
--
-- WORKFLOW:
-- 1. Read the business question and TODO comment below
-- 2. Open Copilot Chat (Cmd+Shift+I / Ctrl+Shift+I)
-- 3. Paste the provided Copilot prompt
-- 4. Copy the SQL that Copilot generates
-- 5. Paste it below the TODO comment in this file
-- 6. Also paste it into the matching cell in exploration.ipynb
-- 7. Run the cell (Shift+Enter) and read the results
--
-- IMPORTANT — SQLite Syntax Notes:
--   ✅ Use: strftime('%m', date)   ← extract month in SQLite
--   ❌ Not: MONTH(date)            ← that is MySQL/PostgreSQL syntax
--   ✅ Use: CAST(x AS REAL)        ← convert to decimal in SQLite
--   ✅ Use: julianday()            ← date arithmetic in SQLite
--
-- TABLE AVAILABLE: sales_transactions
--   Columns: transaction_id, date, region, product_id,
--            product_category, units_sold, unit_price,
--            discount_pct, revenue, customer_id
-- ============================================================



-- ============================================================
-- BEGINNER LEVEL QUERIES (Complete at least 2 of these 3)
-- ============================================================

-- ── Query 1: Total Revenue by Region ──────────────────────────────────────────
--
-- BUSINESS QUESTION:
--   Which regions generated the most revenue in Q1?
--   Leadership needs to know where sales are strongest and weakest.
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - Which region is #1? By how much vs #2?
--   - Is there a region significantly below the others?
--   - Does the distribution match leadership's intuition?
--
-- Copilot Chat Prompt:
-- "Write SQL to calculate the SUM of a column named 'revenue' grouped by
--  'region' from a table called 'sales_transactions'.
--  Order results by total revenue descending.
--  Label the sum column as 'total_revenue'.
--  Round the result to 2 decimal places."

-- TODO 1: Write your Query 1 here

SELECT
	region,
	ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_transactions
GROUP BY region
ORDER BY total_revenue DESC;




-- ── Query 2: Top 5 Product Categories by Revenue ──────────────────────────────
--
-- BUSINESS QUESTION:
--   Which product categories are our biggest revenue drivers?
--   Where should we focus promotions next quarter?
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - What % of total revenue does the top category represent?
--   - Is there a surprising category near the top or bottom?
--   - Does high revenue also mean high volume (units sold)?
--
-- Copilot Chat Prompt:
-- "Write SQL to find the top 5 product_category values by total revenue
--  from a table called 'sales_transactions'.
--  Include:
--    - product_category
--    - SUM(revenue) as total_revenue (rounded to 2 decimal places)
--    - SUM(units_sold) as total_units
--    - COUNT(*) as transaction_count
--  Order by total_revenue descending.
--  Use LIMIT 5."

-- TODO 2: Write your Query 2 here

SELECT
	product_category,
	ROUND(SUM(revenue), 2) AS total_revenue,
	SUM(units_sold) AS total_units,
	COUNT(*) AS transaction_count
FROM sales_transactions
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 5;




-- ── Query 3: Transaction Count by Region ──────────────────────────────────────
--
-- BUSINESS QUESTION:
--   How active is each region in terms of number of purchases?
--   A region could have high revenue but low transactions (premium buyers)
--   OR high transactions but lower revenue (budget buyers).
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - Does transaction count rank match the revenue rank from Query 1?
--   - If a region has low transactions but decent revenue, what does that imply?
--
-- Copilot Chat Prompt:
-- "Write SQL to count the number of transactions per region
--  from a table called 'sales_transactions'.
--  Also calculate the average revenue per transaction per region.
--  Order by transaction count descending.
--  Label columns as: region, transaction_count, avg_revenue_per_transaction."

-- TODO 3: Write your Query 3 here

SELECT
	region,
	COUNT(*) AS transaction_count,
	ROUND(AVG(revenue), 2) AS avg_revenue_per_transaction
FROM sales_transactions
GROUP BY region
ORDER BY transaction_count DESC;




-- ============================================================
-- INTERMEDIATE LEVEL QUERIES (Complete after Beginner queries)
-- ============================================================

-- ── Query 4: Monthly Revenue Trend ────────────────────────────────────────────
--
-- BUSINESS QUESTION:
--   How did revenue change month over month in Q1?
--   Is the business trending up, down, or flat?
--
-- NOTE: The 'date' column is formatted as YYYY-MM-DD after cleaning.
--       In SQLite, use strftime('%m', date) to extract the month number.
--       NOT MONTH(date) — that is MySQL syntax and will not work here.
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - Is January → March trending upward? Downward? Flat?
--   - Is there a month with a notable spike or dip?
--   - If revenue dropped in March, what might explain it?
--
-- Copilot Chat Prompt:
-- "Write SQLite SQL to extract the month number from a column named 'date'
--  formatted as YYYY-MM-DD, using strftime('%m', date).
--  Calculate total revenue per month from 'sales_transactions'.
--  Label columns as: month_number, month_name (use CASE WHEN to show Jan/Feb/Mar),
--  and total_revenue (rounded to 2 decimal places).
--  Order by month_number ascending."

-- TODO 4: Write your Query 4 here

SELECT
	strftime('%m', date) AS month_number,
	CASE strftime('%m', date)
		WHEN '01' THEN 'Jan'
		WHEN '02' THEN 'Feb'
		WHEN '03' THEN 'Mar'
	END AS month_name,
	ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_transactions
GROUP BY month_number
ORDER BY month_number ASC;




-- ── Query 5: Revenue and Average Discount by Category ─────────────────────────
--
-- BUSINESS QUESTION:
--   Where are we giving the most discounts — and is it generating revenue,
--   or just eroding margin without growing volume?
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - Which category has the highest average discount?
--   - Does that category also have the highest revenue? (Good sign)
--   - Or does it have LOW revenue despite heavy discounting? (Warning sign)
--   - This is the beginning of a margin analysis conversation.
--
-- Copilot Chat Prompt:
-- "Write SQL to group by product_category from 'sales_transactions' and calculate:
--  - SUM(revenue) as total_revenue
--  - AVG(discount_pct) as avg_discount (rounded to 3 decimal places)
--  - COUNT(*) as transaction_count
--  Order by avg_discount descending."

-- TODO 5: Write your Query 5 here

SELECT
	product_category,
	ROUND(SUM(revenue), 2) AS total_revenue,
	ROUND(AVG(discount_pct), 3) AS avg_discount,
	COUNT(*) AS transaction_count
FROM sales_transactions
GROUP BY product_category
ORDER BY avg_discount DESC;




-- ============================================================
-- ADVANCED LEVEL QUERIES (Complete if time permits)
-- ============================================================

-- ── Query 6: Customer Purchase Frequency and Value ────────────────────────────
--
-- BUSINESS QUESTION:
--   Who are our most valuable customers by total spend and transaction frequency?
--   What percentage of revenue do our top 10 customers represent?
--
-- WHAT TO LOOK FOR IN THE RESULTS:
--   - Are our top spenders also our most frequent buyers?
--   - What is the difference in revenue between the #1 and #10 customer?
--   - If top 10 customers represent >30% of revenue, that is a retention risk.
--
-- Copilot Chat Prompt:
-- "Write SQL to calculate per customer from 'sales_transactions':
--  - customer_id
--  - COUNT(*) as total_transactions
--  - SUM(revenue) as total_revenue (rounded to 2 decimal places)
--  - AVG(revenue) as avg_order_value (rounded to 2 decimal places)
--  - MAX(date) as most_recent_purchase
--  Order by total_revenue descending.
--  Show only the top 10 customers using LIMIT."

-- TODO 6: Write your Query 6 here

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




-- ── Query 7: Discount Impact — Do Discounts Drive Revenue? ───────────────────
--
-- BUSINESS QUESTION:
--   Do discounts actually drive higher revenue per transaction?
--   Or do we give discounts and still get the same (or lower) transaction values?
--
-- INTERPRETATION GUIDE:
--   - If discounted transactions have HIGHER revenue: discounts drive volume ✅
--   - If discounted transactions have LOWER revenue: discounts just reduce margin ⚠️
--   - If about the same: discounts are not moving the needle either way
--
-- Copilot Chat Prompt:
-- "Write SQL to compare transactions from 'sales_transactions':
--  Group 1: discount_pct > 0 (discounted orders)
--  Group 2: discount_pct = 0 (full-price orders)
--  For each group calculate:
--  - A label ('Discounted' or 'Full Price') as discount_group
--  - COUNT(*) as transaction_count
--  - AVG(revenue) as avg_revenue (rounded to 2 decimal places)
--  - SUM(revenue) as total_revenue (rounded to 2 decimal places)
--  Use a CASE WHEN statement to create the group label."

-- TODO 7: Write your Query 7 here

SELECT
	CASE WHEN discount_pct > 0 THEN 'Discounted' ELSE 'Full Price' END AS discount_group,
	COUNT(*) AS transaction_count,
	ROUND(AVG(revenue), 2) AS avg_revenue,
	ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_transactions
GROUP BY discount_group;
