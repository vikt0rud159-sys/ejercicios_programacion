def print_all_pairs(my_dict):
    for key1 in my_dict: #O(n)
        for key2 in my_dict: # O(n^2)
            print(f"{key1}-{key2}") # O(1)


print_all_pairs()  # O(n^2)
# ¿Cuanto dura si hay 1 millón de claves? = O(n^2) = 1,000,000^2 = 1,000,000,000,000(operaciones)
# Tardará mucho tiempo en ejecutarse, ya que la complejidad es cuadrática
# El tiempo variará según el equipo