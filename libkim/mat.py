from .vec import *
class Matrix(object):
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data

    def __add__(self, B):
        c_data = tuple(self.data[i] + B.data[i] for i in range(self.rows * self.columns))
        return Matrix(self.rows, self.columns, c_data)

    def __sub__(self, B):
        c_data = tuple(self.data[i] - B.data[i] for i in range(self.rows * self.columns))
        return Matrix(self.rows, columns, c_data)

    def __mul__(self, b):
        if isinstance(b, Vector):
            c_data = tuple(
                sum(tuple( self.data[i*self.columns+j] * b.data[j] for j in range(self.columns) ))
                for i in range(self.rows))
            return Vector(self.rows, c_data)
        else:
            raise NotImplemented