count = 0
for x in range(1100000000, 1987653210+1):
    if x%16 in [10,15] or x%8 in [0,3]:
        count += 1
print(count)
'''
на конце у R в двоичной сс может получаться
000 или 011 или 1010 или 1111.
Это соответствует 0 или 3 в восьмеричной сс и
10 или 15 в шестнадцатеричной сс
'''
