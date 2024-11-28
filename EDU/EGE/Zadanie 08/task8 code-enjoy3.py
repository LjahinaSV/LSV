k=0
for x1 in 'КБЛА':
    for x2 in 'КБЛА':
        for x3 in 'КБЛА':
            for x4 in 'КБЛА':
                for x5 in 'КБЛА':
                    for x6 in 'КБЛА':
                        s=x1+x2+x3+x4+x5+x6
                        if s.count('К')==1 and s.count('А')==3 and s.count('Б')==1 and s.count('Л')==1:
                            if s.count('АА')==0:
                                k=k+1
                                print(s)
print(k)
