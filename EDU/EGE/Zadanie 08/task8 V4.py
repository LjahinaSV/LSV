k=0
for x1 in '123456789AB':
    for x2 in '0123456789AB':
        for x3 in '0123456789AB':
            for x4 in '0123456789AB':
                for x5 in '0123456789AB':
                    s = x1+x2+x3+x4+x5
                    if s.count('7')==1 and s.count('9') + s.count('A') + s.count('B') <= 3:
                        k += 1
print(k)
