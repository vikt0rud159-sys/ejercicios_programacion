def validation(func):
    def wrapper(list):
        if len(list) == 0:
            print(f"{list} Error: Lista vacío\n")
            return
        for num in list:
            if not isinstance(num, int):
                print(f"{list} Error: La lista contiene elementos no numéricos\n")
                return
        func(list)
    return wrapper

@validation
def bubble_sort(list):
    bubble_sort_steps = 0
    exchanges = 0
    for leng in range(len(list)):
        bubble_sort_steps +=1
        for index in range(len(list)-1):
            if list[index] > (list[index+1]):
                exchanges +=1
                current = list[index]
                next = list[index+1]
                list[index+1] = current
                list[index] = next
    return print(f"{list} \nIteraciones: {bubble_sort_steps} \nIntercambios: {exchanges}\n")


list_num = [39, 40, 15, 4, 6, 23, 3, 9, 7, 1]
bubble_sort(list_num)

list_num2 = [39, 40, "W"]
bubble_sort(list_num2)

list_num3 = []
bubble_sort(list_num3)