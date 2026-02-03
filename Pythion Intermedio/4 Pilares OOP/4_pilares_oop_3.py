class Vertebrate:
    def get_vertebrate(self, vertebrate):
        self.vertebrate = vertebrate
        print(f"[Vertebrado = {self.vertebrate}]")

class Feeding:
    def get_feeding(self, feeding):
        self.feeding = feeding
        print(f"[Alimentación = {self.feeding}]")

class Reproduce:
    def get_reproduction(self, reproduce):
        self.reproduce = reproduce
        print(f"[Reproducción = {self.reproduce}]\n")

class Animal(Vertebrate, Feeding, Reproduce):
    def __init__(self, name, vertebrate, feeding, reproduce):
        print(name)
        self.get_vertebrate(vertebrate)
        self.get_feeding(feeding)
        self.get_reproduction(reproduce)

cow = Animal("Vaca", True, "Herbívoro", "Sexual")
starfish = Animal("Estrella de mar", False, "Carnívora", "Asexual")