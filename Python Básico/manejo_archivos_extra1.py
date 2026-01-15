def print_file_txt():
    with open("manejo archivos extra1.txt", "r") as file:
        my_list = []
        txt=""
        for line in file:
            my_list.append(line)
        for line in my_list:
            txt += line.rstrip()
            txt += " "
    print(txt)


print_file_txt()