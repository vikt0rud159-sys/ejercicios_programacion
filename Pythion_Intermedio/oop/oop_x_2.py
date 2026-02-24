class Animal:
    class Dog:
        def speak(self, name):
            self.type = "Perro"
            self.name = name
            self.speak = "Guau"
            print(f"\n[Tipo: {self.type}]   [Nombre : {self.name}]   [Sonido : {self.speak}]")

    class Cat:
        def speak(self, name):
            self.type = "Gato"
            self.name = name
            self.speak = "Miau"
            print(f"[Tipo: {self.type}]   [Nombre : {self.name}]   [Sonido : {self.speak}]\n")


dog = Animal.Dog()
dog.speak("Firulais")
cat = Animal.Cat()
cat.speak("Michi")
