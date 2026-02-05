def print_parameters_and_return(func):
    def wrapper(num1, num2):
        print(f"Parámetros: {num1}, {num2}")
        result = func(num1, num2)
        print(f"Retorno: {result}\n")
        return result
    return wrapper

@print_parameters_and_return
def sum_numbers(num1, num2):
    return num1 + num2

sum_numbers(3, 5)