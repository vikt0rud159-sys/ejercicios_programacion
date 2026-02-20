def bubble_sort(list):
    for leng in range(len(list)):
        for index in range(len(list)-1):
            if list[index] > (list[index+1]):
                current = list[index]
                next = list[index+1]
                list[index+1] = current
                list[index] = next
    return list


list_1=[4,3,2,1]
bubble_sort(list_1)
print(list_1)


def bubble_sort_reverse(list):
    for leng in range(len(list)):
        for index in range(len(list)-1, 0, -1):
            if list[index] > (list[index-1]):
                current = list[index]
                next = list[index-1]
                list[index-1] = current
                list[index] = next


list_2=[1,2,3,4]
bubble_sort_reverse(list_2)
print(list_2)