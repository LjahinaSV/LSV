# Решение Евгения Джобса для задачи 55797
from itertools import permutations

s = 'АБД БАВД ВБГ ГВЕЖ ДАБЕ ЕГДЖ ЖЕГ'
s_g = {c[0]:set(c[1:]) for c in s.split()}
s1 = '1346 257 314 4137 5267 615 7245'
print('1 2 3 4 5 6 7')
for x in permutations(set(s) - {' '}):
    s2 = s1
    for a1, a2 in zip('1234567', x):
        s2 = s2.replace(a1, a2)
    s2_g = {c[0]: set(c[1:]) for c in s2.split()}
    if s2_g == s_g:
        print(*x, sep=' ')
