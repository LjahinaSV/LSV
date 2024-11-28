print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f=not(not(x)or y) or (x == z) or w
                if not f:
                    print(x, y, z, w)
 
