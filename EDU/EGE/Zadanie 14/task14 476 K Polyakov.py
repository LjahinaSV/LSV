# 476 К. Поляков
''' 476)	(ЕГЭ-2024) Значение арифметического выражения З100 – х,
где х – целое положительное число, не превышающее 2030,
записали в троичной системе счисления. Определите наибольшее значение х,
при котором в троичной записи числа,
являющегося значением данного арифметического выражения,
содержится ровно пять нулей.
В ответе запишите число в десятичной системе счисления.
'''
for x in range(2030,1,-1):
    a=3**100-x
    k=0
    s=''
    while a != 0:
        s=str(a%3)+s
        if a%3 == 0:
            k+=1
        a//=3    
    if k == 5:
        # print(s, x, k)
        print(x)
        break

# 2024
    
