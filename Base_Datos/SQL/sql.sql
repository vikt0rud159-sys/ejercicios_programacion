CREATE TABLE "invoices"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER REFERENCES "user"("id"),
    "payment_method_id" INTEGER REFERENCES "payment_methods"("id"),
    "purchase_date" DATETIME NOT NULL,
    "total_amount" DECIMAL(10, 2) NOT NULL
);

CREATE TABLE "products_per_invoice"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "quantity" INTEGER NOT NULL,
    "total_amount" DECIMAL(10, 2) NOT NULL,
    "product_id" INTEGER REFERENCES "products"("id"),
    "invoice_id" INTEGER REFERENCES "invoices"("id")
);

CREATE TABLE "products"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "code" INTEGER NOT NULL,
    "name" VARCHAR(15) NOT NULL,
    "price" DECIMAL(10, 2) NOT NULL,
    "entry_date" DATETIME NOT NULL,
    "brand" VARCHAR(15) NOT NULL,
    "stock_available" INTEGER NOT NULL
);

CREATE TABLE "shopping_cart"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "shopping_cart_id" INTEGER REFERENCES "user"("id"),
    "product_code" INTEGER REFERENCES "products"("id")
);

CREATE TABLE "user"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "full_name" VARCHAR(25) NOT NULL,
    "email" VARCHAR(25) UNIQUE NOT NULL,
    "registration_date" DATETIME NOT NULL
);

CREATE TABLE "reviews"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER REFERENCES "user"("id"),
    "review_id" INTEGER NOT NULL,
    "product_code" INTEGER REFERENCES "products"("id"),
    "comment" VARCHAR(100) NOT NULL,
    "rating_1_to_5" INTEGER DEFAULT 5 CHECK ("rating_1_to_5" BETWEEN 1 AND 5),
    "date" DATETIME NOT NULL
);

CREATE TABLE "payment_methods"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "method_type" VARCHAR(10) NOT NULL,
    "bank_name" VARCHAR(10) NOT NULL
);

ALTER TABLE "invoices"
    ADD buyer_phone_number VARCHAR(15);

ALTER TABLE "invoices"
    ADD cashier_employee_code INTEGER;
