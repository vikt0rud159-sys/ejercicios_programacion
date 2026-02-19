def linear_search(my_list, target):
    for item in my_list: # O(n)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)


def binary_search(my_list, target):
    low = 0 # O(1)
    high = len(lst) - 1 # O(1)
    while low <= high: # O(log n)
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else: # O(1)
            high = mid - 1 # O(1)
    return False # O(1)

list=[]
linear_search(list) # O(n)
binary_search(list) # O(log n)

# linear_search(): Conviene utilizar cuando: Listas pequeñas, desordenadas y/o simpleza
# binary_search(): Conviene utilizar cuando: Listas grandes, ordenadas y/o velocidad

# ¿Qué pasa si la lista no está ordenada? linear_search(): Funciona correctamente
# ¿Qué pasa si la lista no está ordenada? binary_search(): Puede generar errores