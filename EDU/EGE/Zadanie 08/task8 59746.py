from itertools import permutations
word = '0123456789'
c = 0
for j in range(1,11):
    for i in permutations(word,j):
        x = ''.join(i)
        if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
            c += 1
print(c + 1) #+1 случай когда число равно 0