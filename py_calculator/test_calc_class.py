from calc_class import *

import pytest

# "Constants"

NUMBER_1 = 3.0
NUMBER_2 = 2.0


# Fixtures


@pytest.fixture
def calculator():
    return Calculator()


# Helpers


def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# Test Cases


def test_last_answer_init(calculator):
    assert calculator.last_answer == 0.0


def test_add(calculator):
    answer = calculator.add(NUMBER_1, NUMBER_2)
    verify_answer(5.0, answer, calculator.last_answer)


#    Please implement tests for the rest of functions
#    - subtract
#    - multiply
#    - divide
#    - maximum
#    - minimum
