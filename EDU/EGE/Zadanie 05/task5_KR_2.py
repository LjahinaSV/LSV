for n in range (0,1000):
    s=format(n,'b')
    s=str(s)
    s=s+str(s.count('1')%2)
    s=s+str(s.count('1')%2)
    r=int(s,2)
    if r>43:
        print(r)
        break
    
