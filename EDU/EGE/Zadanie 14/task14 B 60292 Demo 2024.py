# 60292 Demo 2024 Задание 14 B
''' Значение арифметического выражения
3 *3125**8 + 2 * 625**7 − 4* 625**6 + 3* 125**5 − 2* 25**4 − 2024
записали в системе счисления с основанием 25.
Сколько значащих нулей содержится в этой записи?
'''

x = 3 * (3125**8) +2 * (625**7) -4 * (625**6) + 3 * (125**5) -2 * (25**4) -2024
c = 0
while x != 0:
    if x % 25 == 0:
        c += 1
    x //= 25
print(c)
# 9
