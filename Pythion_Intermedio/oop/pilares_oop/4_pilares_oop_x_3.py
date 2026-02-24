class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return self._brand, self._year


class Car(Vehicle):
    def __init__(self, brand, year, door):
        super().__init__(brand, year)
        self.door = door

    def get_info(self):
        return f"Brand: {self._brand}", f"Year: {self._year}", f"Doors: {self.door}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        return f"Brand: {self._brand}", f"Year: {self._year}", f"Type: {self.type}"


vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())
print(vehicle2.get_info())
print()