x = int(input())
tMax = x
i = 1
while x != 0:
    x = int(input())
    if x > tMax:
        tMax = x
        i = 1
    elif x == tMax:
        i += 1
print(i)
