# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С
# (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []


def merge(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r = a[i]
            i += 1
        else:
            r = b[j]
            j += 1
        c.append(r)
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


merge(a, b)
print(*c)
