#64944
''' В системе счисления с основанием p выполняется равенство
zxyx7 + xy836  =  wzx64. Буквами x, y, z и w обозначены некоторые цифры
из алфавита системы счисления с основанием p.
Определите значение числа xyzw из p сс
и запишите это значение в десятичной системе счисления.
'''
for p in range(9,30):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if z*p**4+x*p**3+y*p**2+x*p+7 + x*p**4+y*p**3+8*p**2+3*p+6== \
                       w*p**4+z*p**3+x*p**2+6*p+4:
                        print(f'p={p} x={x} y={y} z={z} w={w}')
                        print(x*p**3+y*p**2+z*p+w)

# 1763

# Приведём решение Ильи Андрианова на языке Python.
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(9, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                for w in alphabet[:p]:
                    if int(z+x+y+x+'7', p) + int(x+y+'836', p) == int(w+z+x+'64', p):
                        print(int(x+y+z+w, p))

