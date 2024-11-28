print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f= ((not(y) or w) ==(not(x) or not(z))) and (x or w)
                
                print(y, z, w, x, f)
                    
