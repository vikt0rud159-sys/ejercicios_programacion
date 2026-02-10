from datetime import datetime

def log_call(func):
    def wrapper(num1, num2):
        result = func(num1, num2)
        print(f"\nfunc:{func.__name__} - args: {num1, num2} - [{datetime.now()}] - Resultado: {result}\n")
    return wrapper


def validate_numbers(func):
    def wrapper(num1, num2):
        try:
            sum((num1, num2))
            func(num1, num2)
            return
        except:
            print("No todos los valores no son numéricos\n")
    return wrapper


@validate_numbers
@log_call
def multiply(num1, num2):
    return num1 * num2


multiply(3, 4)