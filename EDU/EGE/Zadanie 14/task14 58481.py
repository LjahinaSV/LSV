# 58481
''' В системе счисления с основанием p выполняется равенство 12 · 34  =   xy2.
Буквами x и y обозначены некоторые цифры из алфавита системы счисления
с основанием p. Определите значение числа yx в p сс
и запишите это значение в десятичной системе счисления.
'''
for p in range(5,37):
    for x in range(p):
        for y in range(p):
            if x*p**2 + y*p +2 == (p+2)*(3*p+4):
                print(f'p= {p}, x= {x}, y= {y}')
                print(f'Rezultat: yx in 10 ss {y*p+x}')

# Ответ 34 р=6, х=4, у=5. 5*6+4=34

# Приведём решение задачи Ильи Андрианова на языке Python.

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(5, 36):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'12', p) * int(f'34', p) == int(f'{x}{y}{2}', p):
                print(int(f'{y}{x}', p))

