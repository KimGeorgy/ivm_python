class Matrix:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data

    def __add__(self, B):
        c_data = tuple(self.data[i] + B.data[i] for i in range(self.rows * self.columns))
        return Matrix(self.size, c_data)

    def __sub__(self, B):
        c_data = tuple(self.data[i] - B.data[i] for i in range(self.rows * self.columns))
        return Matrix(self.size, c_data)

    def __mult__(self, b):
        c_data = tuple(
            sum(tuple( self.data[i*self.columns+j] * b.data[j] for j in range(self.columns) ))
            for i in range(self.rows))
        return Matrix(self.size, c_data)