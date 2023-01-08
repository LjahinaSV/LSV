# Монахов Владимир Николаевич Учащийся год назад
# Строится массив подсчёта величин набранных баллов из 181 элемента
# (суммарные баллы до 120 не считаются, т.к. точно не являются проходными),
# массив разворачивается
# и перебором по нему суммируются количества счастливчиков,
# пока это кол-во не превышает K.
with open('input.txt', 'r', encoding='utf8') as inFile:
    L = [tuple(i.split()) for i in inFile]
f_Out = open('output.txt', 'w', encoding='utf8')
K = int(L[0][0])
S = [0] * 181
N = 1

for i in range(1, len(L)):
    m1 = int(L[i][-3])
    m2 = int(L[i][-2])
    m3 = int(L[i][-1])
    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        S[m1 + m2 + m3 - 120] += 1
S = S[::-1]

count = 0
for j in range(len(S)):
    if count + S[j] > K:
        break
    if S[j] > 0:
        count += S[j]
        N = 300 - j
    if j == len(S)-1:
        N = 0

print(N, file=f_Out)
f_Out.close()
