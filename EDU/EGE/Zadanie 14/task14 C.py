k=0 #Счётчик нулей в семеричной системе
x=2031 # начальное значение на 1 больше, чем в условии
while k!=71:
    x-=1
    f = 7**170 + 7**100 - x
    #Счётчик нулей в семеричной системе
    k=0

    #Перебираем цифры в семеричной системе
    while f>0:
        if f%7==0:
            k += 1
        f = f // 7
    
    
print(x)

# ответ 2029
# в моём варианте программа работает быстрее
