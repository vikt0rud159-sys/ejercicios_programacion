def get_text_to_convert(my_list):
    with open("manejo archivos extra3.1.txt") as file:
        for line in file:
            my_list.append(line.upper())


def write_new_file(my_list):
    with open("manejo archivos extra3.2.txt", "w") as file:
        for value in my_list:
            file.write(value)
        print("Completado")


def convert_a_file_to_uppercase():
    my_list = []
    try:
        get_text_to_convert(my_list)
        write_new_file(my_list)
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')


convert_a_file_to_uppercase()