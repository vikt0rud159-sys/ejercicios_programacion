def bubble_sort(list):
    for leng in range(len(list)): # O(n)
        for index in range(len(list)-1): # O(n^2)
            if list[index] > (list[index+1]): # O(1)
                current = list[index] # O(1)
                next = list[index+1] # O(1)
                list[index+1] = current # O(1)
                list[index] = next # O(1)


list_1=[4,3,2,1] # O(1)
bubble_sort(list_1) # O(n^2)
print(list_1) # O(1)

# max = O(n^2)