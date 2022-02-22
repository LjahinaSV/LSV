x = int(input())
tMax = x
predMax = 1
while x != 0:
    x = int(input())
    if x >= tMax:
        predMax = tMax
        tMax = x
    if predMax < x < tMax:
        predMax = x
print(predMax)
