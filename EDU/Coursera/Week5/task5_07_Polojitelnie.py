# Найдите количество положительных элементов в данном списке.
a = list(map(int, input().split()))
k = 0
for i in range(0, len(a)):
    if a[i] > 0:
        k += 1
print(k)
