from funciones4 import reversed_srting


def test_reversed_srting_short_well():
    str_input = "Hola"
    assert reversed_srting(str_input) == "aloH"


def test_reversed_srting_large_well():
    str_input = "Estoy aquí para ayudarte en lo que necesites"
    assert reversed_srting(str_input) == "setisecen euq ol ne etraduya arap íuqa yotsE"


def test_reversed_srting_void_well():
    str_input = ""
    assert reversed_srting(str_input) == ""