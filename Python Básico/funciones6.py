original_string = "python-variable-funcion-computadora-monitor"


my_list = []


def string_to_alphabetical_list():
  word = ""
  for char in original_string:
    if char != "-":
      word += char
    else:
      my_list.append(word)
      word = ""
  my_list.sort()


def list_to_string():
  result = ""
  counter = 0
  for word in my_list:
    result += word
    counter += 1
    if len(my_list) == counter:
      return print(result)
    result += "-"


def sort_string_alphabetically():
  string_to_alphabetical_list()
  list_to_string()


sort_string_alphabetically()