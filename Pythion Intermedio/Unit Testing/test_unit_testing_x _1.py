from unit_testing_x_1 import subtract, sum_all, average


def test_substract_with_positive_numbers():
    assert subtract(1, 2) == -1


def test_substract_with_negative_numbers():
    assert subtract(-1, -2) == 1

def test_substract_with_0():
    assert subtract(0, 0) == 0


def test_sum_all_with_positive_numbers():
    assert sum_all(1, 2, 3) == 6

def test_sum_all_with_negative_numbers():
    assert sum_all(-1, -2, -3) == -6


def test_sum_all_with_0():
    assert sum_all(0, 0) == 0


def test_average_with_positive_numbers():
    assert average(1, 2, 3) == 2


def test_average_with_negative_numbers():
    assert average(-1, -2, -3) == -2


def test_average_with_0():
    assert average(0, 0) == 0