# работает!!!
def sorter(point):
    return point[0]

n = int(input())
towns = list(map(int, input().split()))
m = int(input())
shelters = list(map(int, input().split()))
for i in range(n):
    towns[i] = (towns[i], i + 1)
for i in range(m):
    shelters[i] = (shelters[i], i + 1)
towns.sort()
shelters.sort()
i = 0
j = 0
v = []
while i < len(towns):
    if j == len(shelters) - 1:
        v.append((towns[i][1], shelters[j][1]))
    else:
        if towns[i][0] <= shelters[j][0] + ((shelters[j+1][0] - shelters[j][0])//2):
            v.append((towns[i][1], shelters[j][1]))
        elif towns[i][0] > shelters[j][0] + ((shelters[j+1][0] - shelters[j][0])//2):
            j += 1
            continue
    i += 1
v.sort(key=sorter)
for i in range(len(v)):
    print(v[i][1], end=' ')