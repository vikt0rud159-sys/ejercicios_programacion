def open_and_sort_file(my_list):
    try:
        with open("nombres_canciones.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                my_list.append(line)
            my_list.sort()
    except Exception:
        print("Archivo no encontrado:")
        exit()


def write_new_file(my_list):
    with open("nombres_canciones_alfa.txt", "w", encoding="utf-8") as file:
        for value in my_list:
            file.write(value)


def create_new_sort_file():
    my_list = []
    try:
        open_and_sort_file(my_list)
        write_new_file(my_list)
        print("Completado")
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')


create_new_sort_file()