class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        self.area = self.width * self.height
        print(f"Area:  {self.area}")
    
    def get_perimeter(self):
        self.perimeter = (self.width + self.height) * 2
        print(f"Perimetro:  {self.perimeter}")


def get_rectangle_info():
    while True:
        try:
                height = float(input("Ingrese la altura: "))
                width = float(input("Ingrese el ancho: "))
                if width <= 0 or height <= 0:
                    print("[Existe un valor negativo, los valores deben ser positivos]\n")
                else:
                    return width, height
        except ValueError:
            print("[Debe de ser un valor numerico]\n")


rectangle_info = get_rectangle_info()
my_rectangle = Rectangle(rectangle_info[0], rectangle_info[1])
my_rectangle.get_area()
my_rectangle.get_perimeter()