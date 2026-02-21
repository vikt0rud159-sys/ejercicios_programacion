import random
from funciones3 import sum_num_list


def test_sum_num_list_short_well():
    list_input = [4, 6]
    assert sum_num_list(list_input) == 10


def test_sum_num_list_large_well():
    list_input = [random.randint(1, 1000) for _ in range(101)]
    assert sum_num_list(list_input) == sum(list_input)


def test_sum_num_list_void_well():
    list_input = []
    assert sum_num_list(list_input) == 0