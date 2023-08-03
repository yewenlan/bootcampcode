from py_calculator.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0


#    Please implement tests for the rest of functions
#    - subtract
#    - multiply
#    - divide
#    - maximum
#    - minimum


def test_sub():
    value = sub(NUMBER_1, NUMBER_2)
    assert value == 1.0


def test_mul():
    value = mul(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_div():
    value = div(NUMBER_1, NUMBER_2)
    assert value == 1.5


def test_max():
    value = maximum(NUMBER_1, NUMBER_2)
    assert value == 3.0


def test_min():
    value = minimum(NUMBER_1, NUMBER_2)
    assert value == 2.0
