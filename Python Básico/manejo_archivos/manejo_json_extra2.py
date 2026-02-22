import json


def open_json():
    try:
        with open("pokemon_lvl.json", "r") as file:
            pokemon = json.load(file)
    except Exception:
        print("\nError de lectura (archivo.json)\n")
        exit()
    return pokemon


def search_type(pokemon, search):
    poke_list = []
    try:
        for index in range(0, len(pokemon)):
            poke = pokemon[index]
            name = poke["name"]
            type = poke["type"]
            type = str(type).replace("[", "").replace("]", "").lower()
            if type == f"'{search}'":
                poke_list.append(name["english"])
    except KeyError as ex:
        print(f"Valor no encontrado: {ex}")
        exit()
    return poke_list


def convert_spanish_to_english(search):
    if search == "electrico":
        search = "electric"
    elif search == "fuego":
        search = "fire"
    elif search == "agua":
        search = "water"
    return search


def get_all_pokemon_of_type():
    try:
        pokemon = open_json()
        search = input("Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego):").lower()
        search = convert_spanish_to_english(search)
        poke_list = search_type(pokemon, search)
        print("\nLos pokemos que existen de ese tipo son:")
        for value in poke_list:
            print (value)
    except Exception as ex:
        print(f"Error: {ex}")
        exit()
    print("\n")


get_all_pokemon_of_type()