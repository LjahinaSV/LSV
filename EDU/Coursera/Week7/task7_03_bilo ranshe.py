# Встречалось ли число раньше
myList = list(map(int, input().split()))
# print(myList)
S = set()
for a in myList:
    l1 = len(S)
    S.add(a)
    l2 = len(S)
    if l1 == l2:
        print('YES')
    else:
        print('NO')
