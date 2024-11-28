rmin=999999
for n in range(1,1000):
    s=format(n, 'b')
    s=str(s)
    if len(s)%2==0:
        s+='1'
    else:
        s='1'+s+'0'
    r=int(s, 2)
    if r >666:
        # print(r)
        rmin=min(r,rmin)

print(rmin)
        


        
