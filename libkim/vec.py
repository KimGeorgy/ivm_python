from math import sqrt
class Vector(object):
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def __add__(self, b):
        c_data = tuple(self.data[i] + b.data[i] for i in range(self.size))
        return Vector(self.size, c_data)

    def __sub__(self, b):
        c_data = tuple(self.data[i] - b.data[i] for i in range(self.size))
        return Vector(self.size, c_data)

    def __mul__(self, alpha):
        if isinstance(alpha, (int, float)):
            c_data = tuple(a * alpha for a in self.data)
            return Vector(self.size, c_data)

    def __abs__(self):
        abs_sq = 0
        for a in self.data:
            abs_sq += a * a
        return sqrt(abs_sq)