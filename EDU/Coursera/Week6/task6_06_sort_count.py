# сортировка подсчетом
a = list(map(int, input().split()))
#  print(a)


def CountSort(a):
    cntMarks = [0] * 101
    for mark in a:
        cntMarks[mark] += 1
    a = ''
    for nowMark in range(101):
        a += (str(nowMark) + ' ') * cntMarks[nowMark]
        #  print((str(nowMark) + ' ') * cntMarks[nowMark], end='')
    return a


print(CountSort(a))
