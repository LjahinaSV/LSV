from itertools import permutations
alf='0234567'
ch='0246'
nch='357'
c=0

for p in permutations(alf,5):
    x=''.join(p)
    if x[0]!='0' and \
       x[0] in ch and \
       x[2] in ch and \
       x[4] in ch and \
       x[1] in nch and \
       x[3] in nch or \
       x[0] in nch and \
       x[2] in nch and \
       x[4] in nch and \
       x[1] in ch and \
       x[3] in ch:
       c+=1
print(c)
# отв 180
