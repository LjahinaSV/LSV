# быстрая сортировка O(n*log(n))
# Но если на каждой итерации выбирается минимальный (максимальный) элемент структуры,
# то затраты по времени могут быть до O(n^2)
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)