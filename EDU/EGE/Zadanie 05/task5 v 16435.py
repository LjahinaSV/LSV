for n in range(2,999999):
    s=format(n, 'b')
    s=str(s)
    s=s[:-1]
    if n%2==0:
        s+='01'
    else:
        s+='10'
    r=int(s, 2)
    if r == 2017:
        print(n)
        break
        


        
