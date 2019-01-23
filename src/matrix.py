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

        result = [[self[(i, j)] + other[(i, j)] for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, result)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.scale(other)
        elif isinstance(other, Matrix):
            return self.product(other)
            print('matrix')

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.scale(other)

    def scale(self, s):
        result = [[self[(i, j)] * s for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, result)

    def product(self, other):
        # (AB)_{ij} = \sum_{k}{(A_{ik} B_{kj})}
        result = [[self.inner(i, j, other) for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, other.n, result)

    def inner(self, row, col, other):
        sum = 0
        for k in range(self.n):
            sum += self[(row, k)] * other[(k, col)]
        return sum

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
mat2 = Matrix(3, 3, [[11, 12, 13], [21, 22, 23], [31, 32, 33]])
mat3 = Matrix(3, 3, [[0, 8, -3], [5, -9, 0], [1, 0, 12]])

rot_z = Matrix(3, 3, [[0, 1, 0], [-1,0,0], [0,0,1]])
vec = Matrix(1, 3   , [[0,1,1]])

print(rot_z)
print(vec)

print(vec *rot_z )