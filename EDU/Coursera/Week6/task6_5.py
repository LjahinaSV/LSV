# Отсортировать список участников по алфавиту
fIn = open('input.txt', 'r', encoding='utf8')
fOut = open('output.txt', 'w', encoding='utf8')
lines = fIn.readlines()
lines.sort()
for line in lines:
    a = line.split()
    b = a[0] + ' ' + a[1] + ' ' + a[3]
    print(b, file=fOut)
fIn.close()
fOut.close()
