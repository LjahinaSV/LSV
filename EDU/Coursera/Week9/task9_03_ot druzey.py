# Kulagin Anton Igorevich
import copy
from sys import stdin
import itertools


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, arr):
        self.arr = copy.deepcopy(arr)

    def __str__(self):
        return '\n'.join(['\t'.join([str(x) for x in y]) for y in self.arr])

    def size(self):
        return len(self.arr), len(self.arr[0])

    def __add__(self, other):
        if len(self.arr) == len(other.arr):
            res = itertools.starmap(lambda x, y: [(x[i] + y[i]) for i in range(len(self.arr[0]))], zip(self.arr, other.arr))
            return Matrix(res)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        multiply = [[x * other for x in y] for y in self.arr]
        self.multiply = multiply
        return Matrix(multiply)

    __rmul__ = __mul__

    def transpose(self):
        self.arr = [[self.arr[x][y] for x in range(len(self.arr))] for y in range(len(self.arr[0]))]
        return Matrix(self.arr)

    @staticmethod
    def transposed(other):
        return Matrix([[other.arr[x][y] for x in range(len(other.arr))] for y in range(len(other.arr[0]))])


exec(stdin.read())

# https://automatetheboringstuff.com/ 