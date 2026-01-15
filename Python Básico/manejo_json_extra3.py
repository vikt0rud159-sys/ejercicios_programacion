import json

def open_json():
    try:
        with open("pokemon_lvl.json", "r") as file:
                pokemon = json.load(file)
                return pokemon
    except Exception:
        print("\nError de lectura (archivo.json)\n")
        exit()


def print_info(pokemon):
    try:
        for index in range(0, len(pokemon)):
            poke = pokemon[index]
            name = poke["name"]
            print(f"Name: {name["english"]}")
            for key, value in poke["base"].items():
                if key != "LVL":
                    print(f"{key} {value}")
            print("\n")
    except KeyError as ex:
        print(f"Valor no encontrado: {ex}")
        exit()

def get_pokemon_info():
    try:
        pokemon = open_json()
        print_info(pokemon)
    except Exception as ex:
        print(f"Error: {ex}")
        exit()

get_pokemon_info()