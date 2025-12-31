def insert_txt():
    string = input("Ingrese una linea de txt: ")
    with open("manejo archivos extra4.txt", "a") as file:
        file.write(f"\n{string}")
        print("Completado")

insert_txt()