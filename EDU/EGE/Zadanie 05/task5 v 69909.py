rmax=0
for n in range(1,13):
    s=format(n, 'b')
    s=str(s)
    if n%2==0:
        s+='10'
    else:
        s='1'+s+'00'
    r=int(s, 2)
    # if r >rmax:
    rmax=max(r,rmax)

print(rmax)
        


        
