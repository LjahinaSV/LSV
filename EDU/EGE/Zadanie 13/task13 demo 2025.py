#  Задание 13 Демо 2025
from itertools import product
 
count = 0
 
for i in product ('01', repeat = 11 ):
    s = ''.join(i)
    s='101011000001000010101'+s
    if s.count('1')%5 !=0:
        count += 1
print(count)
# 1663
