for n in range(1, 1000):
    s=format(n, 'b')
    s=s.replace('0', '*')
    s=s.replace('1', '10')
    s=s.replace('*', '01')
    r=int(s, 2)
    if r%2!=0 and r<256:
        print(r)
