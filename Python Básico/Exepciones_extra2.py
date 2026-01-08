my_list = ['4', 'hola', '10', '5.2']

def convert_list_to_ints():
  print("Resultado:")
  for value in my_list:
    try:
      value = int(value)
      print(f"{value} convertido a {value}")
    except ValueError:
      print(f"No se pudo convertir el elemento: {value}")

convert_list_to_ints()