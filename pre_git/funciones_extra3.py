def count_vowels_of_string():
    string = input("Ingrese un palabra: ")
    str_lower = string.lower()
    counter = 0
    for char in str_lower:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            counter += 1
    return print(counter)


count_vowels_of_string()