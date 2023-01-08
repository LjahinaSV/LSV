# Принадлежит ли точка кругу с центром не в начале координат


Dict = {True: 'YES', False: 'NO'}
x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


print(Dict.get(IsPointInCircle(x, y, xc, yc, r)))
