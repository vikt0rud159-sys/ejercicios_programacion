import json


def get_info():
    name = input("Ingrese nombre del pokemon: ")
    poke_type = input("Ingrese tipo del pokemon: ")
    try:
        hp = int(input("HP (numérico): "))
        attack = int(input("Ataque (numérico): "))
        defense = int(input("Defensa (Valor numérico): "))
        sp_attack = int(input("Ataque especial (Valor numérico): "))
        sp_defense = int(input("Defensa especial (Valor numérico): "))
        speed = int(input("Velocidad (Valor numérico): "))
    except ValueError:
        print("Error de valor (Dato no numérico)")
        exit()
    new_pokemon = {
        "name": {
            "english": name
        },
        "type": [
            poke_type
        ],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon


def open_json():
    try:
        with open("pokemon.json", "r") as file:
            pokemon = json.load(file)
    except Exception:
        print("\nError de lectura (archivo.json)\n")
        exit()
    return pokemon


def save_json(pokemon):
    with open("pokemon.json", "w") as file:
        json.dump(pokemon, file, indent=4)


def add_pokemon_json():
    try:
        new_pokemon = get_info()
        pokemon = open_json()
        pokemon.append(new_pokemon)
        save_json(pokemon)
        print("¡Nuevo Pokémon agregado exitosamente!")
    except Exception as ex:
        print(f"Error: {ex}")
        exit()


add_pokemon_json()