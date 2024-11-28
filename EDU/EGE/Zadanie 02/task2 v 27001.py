print('x y z w f')

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f=(x and y and not(z))==(y or z or not(w))
                if f:
                    print(x,y,z,w,f, sep=' ')
