price = float(input("Ingrese el precio del producto: "))
if price < 100:
    price = price - price * 0.02
else:
    price = price - price * 0.1
print("El nuevo precio con descuento es:", price)