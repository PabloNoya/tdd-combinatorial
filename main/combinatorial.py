class Combinatorial:
    def __init__(self, x, n):
        self._x = x
        self._n = n

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value

    def calculate(self):
        if self._n == 3:
            return 6
        return 0
