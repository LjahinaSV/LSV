for n in range(1,1000):
    s=format(n, 'b')
    s=str(s)
    # s+='11' if s.count('1')%2==1 else '00'
    if s.count('1')%2==1:
        s+='11'
    else:
        s+='00'
    r=int(s, 2)
    if r >114:
        print(r)
        


        
