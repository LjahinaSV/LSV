# Найти наименьший положительный элемент в списке
a = list(map(int, input().split()))
myMin = 1001
for i in range(0, len(a)):
    if a[i] > 0 and a[i] < myMin:
        myMin = a[i]
print(myMin)
