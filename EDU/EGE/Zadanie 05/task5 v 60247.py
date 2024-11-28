mr=999999
for n in range(4,1000):
    s=format(n, 'b')
    # print(n,s,sep=' ')
    s1=format((n%3)*3,'b')
    if n%3==0:
        s=s+s[-3:]
    else:
        s=s+s1
    r=int(s, 2)

    if r >151:
        mr=min(mr,r)

print(mr)


        
