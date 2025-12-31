name = ""
age = ""

def get_name():
  global name
  name = input("Ingrese su nombre: ")
  try:
    if name.isdigit():
      raise ValueError()
  except:
    print("El nombre no puede ser un número")
    exit()
  return name


def get_age():
  global age
  age = input("Ingrese su edad: ")
  try:
    age = int(age)
  except ValueError:
    print("Número no valido")
    exit()
  return age


def print_greeting():
  try:
    get_name()
    get_age()
  except Exception as ex:
    print(f'An unexpected error ocurred: {ex}')
  print(f"Hola {name}, su edad es {age}")


print_greeting()