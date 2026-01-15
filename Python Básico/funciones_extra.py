word = input("Ingrese una palabra: ")
search = input("Ingrese carácter a buscar: ")


def count_character():
    counter = 0
    for char in word:
        if char == search:
            counter += 1
    return print(f"Se a encontrado {counter} veces el carácter")


count_character()