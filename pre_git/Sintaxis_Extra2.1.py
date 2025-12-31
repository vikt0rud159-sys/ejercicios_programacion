import random
random_number = random.randint(1, 10)
number = 0
while int(number) != random_number:
    number = input("Adivina el número entre 1 y 10: ")
print("¡Felicidades! Has adivinado el número:", random_number)