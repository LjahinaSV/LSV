print('a b c d')
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                f=((a or b) <= (not(c) and a)) and d
                if f==1:
                    print(a,b,c,d,sep=' ')
