-- Query1: Describe the table
DESCRIBE TABLE Kasapreko;

-- Query 2: Find the total transaction amount for the year 2023
SELECT SUM("Transaction Amount") AS Total_Transaction_Amount
FROM Kasapreko
WHERE EXTRACT(YEAR FROM "Transaction Date") = 2023;

-- Query 3: Calculate the average transaction amount per product
SELECT Product, AVG("Transaction Amount") AS Avg_Transaction_Amount
FROM Kasapreko
GROUP BY Product;

-- Query 4: Identify the top 5 customers by total transaction amount
SELECT "Customer Name", SUM("Transaction Amount") AS Total_Transaction_Amount
FROM Kasapreko
GROUP BY "Customer Name"
ORDER BY Total_Transaction_Amount DESC, "Customer Name"
LIMIT 5;

-- Query 5: Identify Customer Preference for medium of communication, website/app
SELECT "Customer Preference", COUNT(*) AS Results
FROM Kasapreko
GROUP BY "Customer Preference"
ORDER BY COUNT(*) DESC;

-- Query 6: Find out the number of transactions in the year 2024
SELECT COUNT("Transaction Amount")
FROM Kasapreko
WHERE EXTRACT(YEAR FROM "Transaction Date") = 2024;

-- Query 7: Identify which product has the least number of purchase and quantity purchased 
SELECT Product, COUNT(*) AS Purchases_Count, MIN("Product Quantity") AS Min_Product_Quantity 
FROM Kasapreko
GROUP BY Product
ORDER BY Purchases_Count ASC
LIMIT 1;


-- Query 8: Total number of distinct/unique customers
SELECT COUNT(DISTINCT "Name") AS Total_Customers
FROM Kasapreko;

-- Query 9: Identify total number of customers with an address with 'suite'
SELECT "Customer Name", COUNT(*) AS Customers_With_Box_Address
FROM Kasapreko
WHERE "Address" LIKE '%Box%';

-- Query 10: Find total quantity of each product sold till date
SELECT Product, SUM(Product Quantity) AS Total_Quantity_Sold
FROM Kasapreko
GROUP BY Product;
