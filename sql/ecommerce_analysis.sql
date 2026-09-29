CREATE DATABASE ECommerceAnalytics;
GO

USE ECommerceAnalytics;
GO

SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
ORDER BY TABLE_NAME;
SELECT TOP 10 *
FROM dbo.ecommerce_events;

--To check how many records are there.
SELECT COUNT(*) AS total_records
FROM dbo.ecommerce_events;

-- Count purchases by product category

SELECT
    product_category,
    COUNT(*) AS purchase_count
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY product_category
ORDER BY purchase_count DESC;

-- Calculate total purchase revenue

SELECT
    SUM(revenue) AS total_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase';

-- Calculate revenue by product category

SELECT
    product_category,
    SUM(revenue) AS total_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY product_category
ORDER BY total_revenue DESC;
-- Calculate revenue by device

SELECT
    device,
    SUM(revenue) AS total_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY device
ORDER BY total_revenue DESC;

-- Calculate revenue by country

SELECT
    country,
    SUM(revenue) AS total_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY country
ORDER BY total_revenue DESC;

-- Find the top 10 customers by purchase revenue

SELECT TOP 10
    customer_id,
    SUM(revenue) AS total_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY customer_id
ORDER BY total_revenue DESC;

-- Calculate average purchase value by category

SELECT
    product_category,
    AVG(revenue) AS average_purchase_value
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY product_category
ORDER BY average_purchase_value DESC;

-- Calculate monthly purchase revenue

SELECT
    CONVERT(char(7), event_date, 126) AS month,
    SUM(revenue) AS monthly_revenue
FROM dbo.ecommerce_events
WHERE event_type = 'purchase'
GROUP BY CONVERT(char(7), event_date, 126)
ORDER BY month;

-- Calculate customer purchase rate

SELECT
    COUNT(DISTINCT CASE
        WHEN event_type = 'purchase' THEN customer_id
    END) AS purchasing_customers,
    
    COUNT(DISTINCT customer_id) AS total_customers,
    
    CAST(
        COUNT(DISTINCT CASE
            WHEN event_type = 'purchase' THEN customer_id
        END) * 100.0
        / COUNT(DISTINCT customer_id)
        AS DECIMAL(10,2)
    ) AS purchase_rate_percentage
FROM dbo.ecommerce_events;

-- Count customers who made more than one purchase

SELECT
    COUNT(*) AS repeat_customers
FROM (
    SELECT
        customer_id
    FROM dbo.ecommerce_events
    WHERE event_type = 'purchase'
    GROUP BY customer_id
    HAVING COUNT(*) > 1
) AS customer_purchases;
