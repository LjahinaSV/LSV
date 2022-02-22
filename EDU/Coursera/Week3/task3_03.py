# Дано положительное действительное число X. Выведите его дробную часть.
from math import trunc
a = float(input())
# print(a - int(a))
print(a - trunc(a))
