import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        self.area = math.pi * (self.radius ** 2)


def program():
    area_list = []
    while True:
        try:
            radius = float(input("Introdusca el área del círculo: "))
            my_circle = Circle(radius)
            my_circle.get_area()
            area_list.append(my_circle.area)
            return print(f"[Área = {my_circle.area}]\n")
        except ValueError:
            print("¡Debe ser un numero!\n")


program()