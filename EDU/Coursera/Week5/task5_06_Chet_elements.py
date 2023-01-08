# Выведите все четные элементы списка.
a = list(map(int, input().split()))
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i], end=' ')
