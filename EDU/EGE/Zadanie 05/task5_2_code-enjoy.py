min_n=999999
for n in range(1, 1000):
    s=format(n, 'b')
    if n%2 ==0:
        s=s + '00'
    else:
        s=s + '11'
    r=int(s, 2)

    if r>130:
        min_n=min(min_n,n)

print(min_n)
        
