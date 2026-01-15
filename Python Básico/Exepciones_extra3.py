my_list = ['10', 'manzana', '5.5', '3', 'n/a']


def sum_list_of_floats():
  result = 0
  for value in my_list:
    try:
      value = float(value)
      print(f"{value} sumado correctamente")
      result += value
    except:
      print(f"Elemento inválido: {value}")
  print(f"Total de la suma: {result}")


sum_list_of_floats()