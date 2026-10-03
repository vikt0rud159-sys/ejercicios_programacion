-- 1. Crear categorías y ajustar productos.
CREATE TABLE "categories"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT UNIQUE NOT NULL,
    "description" TEXT NOT NULL
);

ALTER TABLE "products"
    ADD category_id INTEGER REFERENCES "categories"("id");

INSERT INTO "categories" ("name", "description")
VALUES ('Electrónica', 'Productos de electrónica');

INSERT INTO "categories" ("name", "description")
VALUES ('Ropa', 'Productos de ropa');

INSERT INTO "categories" ("name", "description")
VALUES ('Hogar', 'Productos para el hogar y decoración');

UPDATE "products"
    SET "category_id" = 1
    WHERE "id" IN (1, 2);

SELECT * FROM products

-- 2. Carga de productos y filtros básicos.
INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1003, 'Camiseta', 20000, '2026-09-01', 'Nike', 50, 2);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1004, 'Pantalón', 30000, '2026-09-01', 'Adidas', 30, 2);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1005, 'Zapatos', 50000, '2026-09-01', 'Reebok', 20, 2);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1007, 'Mesa', 40000, '2026-09-01', 'IKEA', 10, 3);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1008, 'Silla', 25000, '2026-09-01', 'IKEA', 15, 3);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1009, 'Lámpara', 15000, '2026-09-01', 'Philips', 25, 3);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1010, 'Televisor', 80000, '2026-09-01', 'Samsung', 5, 1);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1011, 'Laptop', 120000, '2026-09-01', 'Dell', 8, 1);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1012, 'Smartphone apple', 60000, '2026-09-01', 'Apple', 12, 1);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available", "category_id")
VALUES (1013, 'Tablet', 40000, '2026-09-01', 'Samsung', 10, 1);

SELECT * FROM products

SELECT * FROM products
WHERE price > 50000;

SELECT * FROM products
WHERE name LIKE '%apple%';

SELECT * FROM products
ORDER BY price DESC LIMIT 5


-- 3. Correcciones de datos en productos.
UPDATE "products"
    SET "stock_available" = 0
    WHERE "price" <= 0;

UPDATE "products"
    SET "price" = "price" + 100
    WHERE "stock_available" < 10;

UPDATE "products"
    SET "stock_available" = "stock_available" - 1
    WHERE "id" = 1;

SELECT * FROM products ORDER BY id ASC LIMIT 10
