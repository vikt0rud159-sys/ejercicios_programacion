number_1 = input("Ingrese primer número: ")
number_2 = input("Ingrese segundo número: ")
number_3 = input("Ingrese tercer número: ")
if int(number_1) > int(number_2) and int(number_1) > int(number_3):
    print("El número mayor es:", number_1)
elif int(number_2) > int(number_1) and int(number_2) > int(number_3):
    print("El número mayor es:", number_2)
else:
    print("El número mayor es:", number_3)