from sys import stdin


class Matrix(list):
    def __init__(self, m_list):
        self.m_list = [line.copy() for line in m_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.m_list])

    def size(self):
        return len(self.m_list), len(self.m_list[0])

    def __add__(self, list1):
        ri, rj = range(len(self.m_list)), range(len(self.m_list[0]))
        return Matrix([[self.m_list[i][j] + list1.m_list[i][j] for j in rj]
                       for i in ri])

    # def __mul__(self, alfa):
    #    ri, rj = range(len(self.m_list)), range(len(self.m_list[0]))
    #    return Matrix([[self.m_list[i][j] * alfa for j in rj] for i in ri])

    # другой способ перебора элементов
    def __mul__(self, alfa):
        return Matrix([a * alfa for a in line] for line in self.m_list)

    __rmul__ = __mul__


# Task 2 check 1
print('check 1')
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())
# Task 2 check 2
print('check 2')
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
# Task 2 check 3
print('check 3')
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)