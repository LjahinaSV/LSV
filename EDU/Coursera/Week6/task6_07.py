# Результаты олимпиады
class Man:
    name = ''
    score = 0


def manKey(man):
    #  return (man.name, -man.score)
    return (-man.score)


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.name = tempManData[0]
    man.score = int(tempManData[1])
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.name)
