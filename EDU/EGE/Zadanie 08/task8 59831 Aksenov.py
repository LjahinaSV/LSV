# Николай Аксёнов
from itertools import *
count = 0
t = ['51','53', '57', '15', '35', '75']
for i in product('012345678', repeat=5):
    p = ''.join(i)
    if p[0] != '0' and p.count('5') == 1 and all (not i in p for i in t):
        count += 1
print(count)
