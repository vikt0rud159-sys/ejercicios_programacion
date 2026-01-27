import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        print(math.pi * (self.radius ** 2))


my_circle = Circle(90)
my_circle.get_area()