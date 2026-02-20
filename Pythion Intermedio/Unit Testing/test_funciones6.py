from funciones6 import string_to_alphabetical_list, list_to_string, sort_string_alphabetically


def test_sort_string_alphabetically_well():
    str_input = "python-variable-funcion-computadora-monitor"
    result = sort_string_alphabetically(str_input)
    assert result == "computadora-funcion-monitor-python-variable"


def test_string_to_alphabetical_list_well():
    str_input = "python-variable-funcion-computadora-monitor"
    my_list = []
    result = string_to_alphabetical_list(str_input, my_list)
    assert result == ['computadora', 'funcion', 'monitor', 'python', 'variable']


def test_list_to_string_well():
    list_input = ['computadora', 'funcion', 'monitor', 'python', 'variable']
    result = list_to_string(list_input)
    assert result == 'computadora-funcion-monitor-python-variable'