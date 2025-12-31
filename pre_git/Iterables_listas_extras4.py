my_list = []
new_list = []
counter = 1
total = 0
while counter < 6:
    num = int(input(f"Ingrese un número {counter}:"))
    counter += 1
    my_list.append(num)
for value in my_list:
    total += value
total_average = total / len(my_list)
print(f"Promedio: {total_average}.")
for value in my_list:
    if value > total_average:
        new_list.append(value)
print(f"Nueva lista: {new_list}.")