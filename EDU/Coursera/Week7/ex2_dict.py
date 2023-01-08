sqrt = {}  # создание и заполнение словаря
sqrt[3] = 9
sqrt[10] = 100
print(sqrt)
sqrt[1] = 1
print(sqrt)  # выводит весь словарь
print(sqrt[10]) # выводит значение по ключу / находит значение по ключу
print(*sqrt)  # выводит все ключи
# Создание словаря из чего-либо iterable
myDict = dict([('x', 5), ('y', 3)])  # создание из списка
print(myDict)
myDict = dict([['key1', 'value1'], ('key2', 'value2')])
print(myDict)
#
countries = {'Russia' : 'Europe', 'Germany' : 'Europe', 'Australia' : 'Australia'}
for i in countries:
    print(i, countries[i])  # перебор всех пар в словаре по ключам

# Удаление из словаря по ключу
phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
print(phones)
print('police - ',phones['police'])
del phones['police']
# print(phones['police']) после удаления вызовет ошибку
print(phones)
