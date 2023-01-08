# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.
a = list(map(int, input().split()))
myMin = a[0]
myMax = a[0]
iMin = 0
iMax = 0
for i in range(1, len(a)):
    if a[i] < myMin:
        myMin = a[i]
        iMin = i
    if a[i] > myMax:
        myMax = a[i]
        iMax = i
a[iMin] = myMax
a[iMax] = myMin
print(*a)
