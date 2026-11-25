-- 1. Executive RFM Segment Summary (Customer Share & Revenue Share)
SELECT 
    Segment,
    COUNT(DISTINCT CustomerID) AS customer_count,
    ROUND(COUNT(DISTINCT CustomerID) * 100.0 / SUM(COUNT(DISTINCT CustomerID)) OVER(), 2) AS customer_pct,
    ROUND(SUM(Monetary), 2) AS total_revenue,
    ROUND(SUM(Monetary) * 100.0 / SUM(SUM(Monetary)) OVER(), 2) AS revenue_pct,
    ROUND(AVG(Monetary), 2) AS avg_customer_spend,
    ROUND(AVG(Frequency), 1) AS avg_frequency,
    ROUND(AVG(Recency), 0) AS avg_recency_days
FROM rfm_segments
GROUP BY Segment
ORDER BY total_revenue DESC;

-- 2. Priority Win-Back Target List (High-Value At-Risk & Hibernating Buyers)
SELECT 
    CAST(CustomerID AS INT) AS customer_id,
    Recency AS days_since_last_order,
    Frequency AS total_orders,
    ROUND(Monetary, 2) AS total_spend,
    RFM_Score,
    Segment
FROM rfm_segments
WHERE Segment IN ('At Risk', 'Hibernating', 'Big Spenders')
  AND Recency > 90
ORDER BY Monetary DESC;