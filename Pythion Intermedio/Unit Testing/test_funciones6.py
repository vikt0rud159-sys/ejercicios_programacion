from funciones6 import string_to_alphabetical_list, list_to_string, sort_string_alphabetically


def test_sort_string_alphabetically_well():
    str_input = "python-variable-funcion-computadora-monitor"
    assert sort_string_alphabetically(str_input) == "computadora-funcion-monitor-python-variable"


def test_string_to_alphabetical_list_well():
    str_input = "python-variable-funcion-computadora-monitor"
    my_list = []
    assert string_to_alphabetical_list(str_input, my_list) == ['computadora', 'funcion', 'monitor', 'python', 'variable']


def test_list_to_string_well():
    list_input = ['computadora', 'funcion', 'monitor', 'python', 'variable']
    assert list_to_string(list_input) == 'computadora-funcion-monitor-python-variable'