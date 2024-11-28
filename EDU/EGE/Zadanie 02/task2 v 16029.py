print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f= (not(x) and not(y)) or (y==z) or not(w)
                if f == 0:
                    # print(z, y, x, w) # проверка
                    print(x, y, z, w)
