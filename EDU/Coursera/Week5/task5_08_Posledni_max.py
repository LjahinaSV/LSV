# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка.
a = list(map(int, input().split()))
k = 0
mmax = a[0]
for i in range(0, len(a)):
    if a[i] >= mmax:
        mmax = a[i]
        k = i
print(mmax, k, end=' ')
