import json


def open_json():
    try:
        with open("pokemon_lvl.json", "r") as file:
            pokemon = json.load(file)
    except Exception:
        print("\nError de lectura (archivo.json)\n")
        exit()
    return pokemon


def group_type(pokemon):
    poke_dict = {}
    count_dict = {}
    try:
        for index in range(0, len(pokemon)):
            poke = pokemon[index]
            for value in poke["type"]:
                if value not in poke_dict:
                    poke_dict[value] = poke["base"]["LVL"]
                    count = 1
                    count_dict[value+"count"] = count
                else:
                    poke_dict[value] = poke_dict[value] + poke["base"]["LVL"]
                    count_dict[value+"count"] = count +1
    except KeyError as ex:
        print(f"Valor no encontrado: {ex}")
        exit()
    return poke_dict, count_dict


def get_average_lvl_by_type():
    try:
        pokemon = open_json()
        poke_dict, count_dict = group_type(pokemon)
        for key, value in poke_dict.items():
            print (f"Tipo: {key} → Promedio de nivel: {value/count_dict[key + "count"]}")
    except Exception as ex:
        print(f"Error: {ex}")


get_average_lvl_by_type()