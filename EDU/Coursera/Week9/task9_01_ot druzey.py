# from copy import deepcopy
from sys import stdin


class Matrix(list):
    def __init__(self, m_list):
        self.m_list = [line.copy() for line in m_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.m_list])

    def size(self):
        return len(self.m_list), len(self.m_list[0])


# exec(stdin.read())
# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)

# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))
print(str(m1))

# Task 1 check 3
print('check 3')
m = Matrix([[1, 1, 1], [0, 100, 10], [2, 3, 4]])
print(str(m) == '1\t1\t1\n0\t100\t10\n2\t3\t4')
print(str(m))
print(Matrix.size(m))
# check4
print('check 4')
m = list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(Matrix(m))
print(str(m))
print(str(Matrix(m)))
print(Matrix.size(Matrix(m)))
