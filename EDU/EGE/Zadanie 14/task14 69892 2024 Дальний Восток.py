#69892 Осн волна 2024 ДВ
''' Значение арифметического выражения
3 * 289**2024 + 81 * 49**121 − 9 * 16**81 − 6011
записали в системе счисления с основанием 31. Определите сумму цифр
с числовым значением, не превышающим 17, в записи этого числа.
'''
a=3*289**2024+81*49**121-9*16**81-6011
summ=0
while a != 0:
    ost=a%31
    if ost <= 17:
        summ+=ost
    a//=31
print(summ)
