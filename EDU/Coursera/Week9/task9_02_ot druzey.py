from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, m=[]):
        self.m = deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.m])

    def __add__(self, other):
        ri, rj = range(len(self.m)), range(len(self.m[0]))
        return Matrix([[self.m[i][j] + other.m[i][j] for j in rj] for i in ri])

    def __mul__(self, skal):
        ri, rj = range(len(self.m)), range(len(self.m[0]))
        return Matrix([[self.m[i][j] * skal for j in rj] for i in ri])

    # другой способ перебора элементов
    # def __mul__(self, skal):
    #    return Matrix([a * skal for a in line] for line in self.matrix)

    __rmul__ = __mul__

    def size(self):
        return (len(self.m), len(self.m[0]))

exec(stdin.read())
