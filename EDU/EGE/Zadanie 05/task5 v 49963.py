mn=9999
for n in range(1,10000):
    s=format(n, 'b')
    s=str(s)
    i=0
    a=0
    b=0
    while i< len(s):
        if i%2==1 and s[i]=='1':
            a+=1
        if i%2==0 and s[i]=='0':
            b+=1
        i+=1
    
    r=abs(a-b)
    # print(n,r,sep=' ')
    if r == 5:
        mn=min(mn,n)

print(mn)
        


        
