def check_list_of_values(func):
    def wrapper(*args):
        try:
            sum(args)
            func(args)
        except TypeError:
            print("Al menos uno de los parámetros no es un número")
        return
    return wrapper

@check_list_of_values
def print_numbers(*args):
    print(args)
    return args

print_numbers(3, 5, 7, 8)
print_numbers(3, 5, 7, "W")