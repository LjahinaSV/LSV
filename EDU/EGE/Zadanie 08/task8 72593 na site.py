# 72593 inf-ege.sdamgia.ru
import time
start_time = time.time()  # время начала выполнения
from itertools import product
 
count = 0
 
for i in product ('01a', repeat = 8 ):
    s = ''.join(i)
    if s[0] != '0' and s.count('0') == 2 and s.count('a') <5:
        count += 9**s.count('1') * 6**s.count('a')
print(count)
end_time = time.time()  # время окончания выполнения
print(f"Время выполнения программы: {end_time - start_time} секунд")
# Ответ 229405365 сосчитал мгновенно
