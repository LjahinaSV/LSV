#64899
''' В системе счисления с основанием p выполняется равенство
zxyx4 + xy658  =  wzx73. Буквами x, y, z и w обозначены некоторые цифры
из алфавита системы счисления с основанием p.
Определите значение числа xyzw в p сс
и запишите это значение в десятичной системе счисления.

for p in range(9,30):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    t1=z*p**4+x*p**3+y*p**2+x*p+4
                    t2=x*p**4+y*p**3+6*p**2+5*p+8
                    t3=w*p**4+z*p**3+x*p**2+7*p+3
                    if  t1+t2 == t3:
                        print(f'p={p} x={x} y={y} z={z} w={w}')
                        print(x*p**3+y*p**2+z*p+w)
                        

# 1114 Первый вариант программы работает намного дольше 
'''

alph = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(9, 37):
    for x in alph[:p]:
        for y in alph[:p]:
            for z in alph[:p]:
                for w in alph[:p]:
                    if int(z+x+y+x+'4', p) + int(f'{x}{y}658', p) == int(f'{w}{z}{x}73', p):
                        print(int(x+y+z+w, p))
                    

