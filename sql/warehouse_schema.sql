-- warehouse_schema.sql
-- Star schema design for SoftCart sales data warehouse
-- Includes dimension and fact tables with foreign key relationships

CREATE TABLE IF NOT EXISTS softcartDimDate (
    date_id INT PRIMARY KEY,
    date DATE,
    year INT,
    quarter INT,
    month CHAR(2),
    month_name VARCHAR(20),
    week INT,
    day INT,
    day_name VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS softcartDimCategory (
    category_id INT PRIMARY KEY,
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS softcartDimItem (
    item_id INT PRIMARY KEY,
    item VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS softcartDimCountry (
    country_id INT PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS softcartFactSales (
    sale_id INT PRIMARY KEY,
    date_id INT,
    amount NUMERIC,
    item_id INT,
    category_id INT,
    country_id INT,
    FOREIGN KEY (date_id) REFERENCES softcartDimDate(date_id),
    FOREIGN KEY (item_id) REFERENCES softcartDimItem(item_id),
    FOREIGN KEY (category_id) REFERENCES softcartDimCategory(category_id),
    FOREIGN KEY (country_id) REFERENCES softcartDimCountry(country_id)
);
