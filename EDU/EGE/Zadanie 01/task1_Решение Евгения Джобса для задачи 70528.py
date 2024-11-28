# Решение Евгения Джобса для задачи 70528
from itertools import permutations

s = 'ABC BAD CAEG DBFG ECF FDEG GCDF'
s_g = {c[0]:set(c[1:]) for c in s.split()}
s1 = '1457 246 3567 412 5136 6235 713'
print('1 2 3 4 5 6 7')
for x in permutations(set(s) - {' '}):
    s2 = s1
    for a1, a2 in zip('1234567', x):
        s2 = s2.replace(a1, a2)
    s2_g = {c[0]: set(c[1:]) for c in s2.split()}
    if s2_g == s_g:
        print(*x, sep=' ')

'''
s = 'Выписываем граф для каждой вершины,
т.е вершину и все вершины, с которыми она соединина'
s1 = 'Выписываем для каждого пункта номер пункта из таблицы и все пункты,
с которыми он соединён'
руппы разделены пробелом
'''
 
