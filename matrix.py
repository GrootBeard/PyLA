import numbers


class Matrix:

    def __init__(self, m, n, values=None):
        self.m = m
        self.n = n

        self._matrix = [[0 for i in range(n)] for i in range(m)]

        if values:
            self._matrix = values

    @staticmethod
    def identity(m, n):
        matrix = Matrix(m, n)
        for i in range(min(m, n)):
            matrix[(i, i)] = 1

        return matrix

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError('Matrices don\'t have the same dimensions')

        result = [[0 for i in range(self.n)] for i in range(self.m)]
        for j in range(self.n):
            for i in range(self.m):
                result[i][j] = self[(i, j)] * s

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            print('number')
            return self.scale(other)
        elif isinstance(other, Matrix):
            print('matrix')

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.scale(other)
            print('number')

    def scale(self, s):
        result = [[0 for i in range(self.n)] for i in range(self.m)]
        for j in range(self.n):
            for i in range(self.m):
                result[i][j] = self[(i, j)] * s
        return Matrix(self.m, self.n, result)

    def __getitem__(self, x):
        return self._matrix[x[0]][x[1]]

    def __setitem__(self, x, value):
        self._matrix[x[0]][x[1]] = value

    def __str__(self):
        value = ""
        for x in range(self.m):
            for y in range(self.n):
                value += '{} '.format(self[(x, y)])
            value += '\n'
        return value


mat = Matrix.identity(3, 3)
mat2 = Matrix(2, 3, [[11, 12, 13], [21, 22, 23], ])
print(mat2)
mat2 = mat2 * 5
print(mat2)
print(mat2._matrix)
print(mat + mat)

mat * mat2
