for n in range (0,1000):
    s=format(n,'b')
    s=str(s)
    if n%2==0:
        s='1'+s+'0'
    else:
        s='11'+s+'11'
    r=int(s,2)
    if r>52:
        print(n)
        break
