for n in range(128, 256):
    s=format(n, 'b')
    s = str(s)
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r=int(s, 2)
    x=n-r
    if x==105:
        print(n)
        

