word_list = []


def get_words():
    counter = 1
    while counter < 6:
        word = input(f"Ingrese una palabra ({counter} de 5): ")
        word_list.append(word)
        counter += 1


def select_words(num_char):
    n_char_list = []
    for word in word_list:
        if len(word) >= num_char:
            n_char_list.append(word)
    return print(n_char_list)


def get_word_with_n_char():
    get_words()
    num_char = int(input("Ingrese el numero de letras minimas en la palabra: "))
    select_words(num_char)


get_word_with_n_char()