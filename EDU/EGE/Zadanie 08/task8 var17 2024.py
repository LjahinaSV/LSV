alph='01234567'
q=0
for a in alph[1:]:
    for b in alph:
        for c in alph:
            for d in alph:
                if (a==b and b!=c and b!=d and c!=d) or (b==c and c!=d and c!=a and a!=d) or \
                   (c==d and c!=a and c!=b and a!=b):
                    q+=1
print(q)
# ответ 882
