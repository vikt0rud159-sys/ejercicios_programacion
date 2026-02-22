my_list = []
new_list = []
counter = 1
while counter < 6:
    string = input(f"Ingrese una palabra {counter}:")
    counter += 1
    my_list.append(string)
    if len(string) >= 4:
        new_list.append(string)
print(new_list)
