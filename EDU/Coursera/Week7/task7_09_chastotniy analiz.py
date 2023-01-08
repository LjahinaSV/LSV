# Частотный анализ
with open('input.txt') as inF:
    lines = inF.readlines()
# print(lines)
myDict = dict()
t = []
for a in lines:
    a = a.strip()
    # print(a)
    b = list(map(str, a.split(' ')))
    # print(b)
    for c in b:
        if c not in myDict:
            myDict[c] = 0
        myDict[c] += 1
# print(myDict)
# создаём из словаря список кортежей
for k, v in myDict.items():
    t.append((-v, k))
# Сортируем и выводим ключи
for v, k in sorted(t):
    print(k)
