inf = open('input.txt', 'r', encoding='utf8')
outf = open('output.txt', 'w', encoding='utf8')
d = dict()
n = 0
# Создаем словарь президентов с количеством голосов
for a in inf:
    a = a.strip()
#    if a not in d:
#        d[a] = 0
#    d[a] += 1
    d[a] = d.get(a, 0) + 1
    n += 1
# print(d)
# Сортируем словарь по количеству голосов,
# преобразовав его по ходу в список кортежей  методом items()
d = sorted(d.items(), key=lambda item: [-int(item[1]), item[0]])
# print(d)
for i in range(2):
    if float(d[i][1]) > n / 2:
        print(d[i][0], file=outf)
        break
    else:
        print(d[i][0], file=outf)
inf.close()
outf.close()
