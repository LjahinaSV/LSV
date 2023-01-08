# Полиглоты
# inF = open('input7.txt', 'r', encoding='utf8')
inF = open('input.txt', 'r', encoding='utf8')
N = int(inF.readline())
lines = inF.readlines()
# print('N=', N)
# print(lines)
SP = set()  # пересечение, языки, которые изучают во всех школах
SO = set()  # объединение, языки, которые изучают хотя бы в одной из школ
k = 0  # счетчик прочитанных записей
school = set()  # языки, изучаемые в Mi школе
for i in (range(1, N + 1)):
    M = int(lines[k])
    # print('M=', M)
    school = set()
    k += 1
    for j in (range(1, M + 1)):
        school.add(*tuple(lines[k].split()))
        k += 1
        # print(*school)
    if i == 1:
        SP = school
    else:
        SP &= school
    SO |= school
print(len(SP))
print(*list(SP), sep='\n')
print(len(SO))
print(*list(SO), sep='\n')
inF.close()
