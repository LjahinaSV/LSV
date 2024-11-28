print('x y z w')

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f=(not(w)or x) and ((not(y)or z) == (not(x) or y))
                if f:
                    
                    print(x,y,z,w,f,sep=' ')
