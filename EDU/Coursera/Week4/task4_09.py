# Сократите дробь
n, m = int(input()), int(input())


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


def ReduceFraction(x, y):
    k = gcd(x, y)
    x = x // k
    y = y // k
    return x, y


print(*ReduceFraction(n, m))
