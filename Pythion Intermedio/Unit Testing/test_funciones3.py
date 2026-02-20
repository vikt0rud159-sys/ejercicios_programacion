import random
from funciones3 import sum_num_list


def test_sum_num_list_short_well():
    list_input = [4, 6]
    result = sum_num_list(list_input)
    assert result == 10


def test_sum_num_list_large_well():
    list_input = [random.randint(1, 1000) for _ in range(101)]
    result = sum_num_list(list_input)
    assert result == sum(list_input)


def test_sum_num_list_void_well():
    list_input = []
    result = sum_num_list(list_input)
    assert result == 0