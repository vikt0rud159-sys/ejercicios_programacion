import random
import pytest
from ordenamiento import bubble_sort

def test_bubble_sort_short_list_well():
    list_input = [3,1]
    assert bubble_sort(list_input) == [1, 3]


def test_bubble_sort_large_list_well():
    list_input = [random.randint(1, 1000) for _ in range(101)]
    assert bubble_sort(list_input) == sorted(list_input)


def test_bubble_sort_void_list_well():
    list_input = []
    assert bubble_sort(list_input) == []


def test_bubble_sort_without_list_fail():
    list_input = {"W": 2, "A": 1}
    with pytest.raises(KeyError):
        bubble_sort(list_input)