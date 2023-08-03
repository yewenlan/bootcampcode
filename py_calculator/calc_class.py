from py_calculator.calc_func import *


class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def _do_math(self, a, b, func):
        self._last_answer = func(a, b)
        return self.last_answer

    def add(self, a, b):
        return self._do_math(a, b, add)

    def subtract(self, a, b):
        return self._do_math(a, b, sub)

    def multiply(self, a, b):
        return self._do_math(a, b, mul)

    def divide(self, a, b):
        return self._do_math(a, b, div)

    def maximum(self, a, b):
        return self._do_math(a, b, maximum)

    def minimum(self, a, b):
        return self._do_math(a, b, minimum)

#    Please implement the rest of functions
#    - subtract
#    - multiply
#    - divide
#    - maximum
#    - minimum
