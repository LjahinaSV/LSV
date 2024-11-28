f=open('9.txt')

k=0

for s in f:
    a = list(map(int,s.split())) # делаем список целых чисел
    k3=0
    k1=0
    summ3=0
    summ1=0
    for x in a:
        if a.count(x)==3:
            k3=3
            summ3+=x
        if a.count(x)==1:
            k1+=1
            summ1+=x
    if k3==3 and k1==3 and summ3**2 > summ1**2:
        k+=1
print(k)
f.close()

# 273
