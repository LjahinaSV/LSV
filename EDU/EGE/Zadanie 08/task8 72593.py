# 72593
''' Определите количество восьмизначных 16-⁠ричных чисел,
в записи которых ровно два нуля и не более четырёх цифр,
для записи которых используются буквы. '''
from itertools import product
import time
start_time = time.time()  # время начала выполнения
a='0123456789ABCDEF'
c=0
for s in product(a,repeat=8):
    if s[0] != '0' and s.count('0')==2:
        if s.count('A') + s.count('B') + s.count('C') \
           + s.count('D') + s.count('E') + s.count('F') <= 4:
            c+=1
print(c)
end_time = time.time()  # время окончания выполнения
print(f"Время выполнения программы: {end_time - start_time} секунд")
# 229405365 Очень долго считает.
