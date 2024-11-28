alph='0123456789AB'
q=0
for a in alph[1:]:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    t=a+b+c+d+e
                    if t.count('7')==1 and t.count('9')+t.count('A')+t.count('B')<=3:
                       q+=1
print(q)
    
