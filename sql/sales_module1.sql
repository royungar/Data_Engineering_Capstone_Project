-- Create the database and switch to it
CREATE DATABASE sales;
USE sales;

-- Create the sales_data table
CREATE TABLE sales_data (
  product_id INT,
  customer_id INT,
  price INT,
  quantity INT,
  timestamp TIMESTAMP
);

-- Create an index on the timestamp column
CREATE INDEX ts ON sales_data(timestamp);

-- -- Optional validation queries 
-- SHOW TABLES;
-- SELECT COUNT(*) FROM sales_data;
-- SHOW INDEXES FROM sales_data;