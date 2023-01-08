# class Man:
#     fam = ''
#     name = ''
#     gruppa = 0
#     ball = 0


fileIn = open('input.txt', 'r', encoding='utf8')
cl9 = 0
k9 = 0
cl10 = 0
k10 = 0
cl11 = 0
k11 = 0
for line in fileIn:
    myList = line.split()
    if myList[2] == '9':
        cl9 += int(myList[3])
        k9 += 1
    if myList[2] == '10':
        cl10 += int(myList[3])
        k10 += 1
    if myList[2] == '11':
        cl11 += int(myList[3])
        k11 += 1
    # print(int(myList[2]), int(myList[3]))
print(cl9/k9 if k9 != 0 else k9, end=' ')
print(cl10/k10 if k10 != 0 else k10, end=' ')
print(cl11/k11 if k11 != 0 else k11)
fileIn.close()
