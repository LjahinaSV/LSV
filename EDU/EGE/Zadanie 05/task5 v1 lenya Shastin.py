for n in range(1,1000):
    s=format(n,'b')
    s=str(s)
    if len(s)%2==0:
        s+='11'
    else:
        s+='01'
    r=int(s,2)
    if r>61:
        print(r)
        break
