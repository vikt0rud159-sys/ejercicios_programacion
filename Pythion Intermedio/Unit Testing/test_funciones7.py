from funciones7 import get_prime_numbers


def test_get_prime_numbers_all_prime_numbers_well():
    input_list = [2, 3, 5, 7]
    assert get_prime_numbers(input_list) == [2, 3 ,5, 7]


def test_get_prime_numbers_without_prime_numbers_well():
    input_list = [1, 4, 8, 10]
    assert get_prime_numbers(input_list) == []


def test_get_prime_numbers_mixed_well():
    input_list = [1, 4, 6, 7, 13, 9, 67]
    assert get_prime_numbers(input_list) == [7, 13, 67]