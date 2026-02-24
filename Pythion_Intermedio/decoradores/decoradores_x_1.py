def repeat_twice(func):
    def wrapper(name):
        print(F"Hola, {func(name)}")
        print(F"Hola, {func(name)}")
    return wrapper


@repeat_twice
def print_hello_name(name):
    return name


print_hello_name("Lola")