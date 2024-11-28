f=open('69914.txt')
k=0
for s in f:
    a=[int(x) for x in s.split()]
    a1=[x for x in a if a.count(x)==3]
    a2=[x for x in a if a.count(x)==1]
    if len(a1)==3 and len(a2)==3:
        if (a1[0]+a1[1]+a1[2])//3 >= (a2[0]+a2[1]+a2[2])//3:
            k+=1
print(k)
f.close()
# 12
