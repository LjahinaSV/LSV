# 69914 Откройте файл электронной таблицы, содержащей в каждой строке
# шесть натуральных чисел. Определите количество строк таблицы,
# содержащих числа, для которых выполнены оба условия:
# —  в строке есть одно число, которое повторяется трижды, остальные три числа различны;
# —  повторяющееся число строки не меньше, чем среднее арифметическое трёх её неповторяющихся чисел.
# В ответе запишите только число.

k=0
# c=0
f=open('69914.txt')
for s in f:
    # c+=1
    a=list(map(int,s.split()))
    # a=[int(i) for i in s.split()]
    k1 =0
    k3 = 0
    summ1=0
    summ3 = 0
    for x in a:
        if a.count(x)==3:
            k3=3
            summ3+=x
        if a.count(x)==1:
            k1+=1
            summ1+=x
    if k3==3 and k1==3:
            if summ3 / 3 >= summ1 / 3:
                k+=1
                # print(a, c)
print(k)
f.close()
# 16 ??? Почему-то 4 раза повторяет предыдущую запись
# Нашла ошибку. Последний if написала в цикле for x
# Ответ 12


 
