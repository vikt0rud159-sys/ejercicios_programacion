CREATE TABLE `Invoices`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Invoice Number` BIGINT NOT NULL,
    `Purchase date` DATETIME NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Quantity` BIGINT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Product ID` BIGINT NOT NULL,
    `Invoice ID` BIGINT NOT NULL
);
CREATE TABLE `Products`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Code` BIGINT NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry date` DATETIME NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Products` BIGINT NOT NULL
);
CREATE TABLE `Shopping Cart Products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Shopping Cart ID` BIGINT NOT NULL,
    `Product ID` BIGINT NOT NULL
);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `Shopping Cart`(`Products`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `Products Per Invoice`(`Invoice ID`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart`(`id`);
ALTER TABLE
    `Shopping Cart Products` ADD CONSTRAINT `shopping cart products_shopping cart id_foreign` FOREIGN KEY(`Shopping Cart ID`) REFERENCES `Shopping Cart`(`id`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `Shopping Cart Products`(`Product ID`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `Products Per Invoice`(`Product ID`);