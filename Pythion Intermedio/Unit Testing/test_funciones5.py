from funciones5 import count_uppercase_and_lowercase


def test_short_count_uppercase_and_lowercase_well():
    str_input = "Hola"
    result = count_uppercase_and_lowercase(str_input)
    assert result == (1, 3)


def test_large_count_uppercase_and_lowercase_well():
    str_input = "Hola, Estoy aquí para ayudarte en lo que necesites"
    result = count_uppercase_and_lowercase(str_input)
    assert result == (2, 39)


def test_count_uppercase_and_lowercase_void_well():
    str_input = ""
    result = count_uppercase_and_lowercase(str_input)
    assert result == (0, 0)