from funciones4 import reversed_srting


def test_reversed_srting_short_well():
    str_input = "Hola"
    result = reversed_srting(str_input)
    assert result == "aloH"


def test_reversed_srting_large_well():
    str_input = "Estoy aquí para ayudarte en lo que necesites"
    result = reversed_srting(str_input)
    assert result == "setisecen euq ol ne etraduya arap íuqa yotsE"


def test_reversed_srting_void_well():
    str_input = ""
    result = reversed_srting(str_input)
    assert result == ""