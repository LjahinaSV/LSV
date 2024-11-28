i=0
alf='01'
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        for a7 in alf:
                            for a8 in alf:
                                for a9 in alf:
                                    for a10 in alf:
                                        for a11 in alf:
                                            t = '101011000001000010101'+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
                                            s=t.count('1')
                                            if s % 5 != 0:
                                                i+=1
print(i)
