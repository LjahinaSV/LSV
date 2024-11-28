alph='0123456789ab'
x=0
for a1 in '123456789ab':
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    s=a1+a2+a3+a4+a5
                    t=s.count('7')
                    h=s.count('9')+s.count('a')+s.count('b')
                    if t==1 and h<=3:
                        x+=1
print(x)                    
