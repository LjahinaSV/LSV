# Проценты
from math import trunc
p = int(input())
x = int(input())
y = int(input())
a = trunc((x * 100 + y) + (x * 100 + y) * p / 100)
print('{:.0f}'.format(a // 100), end=' ')
print('{:.0f}'.format(a % 100))
