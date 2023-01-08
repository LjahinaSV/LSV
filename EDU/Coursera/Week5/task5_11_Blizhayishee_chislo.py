# Найти в массиве элемент, самый близкий по величине к данному числу.
n = int(input())  # n<=1000
a = list(map(int, input().split()))
x = int(input())  # |x|<=1000
myMin = abs(a[0] - x)
iMin = a[0]
for now in a:
    if abs(now - x) < myMin:
        myMin = abs(now - x)
        iMin = now
print(iMin)
