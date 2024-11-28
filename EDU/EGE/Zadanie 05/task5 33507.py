n_min=9**10
for n in range(2, 9999):
    s=format(n, 'b')
    s = str(s)
    s = s[:-1]+s[1]+s[1]
    
    r=int(s, 2)
    
    if r>92:
        n_min=min(n_min,n)


print(n_min)
        

