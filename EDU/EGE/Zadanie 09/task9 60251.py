'''60251 Определите количество строк таблицы,
содержащих числа, для которых выполнены оба условия:
—  в строке есть два числа, каждое из которых повторяется дважды,
остальные числа различны;
—  среднее арифметическое всех повторяющихся чисел строки меньше
среднего арифметического всех её чисел. Демо 2024 '''

count=0
f=open('60251.txt')
for s in f:
    a=list(map(int,s.split()))
    # print(a)
    s_all=sum(a)
    # print(s_all)
    # break
    s_rep=0
    k=0
    for x in a:
        if a.count(x)==2:
           s_rep+=x
           k += 1
           # print(s_rep, k)
    # break
    if k==4:
        if s_rep/4 < s_all/7:
            count+=1

print(count)
f.close()

#
