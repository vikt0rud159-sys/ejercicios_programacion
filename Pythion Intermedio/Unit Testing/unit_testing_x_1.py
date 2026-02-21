def subtract(number1, number2):
    try:
        return number1 - number2
    except TypeError:
        print("!Todos los valores deben ser números¡")


def sum_all(*args):
    try:
        return sum(args)
    except TypeError:
        print("!Todos los valores deben ser números¡")


def average(*args):
    try:
        return sum(args) / int(len(args))
    except TypeError:
        print("!Todos los valores deben ser números¡")


print(subtract(1, 2))
print(sum_all(1, 2, 3))
print(average(2, 2, 3))