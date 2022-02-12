def find(array, element):  # поиск элемента в массиве
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):  # количество вхождений элемента в массив
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count


array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
print(count(array, element))
