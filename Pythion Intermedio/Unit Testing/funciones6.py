original_string = "python-variable-funcion-computadora-monitor"


def string_to_alphabetical_list(original_string, my_list):
    word = ""
    for char in original_string:
        if char != "-":
            word += char
        else:
            my_list.append(word)
            word = ""
    my_list.append(word)
    my_list.sort()
    return my_list


def list_to_string(my_list):
    result = ""
    counter = 0
    for word in my_list:
        result += word
        counter += 1
        if len(my_list) == counter:
            print(result)
            return result
        result += "-"


def sort_string_alphabetically(original_string):
    my_list = []
    string_to_alphabetical_list(original_string, my_list)
    result = list_to_string(my_list)
    return result


sort_string_alphabetically(original_string)