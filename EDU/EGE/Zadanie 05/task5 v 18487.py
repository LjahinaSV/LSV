n_max=0
for n in range(1, 101):
    s=format(n, 'b')
    s=s[::-1]
    
    r=int(s, 2)
    if r==13 and n<=100:
        n_max=max(n,n_max)

print(n_max)
