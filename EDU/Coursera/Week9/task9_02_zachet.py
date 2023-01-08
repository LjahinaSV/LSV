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

    def __mul__(self, alfa):
        ri, rj = range(len(self.m_list)), range(len(self.m_list[0]))
        return Matrix([[self.m_list[i][j] * alfa for j in rj] for i in ri])

    __rmul__ = __mul__


exec(stdin.read())
