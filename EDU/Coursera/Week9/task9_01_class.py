from sys import stdin


class Matrix(list):
    def __init__(self, m_list):
        self.m_list = [line.copy() for line in m_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.m_list])

    def size(self):
        return len(self.m_list), len(self.m_list[0])


exec(stdin.read())
