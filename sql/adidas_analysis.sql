-- Query 1: Overall Business KPIs

SELECT
    SUM("Total Sales") AS total_revenue,
    SUM("Units Sold") AS total_units_sold,
    SUM("Operating Profit") AS total_profit,
    SUM("Operating Profit") * 1.0 / SUM("Total Sales") AS operating_margin
FROM sales;

-- Query 2: Revenue by Region

SELECT
    Region,
    SUM("Total Sales") AS total_revenue
FROM sales
GROUP BY Region
ORDER BY total_revenue DESC;
