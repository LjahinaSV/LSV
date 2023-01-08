# Константин Гижук Учащийся 4 месяца назад
from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, List):
        self.newList = deepcopy(List)

    def __str__(self):
        return '\n'.join(map(
            lambda x: '\t'.join(map(str, x)),
            self.newList))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[i * other for i in list] for list
                           in self.newList])
        elif isinstance(other, Matrix) \
                and len(self.newList[0]) == len(other.newList):
            a1 = self.newList
            a2 = Matrix.transposed(other).newList
            List = []
            for i in range(len(a1)):
                list = []
                for j in range(len(a2)):
                    list += sum(map(lambda x, y: x * y, a1[i], a2[j])),
                List += list,
            return Matrix(List)
        elif isinstance(other, Matrix) and \
                len(self.newList[0]) != len(other.newList):
            raise MatrixError(self, other)

    def size(self):
        return ((len(self.newList), len(self.newList[0])))

    def __add__(self, other):
        if len(self.newList) == len(other.newList) and \
                len(self.newList[0]) == len(other.newList[0]):
            return Matrix(list(map(lambda x, y: list(
                map(lambda z, q: z + q, x, y)),
                                   self.newList, other.newList)))
        else:
            raise MatrixError(self, other)

    def transpose(self):
        List = []
        for i in range(len(self.newList[0])):
            list = []
            for j in range(len(self.newList)):
                list += self.newList[j][i],
            List += list,
        self.newList = List
        return Matrix(self.newList)

    @staticmethod
    def transposed(self):
        List = []
        for i in range(len(self.newList[0])):
            list = []
            for j in range(len(self.newList)):
                list += self.newList[j][i],
            List += list,
        return Matrix(List)

    __rmul__ = __mul__


exec(stdin.read())
