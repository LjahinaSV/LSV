from itertools import product
 
count = 0
 
for i in product ('01a', repeat = 8 ):
    s = ''.join(i)
    if s[0] != '0' and s.count('0') == 2 and s.count('a') <5:
        count += 9**s.count('1') * 6**s.count('a')
        print(s)
        # count+=1
        if count==30:
            break
print(count)
