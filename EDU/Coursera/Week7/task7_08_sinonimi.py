# Словарь синонимов
# Формат ввода
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два слова-синонима.
# После этого следует одно слово.
# Формат вывода
# Программа должна вывести синоним к данному слову.
# inF = open('input.txt')
# myDict = dict()
# for i in range(int(inF.readline())):
#     a, b = inF.readline().split()
#     myDict[a], myDict[b] = b, a
# print(myDict[inF.readline()])
# inF.close()
# print(myDict)
myDict = dict()
for i in range(int(input())):
    a, b = input().split()
    myDict[a], myDict[b] = b, a
print(myDict[input()])
