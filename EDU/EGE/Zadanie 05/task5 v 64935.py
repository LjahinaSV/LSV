k=0
for n in range(550000000,1437653211):
    s=format(n, 'b')
    s1=format(n%4,'b')
    s=s+s1
    r=int(s, 2)

    if r >= 1100000000 and r <= 1987653210:
        k+=1

print(k)
'''моё решение даёт ответ 2, диапазон для n подобрала неверно
работает долго, диапазон для N обоснованно подобрать невозможно '''

        
