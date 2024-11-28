n_max=0
for n in range(1, 256):
    s=format(n, 'b')

    # делаем 8-ое число
    while(len(s)<8):
        s='0'+s

    s=s[:-1] # удаляется последняя цифра
    s=s[::-1] # число переворачивается

    r=int(s, 2)
    if n<100 and r==n:
        n_max=max(n_max,n)

print(n_max)
