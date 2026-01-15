my_list = []
counter = 1
low = float("inf")
while counter < 5:
    num = int(input(f"Ingrese un número {counter}:"))
    if num < low:
        low = num
    counter += 1
    my_list.append(num)
print(f"{my_list}, El más bajo fue {low}.")