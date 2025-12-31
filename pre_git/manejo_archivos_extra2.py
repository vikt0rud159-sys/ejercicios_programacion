def word_count_file():
    my_list = []
    with open("manejo archivos extra2.txt") as file:
        string = ""
        for line in file:
            line.rstrip()
            for char in line:
                string += char
                if char == " " or char == "\n":
                    my_list.append(string)
                    string = ""
    my_list.append(string)
    print(f"Este archivo contiene ", len(my_list), "palabras")


word_count_file()