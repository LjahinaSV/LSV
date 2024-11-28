#61360
''' В числе 12x643y7 в 37сс x и y обозначают некоторые цифры
из алфавита системы счисления с основанием 37.
Определите такие значения x и y, при которых приведённое число кратно 36,
а число yx в 37сс имеет наибольшее возможное значение.
В ответе запишите значение числа yx из 37сс в десятичной системе счисления.
'''
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
p=37
rez=[]
for x in range(p):
    for y in range(p):
        a=1*p**7+2*p**6+x*p**5+6*p**4+4*p**3+3*p**2+y*p+7
        if a%36==0:
            rez.append(y*p+x)
            # print(f'p= {p} x= {x} y= {y} yx= {y*p+x}')
if rez:
    print(max(rez))

# Ответ 1345


# Приведём решение Юрия Красильникова на языке Python.
def num(digits,base): # функция переводит в 10сс из любого основания сс
    n = 0
    for d in digits:
        n=n * base + d
    return n
 
a = [num([y,x],37) for x in range(37) for y in range(1,37) if num([1,2,x,6,4,3,y,7],37)%36==0]
print(max(a))
