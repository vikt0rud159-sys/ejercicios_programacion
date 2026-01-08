my_list = []
counter = 1
search_counter = 0
num_list = int(input("Cantidad de números para la lista:"))
while counter < num_list + 1:
    num = int(input(f"Ingrese un número {counter}:"))
    counter += 1
    my_list.append(num)
search = int(input("Ingrese número a buscar:"))
for value in my_list:
    if value == search:
        search_counter += 1
print(f"El número {search} se encontró {search_counter} veces.")