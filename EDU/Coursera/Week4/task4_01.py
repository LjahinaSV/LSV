# Минимум 4-х целых чисел
a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min4(a, b, c, d):
    e = min(a, b)
    e = min(e, c)
    e = min(e, d)
    return e


print(min4(a, b, c, d))
