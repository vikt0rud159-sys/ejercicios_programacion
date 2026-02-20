from funciones7 import get_prime_numbers


def test_get_prime_numbers_all_prime_numbers_well():
    input_list = [2, 3, 5, 7]
    result = get_prime_numbers(input_list)
    assert result == [2, 3 ,5, 7]


def test_get_prime_numbers_without_prime_numbers_well():
    input_list = [1, 4, 8, 10]
    result = get_prime_numbers(input_list)
    assert result == []


def test_get_prime_numbers_mixed_well():
    input_list = [1, 4, 6, 7, 13, 9, 67]
    result = get_prime_numbers(input_list)
    assert result == [7, 13, 67]