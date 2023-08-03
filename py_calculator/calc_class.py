from calc_func import *


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


#    Please implement the rest of functions
#    - subtract
#    - multiply
#    - divide
#    - maximum
#    - minimum
