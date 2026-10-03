INSERT INTO "user" ("full_name", "email", "registration_date")
VALUES ('Victor Manuel', 'victor@e.com', '2026-09-27 10:00:00');

INSERT INTO "user" ("full_name", "email", "registration_date")
VALUES ('Carmen Patricia', 'carmen@e.com', '2026-09-27 10:00:00');

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available")
VALUES (1001, 'Teclado', 51000, '2026-09-01 08:00:00', 'Logitech', 15);

INSERT INTO "products" ("code", "name", "price", "entry_date", "brand", "stock_available")
VALUES (1002, 'Mouse', 25000, '2026-09-01 08:00:00', 'Razer', 30);

INSERT INTO "payment_methods" ("method_type", "bank_name")
VALUES ('Tarjeta', 'BAC');

INSERT INTO "payment_methods" ("method_type", "bank_name")
VALUES ('Efectivo', 'N/A');

INSERT INTO "invoices" ("user_id", "payment_method_id", "purchase_date", "total_amount", "buyer_phone_number", "cashier_employee_code")
VALUES (1, 1, '2026-09-27 10:30:00', 76000, '88888888', 501);

INSERT INTO "products_per_invoice" ("quantity", "total_amount", "product_id", "invoice_id")
VALUES (1, 51000, 1, 1);

INSERT INTO "products_per_invoice" ("quantity", "total_amount", "product_id", "invoice_id")
VALUES (1, 25000, 2, 1);

INSERT INTO "shopping_cart" ("shopping_cart_id", "product_code")
VALUES (1, 1);

INSERT INTO "reviews" ("user_id", "review_id", "product_code", "comment", "rating_1_to_5", "date")
VALUES (1, 101, 1, 'Excelente producto, llegó a tiempo.', 5, '2026-09-27 11:00:00');

INSERT INTO "invoices" ("user_id", "payment_method_id", "purchase_date", "total_amount", "buyer_phone_number", "cashier_employee_code")
VALUES (2, 1, '2026-09-27 12:30:00', 25000, '99999999', 501);

INSERT INTO "products_per_invoice" ("quantity", "total_amount", "product_id", "invoice_id")
VALUES (1, 25000, 2, 2);

INSERT INTO "shopping_cart" ("shopping_cart_id", "product_code")
VALUES (2, 2);
