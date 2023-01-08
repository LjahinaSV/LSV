# Принадлежит ли точка квадрату


Dict = {True: 'YES', False: 'NO'}
x, y = float(input()), float(input())


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


print(Dict.get(IsPointInSquare(x, y)))
