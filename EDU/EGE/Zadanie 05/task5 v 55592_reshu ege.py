def novoech(pr):
    for i in range (0, 3):
        n = str(pr)
        nechet = n.count('1') + n.count('3') + n.count('5') + n.count('7') + n.count('9')
        chet = n.count('0') + n.count('2') + n.count('4') + n.count('6') + n.count('8')
        if nechet > chet:
            pr = pr*2
        elif nechet < chet:
            pr = pr*2 + 1
        elif nechet ==chet:
            if nechet%2 == 0:
                pr = pr*2
            else:
                pr = pr*2 + 1
    return pr
minch = 123455//8
for pr in range (minch - 1, minch + 2):
    r = novoech(pr)
    if r >= 123455:
        minch = pr
        break
maxch = 987654321//8
for pr in range (maxch - 1, maxch + 2):
    r = novoech(pr)
    if r <= 987654321:
        maxch = pr
print ( maxch - minch + 1 )
