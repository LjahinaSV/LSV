#
a = float(input())
n = int(input())


def power2(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power2(a * a, n // 2)
    else:
        return a * power2(a, n - 1)


print(power2(a, n))
