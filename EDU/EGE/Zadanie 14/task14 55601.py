# 55601
''' В системе счисления с основанием p выполняется равенство y4y +  y65  =  xz23.
Буквами x, y и z обозначены некоторые цифры из алфавита системы счисления
с основанием p. Определите значение числа xyz в p сс
и запишите это значение в десятичной системе счисления.
'''

for p in range(7,37):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if y*p**2+4*p+y + y*p**2+6*p+5 == x*p**3+z*p**2+2*p+3:
                    print(f'p= {p} x={x} y= {y} z= {z}')
                    print(f' Rez= {x*p**2+y*p+z}')

# 150

alph = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(7, 37):
    for x in alph[:p]:
        for y in alph[:p]:
             for z in alph[:p]:
                 if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}23', p):
                        #  if int(y+'4'+y, p)+ int(y+'65', p)== int(x+z+'23', p):
                        print(int(f'{x}{y}{z}', p))
                        
                    
