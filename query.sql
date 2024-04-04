-- Query1: Select all columns for all productions
SELECT * FROM productions;

-- Query 2: Select production quantities and their corresponding locations
SELECT "Production_Quantity_kg", "Production_Location" FROM productions;

-- Query 3: Find the total production quantity for a specific location
SELECT "Production_Location", SUM("Production_Quantity (kg)") AS "Total_Quantity"
FROM productions
GROUP BY "Production_Location";

-- Query 4: Find the average production cost
SELECT AVG("Production_Cost") AS "Average_Cost" FROM productions;

-- Query 5: Find the total production hours for a specific date
SELECT "Production_Date", SUM("Production_Hours") AS "Total_Hours"
FROM productions
GROUP BY "Production_Date";

-- Query 6: Find the total production quantity and cost for each date
SELECT "Production_Date", SUM("Production_Quantity_kg") AS "Total_Quantity", SUM("Production_Cost") AS "Total_Cost"
FROM productions
GROUP BY "Production_Date";

-- Query 7: Find the production locations where the quantity produced is above a certain threshold
SELECT "Production_Location"
FROM productions
WHERE "Production_Quantity_kg" > [threshold];


-- Query 8: Find the production quantities and costs within a date range
SELECT "Production_Date", SUM("Production_Quantity_kg") AS "Total_Quantity", SUM("Production_Cost") AS "Total_Cost"
FROM productions
WHERE "Production_Date" BETWEEN [start_date] AND [end_date]
GROUP BY "Production_Date";

-- Query 9: Calculate the average production quantity per hour
SELECT AVG("Production_Quantity_kg") / AVG("Production_Hours") AS "Average Quantity per Hour"
FROM productions;

--Query 10: Find the highest production quantity along with its corresponding date
SELECT "Production_Date", MAX("Production_Quantity_kg") AS "Highest Quantity"
FROM productions;
