for n in range(1, 256):
    s=format(n, 'b')

    # делаем 8-ое число
    while(len(s)<8):
        s='0'+s
    for i in range(0,len(s)):
        if s[i]=='0':
            s=s[:i]+'1'+s[i+1:]
        else:
            s=s[:i]+'0'+s[i+1:]
    
    r=int(s, 2)
    x=r-n
    if x==133:
        print(n)
        break

