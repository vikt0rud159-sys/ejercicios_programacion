time = int(input("Ingresa tiempo en segundos: "))
if time > 600:
    print("Mayor")
elif time == 600:
    print("Igual")
else:
    print("Faltan", 600 - time, "segundos para llegar a 10 minutos")