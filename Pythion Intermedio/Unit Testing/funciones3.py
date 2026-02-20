num_list = [4, 6, 2, 29]


def sum_num_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total


print(sum_num_list(num_list))