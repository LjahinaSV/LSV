# Выведите все элементы списка, которые больше предыдущего элемента
a = list(map(int, input().split()))
pred = a[0]
for i in range(0, len(a)):
    if a[i] > pred:
        print(a[i], end=' ')
    pred = a[i]
