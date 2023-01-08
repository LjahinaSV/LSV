# Номер появления слова
with open('input.txt', 'r', encoding='utf8') as inF:
    lines = inF.read().split()
# print(lines)
myDict = dict()
for line in lines:
    if line not in myDict:
        myDict[line] = 0
    print(myDict[line], end=' ')
    myDict[line] += 1
