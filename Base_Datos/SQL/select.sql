SELECT *
FROM products;

SELECT *
FROM products
WHERE price > 50000;

SELECT product_id, COUNT(id) AS total_compras
FROM products_per_invoice
GROUP BY product_id;

SELECT product_id, SUM(total_amount) AS total_purchased, COUNT(id) AS total_purchases
FROM products_per_invoice
GROUP BY product_id;

SELECT *
FROM invoices
WHERE user_id = 1;

SELECT *
FROM invoices
ORDER BY total_amount DESC;

SELECT *
FROM invoices
WHERE id = 1;
