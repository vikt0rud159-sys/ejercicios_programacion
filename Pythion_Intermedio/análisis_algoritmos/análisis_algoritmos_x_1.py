# Versión 1:
def manual_add(n):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n)
        result += i # O(1)
    return result # O(1)


# Versión 2:
def add_formula(n):
    return number * (number + 1) // 2 # O(1)


manual_add() # O(n)
add_formula() # O(1)

# Usaría la versíon 2 
# - Es más fácil de leer 
# - Tiene cladificación O(1)
# - Es más rápida