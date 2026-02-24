my_list = [4, 3, 6, 1, 7]
first = my_list.pop(4)
last = my_list.pop(0)
my_list.insert(0, first)
my_list.append(last)
print(my_list)

