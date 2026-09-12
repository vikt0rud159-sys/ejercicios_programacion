CREATE TABLE "Invoices"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "User ID" INT REFERENCES "User"("id"),
    "Payment Method ID" INT REFERENCES "Payment Methods"("id"),
    "Purchase date" DATETIME NOT NULL,
    "Total amount" DECIMAL(10, 2) NOT NULL
);

CREATE TABLE "Products Per Invoice"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "Quantity" INT NOT NULL,
    "Total amount" DECIMAL(10, 2) NOT NULL,
    "Product ID" INT REFERENCES "Products"("id"),
    "Invoice ID" INT REFERENCES "Invoices"("id")
);

CREATE TABLE "Products"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "Code" INT NOT NULL,
    "Name" VARCHAR(15) NOT NULL,
    "Price" DECIMAL(10, 2) NOT NULL,
    "Entry date" DATETIME NOT NULL,
    "Brand" VARCHAR(15) NOT NULL,
    "Stock available" INT NOT NULL
);

CREATE TABLE "Shopping Cart"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "Shopping Cart ID" INT REFERENCES "User"("id"),
    "Product code" INT REFERENCES "Products"("id")
);

CREATE TABLE "User"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "Full name" VARCHAR(25) NOT NULL,
    "Email" VARCHAR(25) UNIQUE NOT NULL,
    "Registration date" DATETIME NOT NULL
);

CREATE TABLE "Reviews"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "User ID" INT REFERENCES "User"("id"),
    "Review ID" INT NOT NULL,
    "Product code" INT REFERENCES "Products"("id"),
    "Comment" VARCHAR(100) NOT NULL,
    "Rating (1 al 5)" INT DEFAULT 5 CHECK ("Rating (1 al 5)" BETWEEN 1 AND 5),
    "Date" DATETIME NOT NULL
);

CREATE TABLE "Payment Methods"(
    "id" INT AUTO_INCREMENT PRIMARY KEY,
    "Method type" VARCHAR(10) NOT NULL,
    "Bank name" VARCHAR(10) NOT NULL
);

ALTER TABLE "Invoices"
    ADD  BuyerPhoneNumber VARCHAR(15);

ALTER TABLE "Invoices"
    ADD CashierEmployeeCode INT;
