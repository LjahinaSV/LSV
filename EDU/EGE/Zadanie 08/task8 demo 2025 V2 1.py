from itertools import product
count = 0
alph='0123456789AB'
for s in product(alph, repeat=5):
    if s.count("7") > 1:
        count += 1
    # print(s)
# print(type(s))
print(count)
# and s[0] != "0":
#    if s.count("9")+ s.count("A") + s.count("B") <=3:
#  and s[0]!='0':
