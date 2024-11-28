c=0
alph='01234567'
chet='0246'
nchet='1357'
for x1 in alph:
    for x2 in alph:
        for x3 in alph:
            for x4 in alph:
                for x5 in alph:
                    r=x1+x2+x3+x4+x5
                    if x1 != '0' and \
                    r.count('1') < 1 and r.count('0') <= 1 and r.count('2') <= 1 and \
                    r.count('3') <= 1 and r.count('4') <= 1 and r.count('5') <= 1 and \
                    r.count('6') <= 1 and r.count('7') <= 1 and \
                    ((x1 in nchet and x3 in nchet and x5 in nchet and x2 in chet and x4 in chet )\
                     or \
                    (x1 in chet and x3 in chet and x5 in chet and x2 in nchet and x4 in nchet )):
                        c+=1
print(c)
# ответ 180
