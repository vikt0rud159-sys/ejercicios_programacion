class Inventory:
    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def evaluate_inventory(self, products_list):
            total = 0
            for product in products_list:
                total += product.price * product.quantity
            print(f"\n[Valor Total: {total}]\n")


def program():
    products_list = []
    while True:
        add = input("Añadir producto: [S][N]   ")
        if add.lower() == "s":
            product = add_product()
            products_list.append(product)
        show = input("Mostrar valor de inventario: [S][N]   ")
        if show.lower() == "s":
            product.evaluate_inventory(products_list)
        else:
            print()
            break


def add_product():
    name = input("   Nombre del producto: ")
    while   True:
        try:
            price = float(input("   Precio del producto: "))
            quantity = float(input("   Cantidad disponible: "))
            product = Inventory.Product(name, price, quantity)
            return product
        except ValueError:
            print("¡Debe ser un valor numerico!\n")


program()