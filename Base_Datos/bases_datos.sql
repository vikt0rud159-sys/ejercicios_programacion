CREATE TABLE `Invoices`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `User ID` BIGINT NOT NULL,
    `Invoice Number` BIGINT NOT NULL,
    `Purchase date` DATETIME NOT NULL,
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
    `Shopping Cart ID` BIGINT NOT NULL,
    `Product code` BIGINT NOT NULL
);
CREATE TABLE `User`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Full name` VARCHAR(255) NOT NULL,
    `Email` VARCHAR(255) NOT NULL,
    `Registration date` DATETIME NOT NULL
);
ALTER TABLE
    `User` ADD UNIQUE `user_email_unique`(`Email`);
CREATE TABLE `Reviews`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Review ID` BIGINT NOT NULL,
    `Product code` BIGINT NOT NULL,
    `Comment` VARCHAR(255) NOT NULL,
    `Rating (1 al 5)` BIGINT NOT NULL,
    `Date` DATETIME NOT NULL
);
CREATE TABLE `Payment Methods`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Method ID` BIGINT NOT NULL,
    `Method type` VARCHAR(255) NOT NULL,
    `Bank name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_review id_foreign` FOREIGN KEY(`Review ID`) REFERENCES `User`(`id`);
ALTER TABLE
    `Payment Methods` ADD CONSTRAINT `payment methods_method id_foreign` FOREIGN KEY(`Method ID`) REFERENCES `User`(`id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_total amount_foreign` FOREIGN KEY(`Total amount`) REFERENCES `Payment Methods`(`id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `Products Per Invoice`(`Invoice ID`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_product code_foreign` FOREIGN KEY(`Product code`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_shopping cart id_foreign` FOREIGN KEY(`Shopping Cart ID`) REFERENCES `User`(`id`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_product code_foreign` FOREIGN KEY(`Product code`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `Products Per Invoice`(`Product ID`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_user id_foreign` FOREIGN KEY(`User ID`) REFERENCES `User`(`id`);
