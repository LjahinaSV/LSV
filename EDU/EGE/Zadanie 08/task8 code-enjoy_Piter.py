from itertools import *
alph='ABCD'
k=0
for sp in product(alph,repeat=5):
    s=''.join(sp)
    if s.count('A')==1:
        k+=1
print(k)
