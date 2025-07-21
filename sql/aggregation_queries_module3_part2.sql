-- Query 1: GROUPING SETS to aggregate sales by country, category, and both
SELECT 
    dco.country, 
    dca.category, 
    SUM(fs.amount) AS totalsales
FROM "FactSales" fs
LEFT JOIN "DimCountry" dco
    ON fs.countryid = dco.countryid
LEFT JOIN "DimCategory" dca
    ON fs.categoryid = dca.categoryid
GROUP BY GROUPING SETS (
    (dco.country), 
    (dca.category), 
    (dco.country, dca.category)
);

-- Query 2: ROLLUP to show totals by year, country, and sub-totals per grouping level
SELECT 
    dd.Year AS year, 
    dco.country, 
    SUM(fs.amount) AS totalsales
FROM "FactSales" fs
LEFT JOIN "DimDate" dd
    ON fs.dateid = dd.dateid
LEFT JOIN "DimCountry" dco
    ON fs.countryid = dco.countryid
GROUP BY ROLLUP (
    dd.Year, 
    dco.country
)
ORDER BY dd.Year, dco.country;

-- Query 3: CUBE to analyze average sales by year and country, including all combinations
SELECT 
    dd.Year AS year, 
    dco.country, 
    AVG(fs.amount) AS averagesales
FROM "FactSales" fs
LEFT JOIN "DimDate" dd
    ON fs.dateid = dd.dateid
LEFT JOIN "DimCountry" dco
    ON fs.countryid = dco.countryid
GROUP BY CUBE (
    dd.Year, 
    dco.country
)
ORDER BY dd.Year, dco.country;

-- Query 4: Materialized View to store total sales per country
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT 
    dco.country, 
    SUM(fs.amount) AS totalsales
FROM "FactSales" fs
LEFT JOIN "DimCountry" dco
    ON fs.countryid = dco.countryid
GROUP BY dco.country;