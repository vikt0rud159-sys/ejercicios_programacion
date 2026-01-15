global_variable = ("Hola")


def create_variable_goodbye():
    goodbye = "Adios"

def change_global_variable_hello():
    global global_variable
    global_variable = "Hola mundo"
    print(global_variable)


print(global_variable)
change_global_variable_hello()
print(global_variable)
print(goodbye) 