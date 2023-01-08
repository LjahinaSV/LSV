# Проходной балл
f_In = open('input.txt', 'r', encoding='utf8')
f_Out = open('output.txt', 'w', encoding='utf8')
k = int(f_In.readline())
# print(k)
inList = [0]*301
in_list = []
lines = f_In.readlines()[0:]  # чтение файла со второй записи
for stroka in lines:
    line = list(stroka.split())
    # print(school)
    if int(line[-3]) > 39 and int(line[-2]) > 39 and int(line[-1]) > 39:
        score1 = int(line[-3])
        score2 = int(line[-2])
        score3 = int(line[-1])
        sumScore = score1 + score2 + score3
        # print(score1, score2, score3, sumScore)
        inList[sumScore] += 1
        in_list.append(sumScore)


in_list.sort(reverse=True)

if len(in_list) <= k or k == 0:
    print(0, file=f_Out)
else:
    if in_list[k - 1] == in_list[k]:
        d = k - 1
        while d > 0 and in_list[d - 1] == in_list[d]:
            d = d - 1
        if d == 0:
            print(1, file=f_Out)
        else:
            print(in_list[d - 1], file=f_Out)
    else:
        print(in_list[k - 1], file=f_Out)
f_In.close()
f_Out.close()
