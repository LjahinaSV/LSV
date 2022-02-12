import random


class MyExc(Exception):
    pass


class ValueTooSmall(MyExc):
    pass


class ValueTooLarge(MyExc):
    pass


class ValueEqFirst(MyExc):
    pass


def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            # count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] <= element <= array[middle + 1]:  # если элемент в середине,
        if array[middle] == element:
           while  array[middle] == element and middle > 0:  # ищем слева пока не найдём меньший
               middle -= 1
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


try:
    array = list(map(int, input('Введите список чисел через пробел:').split()))
except ValueError:
    print('Ввели не число. Выходим.')
    exit()
else:
    print('OK!')


try:
    element = int(input("Введите число: "))
except ValueError:
    print('Это не число. Выходим.')
    exit()
else:
    print('OK!')


left = 0
right = len(array) - 1
qsort_random(array, left, right)
print(array)
try:
    if element < array[left]:
        raise ValueTooSmall
    elif element > array[right]:
        raise ValueTooLarge
    elif element == array[left]:
        raise ValueEqFirst
    else:
        print(binary_search(array, element, left, right))

except ValueTooSmall:
    print(f'Введённое число {element}  меньше первого элемента в списке, равного {array[left]}')
except ValueTooLarge:
    print('Номер позиции элемента, который предшествует введённому, равен', right)
except ValueEqFirst:
    print('Введённое число', element, 'равно первому элементу в списке, у него нет предшественника')
