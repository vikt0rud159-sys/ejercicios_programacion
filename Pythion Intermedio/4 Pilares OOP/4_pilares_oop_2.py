from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area():
        pass
    
    @abstractmethod
    def calculate_perimeter():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        print(f"Área = {self.area}")
    
    def calculate_perimeter(self):
        self.perimeter = (math.pi * (self.area * 2))
        print(f"Perimetro = {self.perimeter}\n")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        self.area = self.side ** 2
        print(f"Área = {self.area}")
    
    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        print(f"Perimetro = {self.perimeter}\n")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        self.area = self.width * self.height
        print(f"Área:  {self.area}")
    
    def calculate_perimeter(self):
        self.perimeter = (self.width + self.height) * 2
        print(f"Perimetro:  {self.perimeter}\n")


while True:
    shape = input("[Circulo(C)] [Cuadrado(S)] [Rectangulo(R)]   ")
    if shape.lower() == "c":
        circle = Circle(90)
        circle.calculate_area()
        circle.calculate_perimeter()
        break
    elif shape.lower() == "s":
        square = Square(10)
        square.calculate_area()
        square.calculate_perimeter()
        break
    elif shape.lower() == "r":
        rectangle = Rectangle(10, 50)
        rectangle.calculate_area()
        rectangle.calculate_perimeter()
        break
    else:
        print("¡Valor no válido!\n")