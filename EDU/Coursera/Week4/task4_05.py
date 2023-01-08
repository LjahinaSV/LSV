# Проверка числа на простоту


def MinDivisor(n):  # Минимальный делитель
    if n % 2 == 0:
        return 2
    i = 3
    while n % i != 0 and i * i <= n:
        i += 2
    if i * i <= n:
        return i
    return n


N = int(input())
if N == MinDivisor(N):
    print('YES')
else:
    print('NO')
