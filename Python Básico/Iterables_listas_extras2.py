my_list = []
negative = 0
counter = 1
while counter < 6:
    num = int(input(f"Ingrese un número {counter}:"))
    counter += 1
    my_list.append(num)
for value in my_list:
    if value <= 0:
        negative = 1
if negative == 1:
    print("La lista tiene números negativos o ceros.")
else:
    print("Todos los números son positivos.")
