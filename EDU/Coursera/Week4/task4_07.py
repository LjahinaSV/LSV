# сложение без сложения a,b <= 900
a, b = int(input()), int(input())


def summa(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a < b:
        return summa(a - 1, b + 1)
    else:
        return summa(a + 1, b - 1)


if a <= 900 and b <= 900:
    print(summa(a, b))
