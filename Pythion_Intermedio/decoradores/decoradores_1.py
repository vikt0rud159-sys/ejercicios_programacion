def print_parameters_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros: {args, kwargs} Retorno: {func(*args, **kwargs)}\n")
    return wrapper

@print_parameters_and_return
def save_info(*args, **kwads):
    return "save_info retorn"

save_info(3, 5, m="M")
