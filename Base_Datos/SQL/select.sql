SELECT *
    FROM "Products";

SELECT *
    FROM "Products"
    WHERE "Price" > 50000;

SELECT "Product ID", COUNT(id)
    FROM "Products Per Invoice";

SELECT "Product ID", SUM("Total amount") AS TotalPurchased, COUNT(id) AS TotalPurchases
FROM "Products Per Invoice"
GROUP BY "Product ID";

SELECT *
    FROM "Invoices"
    GROUP BY "User ID";

SELECT *
    FROM "Invoices"
    GROUP BY "Total amount" DESC;

SELECT *
    FROM "Invoices"
    WHERE "id" = 1;
