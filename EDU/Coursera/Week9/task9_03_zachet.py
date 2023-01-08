import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, m_list):
        self.m_list = copy.deepcopy(m_list)

    def __str__(self):
        return '\n'.join(['\t'.join([str(x) for x in y]) for y in self.m_list])

    def size(self):
        return len(self.m_list), len(self.m_list[0])

    def __add__(self, other):
        if len(self.m_list) == len(other.m_list):
            ri, rj = range(len(self.m_list)), range(len(self.m_list[0]))
            return Matrix([[self.m_list[i][j] + other.m_list[i][j] for j in rj]
                           for i in ri])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        multiply = [[x * other for x in y] for y in self.m_list]
        self.multiply = multiply
        return Matrix(multiply)

    __rmul__ = __mul__

    def transpose(self):
        self.m_list = [[self.m_list[x][y] for x in range(len(self.m_list))]
                       for y in range(len(self.m_list[0]))]
        return Matrix(self.m_list)

    @staticmethod
    def transposed(other):
        return Matrix([[other.m_list[x][y] for x in range(len(other.m_list))]
                       for y in range(len(other.m_list[0]))])


exec(stdin.read())
