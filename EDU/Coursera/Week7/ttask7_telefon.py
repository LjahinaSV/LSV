# Чернов Андрей Александрович Учащийся 6 месяцев назад
# телефонная книга
def num(s):     # функция, приводящая номер к одному виду
    temp = []
    # набираем в текущий только цифры
    # проходим по строке. если цифра - добавляем
    for i in s:
        if i.isdigit():
            temp.append(int(i))

    # если длина 11 - обрезаем первый знак (7 или 8)
    # если другая - добавляем код 495
    if len(temp) == 11:
        temp = temp[1:]
    else:
        temp = [495] + temp
    # выводим символы кучей друг за другом
    return ''.join(map(str, temp))


inFile = open('input.txt')
s = inFile.readline()
for line in inFile:
    # приводим к одному виду и сравниваем
    print('YES' if num(line) == num(s) else "NO")
inFile.close()