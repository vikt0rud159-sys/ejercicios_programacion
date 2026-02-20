import pytest
from unit_testing_x_2 import divide


def test_divide_well():
    assert divide(10, 2) == 5


def test_divide_0_fail():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_str_fail():
    with pytest.raises(TypeError):
        divide("a", 1)