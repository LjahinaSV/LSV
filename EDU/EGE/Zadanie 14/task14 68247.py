# 68247
''' Числа AB267D1p и F024A89p записаны в системе счисления с основанием p.
При каком минимальном p сумма этих чисел будет делиться на p – 1?
'''
#for p in range(16,37):
#    if (int(f'AB267D1', p) + int(f'F024A89',p)) % (p-1)== 0:
#        print(p)
# print(int('AB267D1',36)+int(f'F024A89',36)) для отладки. СС > 36
#
for p in range(16,100):
    x1= 10*p**6 + 11*p**5 + 2*p**4 + 6*p**3 + 7*p**2 + 13*p**1 + 1
    x2= 15*p**6 +  0*p**5 + 2*p**4 + 4*p**3 + 10*p**2 + 8*p**1 + 9
    if (x1+x2) % (p-1) == 0:
        print(p)
        break

# 50
otv=[]
for p in range(16,100):
    x1= 10*p**6 + 11*p**5 + 2*p**4 + 6*p**3 + 7*p**2 + 13*p**1 + 1
    x2= 15*p**6 +  0*p**5 + 2*p**4 + 4*p**3 + 10*p**2 + 8*p**1 + 9
    if (x1+x2) % (p-1) == 0:
        otv.append(p)
print(min(otv))

    

